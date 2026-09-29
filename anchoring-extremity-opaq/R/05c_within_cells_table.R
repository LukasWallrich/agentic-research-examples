# Descriptive table of the within-item cells (after exclusions), for the manuscript.
suppressPackageStartupMessages(library(data.table))
source(file.path("R", "estimators.R"))
f <- readRDS(file.path("output", "confirmatory", "fits.rds"))
W <- drop_gross_errors(f$W)
tab <- W[, .(item = anchoring_item[1], true_value = t[1], estimates = .N, participants = uniqueN(pid),
             anchor_levels = uniqueN(a), anchor_min = min(a), anchor_max = max(a),
             x_min = min(x), x_max = max(x),
             anchor_type = fifelse(anchortype[1] == 1, "random", "fixed"),
             sides = fifelse(all(x > 0), "above truth only", fifelse(all(x < 0), "below truth only", "both"))),
         by = .(study = reference_short, cell)][, cell := NULL][]
fwrite(tab, file.path("output", "within_cells_table.csv"))
print(tab)
