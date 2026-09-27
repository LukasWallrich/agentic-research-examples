# Inclusion rules shared by the prediction simulation and the confirmatory analysis.
# build_sets() works on design columns; when `estimate` is present it is carried along.

source(file.path("R", "read_opaq.R"))

ratio_tasktypes <- c("quantity", "number", "price", "length", "height", "distance",
                     "weight", "population", "volume", "speed", "duration", "birth rate",
                     "income", "width", "area", "circumference", "age")
# Studies whose anchors were computed from each participant's own unanchored estimates.
endogenous_anchor_studies <- c("Röseler & Wagner, 2021")

min_levels_within <- 3     # distinct anchor values per cell for the within-item set
min_log_spread <- 0.25     # across-cell set: log(A_high / A_low) of at least 0.25
min_n_side <- 10           # across-cell set: at least 10 estimates per anchor side

build_sets <- function(d) {
  d <- copy(d)
  d[, `:=`(a = suppressWarnings(as.numeric(anchor)), t = suppressWarnings(as.numeric(true_value)))]
  d[, cell := paste(reference_short, anchoring_item, sep = " || ")]
  d[, pid := paste(reference_short, participant_id, sep = " || ")]
  base <- d[anchortype %in% 1:3 & scaletype == 1 & tasktype %in% ratio_tasktypes &
              !is.na(a) & a > 0 & !is.na(t) & t > 0 &
              !reference_short %in% endogenous_anchor_studies]
  base[, t := t[1], by = cell]   # one true value per cell
  base[, x := log(a / t)]        # anchor position relative to truth (log scale)

  lev <- base[, .(n_levels = uniqueN(a), anchortype = min(anchortype)), by = cell]
  within <- base[cell %in% lev[n_levels >= min_levels_within, cell]]

  pairs <- base[anchortype %in% 2:3 & !is.na(anchorhigh)]
  pc <- pairs[, .(study = reference_short[1], item = anchoring_item[1], t = t[1],
                  n_low_values = uniqueN(a[anchorhigh == 0]), n_high_values = uniqueN(a[anchorhigh == 1]),
                  a_low = a[anchorhigh == 0][1], a_high = a[anchorhigh == 1][1],
                  n_low = sum(anchorhigh == 0), n_high = sum(anchorhigh == 1),
                  anchortype = anchortype[1]), by = cell]
  pc <- pc[n_low_values == 1 & n_high_values == 1 & a_high > a_low &
             log(a_high / a_low) >= min_log_spread & n_low >= min_n_side & n_high >= min_n_side]
  pc[, `:=`(x_low = log(a_low / t), x_high = log(a_high / t))]
  pc[, extremity := (abs(x_low) + abs(x_high)) / 2]
  across <- pairs[cell %in% pc$cell]

  list(within = within, across_rows = across, across_cells = pc)
}
