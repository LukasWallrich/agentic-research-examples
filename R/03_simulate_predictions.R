# Predicted estimator outcomes for each process model on the exact OpAQ designs
# (anchor values, true values, participants and cell sizes). Reads design columns only.

suppressPackageStartupMessages({ library(data.table); library(parallel) })
source(file.path("R", "design_sets.R"))
source(file.path("R", "models.R"))
source(file.path("R", "estimators.R"))

n_reps <- c(M0 = 200, M1 = 500, M1R = 500, M2 = 500, M3 = 500, M4 = 500)
sigma_range <- c(0.3, 1.2)      # belief uncertainty per item (log units)
bias_centre_range <- c(-0.3, 0.3)
bias_sd <- 0.3

sets <- build_sets(read_opaq(include_outcomes = FALSE))
within_rows <- sets$within[, .(cell, pid, x, anchortype)]
across_rows <- sets$across_rows[, .(cell, pid, x, anchorhigh)]
cells <- unique(c(within_rows$cell, across_rows$cell))
calib <- fread(file.path("output", "calibration_grid.csv"))[accepted == TRUE]

one_rep <- function(model, rep) {
  set.seed(1e5 * match(model, names(n_reps)) + rep)
  target <- model
  par <- if (model == "M0") list() else {
    g <- calib[calib$model == target]
    keep <- names(which(sapply(g, function(v) !all(is.na(v)))))
    as.list(g[sample(.N, 1), intersect(c("s", "t", "cost", "kappa", "w", "k", "c"), keep), with = FALSE])
  }
  cellpar <- data.table(cell = cells, sigma = runif(length(cells), sigma_range[1], sigma_range[2]),
                        bias = rnorm(length(cells), runif(1, bias_centre_range[1], bias_centre_range[2]), bias_sd))
  w <- copy(within_rows)[, y := simulate_responses(model, within_rows, cellpar, par)]
  a <- copy(across_rows)[, y := simulate_responses(model, across_rows, cellpar, par)]
  fw <- fit_within(w)
  fr <- fit_within(w[anchortype == 1])
  ff <- fit_within(w[anchortype != 1])
  fa <- fit_across(cell_indices(a, sets$across_cells))
  data.table(model, rep, par = paste(names(par), unlist(par), sep = "=", collapse = ";"),
             b = fw$b, b_se = fw$b_se, g = fw$g, g_se = fw$g_se, rho = fw$rho, rho_se = fw$rho_se,
             b_random = fr$b, g_random = fr$g, g_random_se = fr$g_se, rho_random = fr$rho, rho_random_se = fr$rho_se,
             b_fixed = ff$b, g_fixed = ff$g, g_fixed_se = ff$g_se, rho_fixed = ff$rho, rho_fixed_se = ff$rho_se,
             across_slope = fa$slope, across_slope_se = fa$slope_se, across_mean_ai = fa$mean_ai)
}

jobs <- rbindlist(lapply(names(n_reps), function(m) data.table(model = m, rep = seq_len(n_reps[[m]]))))
res <- rbindlist(mclapply(seq_len(nrow(jobs)), function(i) {
  tryCatch(one_rep(jobs$model[i], jobs$rep[i]), error = function(e) data.table(model = jobs$model[i], rep = jobs$rep[i], error = conditionMessage(e)))
}, mc.cores = 8), fill = TRUE)
fwrite(res, file.path("output", "predictions_raw.csv"))

q <- function(v) paste0(sprintf("%.3f", median(v, na.rm = TRUE)), " [", sprintf("%.3f", quantile(v, .025, na.rm = TRUE)), ", ", sprintf("%.3f", quantile(v, .975, na.rm = TRUE)), "]")
summ <- res[is.na(if ("error" %in% names(res)) error else NA), .(reps = .N, b = q(b), g = q(g), rho = q(rho), g_random = q(g_random), g_fixed = q(g_fixed),
                                  rho_random = q(rho_random), rho_fixed = q(rho_fixed),
                                  b_random = q(b_random), b_fixed = q(b_fixed), across_slope = q(across_slope),
                                  across_mean_ai = q(across_mean_ai), share_g_pos = mean(g > 0)), by = model]
fwrite(summ, file.path("output", "predictions_summary.csv"))
print(summ)
