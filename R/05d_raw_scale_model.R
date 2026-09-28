# Exploratory E6: constant-weight integration on the raw scale (M2raw).
# The estimate is a fixed weighted average of anchor and belief in raw units:
# estimate = w * anchor + (1 - w) * belief, with a log-normal belief. On the log scale this
# implies falling elasticity for anchors below the belief and rising elasticity above it.
# The model is simulated on the OpAQ within-item design and passed through the pooled H1
# estimator and the side-specific curvature model of exploratory analysis E1.

suppressPackageStartupMessages({ library(data.table); library(lme4); library(parallel) })
source(file.path("R", "design_sets.R"))
source(file.path("R", "models.R"))
source(file.path("R", "estimators.R"))
out_dir <- file.path("output", "exploratory")

# Without response noise the raw-scale Jacowitz & Kahneman index of M2raw equals w; with the
# log-scale response noise used here it is within 0.02 of w for sigma between 0.3 and 1.2
# (checked by simulation during review), so w is drawn from the .30-.60 calibration band.
sets <- build_sets(read_opaq(include_outcomes = FALSE))
rows <- sets$within[, .(cell, pid, x)]
cells <- unique(rows$cell)

fit_sides <- function(dat) {
  dat <- drop_gross_errors(dat)
  dat[, `:=`(xx_neg = fifelse(x < 0, x * abs(x), 0), xx_pos = fifelse(x > 0, x * abs(x), 0))]
  m <- lmer(y ~ x + xx_neg + xx_pos + (1 + x || cell) + (1 | pid), data = dat,
            control = lmerControl(calc.derivs = FALSE, check.conv.singular = "ignore"))
  fixef(m)[c("xx_neg", "xx_pos")]
}

res <- rbindlist(mclapply(1:300, function(i) {
  set.seed(8e5 + i)
  w <- runif(1, 0.30, 0.60)
  cellpar <- data.table(cell = cells, sigma = runif(length(cells), 0.3, 1.2),
                        bias = rnorm(length(cells), runif(1, -0.3, 0.3), 0.3))
  r <- merge(rows[, .(row_id = .I, cell, pid, x)], cellpar, by = "cell")[order(row_id)]
  persons <- unique(r$pid)
  u <- setNames(rnorm(length(persons), 0, 0.15), persons)
  mu <- r$bias + u[r$pid] + rnorm(nrow(r), 0, belief_sd_share * r$sigma)
  est <- w * exp(r$x) + (1 - w) * exp(mu)                      # raw-scale averaging (truth = 1)
  y <- log(est) + rnorm(nrow(r), 0, response_sd_share * r$sigma)
  gross <- runif(nrow(r)) < contamination_p
  y[gross] <- y[gross] + rnorm(sum(gross), 0, contamination_sd)
  d <- copy(rows)[, y := y]
  fw <- tryCatch(fit_within(d), error = function(e) NULL)
  fs <- tryCatch(fit_sides(d), error = function(e) NULL)
  if (is.null(fw) || is.null(fs)) return(NULL)
  data.table(rep = i, w, b = fw$b, g = fw$g, rho = fw$rho, g_below = fs[["xx_neg"]], g_above = fs[["xx_pos"]])
}, mc.cores = 8))
fwrite(res, file.path(out_dir, "E6_raw_scale_model_draws.csv"))
q <- function(v) c(median = median(v), lo = unname(quantile(v, .025)), hi = unname(quantile(v, .975)))
summ <- rbindlist(lapply(c("b", "g", "rho", "g_below", "g_above"), function(k) data.table(statistic = k, t(q(res[[k]])))))
fwrite(summ, file.path(out_dir, "E6_raw_scale_model_summary.csv"))
print(summ)
