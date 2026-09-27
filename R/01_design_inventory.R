# Design-only inventory of OpAQ: counts of studies, items and anchor configurations.
# Reads design columns only (see R/read_opaq.R); no estimates are loaded.

source(file.path("R", "read_opaq.R"))
d <- read_opaq(include_outcomes = FALSE)
out <- file.path("output", "design_inventory.txt")
sink(out)

cat("Rows:", nrow(d), "\nStudies (reference_short):", uniqueN(d$reference_short),
    "\nItems (anchoring_item text):", uniqueN(d$anchoring_item),
    "\nItem x study cells:", uniqueN(d[, .(reference_short, anchoring_item)]), "\n\n")

for (v in c("anchortype", "scaletype", "comparative_question", "direction", "incentive",
            "experiment_type", "stimulitype", "sampletype", "anchorhigh")) {
  cat("--", v, "(rows)\n"); print(d[, .N, by = v][order(get(v))])
}
cat("-- tasktype (rows, top 40)\n"); print(head(d[, .N, by = tasktype][order(-N)], 40))

d[, anchor_num := suppressWarnings(as.numeric(anchor))]
d[, true_num := suppressWarnings(as.numeric(true_value))]
cat("\nRows with non-numeric anchor:", d[is.na(anchor_num), .N],
    "\nRows with missing/non-numeric true value:", d[is.na(true_num), .N], "\n")

cells <- d[!is.na(anchor_num) & !is.na(anchorhigh), .(
  n = .N, n_anchor_values = uniqueN(anchor_num),
  n_high_values = uniqueN(anchor_num[anchorhigh == 1]), n_low_values = uniqueN(anchor_num[anchorhigh == 0]),
  n_high = sum(anchorhigh == 1, na.rm = TRUE), n_low = sum(anchorhigh == 0, na.rm = TRUE),
  anchortype = paste(sort(unique(anchortype)), collapse = "/"),
  scaletype = paste(sort(unique(scaletype)), collapse = "/"),
  tasktype = tasktype[1], true = true_num[1],
  a_low = if (any(anchorhigh == 0)) median(anchor_num[anchorhigh == 0]) else NA_real_,
  a_high = if (any(anchorhigh == 1)) median(anchor_num[anchorhigh == 1]) else NA_real_
), by = .(reference_short, anchoring_item)]

cat("\n-- Item x study cells by anchor configuration\n")
print(cells[, .N, by = .(has_both_sides = n_high > 0 & n_low > 0,
                         two_fixed_values = n_high_values == 1 & n_low_values == 1)])
cat("\n-- Cells by anchortype\n"); print(cells[, .N, by = anchortype][order(-N)])
cat("\n-- Cells by scaletype\n"); print(cells[, .N, by = scaletype][order(-N)])

pair <- cells[n_high_values == 1 & n_low_values == 1 & anchortype %in% c("2", "3")]
pair[, `:=`(pos = a_low > 0 & a_high > 0 & !is.na(true) & true > 0)]
pair[pos == TRUE, `:=`(log_spread = log(a_high / a_low),
                       log_ext_high = log(a_high / true), log_ext_low = log(true / a_low))]
cat("\n-- Classic fixed two-anchor cells (anchortype 2/3):", nrow(pair),
    "; with positive anchors and true value:", pair[pos == TRUE, .N],
    "; open scale:", pair[pos == TRUE & scaletype == "1", .N], "\n")
cat("   n per cell (quantiles):\n"); print(quantile(pair$n, c(0, .1, .25, .5, .75, .9, 1)))
cat("   log(A_high/A_low) quantiles:\n"); print(quantile(pair$log_spread, c(0, .05, .1, .25, .5, .75, .9, .95, 1), na.rm = TRUE))
cat("   log(A_high/true) quantiles:\n"); print(quantile(pair$log_ext_high, c(0, .05, .1, .25, .5, .75, .9, .95, 1), na.rm = TRUE))
cat("   log(true/A_low) quantiles:\n"); print(quantile(pair$log_ext_low, c(0, .05, .1, .25, .5, .75, .9, .95, 1), na.rm = TRUE))
cat("   Cells where true value lies outside [A_low, A_high]:",
    pair[pos == TRUE & (true < a_low | true > a_high), .N], "\n")

cat("\n-- Within-item extremity variation\n")
multi <- cells[n_high_values > 1 | n_low_values > 1]
cat("Cells with >1 distinct anchor value on a side:", nrow(multi), "\n")
print(multi[, .(reference_short, anchoring_item, n_high_values, n_low_values, anchortype, n)][order(-n)][1:min(.N, 40)])
across <- pair[, .(n_studies = .N, n_spreads = uniqueN(round(log_spread, 3))), by = anchoring_item][n_studies > 1]
cat("\nItems (by identical text) appearing in >1 study as classic pairs:", nrow(across),
    "; with >1 distinct spread:", across[n_spreads > 1, .N], "\n")
print(head(across[order(-n_studies)], 30))
cat("\n-- Studies contributing classic pairs:", uniqueN(pair$reference_short), "\n")
print(pair[, .(cells = .N), by = reference_short][order(-cells)])
sink()
fwrite(cells, file.path("output", "design_cells.csv"))
message("Wrote ", out)
