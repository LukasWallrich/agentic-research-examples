# Preregistration

**Title:** When does weighting by confidence hurt the crowd? A finite-sample boundary, a simulation, and a descriptive base rate across open judgment datasets.

**Author of record:** to be determined by the project owner. This document is a local prospective commitment, not a public registration.

**Version:** 1.0 — written 28 September 2026, before any outcome aggregation or hypothesis-bearing simulation was computed.

**Data:** The Confidence Database (Rahnev, D., Desender, K., Lee, A. L. F., Adler, W. T., Aguilar-Lleyda, D., Akdoğan, B., et al., 2020, *Nature Human Behaviour*, 4(3), 317–325, https://doi.org/10.1038/s41562-019-0813-1). Hosted on OSF at https://osf.io/s46pr/ under CC0 1.0. Per-study files are `data_*.csv` with companion `readme_*.txt`. The simulation requires no external data.

**Licence and identifiers:** CC0 permits unrestricted reuse. No personal identifiers are used; the per-study files contain only trial-level task data plus, in a few cases, coarse demographics (age/sex), which are not analysed.

---

## 1. Background and rationale

Confidence-weighted aggregation of judgments (CW) is often described as theoretically optimal: if each judge's reported confidence tracks the probability of being correct and errors are independent, weighting votes by confidence is Bayes-optimal for recovering a binary truth. Equal weighting (EW, the simple majority) ignores confidence entirely.

Three established literatures constrain what can be claimed:
- Committee theory derives optimal weighted-majority rules and shows that correlated votes change the optimum (Shapley & Grofman, 1984; Ladha, 1995; Kaniovski, 2010).
- The forecast-combination puzzle shows estimated optimal weights routinely fail to beat the simple average because of estimation noise (Smith & Wallis, 2009; Claeskens et al., 2016), and Huang, Broomell and Golman (2024) give a test for when weighting "just adds noise".
- Empirical crowd work already compares confidence-based and equal aggregation (Meyen et al., 2021; Saha Roy et al., 2021; Berger et al., 2025 preprint).

This study does not claim those results. It asks a narrower, finite-sample question in psychometric coordinates: **given the number of judges, the confidence–accuracy calibration curve, and the within-item error correlation, when does CW lose to EW, and is partial shrinking better than either?** It then maps the estimated inputs across open judgment datasets.

## 2. What has already been seen of the data (disclosure)

Before writing this preregistration I inspected **only structural and codebook properties** of the Confidence Database, to confirm that a study is feasible. Specifically:

- The list of 360 file names and sizes on OSF node `s46pr`, and the 180 `data_*.csv` files.
- Column headers of all 180 CSVs.
- Per-dataset counts of rows, unique `Subj_idx`, unique `Stimulus`, whether a `Accuracy`/`Correct` column exists, and whether the `Response` column has exactly two levels.
- The median number of unique subjects per `Stimulus` value.
- The fraction of `Stimulus` cells for which a truth reconstructed from `Response` and `Accuracy` (for binary responses) is unique.
- `Database_Information.xlsx` study-level fields (stimuli description, number of subjects, trials per subject, confidence type).
- The first eight rows of `data_Akdogan_2017_Exp3.csv` to confirm file format.

**No** aggregation of accuracy, confidence, or choice was computed; **no** CW-vs-EW comparison was run; **no** calibration slope or error correlation was estimated. The simulation was not run. The counts above are retained in `scoping/conf_feasibility.csv` and `scoping/conf_direct_test_feasibility.csv`.

## 3. Definitions

**Item.** A cell shared across judges, defined as the tuple of (a) the dataset's `Stimulus` column and (b) every column present in the dataset from the fixed design list `D = [Contrast, Coherence, Difficulty, SN, SOA, Orientation, StimulusType, Condition, Task, Category, Temporal_distance, Error]`. If no design column is present, the item is the `Stimulus` value alone.

**Judge's vote in an item.** For judge j in item i, `v_ji = mean over j's trials in item i of (2 · Accuracy − 1)`, so +1 is a correct trial and −1 an incorrect trial. This uses the recorded per-trial correctness directly and does not require reconstructing the truth from responses.

**Confidence.** `c_ji = mean reported Confidence over j's trials in item i`, min–max normalised to [0, 1] within the dataset. If confidence is constant within a dataset, that dataset is excluded.

**Crowd estimates for item i with judge set S (|S| = m):**
- Equal-weighted (EW): `x̄_i = (1/m) Σ_{j∈S} v_ji`.
- Confidence-weighted (CW): `x̂_i = Σ_{j∈S} (c_ji · v_ji) / Σ_{j∈S} c_ji`.

**Crowd decision.** Correct if the estimate is strictly positive.

**Crowd accuracy of a rule** = the fraction of items on which the crowd decision is correct, averaged over repeated random draws of judge sets (group subsampling).

## 4. Formal component

We model each judge–item pair as producing a correctness signal and a confidence:
- item difficulty `δ_i ~ N(0, 1)`;
- shared within-item error `u_i ~ N(0, τ²)`;
- judge-private error `ε_ji ~ N(0, σ²)`;
- signal `s_ji = δ_i + u_i + ε_ji`; vote `v_ji = sign(s_ji)`;
- confidence `c_ji = Φ(γ · (s_ji + κ · u_i)) + ν_ji`, clipped to (0,1), with `ν_ji ~ N(0, ω²)`.

Here `τ` controls the within-item error correlation ρ; `κ` is confidence miscalibration toward the shared error (κ = 0 is well-calibrated, κ > 0 means confident judges are also the shared-biased ones); `γ` is the confidence–signal sharpness.

We derive (a) the expected-accuracy gap `Δ(m) = E[Acc_CW(m)] − E[Acc_EW(m)]` in the large-m limit as a function of the covariance between confidence and the shared error, and (b) the finite-sample penalty from random weights. We then define the **shrinkage estimator** `x^λ_i = (1−λ)·x̄_i + λ·x̂_i` and the accuracy-optimal `λ*(m; ρ, κ, γ)`. The formal write-up is delivered in the analysis output; where a closed form is not tractable we report a high-precision numerical solution and say so.

## 5. Simulation

A generative simulation on the model in §4, sweeping:
- `m ∈ {3, 4, 5, 7, 9, 13, 17, 25, 41, 65}` (judges per item),
- `ρ` implied by `τ ∈ {0, 0.25, 0.5, 0.75, 1.0}` (and `σ` fixed so that baseline accuracy spans roughly 0.6–0.9),
- `κ ∈ {0, 0.25, 0.5, 0.75, 1.0}` (miscalibration toward shared error),
- `γ` calibrated so the confidence–accuracy slope spans a plausible range,
- `ω` (confidence noise) in two levels.

Each cell: 40,000 items × m judges, 200 Monte-Carlo repetitions with fixed seeds. Report `Δ(m)` and `λ*(m)` surfaces.

**Simulation failure condition (must be stated and checked).** The simulation must reproduce at least one of:
(i) the qualitative published finding that real groups weight more equally than confidence-optimal CWMV prescribes (Meyen et al., 2021); or
(ii) the sign pattern of the empirical `Δ(m)` estimated in §6.
If neither is reproduced, we report that the shared-error/miscalibration account fails to explain the data and say so explicitly.

## 6. Empirical component

**Inclusion (applied to all 180 CSVs, structural rules fixed here):**
1. Has `Confidence` and (`Accuracy` or `Correct`) and `Stimulus` columns.
2. ≥ 8 unique `Subj_idx`.
3. Confidence not constant within the dataset.
4. ≥ 2 items with ≥ 3 distinct judges.
5. ≥ 20 % of trials retained after the RT/validity rule below.

**Trial rules:** keep all rows; no RT filtering is applied (RT is not analysed). Where a dataset provides an explicit trial-exclusion flag column, rows flagged for exclusion are dropped. Robustness: repeat with confidence values clipped to the dataset's 5th–95th percentile.

**Primary empirical quantity.** For each included dataset and each `m ∈ {3, 5, 7, 9, 13, 17, 25, 40}` not exceeding the dataset's median judges per item:
1. Draw `R = 5,000` random judge subsets of size m from the judges present in each item.
2. Compute EW and CW crowd decisions and the accuracy over items and draws.
3. Record `Δ(m) = Acc_CW(m) − Acc_EW(m)`.

Meta-analyse `Δ(m)` across datasets (random-effects; bootstrap 95 % CIs, 5,000 resamples, seeds fixed).

**Estimated psychometric inputs per dataset:**
- calibration slope β: logistic regression of trial `Accuracy` on normalised `Confidence` (subject-clustered bootstrap SE);
- within-item error correlation ρ: the intraclass correlation of correctness among judges within items;
- confidence dispersion: SD of normalised confidence.

**Exploratory (clearly labelled):** task-type and group-size moderators; a specification curve over item definitions; the empirical performance of `x^λ` for λ ∈ {0, 0.25, 0.5, 0.75, 1}.

## 7. Hypotheses and inference criteria

- **H1 (boundary exists).** The simulation contains a non-empty region with `Δ(m) < 0`. *Supported if* that region has positive volume across the swept grid; *refuted if* `Δ(m) ≥ 0` everywhere to within Monte-Carlo error (0.002).
- **H2 (finite-sample advantage).** Holding (ρ, κ, γ) fixed, `Δ(m)` is non-decreasing in m. *Supported if* violations are within Monte-Carlo error; *refuted if* `Δ(m)` decreases reliably over a substantial m-range.
- **H3 (interior optimum).** There exists a non-empty region with `0 < λ* < 1`. *Supported if* the numerically optimised `λ*` is interior for at least one swept cell; *refuted if* `λ* ∈ {0, 1}` everywhere.
- **H4 (empirical prevalence).** Across included datasets, `Δ̄` (averaged over m) is small and heterogeneous; a non-trivial fraction of datasets has `Δ̄ ≤ 0`. Reported descriptively; no directional NHST on the pooled mean.
- **H5 (calibration/correlation moderation).** Datasets with flatter β and higher ρ show a smaller (more negative) `Δ̄`. *Supported if* the prespecified regression of `Δ̄` on β and ρ has the predicted signs and the 95 % CI excludes zero for at least one predictor.
- **H6 (model reproduces data).** Using each dataset's estimated (β, ρ) mapped to model parameters, the simulation reproduces the sign of that dataset's `Δ̄` for ≥ 60 % of datasets. *Refuted if* < 60 %.

**Multiplicity:** the six hypotheses are ordered; H1–H3 are simulation results and require no multiplicity correction. For H5's two predictors we report both and treat them as a set.

## 8. Interpretation of each possible outcome

| Outcome | Interpretation |
|---|---|
| CW > EW robustly, model reproduces it, `Δ` grows with m | Confidence weighting is generally safe and improves with crowd size; the harmful region exists in theory but is empirically rare. |
| CW ≤ EW for a meaningful fraction, predicted by flat β / high ρ | Supports the finite-sample boundary; miscalibration and shared error, not estimation noise alone, drive the harm. |
| `Δ ≈ 0` throughout | The theory's predicted differences are too small to detect at these effect sizes; report as an informative null and state the detectable bound. |
| Simulation fails H6 | The shared-error/miscalibration account does not explain the data; report the failure and the direction of misfit. |
| Empirical leg too thin (few included datasets) | Report the formal and simulation results only, and say so in the abstract. |

## 9. Exclusions and deviations

Any change to §5–§7 after this commit is a deviation, recorded in `deviations.md` with its reason and its effect on the conclusions. Exploratory analyses are labelled exploratory everywhere they appear.

## 10. Reproducibility

One command (`./run_all.sh`) regenerates all simulated raw data, analyses, estimates, checks, figures, and the manuscript's numbers from the committed seeds and configuration. No credentials, paid APIs, or network access are required after the first dependency installation. Package versions are pinned.

## 11. AI involvement

The analysis is written and run with AI assistance; the manuscript, references, and claims are checked against Crossref and the cited sources. AI involvement is disclosed in `ai_disclosure.md`. No manuscript was submitted, no person contacted, and no account created.