# Estimators applied identically to simulated and observed data.
# y is log(estimate / true value); x is log(anchor / true value).

suppressPackageStartupMessages({ library(lme4); library(metafor); library(data.table) })

# Gross-error rule: drop responses further from the true value (log scale) than both a factor of
# 1,000 and ten times the most extreme anchor used for that cell. A response equal to any anchor
# is always retained, so the rule cannot remove strongly anchored answers.
drop_gross_errors <- function(dat) {
  dat <- dat[is.finite(y)]
  dat[, y_limit := pmax(log(1000), max(abs(x)) + log(10)), by = cell]
  dat[abs(y) <= y_limit][, y_limit := NULL][]
}

# Within-item response function: y = a_cell + b x + g x|x|, with uncorrelated random intercepts,
# slopes and curvatures by cell, and random intercepts by participant. b is the average elasticity at the true value; g > 0 means the
# local elasticity rises with anchor extremity, g < 0 means it falls.
fit_within <- function(dat) {
  dat <- drop_gross_errors(dat)
  dat[, xx := x * abs(x)]
  m <- lmer(y ~ x + xx + (1 + x + xx || cell) + (1 | pid), data = dat,
            control = lmerControl(calc.derivs = FALSE, check.conv.singular = "ignore"))
  co <- summary(m)$coefficients
  b <- co["x", "Estimate"]; g <- co["xx", "Estimate"]
  V <- as.matrix(vcov(m))[c("x", "xx"), c("x", "xx")]
  # Relative curvature rho = g / b, with a delta-method standard error.
  grad <- c(-g / b^2, 1 / b)
  list(model = m, b = b, b_se = co["x", "Std. Error"], g = g, g_se = co["xx", "Std. Error"],
       rho = g / b, rho_se = sqrt(drop(t(grad) %*% V %*% grad)), n = nrow(dat))
}

# Across-cell anchoring index: log-scale index per two-anchor cell, meta-regressed on extremity
# (mean absolute log distance of the two anchors from the true value).
cell_indices <- function(rows, cells) {
  r <- merge(drop_gross_errors(rows)[, .(cell, anchorhigh, y)], cells[, .(cell, study, x_low, x_high, extremity)], by = "cell")
  r[, .(med_high = median(y[anchorhigh == 1]), med_low = median(y[anchorhigh == 0]),
        mad_high = mad(y[anchorhigh == 1]), mad_low = mad(y[anchorhigh == 0]),
        n_high = sum(anchorhigh == 1), n_low = sum(anchorhigh == 0),
        study = study[1], x_low = x_low[1], x_high = x_high[1], extremity = extremity[1]), by = cell][
    , `:=`(ai = (med_high - med_low) / (x_high - x_low),
           ai_se = 1.2533 * sqrt(pmax(mad_high, 1e-3)^2 / n_high + pmax(mad_low, 1e-3)^2 / n_low) / (x_high - x_low))][]
}

fit_across <- function(ci) {
  m <- rma.mv(ai, ai_se^2, mods = ~ extremity, random = ~ 1 | study / cell, data = ci, method = "REML")
  list(model = m, slope = unname(coef(m)["extremity"]), slope_se = unname(m$se[2]),
       intercept = unname(coef(m)["intrcpt"]), mean_ai = weighted.mean(ci$ai, 1 / ci$ai_se^2))
}
