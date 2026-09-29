# Design note (pre-preregistration draft)

## Question
How does the proportional influence of an anchor on numeric estimates change as the anchor becomes more extreme? Four process models predict different shapes of the anchor-to-estimate response function on the log scale.

## Models (generative scale: natural log of the quantity)
Participant p has belief centre mu_p ~ N(m, sigma_b^2) with m = log(true) + bias, internal uncertainty sigma, response noise.
- M0 null: y = mu_p + e.
- M1 resource-rational adjustment (Lieder et al., 2018): Metropolis-Hastings chain starts at the anchor x, t steps with Gaussian proposals (SD s*sigma) targeting N(mu_p, sigma^2); y = final state. Local elasticity rises with |x - mu|.
- M2 constant-weight integration (Turner & Schley, 2016 AIM): y = w x + (1 - w) mu_p + e. Elasticity flat.
- M3 adjust to the edge of the plausible range (Epley & Gilovich, 2006): y = x if |x - mu_p| < k sigma, else mu_p + sign(x - mu_p) k sigma. Elasticity 1 near, 0 far.
- M4 plausibility-discounted integration (selective accessibility with plausibility gate; Wegener et al., 2001): y = mu_p + w (x - mu_p) exp(-(x - mu_p)^2 / (2 c^2 sigma^2)) + e. Elasticity falls and turns negative beyond c sigma.
Each model's parameters are drawn from ranges that reproduce Jacowitz & Kahneman's (1995) anchoring index (about .49 with anchors at the 15th and 85th percentiles), allowing .30-.60. sigma, sigma_b and bias are drawn from wide ranges.

## Data subsets (design-only inventory, output/design_inventory.txt)
- Within-item set (primary): item-study cells with >= 3 distinct exogenous anchor values, positive ratio-scale quantity, known true value, open scale. Bahník (2021a): 13 items, ~500 participants each, random anchors 1-1000. Imhoff & Barker (2022, Study 2): 1 item, 20 fixed anchors, n = 786. Frech et al. (2021): 4 items, 10 high anchors each, n = 104. Yoon et al. (2021): 2 ratio-scale items with random anchors. Excluded: Röseler & Wagner (2021; anchors computed from each participant's unanchored estimates and participants selected on anchored responses); WTP/WTA items without a true value.
- Across-cell set (secondary): classic fixed two-anchor cells (anchortype 2/3), positive ratio-scale quantity, open scale, known true value (about 150 cells, ~70 studies).

## Estimators (applied identically to simulated and real data)
- Within-item: trial-level mixed model on y~ = log(estimate/true) with x~ = log(anchor/true): y~ = a_c + b x~ + g x~|x~| + random intercepts and slopes by cell, random intercepts by participant. g > 0: elasticity rises with extremity (M1); g ~ 0 (equivalence bounds from simulation): M2; g < 0: M3/M4.
- Across-cell: log anchoring index per cell = (median log est_high - median log est_low) / (log a_high - log a_low), meta-regressed on mean |x~| with random effects for study.

## Inference
Compare the observed g (95% CI) with each model's simulated predictive interval on the exact OpAQ design. Decision table for every outcome cell.
