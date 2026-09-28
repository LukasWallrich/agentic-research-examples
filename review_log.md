# Review log

## Scope and counting

Idea reviews precede preregistration and do not count as manuscript review rounds. At most three manuscript rounds will be run. Full original reviewer responses are preserved; the response records group related comments but retain all substantive requests. Review outputs are advice, not validation.

## Idea review — Claude CLI

Source: `reviews/ideas/claude.txt` (model metadata recorded separately where available).

1. Identities and Simpson-type reversals are not empirical hypotheses. **Accepted.** They will be derived as benchmarks.
2. Add hybrid/egocentric learning and endogenous reliance feedback. **Declined.** These add uncalibrated psychological parameters and change the estimand; a fixed-label decision problem is a narrower theoretical contribution.
3. Study finite-feedback correction costs. **Accepted.** Ranking loss and regret are primary outcomes.
4. Vary disagreement frequency at a fixed disagreement win rate to identify absolute versus paired learning. **Rejected as stated.** With fixed human marginal benchmark, both estimators' limiting values are unchanged; the proposed difference does not follow. A feedback-display × sampling interaction is the prospective behavioural test instead.
5. Fit parameters to existing data; do parameter recovery. **Declined for this study.** No psychological parameters are fitted; all numerical settings are labelled scenarios. Parameter recovery would not establish that humans use the model.
6. Clarify initial versus final decisions, positivity, horizons, and baseline. **Accepted.** Initial decisions, positive sampling in both strata, fixed verified-outcome budgets, and known marginal self accuracy will be explicit.
7. Universal claim that audited accuracy must be downward-biased above chance. **Rejected as overgeneralised.** Exact joint tables determine the direction; no universal downward-bias premise will be used.

## Idea review — Gemini 3.8 Flash (High), agy

Source: `reviews/ideas/agy.txt`.

1. Distinguish identities, computational results, and empirical predictions. **Accepted.**
2. Investigate finite-horizon bias–variance cost of inverse weighting and capped weights. **Accepted**, with fixed audit counts and post-feedback deployment regret.
3. Add absorbing reliance traps/cumulative regret. **Declined.** Fixed exogenous feedback cannot identify these processes; they will not be claimed.
4. Use Gaussian signal detection and subjective confidence distortion. **Declined.** Two calibrated confidence strata provide an interpretable controlled environment without additional unverifiable parameter choices.
5. Claim feedback format eliminates algorithm aversion, or voluntary auditing has a predictable confidence direction. **Rejected as too strong.** No empirical evidence establishes these universal claims. The human prediction is conditional and experimentally refutable.
6. Compare IPW to exploration policies and clipped correction. **Accepted in bounded form.** Sampling ratios include uniform and increasingly selective policies with positive support; clipped correction is prespecified. No optimality of a particular floor is assumed.
7. Use thousands of runs and define loss. **Accepted.** Monte Carlo uncertainty will be separated from human sampling uncertainty.
