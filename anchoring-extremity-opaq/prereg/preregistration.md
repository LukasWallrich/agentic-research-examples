# Preregistration: How does anchor influence change with anchor extremity? A model-based secondary analysis of the Open Anchoring Quest

Template: Preregistration of secondary data analysis (van den Akker et al., 2021, Meta-Psychology, https://doi.org/10.15626/MP.2020.2625). Question numbers follow the template.

Date: 2026-09-27. This document, the simulation code in `R/`, and the frozen model predictions in `output/predictions_raw.csv` and `output/predictions_summary.csv` are committed to git together, before any outcome variable is read. `R/read_opaq.R` refuses to load the `estimate` column until this file is committed.

## Part 1: Study information

**Q1. Working title.** How does anchor influence change with anchor extremity? Testing process models of anchoring against open trial-level data.

**Q2. Authors.** Lukas Wallrich (Birkbeck, University of London; ORCID 0000-0003-2121-5177), who commissioned and is accountable for the study. The design, code, analyses and text were produced by an AI system (Claude Opus 5.5, Anthropic) working autonomously under Lukas Wallrich's instruction, with review by other AI systems (OpenAI Codex CLI, Google Gemini via the Antigravity CLI). See `ai_disclosure.md`.

**Q3. Research questions.**
- RQ1: Within the same item, does the proportional influence of the anchor on estimates (the local elasticity of the estimate with respect to the anchor, on the log scale) rise, stay constant, or fall as the anchor moves further from the true value?
- RQ2: Across item-study cells with a classic high/low anchor pair, does the log-scale anchoring index rise, stay constant, or fall with anchor extremity?
- RQ3: Which of five process models of anchoring, calibrated in advance to an external benchmark, predicts the observed response functions?

**Q4. Hypotheses.** We state competing model predictions rather than one directional hypothesis. All tests use frequentist estimation with 95% confidence intervals (CIs).

Notation. For each estimate, y = ln(estimate / true value) and x = ln(anchor / true value). Within item-study cells we fit y = a_cell + b·x + g·x|x| (plus random effects; Q19). b is the average elasticity at the true value; g is the curvature: g > 0 means the anchor's proportional pull grows with extremity, g < 0 means it shrinks. rho = g / b is the curvature relative to the average elasticity.

Models (full specification in `R/models.R`; all operate on the log scale):
- **M0 No anchoring.** Estimates ignore the anchor.
- **M1 Anchor-and-adjust with a fixed number of adjustments** (Lieder et al., 2018a, with the number of adjustments held constant): a Metropolis-Hastings chain starts at the anchor and takes t steps towards the belief distribution.
- **M1R Resource-rational anchor-and-adjust** (Lieder et al., 2018a, Eq. 2): as M1, but the number of adjustments minimises expected absolute error plus a time cost per adjustment, so it depends on how far the anchor lies from the belief.
- **M2 Constant-weight integration** (in the spirit of the anchor integration model, Turner & Schley, 2016, with a constant weight): the estimate is a fixed weighted average of anchor and belief.
- **M3 Adjust to the plausible boundary** (Epley & Gilovich, 2006): anchors inside the plausible range are accepted; from anchors outside it people adjust to the nearest edge of the range.
- **M4 Plausibility-discounted integration** (selective accessibility with a plausibility gate; Strack & Mussweiler, 1997; Wegener et al., 2001): the anchor's weight falls smoothly as the anchor becomes implausible.

Predictions (derived by simulation on the exact OpAQ designs; Q20 and `output/predictions_summary.csv`):
- H1 (within-item curvature, pooled): under M1 the curvature g is positive (median 0.062, 95% predictive interval [0.030, 0.095]); under M2 it is zero (0.000 [-0.007, 0.007]; rho [-0.017, 0.016]); under M3 and M4 it is negative (M3: -0.046 [-0.071, -0.022]; M4: -0.066 [-0.110, -0.017]). M1R makes no determinate sign prediction: its curvature depends on its parameters (0.003 [-0.029, 0.082]). Under M0 the average elasticity b is zero, so the shape is undefined.
- H1a/H1b (within-item curvature, random-anchor and fixed-anchor strata separately): same direction as H1 for each model.
- H2 (across-cell slope of the log anchoring index on extremity): under M1 the slope d is positive (0.069 [0.033, 0.120]); under M2 it is zero (0.000 [-0.004, 0.004]); under M3 and M4 it is negative (M3: -0.083 [-0.133, -0.039]; M4: -0.099 [-0.161, -0.049]); M1R tends negative but is indeterminate (-0.037 [-0.117, 0.082]).
- H3 (model adequacy): each model's 95% predictive interval for g, rho, and the across-cell slope, given in Q20. A model is contradicted by the data when an observed statistic lies outside its interval.

## Part 2: Data description

**Q5. Dataset.** Open Anchoring Quest (OpAQ; Röseler et al., 2022, https://doi.org/10.5334/jopd.67; correction https://doi.org/10.5334/jopd.92), file `opaq_70a.csv` (OSF project ygnvb, dated 2023-02-10; SHA-256 18ec245c45427f431c7a01d0b960a7cabf851dffc91ed5f12b10122019966722). Trial-level anchoring data aggregated from openly available and contributed datasets: 95,735 rows, 95 studies, 402 item texts, 466 item-study cells. Each row is one estimate by one participant for one item and one anchor. Cross-sectional; participants mostly lay adults online or in labs, collected 2010-2022 in Europe, Asia and the Americas.

**Q6. Openness.** Publicly available under CC-BY 4.0 (licence field of the OSF project). No registration or agreement needed.

**Q7. Access.** https://osf.io/download/s4zgw/ ; `R/00_fetch.R` downloads it and checks the hash.

**Q8. Date of download.** 2026-09-27 (single analyst).

**Q9. Data collection.** Described in Röseler et al. (2022) and in the source publications listed in the `reference` column; OpAQ harmonised studies that used at least two anchors.

**Q10. Codebook.** Table 1 of Röseler et al. (2022); `labels.xlsx` in the OSF folder "Information for potential contributors" (defines anchortype 5 = incidental/subliminal, which is not in the published table). The file has further columns derived from the estimate (Q18).

**Q11. Manipulated variables.** The anchor value (`anchor`), its side (`anchorhigh`: 1 high, 0 low), and its type (`anchortype`: 1 explicitly random, 2 fixed without explanation, 3 relevant to the target). x = ln(anchor / true value).

**Q12. Measured variables.**
- Outcome: `estimate`, transformed to y = ln(estimate / true value). No other outcome columns are used.
- Design variables and covariates: `true_value`, `reference_short` (study), `anchoring_item` (item), `participant_id`, `tasktype`, `scaletype`, `comparative_question`, `direction`, `incentive`, `experiment_type`.
- Across-cell anchoring index for a cell with one low anchor A_L and one high anchor A_H: AI = [median(y | high) - median(y | low)] / [ln(A_H) - ln(A_L)]. Extremity of the cell: E = (|x_L| + |x_H|) / 2, the mean absolute log distance of the two anchors from the true value.

**Q13. Inclusion and exclusion of units.**
Rows enter only if: `anchortype` is 1, 2 or 3 (excludes self-generated and incidental anchors); `scaletype` = 1 (open response); `tasktype` is a positive ratio-scale quantity (quantity, number, price, length, height, distance, weight, population, volume, speed, duration, birth rate, income, width, area, circumference, age); anchor and true value are numeric and positive; the study is not Röseler & Wagner (2021), whose anchors were computed from each participant's own unanchored estimates. The true value of a cell is the value on its first row.
- Within-item set: cells with at least 3 distinct anchor values. From design columns: 20 cells, 4 studies, 7,952 rows, 1,492 participants. Random-anchor stratum (anchortype 1): Bahník (2021a), 13 cells, 6,578 rows; Yoon et al. (2021, Form C), 2 cells, 172 rows. Fixed-anchor stratum (anchortype 2): Frech et al. (2021), 4 cells, 416 rows (high anchors only, 10 levels); Imhoff & Barker (2022, Study 2), 1 cell, 786 rows (20 levels).
- Across-cell set: cells with anchortype 2 or 3, exactly one low and one high anchor value, ln(A_H / A_L) >= 0.25, at least 10 rows per side. From design columns: 129 cells, 40 studies, 109 items, 24,147 rows. No cell is in both sets.

**Q14. Missing data.** Rows with a missing, non-numeric, zero or negative estimate are excluded (the log is undefined). We will report how many. If a cell loses its eligibility (fewer than 3 anchor values in the within set; fewer than 10 rows on a side in the across set), it is dropped.

**Q15. Outliers.** Gross errors (unit errors, typing slips) are removed with one rule applied identically to simulated and observed data (`drop_gross_errors()` in `R/estimators.R`): a response is dropped when |y| exceeds both ln(1000) and the cell's largest |x| plus ln(10). A response equal to any anchor is always retained. No other trimming. Robustness analysis R1 uses median regression without this rule.

**Q16. Weights.** None.

## Part 3: Knowledge of data

**Q17. Prior work with the dataset.** None by the authors.

**Q18. Prior knowledge.**
- Read before this preregistration: the OpAQ data paper (Röseler et al., 2022); the OpAQ meta-analysis preprint (Röseler & Schütz, 2022, https://doi.org/10.31234/osf.io/wf2tn), which reports that Hedges' g increases with the relative distance between anchor and true value (b = 0.040, k = 312) and that explicitly random anchors show smaller effects; Schley & Weingarten (2026) on anchor extremity; Barrera-Lemarchand et al. (2024), whose anchoring weight falls with anchor distance on percentage items; the Röseler & Wagner (2021) analysis script (to check anchor construction). We have not read the results of Bahník (2021a) or Imhoff & Barker (2022) concerning the shape of the estimate-anchor function ; a literature agent was asked about both papers during scoping, and we committed this plan without waiting for its report because these two studies supply most of the within-item data, so reading their results would amount to seeing the primary outcome pattern.
- Columns read (design only, via `R/read_opaq.R`): reference_short, reference, id, participant_id, sex, age, nationality, anchoring_item, true_value, anchor, anchorhigh, anchortype, tasktype, direction, incentive, comparative_question, experiment_type, stimulitype, sampletype, scaletype, published, preregistered. Outputs seen: `output/design_inventory.txt`, `output/design_cells.csv`, and the cell and row counts in Q13.
- Never read before this commit: `estimate` and every column derived from it (adjustment, absadjustment, score, restr_score, zestimate, zadjustment, zabsadjustment, zscore, outlier, precision, nchar, precise, zsta).
- A 2026 corrigendum to Weber & Röseler (2025; OSF component sz5b9) reports item-to-effect mix-ups in their study. Weber et al. (2021) contributes 14 cells to the across-cell set. Whether the OpAQ master file is affected is unknown (robustness analysis R6).

## Part 4: Analyses

**Q19. Statistical models.** All code is in `R/estimators.R` (shared with the prediction simulation) and `R/04_confirmatory.R`, which was run before this commit in dry-run mode on responses simulated from M2 (`Rscript R/04_confirmatory.R dry-run`, output in `output/dry_run/`) to check that it executes.

H1 (primary). Within-item set, linear mixed model (lme4, REML):
y ~ x + x|x| + (1 + x + x|x| || cell) + (1 | participant),
with uncorrelated random intercepts, slopes and curvatures by cell and random intercepts by participant. Estimates: b (average elasticity), g (curvature), rho = g / b with a delta-method SE.
H1a/H1b. The same model fitted separately to the random-anchor stratum and the fixed-anchor stratum.
H2. Across-cell set: AI and its SE per cell (SE of each median = 1.2533 × MAD / sqrt(n)); multilevel meta-regression (metafor rma.mv, REML) of AI on E with random intercepts for study and cell within study. Estimate: slope d.
H3. For each model, the 2.5th and 97.5th percentiles of its simulated g, rho, b and d (Q20), compared with the observed values.

**Q20. Predicted effects and smallest effects of interest.** Model predictions from `R/03_simulate_predictions.R` (200 for M0 and 500 for each other model replicates per model; each replicate draws model parameters from the set calibrated to Jacowitz & Kahneman's (1995) anchoring index of about .49, allowing .30-.60, and draws item uncertainty sigma ~ U(0.3, 1.2) log units and item bias ~ N(U(-0.3, 0.3), 0.3)):

| Model | b (average elasticity) | g (curvature) | rho = g / b | g, random-anchor stratum | g, fixed-anchor stratum | d (across-cell slope) | mean log anchoring index, across cells |
|---|---|---|---|---|---|---|---|
| M0 | 0.001 [-0.030, 0.018] | -0.000 [-0.008, 0.010] | undefined | -0.000 [-0.009, 0.009] | -0.003 [-0.058, 0.076] | -0.000 [-0.006, 0.005] | 0.000 [-0.005, 0.005] |
| M1 | 0.439 [0.242, 0.638] | 0.062 [0.030, 0.095] | 0.145 [0.056, 0.342] | 0.060 [0.030, 0.094] | 0.083 [-0.043, 0.190] | 0.069 [0.033, 0.120] | 0.692 [0.492, 0.843] |
| M1R | 0.087 [0.007, 0.336] | 0.003 [-0.029, 0.082] | 0.051 [-0.368, 1.389] | 0.005 [-0.026, 0.083] | -0.022 [-0.135, 0.151] | -0.037 [-0.117, 0.082] | 0.079 [0.014, 0.587] |
| M2 | 0.460 [0.317, 0.598] | -0.000 [-0.007, 0.007] | -0.000 [-0.017, 0.016] | -0.000 [-0.008, 0.007] | 0.001 [-0.040, 0.041] | 0.000 [-0.004, 0.004] | 0.459 [0.312, 0.592] |
| M3 | 0.249 [0.140, 0.360] | -0.046 [-0.071, -0.022] | -0.183 [-0.218, -0.146] | -0.043 [-0.068, -0.021] | -0.082 [-0.169, 0.004] | -0.083 [-0.133, -0.039] | 0.103 [0.061, 0.154] |
| M4 | 0.326 [0.063, 0.576] | -0.066 [-0.110, -0.017] | -0.216 [-0.305, -0.144] | -0.063 [-0.105, -0.017] | -0.099 [-0.206, 0.000] | -0.099 [-0.161, -0.049] | 0.112 [0.014, 0.310] |

Cells are medians with 2.5th and 97.5th percentiles across replicates, generated by `R/03c_prereg_tables.R` (`output/prereg_tables.md`, `output/predictive_intervals.csv`). The simulation estimator always fits the full random-effects structure with lme4; the confirmatory analysis uses the same formula in lmerTest with the Q23 fallback. Other fixed simulation assumptions (`R/models.R`): SD of belief centres across people 0.6 sigma; response noise 0.3 sigma; person offset SD 0.15; 2% of responses contaminated with N(0, 2) log-unit errors. M1R additionally has kappa, the agent's own uncertainty relative to the spread of beliefs across people (0.25-1; only 0.25-0.75 reproduce the benchmark). Calibration grid and accepted values: `output/calibration_grid.csv`.

The level predictions (b, mean index) inherit the calibration to Jacowitz & Kahneman's anchors at the 15th and 85th percentiles; the shape predictions (signs of g and d) follow from each model's structure and hold across the whole calibrated parameter range for M1, M2, M3 and M4.

Smallest effect of interest for "no curvature": equivalence bounds of rho in (-0.05, 0.05) for H1 and d in (-0.03, 0.03) for H2. Justification: 0.05 is just below the smallest |rho| inside the 95% predictive interval of any model with a determinate non-zero sign (M1: 0.056; M3: 0.146; M4: 0.144), while M2's interval is (-0.017, 0.016). For d, the smallest |d| of M1, M3 and M4 is 0.033, 0.039 and 0.049, and M2's interval is (-0.004, 0.004). rho is used for the equivalence decision because it does not depend on the overall strength of anchoring.

**Q21. Power / precision.** Operating characteristics of the Q22 decision rules, computed by applying them to each simulated replicate (`R/03b_decision_properties.R`, `output/decision_properties.txt`):

| Generating model | H1 rising | H1 falling | H1 flat | H1 inconclusive | H1 gate failed | H2 rising | H2 falling | H2 flat | H2 inconclusive | H2 gate failed |
|---|---|---|---|---|---|---|---|---|---|---|
| M0 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |
| M1 | 0.998 | 0.000 | 0.000 | 0.002 | 0.000 | 0.996 | 0.000 | 0.000 | 0.004 | 0.000 |
| M1R | 0.338 | 0.212 | 0.000 | 0.292 | 0.158 | 0.186 | 0.542 | 0.014 | 0.250 | 0.008 |
| M2 | 0.002 | 0.000 | 0.996 | 0.002 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| M3 | 0.000 | 0.998 | 0.000 | 0.002 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 |
| M4 | 0.000 | 0.994 | 0.000 | 0.006 | 0.000 | 0.000 | 0.990 | 0.000 | 0.000 | 0.010 |

In the simulation the H2 gate is approximated as a mean log index above 0.01, because the simulation does not compute a CI for the mean index. Precision is lower in the fixed-anchor stratum (5 cells), whose predictive intervals for g overlap zero under M1 and M3; H1b is therefore weak and is reported as such.

**Q22. Inference criteria.**
- Gate G1 (anchoring present): the shape tests for a set or stratum are interpreted only if the lower bound of the 95% CI for b is above 0. If not, we report that set as "no measurable anchoring; shape not testable".
- H1 decision (95% Wald CIs; Satterthwaite degrees of freedom via lmerTest), applied in this order:
  1. CI for rho entirely inside the equivalence bounds (Q20): no meaningful curvature. Consistent with M2; inconsistent with M1, M3, M4.
  2. Otherwise, CI for g entirely above 0: elasticity rises with extremity. Consistent with M1; inconsistent with M2, M3, M4.
  3. Otherwise, CI for g entirely below 0: elasticity falls with extremity. Consistent with M3 and M4; inconsistent with M1 and M2.
  4. Otherwise: inconclusive.
  The equivalence check comes first so that a curvature too small to matter, but statistically non-zero in about 8,000 rows, is classed as flat.
  - M1R predicts no determinate sign, so H1 and H2 verdicts do not test it; it is assessed only under H3.
- H1a/H1b use the same rules within each stratum; if they disagree in sign (both CIs excluding 0 in opposite directions), we report that anchor type moderates the shape and do not pool the conclusion.
- Gate G2 (anchoring present across cells): H2 is interpreted only if the lower bound of the 95% CI for the mean log anchoring index (intercept-only multilevel model) is above 0.
- H2 decision: the same ordered rule applied to d, with its own equivalence bounds (Q20).
- H3: a model is contradicted by a statistic when the observed point estimate lies outside that model's 95% predictive interval. Shape criterion (decides survival): a model survives if the observed g or rho, and the observed d, lie inside its intervals; M0 is also contradicted whenever gate G1 passes. Level criterion (reported, does not decide survival): observed b and mean log anchoring index inside the model's intervals. Levels depend on the calibration to Jacowitz & Kahneman's anchors and task, which need not transfer to OpAQ designs; shapes follow from model structure. We report which models survive; if none survives, we say so.
- The primary conclusion rests on H1 (pooled). H1a/H1b, H2 and H3 are confirmatory secondary tests; we do not correct for multiplicity because each addresses a distinct prediction, and we report all of them.

**Q23. Analytic problems.** If the H1 model fails to converge or is singular, we remove random-effect terms in this order until it converges: curvature variance, slope variance; the participant intercept is kept. If rma.mv fails, we fit a single-level random-effects meta-regression with study-clustered robust SEs (clubSandwich if available, otherwise metafor::robust). Any such change is reported in `deviations.md`.

**Q24. Robustness.**
- R1: median regression (quantreg, tau = .5) of y on cell-specific intercepts and slopes plus a common x|x| term, without the gross-error rule; CI by participant-cluster bootstrap (1,000 draws).
- R2: H1 with the near/far split replacing x|x|: separate slopes for |x| <= 1 and |x| > 1; report the difference.
- R3: H1 without Bahník (2021a).
- R4: H2 with raw-scale anchoring index (Jacowitz & Kahneman, 1995): [median(estimate | high) - median(estimate | low)] / (A_H - A_L). Descriptive only: the models are specified on the log scale, and a dry run with data simulated from M2 gave a raw-scale slope of -0.07 [-0.11, -0.02], so a falling raw-scale index does not discriminate between models.
- R5: H2 adding covariates: anchortype, comparative_question, direction, incentive (0 vs other), experiment_type.
- R6: H2 without Weber et al. (2021).
- R7: H2 with extremity measured as max(|x_L|, |x_H|) and as ln(A_H / A_L).

**Q25. Exploratory analyses (labelled as such in the paper).** Fitting each model's parameters to the observed data (simulation-based estimation) to compare fit; asymmetry between high and low anchors; the relation of Hedges' g to extremity in the across-cell set, for comparison with Röseler & Schütz (2022); plots of binned response functions for each within-item cell.
