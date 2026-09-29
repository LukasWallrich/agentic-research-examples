# Post-hoc checks requested in review round 1 (not preregistered; see deviations.md).
# R1a joint predictive check: share of each model's calibrated replicates whose b and g both fall
#     inside the observed 95% CIs.
# R1b near and far slopes (knot at |x| = 1) with CIs.
# R1c study-specific curvature estimates.
# R1d H2 with a participant bootstrap within studies, and a count of participants who answered
#     under both anchors of the same cell.
# R1e H2 with the Chicago cell (Shanks et al., 2020, Study 3) converted from millions.

suppressPackageStartupMessages({ library(data.table); library(lmerTest); library(metafor) })
source(file.path("R", "design_sets.R"))
source(file.path("R", "estimators.R"))
out_dir <- file.path("output", "review_checks")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
fits <- readRDS(file.path("output", "confirmatory", "fits.rds"))
h1 <- fread(file.path("output", "confirmatory", "h1_within.csv"))[set == "pooled"]
res <- list()
row <- function(est, lo, hi) c(est = unname(est), lo = unname(lo), hi = unname(hi))

# R1a
pred <- fread(file.path("output", "predictions_raw.csv"))[!is.na(b)]
joint <- pred[, .(replicates = .N, share_b_and_g_inside = mean(b >= h1$b_lo & b <= h1$b_hi & g >= h1$g_lo & g <= h1$g_hi),
                  share_g_inside = mean(g >= h1$g_lo & g <= h1$g_hi)), by = model]
fwrite(joint, file.path(out_dir, "R1a_joint_predictive_check.csv"))

# R1b
W <- drop_gross_errors(fits$W)[, h := sign(x) * pmax(abs(x) - 1, 0)]
m <- suppressWarnings(lmerTest::lmer(y ~ x + h + (1 + x + h || cell) + (1 | pid), data = W))
co <- summary(m)$coefficients; V <- as.matrix(vcov(m))
far <- co["x", 1] + co["h", 1]; far_se <- sqrt(V["x", "x"] + V["h", "h"] + 2 * V["x", "h"])
res$R1b_near_slope <- row(co["x", 1], co["x", 1] - 1.96 * co["x", 2], co["x", 1] + 1.96 * co["x", 2])
res$R1b_far_slope <- row(far, far - 1.96 * far_se, far + 1.96 * far_se)

# R1c
Wc <- drop_gross_errors(fits$W)[, xx := x * abs(x)]
for (s in unique(Wc$reference_short)) {
  d <- Wc[reference_short == s]
  f <- if (uniqueN(d$cell) >= 4) y ~ x + xx + (1 + x || cell) + (1 | pid) else if (uniqueN(d$cell) > 1) y ~ x + xx + (1 | cell) else y ~ x + xx
  mm <- if (grepl("\\|", deparse(f))) suppressWarnings(lmerTest::lmer(f, data = d)) else lm(f, data = d)
  cc <- summary(mm)$coefficients
  dfv <- if ("df" %in% colnames(cc)) cc["xx", "df"] else df.residual(mm)
  res[[paste0("R1c_g_", s)]] <- row(cc["xx", 1], cc["xx", 1] - qt(.975, dfv) * cc["xx", 2], cc["xx", 1] + qt(.975, dfv) * cc["xx", 2])
}

# R1d
A <- drop_gross_errors(fits$A)
both <- A[, .(both = any(anchorhigh == 1) & any(anchorhigh == 0)), by = .(cell, pid)][, .(participants_in_both_conditions = sum(both)), by = cell]
res$R1d_cells_with_paired_participants <- row(both[participants_in_both_conditions > 0, .N], NA, nrow(both))
cells_A <- fits$ci_A[, .(cell, study, x_low, x_high, extremity)]
set.seed(20260928)
boot <- replicate(200, {
  b <- A[, .(pid = unique(pid)), by = reference_short][, .(pid = sample(pid, .N, replace = TRUE)), by = reference_short][, draw := .I]
  bd <- A[b[, .(pid, draw)], on = "pid", allow.cartesian = TRUE]
  ci <- tryCatch(cell_indices(bd, cells_A)[is.finite(ai) & is.finite(ai_se)], error = function(e) NULL)
  if (is.null(ci)) return(NA_real_)
  tryCatch(fit_across(ci)$slope, error = function(e) NA_real_)
})
res$R1d_h2_slope_participant_bootstrap <- row(median(boot, na.rm = TRUE), quantile(boot, .025, na.rm = TRUE), quantile(boot, .975, na.rm = TRUE))

# R1e
sets <- build_sets(read_opaq(include_outcomes = TRUE))
Ae <- copy(sets$across_rows)[, est := suppressWarnings(as.numeric(estimate))]
chi <- "Shanks et al., 2020, Study 3 || Population of Chicago"
Ae[cell == chi, est := est * 1e6]
Ae <- Ae[!is.na(est) & est > 0][, y := log(est / t)]
Ae <- drop_gross_errors(Ae)
ok <- Ae[, .(n_low = sum(anchorhigh == 0), n_high = sum(anchorhigh == 1)), by = cell][n_low >= min_n_side & n_high >= min_n_side, cell]
ci_e <- cell_indices(Ae[cell %in% ok], sets$across_cells[cell %in% ok])
me <- rma.mv(ai, ai_se^2, mods = ~ extremity, random = ~ 1 | study / cell, data = ci_e)
res$R1e_h2_slope_chicago_converted <- row(me$beta[2], me$ci.lb[2], me$ci.ub[2])
res$R1e_cells <- row(nrow(ci_e), NA, NA)

tab <- rbindlist(lapply(names(res), function(k) data.table(analysis = k, est = res[[k]][1], lo = res[[k]][2], hi = res[[k]][3])))
fwrite(tab, file.path(out_dir, "review_checks.csv"))
print(joint); print(tab)
