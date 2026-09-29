# Confirmatory analyses as preregistered (prereg/preregistration.md, Q19-Q24).
# Usage: Rscript R/04_confirmatory.R          -> observed OpAQ estimates (after the prereg commit)
#        Rscript R/04_confirmatory.R dry-run  -> estimates replaced by responses simulated from M2,
#                                               to check the pipeline without reading outcomes

suppressPackageStartupMessages({ library(data.table); library(lmerTest); library(metafor); library(quantreg) })
source(file.path("R", "design_sets.R"))
source(file.path("R", "models.R"))
source(file.path("R", "estimators.R"))

dry_run <- identical(commandArgs(trailingOnly = TRUE), "dry-run")
out_dir <- if (dry_run) file.path("output", "dry_run") else file.path("output", "confirmatory")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
z <- qnorm(0.975)
rho_bounds <- c(-0.05, 0.05)
slope_bounds <- c(-0.03, 0.03)

# ---- Data -------------------------------------------------------------------------------------
sets <- build_sets(read_opaq(include_outcomes = !dry_run))
if (dry_run) {
  set.seed(1)
  cells <- unique(c(sets$within$cell, sets$across_rows$cell))
  cellpar <- data.table(cell = cells, sigma = runif(length(cells), 0.3, 1.2), bias = rnorm(length(cells), 0, 0.3))
  for (nm in c("within", "across_rows")) {
    s <- sets[[nm]]
    s[, estimate := t * exp(simulate_responses("M2", s[, .(cell, pid, x)], cellpar, list(w = 0.45)))]
  }
}
add_y <- function(d) {
  d <- copy(d)
  d[, est := suppressWarnings(as.numeric(estimate))]
  d[, y := fifelse(!is.na(est) & est > 0, log(est / t), NA_real_)]
  d
}
W <- add_y(sets$within)
A <- add_y(sets$across_rows)
cells_A <- copy(sets$across_cells)
exclusions <- rbind(
  data.table(set = "within", rows = nrow(W), invalid_estimate = W[is.na(y), .N],
             gross_error = nrow(W[!is.na(y)]) - nrow(drop_gross_errors(W[!is.na(y)]))),
  data.table(set = "across", rows = nrow(A), invalid_estimate = A[is.na(y), .N],
             gross_error = nrow(A[!is.na(y)]) - nrow(drop_gross_errors(A[!is.na(y)]))))
W <- W[!is.na(y)]
A <- A[!is.na(y)]

# Re-check cell eligibility after exclusions (Q14).
W_ok <- drop_gross_errors(W)[, .(levels = uniqueN(a)), by = cell][levels >= min_levels_within, cell]
W <- W[cell %in% W_ok]
A_ok <- drop_gross_errors(A)[, .(n_low = sum(anchorhigh == 0), n_high = sum(anchorhigh == 1)), by = cell][
  n_low >= min_n_side & n_high >= min_n_side, cell]
A <- A[cell %in% A_ok]
cells_A <- cells_A[cell %in% A_ok]

# ---- H1: within-item response function ----------------------------------------------------------
fit_h1 <- function(dat, formula = y ~ x + xx + (1 + x + xx || cell) + (1 | pid)) {
  dat <- drop_gross_errors(dat)
  dat[, xx := x * abs(x)]
  # Q23: simplify random effects step by step if the fit is singular or fails to converge
  forms <- list(formula,
                update(formula, . ~ . - (1 + x + xx || cell) + (1 + x || cell)),
                update(formula, . ~ . - (1 + x + xx || cell) + (1 | cell)))
  for (i in seq_along(forms)) {
    m <- tryCatch(lmerTest::lmer(forms[[i]], data = dat, REML = TRUE), error = function(e) NULL)
    if (!is.null(m) && !isSingular(m) && length(m@optinfo$conv$lme4$messages) == 0) break
  }
  co <- summary(m, ddf = "Satterthwaite")$coefficients
  V <- as.matrix(vcov(m))[c("x", "xx"), c("x", "xx")]
  b <- co["x", "Estimate"]; g <- co["xx", "Estimate"]
  grad <- c(-g / b^2, 1 / b)
  rho_se <- sqrt(drop(t(grad) %*% V %*% grad))
  ci <- function(term) co[term, "Estimate"] + c(-1, 1) * qt(0.975, co[term, "df"]) * co[term, "Std. Error"]
  list(model = m, random_structure = i, n_rows = nrow(dat), n_cells = uniqueN(dat$cell), n_participants = uniqueN(dat$pid),
       b = b, b_ci = ci("x"), g = g, g_ci = ci("xx"), g_df = co["xx", "df"], g_p = co["xx", "Pr(>|t|)"],
       rho = g / b, rho_ci = g / b + c(-1, 1) * z * rho_se)
}
shape_verdict <- function(gate_lo, lo, hi, rel_lo, rel_hi, bounds) {
  if (gate_lo <= 0) return("gate failed: no measurable anchoring, shape not testable")
  if (rel_lo > bounds[1] && rel_hi < bounds[2]) return("flat")
  if (lo > 0) return("rising")
  if (hi < 0) return("falling")
  "inconclusive"
}
h1 <- list(pooled = fit_h1(W), random = fit_h1(W[anchortype == 1]), fixed = fit_h1(W[anchortype != 1]))
h1_tab <- rbindlist(lapply(names(h1), function(k) with(h1[[k]], data.table(
  set = k, n_rows, n_cells, n_participants, random_structure,
  b, b_lo = b_ci[1], b_hi = b_ci[2], g, g_lo = g_ci[1], g_hi = g_ci[2], g_df, g_p,
  rho, rho_lo = rho_ci[1], rho_hi = rho_ci[2],
  verdict = shape_verdict(b_ci[1], g_ci[1], g_ci[2], rho_ci[1], rho_ci[2], rho_bounds)))))

# ---- H2: across-cell anchoring index -------------------------------------------------------------
ci_A <- cell_indices(A, cells_A)
fit_h2 <- function(ci, mods = ~ extremity) {
  m <- tryCatch(rma.mv(ai, ai_se^2, mods = mods, random = ~ 1 | study / cell, data = ci, method = "REML"),
                error = function(e) NULL)
  robust_fallback <- is.null(m)
  if (robust_fallback) {   # Q23 fallback
    m <- robust(rma(ai, ai_se^2, mods = mods, data = ci, method = "REML"), cluster = ci$study,
                clubSandwich = requireNamespace("clubSandwich", quietly = TRUE))
  }
  list(model = m, robust_fallback = robust_fallback)
}
h2_mean <- fit_h2(ci_A, mods = ~ 1)$model
h2 <- fit_h2(ci_A)
h2_coef <- function(m, term = "extremity") {
  i <- which(rownames(m$beta) == term)
  c(est = m$beta[i], lo = m$ci.lb[i], hi = m$ci.ub[i], p = m$pval[i])
}
s2 <- h2_coef(h2$model)
h2_tab <- data.table(n_cells = nrow(ci_A), n_studies = uniqueN(ci_A$study), n_rows = nrow(drop_gross_errors(A)),
                     mean_ai = h2_mean$beta[1], mean_ai_lo = h2_mean$ci.lb, mean_ai_hi = h2_mean$ci.ub,
                     slope = s2[["est"]], slope_lo = s2[["lo"]], slope_hi = s2[["hi"]], slope_p = s2[["p"]],
                     robust_fallback = h2$robust_fallback)
h2_tab[, verdict := shape_verdict(mean_ai_lo, slope_lo, slope_hi, slope_lo, slope_hi, slope_bounds)]

# ---- H3: model adequacy ----------------------------------------------------------------------------
pi <- fread(file.path("output", "predictive_intervals.csv"))
obs <- list(g = h1$pooled$g, rho = h1$pooled$rho, slope = h2_tab$slope,
            # same estimator as fit_across() in the simulation (deviation D1 in deviations.md)
            mean_ai_weighted = weighted.mean(ci_A$ai, 1 / ci_A$ai_se^2))
h3_tab <- pi[, .(model,
                 g_inside = obs$g >= g_lo & obs$g <= g_hi,
                 rho_inside = obs$rho >= rho_lo & obs$rho <= rho_hi,
                 slope_inside = obs$slope >= slope_lo & obs$slope <= slope_hi,
                 b_inside = h1$pooled$b >= b_lo & h1$pooled$b <= b_hi,
                 mean_ai_inside = obs$mean_ai_weighted >= ai_lo & obs$mean_ai_weighted <= ai_hi,
                 mean_ai_weighted = obs$mean_ai_weighted)]
# Shape criteria decide survival; level criteria (b, mean index) depend on the calibration to
# Jacowitz & Kahneman and are reported separately. M0 is also contradicted when gate G1 passes.
h3_tab[, survives_shape := (g_inside | rho_inside) & slope_inside]
h3_tab[model == "M0", survives_shape := survives_shape & h1$pooled$b_ci[1] <= 0]
h3_tab[, survives_level := b_inside & mean_ai_inside]

# ---- Robustness (Q24) ------------------------------------------------------------------------------
rob <- list()
# R1: median regression without the gross-error rule, participant-cluster bootstrap
{
  d <- copy(W)[, xx := x * abs(x)]
  f <- y ~ 0 + factor(cell) + factor(cell):x + xx
  est <- coef(rq(f, tau = 0.5, data = d))["xx"]
  pids <- unique(d$pid)
  set.seed(20260927)
  boot <- replicate(if (dry_run) 100 else 1000, {
    s <- data.table(pid = sample(pids, replace = TRUE))[, draw := .I]
    bd <- d[s, on = "pid", allow.cartesian = TRUE]
    tryCatch(coef(rq(f, tau = 0.5, data = bd))["xx"], error = function(e) NA_real_)
  })
  rob$R1_median_regression_g <- c(est = unname(est), lo = unname(quantile(boot, .025, na.rm = TRUE)), hi = unname(quantile(boot, .975, na.rm = TRUE)))
}
# R2: piecewise slopes, knot at |x| = 1
{
  d <- drop_gross_errors(W)[, h := sign(x) * pmax(abs(x) - 1, 0)]
  m <- withCallingHandlers(lmerTest::lmer(y ~ x + h + (1 + x + h || cell) + (1 | pid), data = d),
                           warning = function(w) { message("R2 warning: ", conditionMessage(w)); invokeRestart("muffleWarning") })
  co <- summary(m)$coefficients
  rob$R2_far_minus_near_slope <- c(est = co["h", "Estimate"], lo = co["h", "Estimate"] - qt(.975, co["h", "df"]) * co["h", "Std. Error"],
                                   hi = co["h", "Estimate"] + qt(.975, co["h", "df"]) * co["h", "Std. Error"])
}
# R3: without Bahník (2021a)
{
  f3 <- withCallingHandlers(fit_h1(W[reference_short != "Bahník, 2021a"]),
                            warning = function(w) { message("R3 warning: ", conditionMessage(w)); invokeRestart("muffleWarning") })
  rob$R3_without_bahnik_g <- c(est = f3$g, lo = f3$g_ci[1], hi = f3$g_ci[2])
}
# R4: raw-scale anchoring index
{
  r <- merge(drop_gross_errors(A)[, .(cell, anchorhigh, est)], cells_A[, .(cell, study, a_low, a_high, extremity)], by = "cell")
  ci4 <- r[, .(ai = (median(est[anchorhigh == 1]) - median(est[anchorhigh == 0])) / (a_high[1] - a_low[1]),
               ai_se = 1.2533 * sqrt(mad(est[anchorhigh == 1])^2 / sum(anchorhigh == 1) + mad(est[anchorhigh == 0])^2 / sum(anchorhigh == 0)) / (a_high[1] - a_low[1]),
               study = study[1], extremity = extremity[1]), by = cell][ai_se > 0]
  rob$R4_raw_index_slope <- h2_coef(fit_h2(ci4)$model)
}
# R5: covariates
{
  cov <- unique(sets$across_rows[, .(cell, anchortype = factor(anchortype), comparative_question, direction,
                                     incentive_any = as.integer(incentive != 0), experiment_type = factor(experiment_type))], by = "cell")
  ci5 <- merge(ci_A, cov, by = "cell")
  keep <- names(which(sapply(ci5[, .(anchortype, comparative_question, direction, incentive_any, experiment_type)], uniqueN) > 1))
  rob$R5_covariates_slope <- h2_coef(fit_h2(ci5, mods = reformulate(c("extremity", keep)))$model)
}
# R6: without Weber et al. (2021)
rob$R6_without_weber_slope <- h2_coef(fit_h2(ci_A[study != "Weber et al., 2021"])$model)
# R7: alternative extremity measures
{
  ci7 <- copy(ci_A)[, `:=`(ext_max = pmax(abs(x_low), abs(x_high)), ext_spread = x_high - x_low)]
  rob$R7_max_distance_slope <- h2_coef(fit_h2(ci7, mods = ~ ext_max)$model, "ext_max")
  rob$R7_log_spread_slope <- h2_coef(fit_h2(ci7, mods = ~ ext_spread)$model, "ext_spread")
}
rob_tab <- rbindlist(lapply(names(rob), function(k) data.table(analysis = k, est = rob[[k]][1], lo = rob[[k]][2], hi = rob[[k]][3])))

# ---- Save ------------------------------------------------------------------------------------------
fwrite(exclusions, file.path(out_dir, "exclusions.csv"))
fwrite(h1_tab, file.path(out_dir, "h1_within.csv"))
fwrite(h2_tab, file.path(out_dir, "h2_across.csv"))
fwrite(ci_A, file.path(out_dir, "h2_cell_indices.csv"))
fwrite(h3_tab, file.path(out_dir, "h3_model_adequacy.csv"))
fwrite(rob_tab, file.path(out_dir, "robustness.csv"))
saveRDS(list(h1 = h1, h2 = h2, h2_mean = h2_mean, W = W, A = A, ci_A = ci_A), file.path(out_dir, "fits.rds"))
print(exclusions); print(h1_tab); print(h2_tab); print(h3_tab); print(rob_tab)
