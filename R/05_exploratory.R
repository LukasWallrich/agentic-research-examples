# Exploratory analyses (not preregistered; prereg Q25 lists their topics).
# E1 asymmetry of curvature for low vs high anchors; E2 near/far elasticity per within-item cell;
# E3 Hedges' g against extremity across cells; E4 across-cell slope with extremity scaled by the
# spread of responses; E5 relaxed-calibration check of whether any model reproduces the observed
# statistics jointly.

suppressPackageStartupMessages({ library(data.table); library(lmerTest); library(metafor); library(parallel) })
source(file.path("R", "design_sets.R"))
source(file.path("R", "models.R"))
source(file.path("R", "estimators.R"))
out_dir <- file.path("output", "exploratory")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

f <- readRDS(file.path("output", "confirmatory", "fits.rds"))
W <- drop_gross_errors(f$W)
A <- drop_gross_errors(f$A)
ci_A <- f$ci_A
res <- list()

# E1: curvature separately for anchors below and above the true value
{
  d <- copy(W)[, `:=`(xx_neg = fifelse(x < 0, x * abs(x), 0), xx_pos = fifelse(x > 0, x * abs(x), 0))]
  m <- lmerTest::lmer(y ~ x + xx_neg + xx_pos + (1 + x || cell) + (1 | pid), data = d)
  co <- summary(m)$coefficients
  for (term in c("xx_neg", "xx_pos"))
    res[[paste0("E1_", term)]] <- c(est = co[term, "Estimate"], lo = co[term, "Estimate"] - qt(.975, co[term, "df"]) * co[term, "Std. Error"],
                                    hi = co[term, "Estimate"] + qt(.975, co[term, "df"]) * co[term, "Std. Error"])
  e1_counts <- W[, .(below = sum(x < 0), above = sum(x > 0)), by = .(reference_short)]
}

# E2: per-cell OLS with separate slopes for near (|x| <= 1) and far (|x| > 1) anchors
{
  e2 <- W[, {
    h <- sign(x) * pmax(abs(x) - 1, 0)
    ok <- sum(abs(x) > 1) >= 20 && sum(abs(x) <= 1) >= 20
    if (ok) { co <- coef(summary(lm(y ~ x + h))); list(n = .N, slope_near = co["x", 1], slope_far = co["x", 1] + co["h", 1],
                                                       diff = co["h", 1], diff_se = co["h", 2]) }
    else list(n = .N, slope_near = NA_real_, slope_far = NA_real_, diff = NA_real_, diff_se = NA_real_)
  }, by = .(cell, reference_short, anchortype)]
  res$E2_cells_far_below_near <- c(est = e2[!is.na(diff), sum(diff < 0)], lo = NA, hi = e2[!is.na(diff), .N])
}

# E3: Hedges' g per across-set cell (log scale) against extremity, as in Röseler & Schütz (2022)
{
  e3 <- A[, {
    yh <- y[anchorhigh == 1]; yl <- y[anchorhigh == 0]
    n1 <- length(yh); n2 <- length(yl)
    sp <- sqrt(((n1 - 1) * var(yh) + (n2 - 1) * var(yl)) / (n1 + n2 - 2))
    g <- (1 - 3 / (4 * (n1 + n2) - 9)) * (mean(yh) - mean(yl)) / sp   # Hedges' g
    list(g = g, v = (n1 + n2) / (n1 * n2) + g^2 / (2 * (n1 + n2)))
  }, by = cell]
  e3 <- merge(e3, ci_A[, .(cell, study, extremity)], by = "cell")
  m3 <- rma.mv(g, v, mods = ~ extremity, random = ~ 1 | study / cell, data = e3)
  res$E3_hedges_g_slope <- c(est = m3$beta[2], lo = m3$ci.lb[2], hi = m3$ci.ub[2])
}

# E4: extremity in units of the within-condition spread of log responses (outcome-based, so
# contaminated by anchoring; shown only to probe the within/across discrepancy)
{
  sp <- A[, .(spread = sqrt((mad(y[anchorhigh == 1])^2 + mad(y[anchorhigh == 0])^2) / 2)), by = cell]
  e4 <- merge(ci_A, sp, by = "cell")[spread > 0][, ext_z := extremity / spread]
  m4 <- rma.mv(ai, ai_se^2, mods = ~ ext_z, random = ~ 1 | study / cell, data = e4)
  res$E4_slope_on_scaled_extremity <- c(est = m4$beta[2], lo = m4$ci.lb[2], hi = m4$ci.ub[2])
  m4b <- rma.mv(ai, ai_se^2, mods = ~ extremity + spread, random = ~ 1 | study / cell, data = e4)
  res$E4_slope_adjusting_spread <- c(est = m4b$beta[2], lo = m4b$ci.lb[2], hi = m4b$ci.ub[2])
  res$E4_spread_coefficient <- c(est = m4b$beta[3], lo = m4b$ci.lb[3], hi = m4b$ci.ub[3])
}

# E5: relaxed calibration. Draw each model's parameters from wide ranges (not restricted to the
# Jacowitz & Kahneman band) and ask whether any draw reproduces the observed within-item b and g
# and the across-cell d and mean index jointly (each inside the observed 95% CI).
{
  h1 <- fread(file.path("output", "confirmatory", "h1_within.csv"))[set == "pooled"]
  h2 <- fread(file.path("output", "confirmatory", "h2_across.csv"))
  sets <- build_sets(read_opaq(include_outcomes = FALSE))
  within_rows <- sets$within[, .(cell, pid, x, anchortype)]
  across_rows <- sets$across_rows[, .(cell, pid, x, anchorhigh)]
  cells <- unique(c(within_rows$cell, across_rows$cell))
  draw_par <- function(model) switch(model,
    M1 = list(s = sample(c(0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5, 2), 1), t = sample(1:60, 1)),
    M1R = list(s = sample(c(0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5, 2), 1), cost = 10^runif(1, -4, -0.5), kappa = runif(1, 0.2, 1)),
    M2 = list(w = runif(1, 0.02, 0.98)),
    M3 = list(k = runif(1, 0.05, 4)),
    M4 = list(w = runif(1, 0.1, 1), c = runif(1, 0.3, 6)))
  invisible(lapply(c(0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5, 2), rr_error_curves))   # workers inherit the cache
  jobs <- CJ(model = c("M1", "M1R", "M2", "M3", "M4"), rep = 1:300)
  e5 <- rbindlist(mclapply(seq_len(nrow(jobs)), function(i) {
    set.seed(7e5 + i)
    model <- jobs$model[i]; par <- draw_par(model)
    cellpar <- data.table(cell = cells, sigma = runif(length(cells), 0.3, 1.2), bias = rnorm(length(cells), runif(1, -0.3, 0.3), 0.3))
    w <- copy(within_rows)[, y := simulate_responses(model, within_rows, cellpar, par)]
    a <- copy(across_rows)[, y := simulate_responses(model, across_rows, cellpar, par)]
    fw <- tryCatch(fit_within(w), error = function(e) NULL)
    fa <- tryCatch(fit_across(cell_indices(a, sets$across_cells)), error = function(e) NULL)
    if (is.null(fw) || is.null(fa)) return(NULL)
    data.table(model, rep = jobs$rep[i], par = paste(names(par), signif(unlist(par), 3), sep = "=", collapse = ";"),
               b = fw$b, g = fw$g, rho = fw$rho, d = fa$slope, mean_ai = fa$mean_ai)
  }, mc.cores = 8))
  e5[, `:=`(b_ok = b >= h1$b_lo & b <= h1$b_hi, g_ok = g >= h1$g_lo & g <= h1$g_hi,
            d_ok = d >= h2$slope_lo & d <= h2$slope_hi, ai_ok = mean_ai >= h2$mean_ai_lo & mean_ai <= h2$mean_ai_hi)]
  e5[, within_ok := b_ok & g_ok][, all_ok := within_ok & d_ok & ai_ok]
  fwrite(e5, file.path(out_dir, "E5_relaxed_calibration_draws.csv"))
  e5_sum <- e5[, .(draws = .N, within_b_and_g = sum(within_ok), across_d_and_ai = sum(d_ok & ai_ok), all_four = sum(all_ok)), by = model]
  fwrite(e5_sum, file.path(out_dir, "E5_relaxed_calibration_summary.csv"))
}

tab <- rbindlist(lapply(names(res), function(k) data.table(analysis = k, est = res[[k]][1], lo = res[[k]][2], hi = res[[k]][3])))
fwrite(tab, file.path(out_dir, "exploratory_results.csv"))
fwrite(e2, file.path(out_dir, "E2_cell_near_far.csv"))
fwrite(e3, file.path(out_dir, "E3_hedges_g.csv"))
fwrite(e1_counts, file.path(out_dir, "E1_anchor_side_counts.csv"))
print(tab); print(e2); print(e5_sum)
