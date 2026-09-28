# Exploratory analyses requested in review round 2 (coarse-review; not preregistered).
# E7  plausibility-discounted integration with a weight floor (M4f), relaxed parameter draws:
#     can it reproduce the within-item b and g and the across-cell d and mean index jointly?
# E8  two-step item-level curvature: quadratic fit per cell, then random-effects meta-analysis.
# E9  multi-band piecewise response function: separate slopes for |x| in [0, .5), [.5, 1),
#     [1, 2), [2, 3) and [3, inf).
# E10 item-level curvature against the spread of estimates for anchors near the true value.

suppressPackageStartupMessages({ library(data.table); library(lmerTest); library(metafor); library(parallel) })
source(file.path("R", "design_sets.R"))
source(file.path("R", "models.R"))
source(file.path("R", "estimators.R"))
out_dir <- file.path("output", "exploratory")
fits <- readRDS(file.path("output", "confirmatory", "fits.rds"))
W <- drop_gross_errors(fits$W)[, xx := x * abs(x)]
res <- list()
row <- function(est, lo, hi) c(est = unname(est), lo = unname(lo), hi = unname(hi))

# ---- E8 --------------------------------------------------------------------------------------
e8 <- W[, {
  co <- coef(summary(lm(y ~ x + xx)))
  list(study = reference_short[1], n = .N, g = co["xx", 1], g_se = co["xx", 2])
}, by = cell]
m8 <- rma(g, g_se^2, data = e8, method = "REML")
res$E8_two_step_pooled_g <- row(m8$beta[1], m8$ci.lb, m8$ci.ub)
res$E8_tau <- row(sqrt(m8$tau2), NA, NA)
res$E8_I2 <- row(m8$I2, NA, NA)
m8b <- rma(g, g_se^2, data = e8[study == "Bahník, 2021a"], method = "REML")
res$E8_two_step_bahnik_g <- row(m8b$beta[1], m8b$ci.lb, m8b$ci.ub)
res$E8_bahnik_g_range <- row(median(e8[study == "Bahník, 2021a"]$g), min(e8[study == "Bahník, 2021a"]$g), max(e8[study == "Bahník, 2021a"]$g))
res$E8_cells_negative <- row(sum(e8$g < 0), NA, nrow(e8))

# ---- E9 --------------------------------------------------------------------------------------
knots <- c(0.5, 1, 2, 3)
for (k in knots) W[, paste0("h", k) := sign(x) * pmax(abs(x) - k, 0)]
hn <- paste0("h", knots)
m9 <- suppressWarnings(lmerTest::lmer(reformulate(c("x", hn, "(1 + x || cell)", "(1 | pid)"), "y"), data = W))
b9 <- fixef(m9); V9 <- as.matrix(vcov(m9))
bands <- c("0-0.5", "0.5-1", "1-2", "2-3", "3+")
e9 <- rbindlist(lapply(seq_along(bands), function(i) {
  terms <- c("x", hn[seq_len(i - 1)])
  est <- sum(b9[terms]); se <- sqrt(sum(V9[terms, terms]))
  data.table(band = bands[i], slope = est, lo = est - 1.96 * se, hi = est + 1.96 * se,
             n = W[abs(x) >= c(0, knots)[i] & abs(x) < c(knots, Inf)[i], .N])
}))
fwrite(e9, file.path(out_dir, "E9_band_slopes.csv"))

# ---- E10 -------------------------------------------------------------------------------------
sp <- W[abs(x) < 0.5, .(near_n = .N, spread = mad(y)), by = cell]
e10 <- merge(e8, sp, by = "cell")[near_n >= 20]
m10 <- rma(g, g_se^2, mods = ~ spread, data = e10, method = "REML")
res$E10_slope_g_on_spread <- row(m10$beta[2], m10$ci.lb[2], m10$ci.ub[2])
res$E10_cells <- row(nrow(e10), NA, NA)
res$E10_correlation <- row(cor(e10$g, e10$spread), NA, NA)
fwrite(e10, file.path(out_dir, "E10_curvature_vs_spread.csv"))
fwrite(e8, file.path(out_dir, "E8_cell_curvatures.csv"))

# ---- E7 --------------------------------------------------------------------------------------
respond_floor <- function(x, mu, sigma, par) {
  d <- x - mu
  mu + par$w * d * (par$f + (1 - par$f) * exp(-d^2 / (2 * (par$c * sigma)^2)))
}
h1 <- fread(file.path("output", "confirmatory", "h1_within.csv"))[set == "pooled"]
h2 <- fread(file.path("output", "confirmatory", "h2_across.csv"))
sets <- build_sets(read_opaq(include_outcomes = FALSE))
within_rows <- sets$within[, .(cell, pid, x)]
across_rows <- sets$across_rows[, .(cell, pid, x, anchorhigh)]
cells <- unique(c(within_rows$cell, across_rows$cell))
sim_floor <- function(rows, cellpar, par) {
  r <- merge(rows[, .(row_id = .I, cell, pid, x)], cellpar, by = "cell")[order(row_id)]
  persons <- unique(r$pid)
  u <- setNames(rnorm(length(persons), 0, 0.15), persons)
  mu <- r$bias + u[r$pid] + rnorm(nrow(r), 0, belief_sd_share * r$sigma)
  y <- respond_floor(r$x, mu, r$sigma, par) + rnorm(nrow(r), 0, response_sd_share * r$sigma)
  gross <- runif(nrow(r)) < contamination_p
  y[gross] <- y[gross] + rnorm(sum(gross), 0, contamination_sd)
  y
}
e7 <- rbindlist(mclapply(1:400, function(i) {
  set.seed(9.5e5 + i)
  par <- list(w = runif(1, 0.1, 1), c = runif(1, 0.3, 6), f = runif(1, 0, 0.8))
  cellpar <- data.table(cell = cells, sigma = runif(length(cells), 0.3, 1.2), bias = rnorm(length(cells), runif(1, -0.3, 0.3), 0.3))
  w <- copy(within_rows)[, y := sim_floor(within_rows, cellpar, par)]
  a <- copy(across_rows)[, y := sim_floor(across_rows, cellpar, par)]
  fw <- tryCatch(fit_within(w), error = function(e) NULL)
  fa <- tryCatch(fit_across(cell_indices(a, sets$across_cells)), error = function(e) NULL)
  if (is.null(fw) || is.null(fa)) return(NULL)
  data.table(rep = i, w = par$w, c = par$c, f = par$f, b = fw$b, g = fw$g, d = fa$slope, mean_ai = fa$mean_ai)
}, mc.cores = 8))
w_ai <- fread(file.path("output", "confirmatory", "h3_model_adequacy.csv"))$mean_ai_weighted[1]
e7[, within_ok := b >= h1$b_lo & b <= h1$b_hi & g >= h1$g_lo & g <= h1$g_hi]
e7[, across_ok := d >= h2$slope_lo & d <= h2$slope_hi]
fwrite(e7, file.path(out_dir, "E7_floor_model_draws.csv"))
res$E7_draws <- row(nrow(e7), NA, NA)
res$E7_within_b_g <- row(sum(e7$within_ok), NA, NA)
res$E7_across_d <- row(sum(e7$across_ok), NA, NA)
res$E7_both <- row(sum(e7$within_ok & e7$across_ok), NA, NA)

tab <- rbindlist(lapply(names(res), function(k) data.table(analysis = k, est = res[[k]][1], lo = res[[k]][2], hi = res[[k]][3])))
fwrite(tab, file.path(out_dir, "round2_exploratory.csv"))
print(tab); print(e9); print(e7[within_ok & across_ok])
