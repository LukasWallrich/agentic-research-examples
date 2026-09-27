# Figures for the manuscript.
# Fig 1: model predictions (response function and local elasticity against anchor distance).
# Fig 2: observed within-item response functions (binned medians) with the fitted H1 curve.
# Fig 3: across-cell log anchoring index and Hedges' g against extremity.

suppressPackageStartupMessages({ library(data.table); library(ggplot2); library(lme4) })
source(file.path("R", "models.R"))
fig_dir <- file.path("manuscript", "figures")
dir.create(fig_dir, recursive = TRUE, showWarnings = FALSE)

pal <- c(M1 = "#2a78d6", M1R = "#e87ba4", M2 = "#1baf7a", M3 = "#eb6834", M4 = "#eda100")
lt <- c(M1 = "solid", M1R = "dotdash", M2 = "longdash", M3 = "dotted", M4 = "twodash")
theme_paper <- theme_minimal(base_size = 10) +
  theme(panel.grid.minor = element_blank(), panel.grid.major = element_line(colour = "grey92"),
        strip.text = element_text(face = "bold", hjust = 0), legend.position = "bottom",
        plot.title = element_text(face = "bold", size = 10))

# ---- Figure 1: model predictions at the median accepted calibration of each model --------------
calib <- fread(file.path("output", "calibration_grid.csv"))[accepted == TRUE]
med_par <- function(m) {
  g <- calib[model == m]
  keep <- names(which(sapply(g, function(v) !all(is.na(v)))))
  g <- g[, intersect(c("s", "t", "cost", "kappa", "w", "k", "c", "jk"), keep), with = FALSE]
  as.list(g[which.min(abs(jk - median(jk)))][, !"jk"])
}
set.seed(11)
grid <- seq(-4, 4, by = 0.1)
f1 <- rbindlist(lapply(names(pal), function(m) {
  par <- med_par(m)
  data.table(model = m, x = grid, y = sapply(grid, function(x) {
    mu <- rnorm(20000, 0, belief_sd_share)
    mean(respond(m, rep(x, 20000), mu, 1, par))
  }))
}))
f1[, elasticity := c(NA, diff(y) / diff(x)), by = model]
f1[, elasticity := frollmean(elasticity, 7, align = "center"), by = model]
f1_long <- rbind(f1[, .(model, x, value = y, panel = "A. Mean estimate (log, relative to belief centre)")],
                 f1[, .(model, x, value = elasticity, panel = "B. Local elasticity (proportional pull)")])
p1 <- ggplot(f1_long, aes(x, value, colour = model, linetype = model)) +
  geom_hline(yintercept = 0, colour = "grey60", linewidth = 0.3) +
  geom_line(linewidth = 0.7, na.rm = TRUE) +
  facet_wrap(~ panel, scales = "free_y") +
  scale_colour_manual(values = pal, name = NULL) + scale_linetype_manual(values = lt, name = NULL) +
  labs(x = "Anchor distance from the belief centre (log units, in SDs of belief uncertainty)", y = NULL) +
  theme_paper
ggsave(file.path(fig_dir, "fig1_model_predictions.png"), p1, width = 7, height = 3.4, dpi = 300, bg = "white")
ggsave(file.path(fig_dir, "fig1_model_predictions.pdf"), p1, width = 7, height = 3.4)

# ---- Figure 2: observed within-item response functions -----------------------------------------
fits <- readRDS(file.path("output", "confirmatory", "fits.rds"))
source(file.path("R", "estimators.R"))
W <- drop_gross_errors(fits$W)
W[, bin := floor(x / 0.5)]   # fixed-width bins of 0.5 log units
binned <- W[, .(x = median(x), y = median(y), n = .N), by = .(cell, reference_short, anchortype, bin)][n >= 10]
m <- fits$h1$pooled$model
# Fitted curve for each cell (fixed effects plus that cell's random effects), over the central 95% of its anchors
curve <- W[, .(x = seq(quantile(x, .025), quantile(x, .975), length.out = 100)), by = .(cell)]
curve[, `:=`(xx = x * abs(x), pid = NA_character_)]
curve[, y := predict(m, newdata = curve, re.form = ~ (1 + x + xx || cell))]
W[, study_label := sprintf("%s (%s anchors)", reference_short, fifelse(anchortype == 1, "random", "fixed"))]
labs_cell <- unique(W[, .(cell, study_label)])
binned <- merge(binned, labs_cell, by = "cell")
curve <- merge(curve, labs_cell, by = "cell")
p2 <- ggplot(binned, aes(x, y)) +
  geom_abline(slope = 1, intercept = 0, colour = "grey75", linewidth = 0.3, linetype = "dashed") +
  geom_hline(yintercept = 0, colour = "grey75", linewidth = 0.3) +
  geom_line(aes(group = cell), colour = "grey55", linewidth = 0.35) +
  geom_point(size = 1.1, colour = "grey30") +
  geom_line(data = curve, aes(group = cell), colour = pal[["M1"]], linewidth = 0.6) +
  facet_wrap(~ study_label, ncol = 2, scales = "free") +
  labs(x = "Anchor, log(anchor / true value)", y = "Estimate, log(estimate / true value)\n(median per 0.5-unit bin of anchors)") +
  theme_paper
ggsave(file.path(fig_dir, "fig2_within_item.png"), p2, width = 7, height = 5.6, dpi = 300, bg = "white")
ggsave(file.path(fig_dir, "fig2_within_item.pdf"), p2, width = 7, height = 5.6)

# ---- Figure 3: across-cell index and Hedges' g against extremity --------------------------------
ci_A <- fits$ci_A
h2 <- fits$h2$model
e3 <- fread(file.path("output", "exploratory", "E3_hedges_g.csv"))
xs <- seq(min(ci_A$extremity), max(ci_A$extremity), length.out = 100)
pr <- predict(h2, newmods = xs)
line3 <- data.table(extremity = xs, est = pr$pred, lo = pr$ci.lb, hi = pr$ci.ub, panel = "A. Log anchoring index (preregistered, H2)")
pts <- rbind(ci_A[, .(extremity, value = ai, w = 1 / ai_se, panel = "A. Log anchoring index (preregistered, H2)")],
             e3[, .(extremity, value = g, w = 1 / sqrt(v), panel = "B. Hedges' g (exploratory)")])
m3 <- metafor::rma.mv(g, v, mods = ~ extremity, random = ~ 1 | study / cell, data = e3)
pr3 <- predict(m3, newmods = xs)
line3 <- rbind(line3, data.table(extremity = xs, est = pr3$pred, lo = pr3$ci.lb, hi = pr3$ci.ub, panel = "B. Hedges' g (exploratory)"))
p3 <- ggplot(pts, aes(extremity, value)) +
  geom_hline(yintercept = 0, colour = "grey60", linewidth = 0.3) +
  geom_point(aes(size = w), shape = 21, fill = "grey70", colour = "white", stroke = 0.3, alpha = 0.8) +
  geom_ribbon(data = line3, aes(y = est, ymin = lo, ymax = hi), fill = pal[["M1"]], alpha = 0.18) +
  geom_line(data = line3, aes(y = est), colour = pal[["M1"]], linewidth = 0.8) +
  facet_wrap(~ panel, scales = "free_y") +
  scale_size_area(max_size = 3, guide = "none") +
  coord_cartesian(ylim = NULL) +
  labs(x = "Anchor extremity: mean |log(anchor / true value)| of the two anchors", y = NULL) +
  theme_paper
ggsave(file.path(fig_dir, "fig3_across_cells.png"), p3, width = 7, height = 3.4, dpi = 300, bg = "white")
ggsave(file.path(fig_dir, "fig3_across_cells.pdf"), p3, width = 7, height = 3.4)
message("Figures written to ", fig_dir)
