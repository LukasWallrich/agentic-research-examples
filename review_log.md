# Review log

Every reviewer comment received, with the response. Reviewer text is retained verbatim in `reviews/`. Reviews were produced by AI reviewers (OpenAI codex, Google Gemini via agy, and the coarse-review pipeline); they are not journal peer review or human endorsement.

---

## Round 1 — codex code and results review (read-only)

Full text: `reviews/round1_codex_code_review.md`. This review was commissioned under Phase 3 of the brief. It found eight issues, most of which were correct and two of which (H6 and the sampling) were serious.

### 1. H6 was marked supported by switching to a near-trivial outcome
**Comment.** The preregistration required ≥ 60% agreement on the sign of the crowd-accuracy gap; the output gave 30/81 (37%). `h6.py` instead declared success if either that or the later-added Brier outcome reached 60%. The Brier result provided no predictive discrimination because every dataset was assigned a cell predicting a negative effect, and predicting "negative" for all gives the same score. This outcome-contingent change was not in `deviations.md`.
**Response: accepted.** `h6.py` was rewritten to report the preregistered sign-accuracy outcome as primary, report the Brier outcome separately with its trivial baseline, and never declare support via the Brier. The manuscript now states H6 is rejected. Recorded in `deviations.md` V2.

### 2. Judge subsets sampled with replacement; seeds unstable
**Comment.** `rng.integers` sampled judges with replacement, so a size-three draw from three judges contained distinct judges only 22% of the time. The seed used Python's process-randomised `hash`, so the fixed-seed reproduction claim did not hold.
**Response: accepted as bugs.** Replaced with sampling without replacement (`argsort` of random keys) and with a stable `zlib.crc32` seed. This materially changed results; recorded in `deviations.md` V6.

### 3. The Brier estimand answers a different question; the "consistent in direction" claim is false
**Comment.** The leave-one-judge-out Brier predicts another judge's correctness, not the crowd's estimate of item truth, so it is not simply a continuous version of the crowd-accuracy test. Its addition after the outcome is disclosed, but the deviation log's claim that the preregistered result was "consistent in direction" is false: the sign gap is +0.0031 and the Brier improvement −0.0008.
**Response: accepted.** The manuscript now describes the Brier estimand as a graded measure that predicts a held-out judge's correctness, and states explicitly that the two measures point in opposite directions. `deviations.md` V2 corrected.

### 4. The simulation deviates from the registered design; the confidence model uses the truth
**Comment.** One realisation per cell rather than 200 repetitions; omitted m = 4; changed τ grid; one noise level. Judge traits were redrawn per item, and confidence depended on the true answer `T_i s_ij`, an information advantage unavailable to a judge. The V1 rationale that κ was "inert" is mathematically unsound.
**Response: partly accepted.** The grid now includes m = 4, the registered τ grid, and two noise levels; judge traits are persistent; confidence now depends on the evidence magnitude `|s|` rather than the truth. The single-realisation choice is recorded (V4), and V1's "inert" wording is corrected.

### 5. H5 and the simulation summaries are overstated
**Comment.** H5 specified the crowd-accuracy gap and predicted a negative ρ coefficient; the fitted coefficient was +0.133 (opposite sign). The negative coefficient highlighted in the manuscript belonged to the added Brier outcome. H2 recorded 51/384 decreasing steps, which does not support non-decreasing. λ* was selected and evaluated on the same items.
**Response: accepted.** After the bug fixes, both H5 regressions are near zero and non-significant; the manuscript now reports H5 as not supported. H2 is reported as not supported with the violation count. The λ* in-sample point is stated.

### 6. The psychometric estimates and pooling do not implement the promised inference
**Comment.** The ICC was applied to trials, not the judge-item table; the logistic optimiser was accepted without a convergence check; the subject-clustered bootstrap SE was absent; the summary was not a random-effects meta-analysis; the clipped-confidence robustness was missing.
**Response: accepted.** ICC now uses the judge-item table; the logistic fit is ridge IRLS and converges for all datasets; the summary is relabelled an unweighted mean (deviation V5); the clipped-confidence robustness was added. The subject-clustered bootstrap SE was not implemented; the moderation uses robust OLS SEs and the limitation is stated.

### 7. Internal inconsistencies
**Comment.** The manuscript still said "80"; the standardisation description was wrong; the "negative in all 48 cells" claim confused the minimum over group sizes with the cell mean; the promised formal derivation was absent; "Bayes-optimal under independence" is too strong (weights should be log odds).
**Response: accepted.** All corrected in the rewrite: consistent dataset counts, a verbal sign condition with an explicit statement that no general closed form is claimed, "negative in 45 of 48 cell means" corrected to the current counts, and the optimality statement changed to log odds.

---

## Round 2 — codex re-review of the revision, and agy manuscript review

Full texts: `reviews/round2_codex_rereview.md`, `reviews/round2_agy_manuscript.md`.

### 2.1 codex: new m = 4 artefact
**Comment.** Even group sizes allow ±1 ties, which the simulation counted as errors for EW while CW usually broke them, creating a spurious +0.107 advantage at m = 4 and contributing 120 of the reported H2 decreases.
**Response: accepted.** Ties now score 0.5 for both rules (deviation V10). H2 violations fell and the affected values were regenerated. H2 remains unsupported.

### 2.2 codex: H6 compared different group-size averages; remaining inconsistencies
**Comment.** H6 matched a dataset average over eligible sizes to a simulation average over all ten sizes, including the corrupted m = 4; the limitations paragraph said the two measures "point the same way"; the abstract rounded 36.8% to 36%.
**Response: accepted.** H6 now compares at a common group size (m = 7) on both sides; the "same way" sentence was corrected to "opposite directions"; the percentages were regenerated.

### 2.3 codex / agy: shrinkage and H3 overstated
**Comment.** "Partial shrinking beats both pure rules almost everywhere" relied on choosing λ on the same simulated items used to score it, and λ* was noisy.
**Response: accepted.** Simulation items were increased from 40,000 to 100,000, the claim was softened to an explicit in-sample result, and the interior-optimum count is reported.

### 2.4 codex / agy: H5 is acceptance of the null
**Comment.** The moderation OLS treats datasets as exchangeable and ignores attenuation from noisy β and ρ; a non-significant slope is not evidence of no effect.
**Response: accepted.** A sentence was added stating that no moderation was detected rather than that none exists, noting attenuation and low power.

### 2.5 agy: item and vote definition create an artificial ceiling
**Comment.** Defining items as condition cells and votes as a participant's average accuracy creates a 93–98% ceiling and does not represent crowd decision making on binary problems.
**Response: accepted as a scope limitation.** No dataset in the Confidence Database provides a shared physical stimulus with a per-item ground truth across participants (verified structurally before preregistration). The manuscript states this limitation explicitly and no longer presents the empirical leg as a controlled crowd decision. The point is also recorded in `weaknesses.md`.

### 2.6 agy: the "derived boundary" is only a heuristic; H6 failure is over-interpreted
**Comment.** Section 2 is qualitative; the claim of a derived boundary should be dropped or a derivation supplied. The H6 failure should not be read as refuting the overconfidence account, since the mapping is coarse and the domains mismatch.
**Response: partly accepted.** The framing was changed from "derive" to "specify the gap" and the sign condition is stated as a condition, not a full derivation; a compact analytic sign condition (weighting gain versus variance cost) is given. The H6 interpretation was softened to a failure of this specific model under this mapping, and the manuscript says whether another account would fit is open.

### 2.7 agy minor points
- Figure numbering did not match file names: **accepted**, files renamed (fig3_lambda.png, fig4_moderation.png).
- m = 40 rests on very few datasets: **accepted**, dataset counts are annotated in Figure 1a.
- Brier axis sign ambiguity: **accepted**, the axis now reads "negative = CW worse".
- `run_all.sh` not found: **not applicable**, the reviewer worked from an isolated copy that did not include it; the script is at the repository root.
- No explicit contrast with Baharad and Ben-Yashar (2009): **accepted**, a sentence was added in Section 2.2.

---

## Round 3 — coarse-review pipeline

Full text: `reviews/round3_coarse_review.md` (pending; the pipeline was launched on an earlier revision and its comments are treated as applying to the structure and substance, which the later revisions did not change in direction).