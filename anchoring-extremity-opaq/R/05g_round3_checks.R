# Post-hoc checks requested in review round 3 (coarse-review; not preregistered).
# R3a minimum detectable across-cell slope (80% power, two-sided alpha = .05) given the H2 SE.
# R3b Yoon et al. anchors outside plausible ranges (height 48-84 inches; age 10-100) and H1
#     without those entries.

suppressPackageStartupMessages({ library(data.table); library(lmerTest) })
source(file.path("R", "estimators.R"))
out_dir <- file.path("output", "review_checks")
fits <- readRDS(file.path("output", "confirmatory", "fits.rds"))
h2 <- fread(file.path("output", "confirmatory", "h2_across.csv"))
res <- list()

se_d <- (h2$slope_hi - h2$slope_lo) / (2 * qnorm(0.975))
res$R3a_h2_slope_se <- se_d
res$R3a_min_detectable_slope <- (qnorm(0.975) + qnorm(0.80)) * se_d

W <- drop_gross_errors(fits$W)
yoon <- W[reference_short == "Yoon et al., 2021, Form C"]
implaus <- yoon[(grepl("sofa", anchoring_item) & (a < 48 | a > 84)) | (grepl("Stephen King", anchoring_item) & (a < 10 | a > 100))]
res$R3b_yoon_entries <- nrow(yoon)
res$R3b_yoon_implausible <- nrow(implaus)
Wt <- W[!id %in% implaus$id][, xx := x * abs(x)]
m <- suppressWarnings(lmerTest::lmer(y ~ x + xx + (1 + x + xx || cell) + (1 | pid), data = Wt))
co <- summary(m)$coefficients
res$R3b_g_without_implausible_yoon <- co["xx", 1]
res$R3b_g_without_implausible_yoon_lo <- co["xx", 1] - qt(.975, co["xx", "df"]) * co["xx", 2]
res$R3b_g_without_implausible_yoon_hi <- co["xx", 1] + qt(.975, co["xx", "df"]) * co["xx", 2]
tab <- data.table(analysis = names(res), value = unlist(res))
fwrite(tab, file.path(out_dir, "round3_checks.csv"))
print(tab)
