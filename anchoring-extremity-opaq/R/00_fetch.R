# Download the Open Anchoring Quest (OpAQ) trial-level data and verify its hash.
# Writes only the header row to data/variables_seen.txt; no data values are read here.

source_url <- "https://osf.io/download/s4zgw/"   # opaq_70a.csv, OSF ygnvb, CC-BY 4.0
expected_sha256 <- "18ec245c45427f431c7a01d0b960a7cabf851dffc91ed5f12b10122019966722"
raw_path <- file.path("data", "raw", "opaq_70a.csv")

sha256_file <- function(path) {
  out <- system2("shasum", c("-a", "256", shQuote(path)), stdout = TRUE)
  strsplit(out, " ")[[1]][1]
}

dir.create(dirname(raw_path), recursive = TRUE, showWarnings = FALSE)
if (!file.exists(raw_path) || !identical(sha256_file(raw_path), expected_sha256)) {
  tmp <- paste0(raw_path, ".part")
  download.file(source_url, tmp, mode = "wb", quiet = TRUE)
  invisible(file.rename(tmp, raw_path))
}
hash <- sha256_file(raw_path)
stopifnot(identical(hash, expected_sha256))

writeLines(readLines(raw_path, n = 1, warn = FALSE), file.path("data", "variables_seen.txt"))
writeLines(c(
  "# Provenance",
  "",
  paste0("- Source: ", source_url, " (opaq_70a.csv, OSF project ygnvb, dated 2023-02-10)"),
  "- Licence: CC-By Attribution 4.0 International (OSF node licence field)",
  "- Dataset paper: Röseler et al. (2022), Journal of Open Psychology Data, https://doi.org/10.5334/jopd.67",
  paste0("- SHA-256: ", hash),
  paste0("- Size (bytes): ", file.size(raw_path))
), file.path("data", "provenance.md"))
message("OpAQ data present, hash verified: ", hash)
