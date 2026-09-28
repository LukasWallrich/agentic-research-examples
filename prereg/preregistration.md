# Preregistration: selective feedback and comparative advisor evaluation

Date: 28 September 2026. Status: local prospective simulation registration, to be committed to git before any hypothesis-bearing run. This is not an independently timestamped registry or Registered Report. The commit hash and output time will be recorded in `prereg/provenance.json` after commitment.

## 1. Question and exposure

When does correcting confidence-selected verification feedback improve a global choice between one's own initial decision and an advisor's decision, at a fixed verified-outcome budget?

This is a simulation study with no participant dataset. Scoping read published findings, mathematical arguments, dataset landing pages and codebooks listed in `scoping/journal_and_data.md`; no participant outcome variable was loaded. Claude and Gemini reviewed an idea in prose. No numeric simulation, parameter sweep, or hypothesis-bearing computational result has been generated. Algebraic inspection established the identities and reversal conditions below. A prior project exists in git history with deleted working files; its outcomes and manuscripts were not opened for this project.

## 2. Known analytic benchmarks (not hypotheses)

Let H and A denote initial human/advisor correctness, and D indicate disagreement of binary responses. Let Δ=E[A−H], d=P(D). Because A−H=0 on agreement, E[A−H|D]=Δ/d. Thus uniformly sampled disagreements preserve the sign when d>0. On a binary disagreement exactly one source is right, so E[A|D]=(1+Δ/d)/2. An absolute learner compares this with known marginal human accuracy h and chooses the advisor only when Δ>d(2h−1). No universal downward bias in absolute advisor accuracy is assumed.

With low-confidence share p, conditional advantages δL and δH, and high:low verification rate ratio k, the unweighted paired numerator is pδL+(1−p)kδH. Its sign can differ from Δ only if the advantages cross zero. Reciprocal sampling weights restore the sign when both strata have positive verification probability. They do not identify the separate marginal accuracies, because agreement feedback is absent. Normalised weighting is not claimed finite-sample unbiased.

## 3. Generative environments

Truth is binary and balanced; symmetry makes correctness tables sufficient. Human confidence strata have calibrated accuracy hL=.60 and hH=.90. Low-confidence share p∈{.25,.50,.75}. Advisor accuracies aL∈{.65,.80,.95}, aH∈{.70,.80,.90}. For each stratum, let lower=max(0,h+a−1), upper=min(h,a); both-correct probability q=lower+r(upper−lower), r∈{0,.50,1}. The four outcome masses (both correct, human only, advisor only, both wrong) are q,h−q,a−q,1−h−a+q. r indexes overlap within feasible bounds, not Pearson correlation. All 81 combinations are reported, including inferior advisors and exact ties. These are scenarios, not empirically fitted parameter estimates or a representative sample of environments.

Two focal scenarios have p=.50 and r=.50:
- Crossing advantage: aL=.80, aH=.80 (advisor global accuracy .80 vs human .75).
- Homogeneous advantage control: aL=.65, aH=.95 (same global accuracies; advisor advantage .05 in each stratum). This additional environment is outside the grid's high-stratum list and is included separately, not pooled twice.

## 4. Feedback and learners

Each run independently draws n verified outcomes with replacement from the exact audit-conditioned categorical distribution. n∈{20,100,500}; 20,000 independent runs per environment × sampling schedule × n. Seed 20260928, NumPy PCG64; use child streams from SeedSequence in deterministic environment/schedule/budget order. Learners in a cell share the same outcome counts for paired comparisons; separate cells use independent streams. No early stopping or changing simulation count after results.

Schedules: random all-case verification, or disagreement-only verification with k∈{1,2,4,8}; for disagreement schedules actual selection probabilities are 1/k in low confidence, 1 in high confidence, and zero on agreements. Report audit yield and n/yield expected opportunities. Equal n equates verified labels, not decision opportunities or total costs.

Four learners choose one source globally for future randomly drawn cases:
- Absolute: observed advisor accuracy minus the known global human accuracy.
- Paired: observed mean A−H.
- IPW paired: weighted mean A−H with inverse selection weights (k for low and 1 for high under disagreement; all weights 1 under random).
- Capped paired: same but cap weights at 2 (random weights 1).

Choose advisor when score>0, self when score<0. At |score|≤1e−12, average exactly over fair random tie-breaking (half adoption), avoiding an extra RNG. Correct global ranking is undefined at |Δ|≤1e−12; retain these cells and report zero regret, mark ranking error missing. Regret per future decision is |Δ| times the probability of choosing the inferior source. Do not call this cumulative regret, personalised delegation, or a model of trust dynamics.

## 5. Confirmatory computational hypotheses

**H1:** In the focal crossing environment with k=4 and n=100, IPW paired has lower expected deployment regret than unweighted paired. Primary contrast is regret(IPW)−regret(paired).

**H2:** In the homogeneous-advantage control with k=8 and n=20, IPW paired has higher expected deployment regret than unweighted paired. Primary contrast is regret(IPW)−regret(paired). This tests whether removing selection can harm finite-label adoption decisions when selection favours informative comparisons.

Compute each contrast within shared simulated histories. Report mean, Monte Carlo standard error (sample SD/sqrt(20,000)), and a two-sided 97.5% normal Monte Carlo interval (z=2.2414027276), giving Bonferroni family-wise coverage of at least 95% for the two prespecified contrasts under the approximation. Support requires the entire interval on the predicted side of zero; an entirely opposite interval contradicts; overlap means unresolved computational precision. These intervals measure simulation error only. No p value or count of agents supplies evidence about humans. Report effect magnitude even if direction passes. Never rerun or alter a hypothesis to secure support.

If H1 fails, weighting is not beneficial at its prespecified scenario/budget; do not claim correction reliably improves adoption. If H2 fails, the anticipated finite-label cost is not demonstrated in its prespecified scenario; do not claim an inevitable correction penalty. If both pass, report a conditional tradeoff, not a universal superiority claim. If neither passes, report that the proposed finite-label predictions failed.

## 6. Prespecified descriptive analyses

Report all cell risks, adoption rates, mean scores, score SDs, exact limiting scores and directions, and audit yields. Compare capped correction, IPW, paired, and absolute learners at every n/k. Summarise grid counts of better/worse/equal expected Monte Carlo regret descriptively with a tolerance of .0005 regret; these counts describe the arbitrary grid, not prevalence in real tasks. Report the lowest observed n at which IPW beats paired in each environment/schedule, or none; do not interpolate an unobserved crossover. Separate cases with no population sign reversal from cases with reversal. Retain all outcomes.

Verification: check nonnegative joint probabilities and correct margins; sign identity and weighted limiting sign throughout; k=1 learner equivalence; exact binomial majority and absolute-threshold error probabilities for focal uniform-disagreement cells; Monte Carlo errors should be within five estimated standard errors plus 1e−4. Add a direct independent categorical/trial simulator check if reviewer requests it, labelled verification rather than a new hypothesis. Floating-point errors halt the pipeline; do not silently exclude cells.

## 7. Refutable human prediction (not tested here)

A future experiment randomises identical feedback histories to advisor-only accuracy, paired accuracy, or selection-adjusted paired summaries, crossed with uniform and high-confidence disagreement selection. Before feedback, participants receive the true marginal human benchmark; they choose a source for fresh random cases, and report perceived global advantage. In the crossing focal world, the estimator mapping predicts greater advisor adoption with paired than absolute displays under uniform disagreement feedback, but loss of that protection under k=4 selective feedback; weighted summaries recover adoption with sufficient n. Its discriminating endpoint is the display-by-schedule interaction in adoption, not simply greater trust. Include an inferior-advisor control to distinguish discrimination from indiscriminate reliance.

The behavioural account fails if, with comprehended displays and manipulation checks, human adoption does not show the predicted interaction, or tracks an alternative rule better. A future study must commit its sample size, quantitative effects/intervals, comprehension criteria, and competing models before collecting data. Current simulations cannot confirm the human mapping, and algebra is not subject to behavioural falsification. The study satisfies prospective empirical refutability by specifying this risky extension, not by claiming to reproduce an existing dataset.

## 8. Exclusions, deviations, and reproducibility

No simulated histories excluded; no participants or personal identifiers. Zero-mass categories remain legal. No exploratory result may replace a confirmatory test. Changes after this commit go in `deviations.md` with timing and reason. All empirical-looking numbers in the manuscript must be generated from analysis outputs; scenario constants will also be included in output metadata. One command `./run_all.sh` regenerates raw synthetic sufficient-statistic counts, analysis tables, checks, and manuscript from the committed configuration. Software versions and file hashes are recorded. Independent Codex reviews code/results; Claude and Gemini review the manuscript, followed by the full coarse pipeline, with at most three manuscript rounds.
