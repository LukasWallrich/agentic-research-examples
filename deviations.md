# Deviations from the preregistration

Each deviation states what changed, when it was decided, whether that was before or after seeing the relevant outcome, and its effect on interpretation.

## V1. Simulation mechanism: judge-level overconfidence (φ) replaced the prereg's κ

- **Preregistration (§4):** confidence miscalibration was modelled as an item-level shift, `c = Φ(γ(s + κu)) + ν`.
- **Change:** confidence now depends on a persistent judge-level overconfidence trait, `c = sigmoid(γ|s| + φo) + ν`, and κ is dropped.
- **Reason:** with κ, the shared error `u_i` is constant across judges within an item, so an item-level shift cannot produce *within-item* miscalibration, which is what changes confidence-weighted aggregation. A judge-level trait can.
- **Correction to an earlier claim:** an earlier version of this log said the κ term was "inert". That was too strong. Because the confidence function is nonlinear, an item-common shift can change judges' *relative* weights. The reason for the change is the within-item point above, not strict inertness.
- **Decided:** while calibrating the model, before the final simulation; the substantive claim is unchanged.

## V2. Added a leave-one-judge-out Brier estimand

- **Preregistration (§6):** the primary empirical quantity was the sign-based activity gap Δ(m); H4/H5 referred to it.
- **Change:** added `Δ_Brier = Brier(EW) − Brier(CW)` for predicting a held-out judge's correctness, computed empirically and in the simulation, and report it alongside Δ(m).
- **Reason:** the sign-based estimand is ceiling-bound (EW accuracy 0.93 at m = 3, 0.98 at m = 40), so it cannot discriminate.
- **Decided:** after seeing the sign-based ceiling. This is disclosed. It is a graded estimand that predicts a *held-out judge's correctness*, not the item's truth, so it is not simply "a continuous version" of the crowd-accuracy test; it answers the adjacent question of whether confidence weighting produces a better-calibrated estimate of whether a judge is right.
- **Correction:** an earlier version of this log said the preregistered result was "consistent in direction" with the Brier result. That is wrong. The preregistered sign-accuracy gap is positive on average (+0.0036) while the Brier improvement is negative (−0.0006); the two measures point in opposite directions. The manuscript now states this.

## V3. Computational bounds

- **Preregistration (§6):** R = 5,000 random judge subsets per group size.
- **Change:** R = 2,000; and, when a dataset has more than 64 eligible items, 64 items are sampled once per group size (not per draw).
- **Decided:** before the final empirical analysis. Monte-Carlo error is ~0.001, below the reported effects.

## V4. Simulation realisation and grid

- **Preregistration (§5):** 200 Monte-Carlo repetitions per cell; `m ∈ {3,4,5,7,...}`; τ grid {0, 0.25, 0.5, 0.75, 1.0}; two confidence-noise levels.
- **Change:** one 40,000-item realisation per cell instead of 200 repetitions (equivalent Monte-Carlo error); the m grid, τ grid, and two noise levels are as registered. An earlier run deviated further (single noise level, different τ grid, no m = 4) and is superseded; this is disclosed for transparency about the revision.
- **Decided:** before the final simulation.

## V5. Meta-analytic summary

- **Preregistration (§6):** "meta-analyse Δ(m) across datasets (random-effects)".
- **Change:** the summary is an **unweighted mean across datasets with a dataset bootstrap CI**, not a random-effects model.
- **Reason:** per-dataset standard errors for the effect are not well defined at this level of description, and the analysis is descriptive rather than an estimate of a population effect.
- **Effect:** the reported mean and CI describe the included datasets; they are not a random-effects estimate. Stated in the manuscript and in the output metadata.

## V6. Corrected sampling and ICC: results changed

- **Change:** three implementation fixes made after the first full run: (a) random judge subsets are drawn **without replacement** (`rng.choice` via `argsort`), where the first run sampled with replacement and could repeat a judge; (b) the within-item error correlation is computed from the **judge-item table**, where the first run used trial-level rows; (c) dataset seeds use a stable `zlib.crc32` hash, where the first run used Python's process-randomised `hash`.
- **Decided:** after an independent code review flagged each of these. These are bug fixes, not design choices.
- **Effect:** material. Under the corrected code the H5 moderation by error correlation is no longer significant (the earlier significant coefficient was an artefact of the sampling and ICC errors), the number of included datasets changes, and the arbitration between the sign and Brier measures changes sign. All numbers in the manuscript come from the corrected code. This deviation is recorded because it changed the conclusions.

## V7. Inclusion requires enough judges for a preregistered group size

- **Preregistration (§6):** inclusion required ≥ 2 items with ≥ 3 judges; group sizes were capped at the dataset's median judges per item.
- **Change:** datasets whose median judges per item is below 3 cannot support any preregistered group size and are excluded.
- **Reason:** a direct consequence of the preregistered cap. It removes 5 datasets that passed the stated inclusion rule.
- **Decided:** with the corrected code, before final reporting.

## V8. Calibration slope fitting

- **Preregistration (§6):** logistic regression of trial accuracy on normalised confidence.
- **Change:** ridge-penalised logistic regression (IRLS) on standardised confidence. The slope is therefore per standard deviation of confidence, not per unit of [0,1], and is comparable to the simulation's slope, which uses the same standardisation.
- **Reason:** unpenalised maximum likelihood failed to converge for 26 of 76 datasets because confidence perfectly separated accuracy.

## V9. Added robustness and grid analyses

- **Change:** added a robustness pass with confidence clipped to its 5th–95th percentile, and a second confidence-noise level in the simulation (as registered).
- **Decided:** before final reporting; these strengthen rather than change the conclusions.

## Summary for the reader

The deviations that change what is reported as the headline result are **V2** (the graded estimand, added after the preregistered estimand proved ceiling-bound), **V5** (descriptive rather than random-effects summary), and **V6** (bug fixes that changed the H5 conclusion and the sign arbitration). The preregistered hypotheses are reported with their outcomes: H1 supported, H2 not supported, H3 supported, H4 descriptive, H5 not supported, H6 rejected. No deviation changed the direction of a conclusion in the paper's favour; V6 changed the H5 conclusion against the paper's original narrative, and the manuscript reports it that way.