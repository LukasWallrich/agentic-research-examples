# Operating characteristics of the preregistered decision rules, computed on the simulated
# predictions: how often each rule reaches each verdict when each model generated the data.

suppressPackageStartupMessages(library(data.table))
r <- fread(file.path("output", "predictions_raw.csv"))[!is.na(b)]

rho_bounds <- c(-0.05, 0.05)     # equivalence bounds for relative curvature (H1)
slope_bounds <- c(-0.03, 0.03)   # equivalence bounds for the across-cell slope (H2)
z <- qnorm(0.975)

verdict <- function(est, se, bounds, rel_est = est, rel_se = se, gate_ok = rep(TRUE, length(est))) {
  lo <- est - z * se; hi <- est + z * se
  rlo <- rel_est - z * rel_se; rhi <- rel_est + z * rel_se
  fifelse(!gate_ok, "gate failed",
    fifelse(rlo > bounds[1] & rhi < bounds[2], "flat",
      fifelse(lo > 0, "rising",
        fifelse(hi < 0, "falling", "inconclusive"))))
}
r[, gate := b - z * b_se > 0]
r[, h1 := verdict(g, g_se, rho_bounds, rho, rho_se, gate)]
r[, h2 := verdict(across_slope, across_slope_se, slope_bounds, gate_ok = across_mean_ai > 0.01)]

tab <- function(v) dcast(r[, .N, by = .(model, v = get(v))][, share := round(N / sum(N), 3), by = model],
                         model ~ v, value.var = "share", fill = 0)
ops <- list(H1 = tab("h1"), H2 = tab("h2"))
q <- function(v) sprintf("%.3f [%.3f, %.3f]", median(v), quantile(v, .025), quantile(v, .975))
intervals <- r[, .(b = q(b), g = q(g), rho = q(rho), g_random = q(g_random), g_fixed = q(g_fixed),
                   across_slope = q(across_slope), across_mean_ai = q(across_mean_ai)), by = model]
bounds <- r[, .(b_lo = quantile(b, .025), b_hi = quantile(b, .975), g_lo = quantile(g, .025), g_hi = quantile(g, .975),
                rho_lo = quantile(rho, .025), rho_hi = quantile(rho, .975),
                slope_lo = quantile(across_slope, .025), slope_hi = quantile(across_slope, .975),
                ai_lo = quantile(across_mean_ai, .025), ai_hi = quantile(across_mean_ai, .975)), by = model]
fwrite(bounds, file.path("output", "predictive_intervals.csv"))
fwrite(intervals, file.path("output", "predictions_summary.csv"))
sink(file.path("output", "decision_properties.txt"))
cat("Equivalence bounds: rho", rho_bounds, "; across-cell slope", slope_bounds, "\n\nH1 verdict shares by generating model\n")
print(ops$H1); cat("\nH2 verdict shares by generating model\n"); print(ops$H2)
cat("\nModel predictive intervals (median [2.5%, 97.5%])\n"); print(intervals)
sink()
cat(readLines(file.path("output", "decision_properties.txt")), sep = "\n")
