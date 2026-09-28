# Deviations and implementation clarifications

Preregistration committed at `68c07e4ca1858f382b131a0ee990adf562a271b0` before any hypothesis-bearing computation. Both registered contrasts and the full registered grid were run without changing their parameters, exclusions, sample sizes, inference rules, or interpretation criteria. No simulated histories were excluded.

## Implementation clarifications

- Algebraic structural zero probabilities within 1e−14 are set to exact zero after checking that none is below −1e−12. Reason: floating-point subtraction at Fréchet bounds can yield last-bit negative values. This does not remove any positive-mass condition or history.
- Raw histories are stored as eight-category count vectors, not ordered trials. Reason: all preregistered estimators depend only on counts; no temporal dynamics were preregistered. These are sufficient raw synthetic inputs for all reported analyses.
- `lowest_observed_n` uses the same preregistered regret tolerance of .0005 as the grid comparison, rather than classifying negligible Monte Carlo fluctuations as an improvement. This resolves an underspecified threshold in the descriptive crossover instruction; it affects only the descriptive budget table and does not change either hypothesis.

## Reviewer-requested verification after results

- An independent Codex reviewer derived focal risks by exact discrete convolution and re-scored selected saved histories with integer arithmetic. This is additional implementation verification, not an exploratory hypothesis or a change to the registered analysis. Files: `scripts/independent_check.py`, `output/independent_check.json`, and `reviews/code/codex_review.md`.

The exploratory analyses below were specified after the registered results were available. They are labelled exploratory throughout the manuscript.

## Exploratory analyses requested in manuscript review round 1

Before running them, the following additions were specified in response to Gemini's comments, after the registered results were known:

- **E1, equal encountered opportunities:** exact score-distribution calculations in the two focal environments with encounter budgets 20, 100, and 500, all registered schedules and learners. Unaudited cases contribute zero; zero labels imply a fair tie. Compare regret and expected labels. This examines a different resource constraint and cannot replace the registered equal-label analysis.
- **E2, misspecified weighting:** exact finite-label risks for assumed low-stratum weights 1, 2, 4, 8, and 16 under true selection ratios 4 and 8, in both focal environments at the registered label budgets. This probes the oracle-weight assumption.
- Report the confidence-contingent oracle's accuracy as an action-space benchmark, not an achieved learned policy. No fitted or optimised cap is introduced.

All are labelled exploratory. There are no additional confirmatory hypotheses, inferential tests, or changes to the original outcomes.

- Reviewer-requested reporting now includes tie probabilities in `summary.csv` and `focal_tie_probabilities.csv`, plus grid summaries by true superiority. Scores, histories, primary estimates, and decisions are unchanged.
- The manuscript displays exact focal verification results alongside the original Monte Carlo contrasts and uses “registered computational predictions”/numerical directions. Machine-readable output retains the preregistered support classifications. This clarifies epistemic status rather than replacing the registered tests.
- A post-review logistic-with-lapse response family and added raw-history/disclosure conditions specify an exploratory future behavioural model comparison. They have not been simulated, fitted, or empirically tested and are not a completed human-study preregistration.

## Exploratory extension requested by the full coarse review

- **E3, matched advantage patterns:** after the full round-1 coarse review, specify a symmetric sign-pattern extension before executing it. Human accuracies remain .60/.90. Advisor advantages are ±.05 independently in the two strata, giving advisor pairs (.65,.95), (.65,.85), (.55,.95), (.55,.85). Cross p=.25,.50,.75, overlap r=0,.50,1, schedules random,d1,d2,d4,d8, and budgets n=20,100,500. Evaluate exact finite-label adoption/regret for all four registered summaries by discrete convolution; retain marginal ties. Report regret-difference magnitudes by advantage pattern and matched ratios/budgets. This is an explicitly exploratory 36-environment extension, not a replacement or expansion of the registered grid for confirmatory inference.
- Add the exact coefficient formula for finite-label adoption risk, documenting the computation already used in independent checks. This is a mathematical derivation, not a new empirical hypothesis.
