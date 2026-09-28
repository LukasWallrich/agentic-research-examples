# Deviations from the preregistration

The preregistration is `prereg/preregistration.md`, committed and tagged `prereg-v1` (commit a40911b, 2026-09-27 22:56 BST). The confirmatory analysis was first run on the observed estimates in commit 14ec907. Each entry states what changed, why, and whether it affects a confirmatory conclusion.

## Deviations

**D1. Estimator for the observed mean anchoring index in H3 (level criterion).**
- Planned: compare the observed "mean log anchoring index" with each model's predictive interval. The first run used the intercept of an intercept-only multilevel meta-analysis (0.416).
- Changed to: the inverse-variance weighted mean of the cell indices (0.241), which is the estimator the prediction simulation used (`fit_across()` in `R/estimators.R`).
- Why: the code review (codex, `reviews/code/codex_answer_code_review_1.txt`) found that simulated and observed values came from different estimators, so the comparison was not like for like.
- Effect: changes the level flags of M2 (still outside) and M4 (now inside). Level criteria do not decide model survival (Q22), so no confirmatory conclusion changes. The H2 test itself still uses the multilevel intercept for gate G2, as preregistered.

**D2. Description of M1R's parameter kappa.**
- The preregistration (Q20) describes kappa as "the agent's own uncertainty relative to the spread of beliefs across people". The code (`R/models.R`, preregistered) multiplies kappa by sigma, the item's belief uncertainty that all other models also use; the spread of belief centres across people is 0.6 sigma.
- Correct description: kappa is the agent's own uncertainty relative to sigma. The frozen predictions came from the code, so they stand; only the wording was wrong.
- Effect: none on any number.

**D3. Code changes after the preregistration that do not change results.**
- `R/00_fetch.R` checks the full SHA-256 of the data file instead of its first 16 characters.
- `R/04_confirmatory.R`: the H2 fallback (Q23) now checks whether clubSandwich is installed before using it, as Q23 specified; the fallback was not triggered. Warnings from robustness fits R2 and R3 are now labelled in the log.
- `R/design_sets.R`: removed the misspelt task type "quantitity" from the list of ratio-scale task types; all 94 rows with that label have anchortype 5 and were excluded anyway.
- Two numerical safeguards in the preregistered code are not described in the preregistration text: `cell_indices()` floors each condition's MAD at 0.001 before computing standard errors, and R4 drops cells whose raw-scale index has a standard error of zero. Neither changed the analysed cell set.
- Effect: after these changes every confirmatory output file except the H3 level columns (D1) is byte-identical to commit 14ec907.

**D4. Relative-curvature CI convention (clarification).**
- Q22 states Wald CIs with Satterthwaite degrees of freedom. For b and g the code uses Satterthwaite t quantiles; for rho = g / b it uses a delta-method SE with a normal quantile, as in the simulation that set the equivalence bounds. This was the preregistered code; we state it here because the Q22 wording does not distinguish the two.

## Applications of preregistered contingency rules (not deviations)

- **Model simplification (Q23).** The pooled H1 model converged with the full random-effects structure. In both strata the full model was singular or failed to converge, and the preregistered fallback removed the random curvature variance (structure 2). The convergence warning in `output/confirmatory_log.txt` comes from a discarded fit.
- **Unit mismatch removed by the gross-error rule (Q15) and eligibility re-check (Q14).** In Shanks et al. (2020, Study 3), "Population of Chicago", participants answered in millions (median 2.6) while the true value (2,746,388) and anchors (200,000; 5,000,000) are raw counts. All 870 valid responses in that cell exceed the gross-error limit, so the cell drops out of the across-cell set (129 design cells, 128 analysed). The other 117 responses removed as gross errors come from 13 studies (including 6 responses to other items of the same Shanks et al. study), mostly Freira et al. (2020, Study 4), a forecast of US COVID-19 deaths made early in the pandemic, and Weber et al. (2021), "Shortest distance between Russia and USA", whose true value is a few kilometres.
- **Operating characteristics (Q21) are approximations.** They were computed with normal critical values and always the full random-effects structure, and the H2 gate was approximated (disclosed in Q21).

## Additional analyses not in the preregistration

All are labelled exploratory or post hoc in the manuscript.
- `R/05_exploratory.R` (E1-E5): topics listed in Q25; E4 (extremity scaled by response spread) and E5 (relaxed-calibration check) were specified after seeing the confirmatory results.
- `R/05b_sensitivity.R` (S1-S3): added after the code review. S1 recalibrates all models to the raw-scale Jacowitz & Kahneman index (the preregistered calibration used a log-scale index, while Jacowitz & Kahneman's .49 is a raw-scale value); S2 tests the dependence of H1 on single studies; S3 checks H2 for influential cells, study clustering and single studies.
- `R/05d_raw_scale_model.R` (E6): simulation of constant-weight integration on the raw scale, added after the citation check showed that Imhoff & Barker (2023) found a linear raw-scale relation for one within-item cell.
- `R/05e_review_checks.R` (R1a-R1e): checks requested in manuscript review round 1: a joint predictive check of b and g, near and far slopes with CIs, study-specific curvature, a participant bootstrap for H2 with a check for paired participants, and H2 with the Chicago cell converted from millions.
