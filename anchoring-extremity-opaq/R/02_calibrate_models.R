# Calibrate each process model to Jacowitz & Kahneman (1995): keep the parameter values whose
# anchoring index in their design lies in [0.30, 0.60] (reported mean index: about .49).
# Uses no OpAQ data.

suppressPackageStartupMessages(library(data.table))
source(file.path("R", "models.R"))
set.seed(20260927)

jk_band <- c(0.30, 0.60)
grids <- list(
  M1 = CJ(s = c(0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5, 2), t = c(1:10, 12, 15, 20, 25, 30, 40, 50, 60)),
  M1R = CJ(s = c(0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5, 2),
            cost = c(0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2),
            kappa = c(0.25, 0.5, 0.75, 1)),
  M2 = data.table(w = seq(0.05, 0.95, by = 0.01)),
  M3 = data.table(k = seq(0.05, 3, by = 0.025)),
  M4 = CJ(w = seq(0.1, 1, by = 0.05), c = seq(0.3, 4, by = 0.1))
)
calib <- rbindlist(lapply(names(grids), function(m) {
  g <- copy(grids[[m]])
  g[, jk := sapply(seq_len(.N), function(i) jk_index(m, as.list(g[i])))]
  g[, model := m][]
}), fill = TRUE)
calib[, accepted := jk >= jk_band[1] & jk <= jk_band[2]]
fwrite(calib, file.path("output", "calibration_grid.csv"))
print(calib[, .(grid_points = .N, accepted = sum(accepted), jk_min = round(min(jk), 2), jk_max = round(max(jk), 2)), by = model])
