# Reader for the OpAQ trial-level file with a blinding guard.
# Design columns can always be read. Outcome columns (the estimate and everything derived
# from it) can only be read once the preregistration is committed to git.

library(data.table)

opaq_path <- file.path("data", "raw", "opaq_70a.csv")
prereg_path <- file.path("prereg", "preregistration.md")

design_cols <- c(
  "reference_short", "reference", "id", "participant_id", "sex", "age", "nationality",
  "anchoring_item", "true_value", "anchor", "anchorhigh", "anchortype", "tasktype",
  "direction", "incentive", "comparative_question", "experiment_type", "stimulitype",
  "sampletype", "scaletype", "published", "preregistered"
)
outcome_cols <- c(
  "estimate", "adjustment", "absadjustment", "score", "restr_score", "zestimate",
  "zadjustment", "zabsadjustment", "zscore", "outlier", "precision", "nchar", "precise", "zsta"
)

prereg_committed <- function() {
  log <- suppressWarnings(system2("git", c("log", "--format=%H", "--", prereg_path),
                                  stdout = TRUE, stderr = FALSE))
  length(log) > 0
}

read_opaq <- function(include_outcomes = FALSE) {
  cols <- design_cols
  if (include_outcomes) {
    if (!prereg_committed()) stop("Outcome columns are blocked until ", prereg_path, " is committed.")
    cols <- c(cols, "estimate")
  }
  fread(opaq_path, select = cols, encoding = "UTF-8", showProgress = FALSE)
}
