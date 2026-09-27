# Markdown tables for the preregistration (Q4, Q20, Q21), generated from the simulation outputs
# so that no number is typed by hand.

suppressPackageStartupMessages(library(data.table))
r <- fread(file.path("output", "predictions_raw.csv"))[!is.na(b)]
f <- function(v) sprintf("%.3f [%.3f, %.3f]", median(v), quantile(v, .025), quantile(v, .975))
pred <- r[, .(b = f(b), g = f(g), rho = if (.BY$model == "M0") "undefined" else f(rho),
              g_random = f(g_random), g_fixed = f(g_fixed), d = f(across_slope), ai = f(across_mean_ai)), by = model]
lines <- c("| Model | b (average elasticity) | g (curvature) | rho = g / b | g, random-anchor stratum | g, fixed-anchor stratum | d (across-cell slope) | mean log anchoring index, across cells |",
           "|---|---|---|---|---|---|---|---|",
           pred[, sprintf("| %s | %s | %s | %s | %s | %s | %s | %s |", model, b, g, rho, g_random, g_fixed, d, ai)])

ops <- readLines(file.path("output", "decision_properties.txt"))
z <- qnorm(0.975)
rho_bounds <- c(-0.05, 0.05); slope_bounds <- c(-0.03, 0.03)
v <- function(est, se, bounds, rel_est = est, rel_se = se, gate_ok = rep(TRUE, length(est))) {
  fifelse(!gate_ok, "gate failed",
    fifelse(rel_est - z * rel_se > bounds[1] & rel_est + z * rel_se < bounds[2], "flat",
      fifelse(est - z * se > 0, "rising", fifelse(est + z * se < 0, "falling", "inconclusive"))))
}
r[, h1 := v(g, g_se, rho_bounds, rho, rho_se, b - z * b_se > 0)]
r[, h2 := v(across_slope, across_slope_se, slope_bounds, gate_ok = across_mean_ai > 0.01)]
share <- function(col, lev) r[, round(mean(get(col) == lev), 3), by = model]$V1
levs <- c("rising", "falling", "flat", "inconclusive", "gate failed")
opt <- data.table(model = unique(r$model))
for (l in levs) { opt[, paste0("H1 ", l) := share("h1", l)]; opt[, paste0("H2 ", l) := share("h2", l)] }
cols <- c(paste0("H1 ", levs), paste0("H2 ", levs))
ops_lines <- c(paste0("| Generating model | ", paste(cols, collapse = " | "), " |"),
               paste0("|", paste(rep("---", length(cols) + 1), collapse = "|"), "|"),
               apply(opt[, c("model", cols), with = FALSE], 1, function(x) paste0("| ", paste(x, collapse = " | "), " |")))
writeLines(c("## Predictions (Q20)", "", lines, "", "## Operating characteristics (Q21)", "", ops_lines),
           file.path("output", "prereg_tables.md"))
cat(readLines(file.path("output", "prereg_tables.md")), sep = "\n")
