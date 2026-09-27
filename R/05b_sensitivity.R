# Post-hoc sensitivity analyses added after the code review (not preregistered; see deviations.md).
# S1 recalibrate the models to Jacowitz & Kahneman's raw-scale index and regenerate predictions;
# S2 study dependence of H1 (leave-one-study-out; study random effects);
# S3 influence and dependence checks for H2 (leave-one-study-out; study-clustered robust CI;
#    without the ten cells with the largest weights).

suppressPackageStartupMessages({ library(data.table); library(lmerTest); library(metafor); library(parallel) })
source(file.path("R", "design_sets.R"))
source(file.path("R", "models.R"))
source(file.path("R", "estimators.R"))
out_dir <- file.path("output", "sensitivity")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
fits <- readRDS(file.path("output", "confirmatory", "fits.rds"))
res <- list()
row <- function(est, lo, hi) c(est = unname(est), lo = unname(lo), hi = unname(hi))

# ---- S1: raw-scale calibration ---------------------------------------------------------------
# The raw-scale index depends on the item's log uncertainty sigma, so it is averaged over the
# same sigma range the prediction simulation uses.
jk_index_raw <- function(model, par, n = 20000, sigmas = c(0.3, 0.6, 0.9, 1.2)) {
  sd_unanchored <- sqrt(belief_sd_share^2 + response_sd_share^2)
  mean(sapply(sigmas, function(sg) {
    a <- qnorm(0.85) * sd_unanchored * sg
    y_of <- function(x) {
      mu <- rnorm(n, 0, belief_sd_share * sg)
      exp(respond(model, rep(x, n), mu, sg, par) + rnorm(n, 0, response_sd_share * sg))
    }
    (median(y_of(a)) - median(y_of(-a))) / (exp(a) - exp(-a))
  }))
}
set.seed(20260928)
grid <- fread(file.path("output", "calibration_grid.csv"))[model != "M0"]
invisible(lapply(unique(na.omit(grid$s)), rr_error_curves))
grid[, jk_raw := unlist(mclapply(seq_len(.N), function(i) {
  set.seed(i)
  p <- as.list(grid[i, intersect(c("s", "t", "cost", "kappa", "w", "k", "c"), names(grid)), with = FALSE])
  jk_index_raw(grid$model[i], p[!sapply(p, is.na)])
}, mc.cores = 8))]
grid[, accepted_raw := jk_raw >= 0.30 & jk_raw <= 0.60]
fwrite(grid, file.path(out_dir, "S1_calibration_raw.csv"))
res$S1_accepted_points <- grid[, .(log_scale = sum(accepted), raw_scale = sum(accepted_raw), both = sum(accepted & accepted_raw)), by = model]

sets <- build_sets(read_opaq(include_outcomes = FALSE))
within_rows <- sets$within[, .(cell, pid, x, anchortype)]
across_rows <- sets$across_rows[, .(cell, pid, x, anchorhigh)]
cells <- unique(c(within_rows$cell, across_rows$cell))
acc <- grid[accepted_raw == TRUE]
jobs <- CJ(model = unique(acc$model), rep = 1:200)
pred <- rbindlist(mclapply(seq_len(nrow(jobs)), function(i) {
  set.seed(9e5 + i)
  mdl <- jobs$model[i]
  g <- acc[acc$model == mdl]
  keep <- names(which(sapply(g, function(v) !all(is.na(v)))))
  par <- as.list(g[sample(.N, 1), intersect(c("s", "t", "cost", "kappa", "w", "k", "c"), keep), with = FALSE])
  cellpar <- data.table(cell = cells, sigma = runif(length(cells), 0.3, 1.2), bias = rnorm(length(cells), runif(1, -0.3, 0.3), 0.3))
  w <- copy(within_rows)[, y := simulate_responses(mdl, within_rows, cellpar, par)]
  a <- copy(across_rows)[, y := simulate_responses(mdl, across_rows, cellpar, par)]
  fw <- tryCatch(fit_within(w), error = function(e) NULL)
  fa <- tryCatch(fit_across(cell_indices(a, sets$across_cells)), error = function(e) NULL)
  if (is.null(fw) || is.null(fa)) return(NULL)
  data.table(model = mdl, b = fw$b, g = fw$g, rho = fw$rho, d = fa$slope, mean_ai = fa$mean_ai)
}, mc.cores = 8))
q <- function(v) sprintf("%.3f [%.3f, %.3f]", median(v), quantile(v, .025), quantile(v, .975))
s1_pi <- pred[, .(reps = .N, b = q(b), g = q(g), rho = q(rho), d = q(d), mean_ai = q(mean_ai),
                  g_lo = quantile(g, .025), g_hi = quantile(g, .975), rho_lo = quantile(rho, .025), rho_hi = quantile(rho, .975),
                  d_lo = quantile(d, .025), d_hi = quantile(d, .975)), by = model]
h1p <- fread(file.path("output", "confirmatory", "h1_within.csv"))[set == "pooled"]
h2 <- fread(file.path("output", "confirmatory", "h2_across.csv"))
s1_pi[, survives_shape := ((h1p$g >= g_lo & h1p$g <= g_hi) | (h1p$rho >= rho_lo & h1p$rho <= rho_hi)) & h2$slope >= d_lo & h2$slope <= d_hi]
fwrite(s1_pi, file.path(out_dir, "S1_predictions_raw_calibration.csv"))

# ---- S2: study dependence of H1 -------------------------------------------------------------
W <- drop_gross_errors(fits$W)[, xx := x * abs(x)]
fit_g <- function(d, f = y ~ x + xx + (1 + x + xx || cell) + (1 | pid)) {
  m <- suppressWarnings(lmerTest::lmer(f, data = d))
  co <- summary(m)$coefficients
  row(co["xx", 1], co["xx", 1] - qt(.975, co["xx", "df"]) * co["xx", 2], co["xx", 1] + qt(.975, co["xx", "df"]) * co["xx", 2])
}
for (s in unique(W$reference_short)) res[[paste0("S2_without_", s)]] <- fit_g(W[reference_short != s])
res$S2_study_random_effect <- fit_g(W, y ~ x + xx + (1 + x + xx || reference_short) + (1 + x + xx || cell) + (1 | pid))
res$S2_bahnik_only <- fit_g(W[reference_short == "Bahník, 2021a"])
res$S2_imhoff_barker_only <- {
  d <- W[reference_short == "Imhoff & Barker, 2022, Study 2"]
  co <- summary(lm(y ~ x + xx, data = d))$coefficients
  row(co["xx", 1], co["xx", 1] - qt(.975, nrow(d) - 3) * co["xx", 2], co["xx", 1] + qt(.975, nrow(d) - 3) * co["xx", 2])
}

# ---- S3: H2 influence and dependence ----------------------------------------------------------
ci_A <- fits$ci_A
h2m <- fits$h2$model
rob <- robust(h2m, cluster = ci_A$study, clubSandwich = TRUE)
res$S3_cluster_robust_slope <- row(rob$beta[2], rob$ci.lb[2], rob$ci.ub[2])
wt <- ci_A[, w := 1 / ai_se^2][order(-w)]
top10 <- wt$cell[1:10]
m10 <- rma.mv(ai, ai_se^2, mods = ~ extremity, random = ~ 1 | study / cell, data = ci_A[!cell %in% top10])
res$S3_without_top10_weight_cells <- row(m10$beta[2], m10$ci.lb[2], m10$ci.ub[2])
loo <- rbindlist(lapply(unique(ci_A$study), function(s) {
  m <- tryCatch(rma.mv(ai, ai_se^2, mods = ~ extremity, random = ~ 1 | study / cell, data = ci_A[study != s]), error = function(e) NULL)
  if (is.null(m)) return(NULL)
  data.table(study = s, slope = m$beta[2], lo = m$ci.lb[2], hi = m$ci.ub[2])
}))
fwrite(loo, file.path(out_dir, "S3_leave_one_study_out.csv"))
res$S3_loo_slope_range <- row(median(loo$slope), min(loo$slope), max(loo$slope))
res$S3_top10_weight_share <- row(sum(wt$w[1:10]) / sum(wt$w), NA, NA)

tab <- rbindlist(lapply(names(res)[names(res) != "S1_accepted_points"], function(k)
  data.table(analysis = k, est = res[[k]][1], lo = res[[k]][2], hi = res[[k]][3])))
fwrite(tab, file.path(out_dir, "sensitivity_results.csv"))
fwrite(res$S1_accepted_points, file.path(out_dir, "S1_accepted_points.csv"))
print(res$S1_accepted_points); print(s1_pi[, .(model, reps, b, g, rho, d, mean_ai, survives_shape)]); print(tab); print(loo)
