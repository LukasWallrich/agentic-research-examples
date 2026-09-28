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

## Independent Codex code/results review

Source: `reviews/code/codex_review.md`; exact verification: `scripts/independent_check.py` and `output/independent_check.json`.

- **C1 (moderate), missing plotting dependency:** accepted. Matplotlib is pinned in `requirements.txt`, installed in the task environment, and manuscript building is in `run_all.sh`.
- **C2 (minor), stale deviations status:** accepted. Replaced the pre-analysis placeholder with current preregistration provenance and explicit implementation clarifications.
- **C3 (minor), internal checks described as independent:** accepted. Internal checks reuse model helpers; a separate reviewer-written integer-score/convolution implementation now checks the focal risks without importing the model code.
- No major numerical or preregistration-alignment issue found. The independent checker covers all focal learner cells and places both exact registered contrasts inside their Monte Carlo intervals. This is implementation verification, not evidence of human behaviour.

## Manuscript round 1 — Claude

Full report: `reviews/manuscript/claude_r1.txt` (raw runtime response `claude_r1.json`). Runtime models: `claude-fable-5-1` with auxiliary `claude-haiku-4-5-20251001`. Verdict: major revision. Each numbered comment is addressed below; the report's M1–M8/m1–m11 are elaborations of these same numbered requests.

| Comment | Response and disposition |
|---|---|
| 1, exact focal risks | Accepted. Independent convolution verifies all focal cells and exact registered contrasts are shown beside Monte Carlo results. The original registered estimates are retained rather than retrospectively replaced. |
| 2, hypothesis/support framing | Accepted in substance. Text calls these registered computational predictions and fixed model consequences, reports numerical directions, and explicitly says prospective reporting does not create empirical uncertainty. Original support classifications remain in machine-readable output to preserve the plan. Rejected the claim that the law of large numbers alone guarantees finite-n risk ordering; exact checks establish those values. |
| 3, reversal threshold | Accepted. Added analytic threshold and explicit focal neutral point. |
| 4, capped neutral boundary | Accepted. Identified the zero target at cap 2 / true ratio 4 and removed any suggestion that near-chance adoption demonstrates a useful compromise. |
| 5, matched focal comparisons | Accepted. Added exact matched-budget/ratio table. |
| 6, nonparallel scenarios | Accepted. Explained differences in disagreement rate, informativeness, ratios and budgets; scenario choices were made deliberately from the analytic structure. No isolated causal-factor claim remains. |
| 7, routing oracle/global task | Accepted. Added exact confidence-contingent oracle and concrete constrained-batch handoff setting. |
| 8, within-stratum pairing | Accepted with qualification. It avoids between-stratum weights for conditional signs; it does not universally dominate in finite samples with sparse strata. No unproved dominance claim added. |
| 9, stratum definition | Accepted. Defined delta conditional on stratum but not disagreement, and displayed the cancellation. |
| 10, information/misspecified weights | Accepted except calibration is not mathematically required for weighting. Listed stratum labels and known selection ratio; gave analytic misspecification condition and exploratory exact sensitivity. |
| 11, capped target/known human benchmark | Accepted. Wrote capped numerator and explained absolute rule's information advantage in random feedback. All rules receive the same records; they use different statistics. |
| 12, opportunity matching | Accepted. Added E1 exact fixed-opportunity analysis and random versus uniform-disagreement equality. Labelled exploratory. |
| 13, display compliance/disclosure | Accepted. Distinguished decision-support intervention from unaided cognition; added raw-history and schedule-disclosure conditions to the future test. |
| 14, response model/refutation | Partly accepted. Specified a monotone logistic-with-lapse family, fixed-across-schedule parameters, distinct orderings, and held-out model comparison. A human practical-effect threshold, power, and sampling protocol cannot be learned from this simulation and are explicitly reserved for a future prospective experiment. No claim of a completed human-study preregistration. |
| 15, references/registries | Accepted. All cited claims checked against primary sources; eight initial published references Crossref-verified, two preprints independently DataCite-verified after documented Crossref 404s. Additional foundations verified as added. Reviewer input initially contained citation keys rather than the citeproc-rendered bibliography; later inputs contain the full bibliography. |
| 16, missing foundations | Accepted selectively. Added Einhorn & Hogarth, Elwin et al., and McNemar with source audits. Elwin is a substantive precedent and counterweight to naive learning. Declined a long indiscriminate citation list: this paper makes no general claim about algorithm aversion or all judge–advisor mechanisms, and Gao directly establishes IPW precedent. |
| 17, human accountability | Agreed as a prerequisite for submission; not falsely asserted. User requested an autonomous local draft and forbade submission. Human endorsement cannot be manufactured. Disclosure retains this limitation. |
| 18, model details | Accepted. Added available Claude model metadata and described coarse as a multi-stage academic review pipeline. Initial idea-call version remains explicitly unavailable. |
| 19, public timestamp | Declined within this task. The user required a git commitment before simulation, which is preserved; the manuscript explicitly distinguishes that from external preregistration. Public deposit cannot retroactively supply a prospective timestamp and is outside local preparation. |
| 20, discussion duplication/grammar | Accepted. Replaced repeated Results sentences with interpretation and corrected grammar. |
| 21, abstract error direction | Accepted. States that mismatched absolute comparison can reject a superior advisor. |
| 22, tolerance units | Accepted. Reports proportion and percentage-point units. |
| 23, tie probabilities | Accepted. Added reporting-only tie probabilities to all simulation rows and a focal supplementary table; did not alter any score or outcome. |
| 24, binary assumption | Accepted. States exactly-one-correct equivalence; removed unnecessary truth-symmetry wording. |
| 25, boundary cells | Accepted. Described zero-probability categories and deterministic limits. |
| 26, grid strata | Accepted. Added superior/inferior/tied breakdown; ties are transparently zero regret. |
| 27, defensive prose | Accepted selectively. Removed repetitive contrastive claims, retaining necessary distinctions of numerical versus behavioural evidence and local versus public commitment. |
| 28, figure uncertainty/labels | Accepted. Added Monte Carlo error bars. The original already had log budget axes and ratio-labelled panels; these are retained. |
| 29, title punctuation | Accepted. Added colon. |
| 30, archive plan | Accepted as a future plan. Named a versioned persistent repository/DOI or journal supplements without inventing a link or publishing anything. |

## Manuscript round 1 — Gemini 3.8 Flash (High)

Full report: `reviews/manuscript/agy_r1.txt`. Verdict: major revision. Responses below cover its numbered list and all corresponding major/minor elaborations.

| Comment | Response and disposition |
|---|---|
| 1, numerical consequences versus empirical tests | Accepted framing correction; retained registered predictions/output labels transparently. Exact focal values now verify directions. The review's claim that asymptotics guarantee the n=100 ordering is not a valid finite-n proof. |
| 2, rendered bibliography | Accepted. Bibliography existed in rendered PDF/HTML; the first text review input omitted citeproc expansion. Later reviews receive full references. |
| 3, foundational JDM | Accepted selectively: Einhorn, Elwin, and McNemar added and audited; broad algorithm-aversion/JAS citations would imply a scope this model does not have. |
| 4, delta definition | Accepted, with cancellation shown. |
| 5, conditional target and non-zero cost | Accepted. Added magnitude/disagreement-rate requirement for non-zero adoption costs. |
| 6, encounter matching | Accepted. Exploratory exact comparison added; directions persist but magnitudes differ. |
| 7, stratified action space | Accepted. Added oracle and within-stratum alternative, without claiming finite-sample dominance. |
| 8, cognitive versus display intervention | Accepted. Reframed immediate target as a decision-support intervention and supplied additional conditions needed to study cognition. |
| 9, misspecified weights | Accepted. Analytic threshold and exploratory exact sensitivity added. |
| 10, cap rationale | Accepted. Simple prespecified intermediate cap, not an optimised choice; neutral-boundary artefact explicitly described. |
| 11, assert human oversight | Cannot honestly comply. No human review has occurred during this autonomous task. The disclosure accurately marks this local draft as requiring human accountability before submission, which the user forbids now. |
| 12, grammar | Accepted. |

## Coarse pipeline runtime note

The first round-1 coarse attempt failed because gpt-5.4 is unsupported by the current authenticated Codex account. No completed review came from it. A one-line CLI probe reproduced the error and the identical probe succeeded with locally available gpt-6-sol. The full pipeline was restarted with that model; this is a runtime retry within round 1, not an additional scientific review round. The local-path mode has no upload callback; no review or manuscript was publicly posted.

## Manuscript round 1 — full coarse pipeline

Full report: `reviews/coarse/r1/review_copy_r1_review.md`. Completed local pipeline using Codex gpt-6-sol, high effort; includes structure, overview, section, mathematical verification, and editorial stages. Recommendation: major revision. It produced six overall concerns, five overlapping key revision targets, and three detailed comments. All are addressed below.

| Comment | Response and disposition |
|---|---|
| Overall 1 / key target 1, confidence-contingent deployment | Accepted scope correction and oracle comparison. The manuscript explicitly targets constrained global batch handoff, gives the conditional oracle, and explains within-stratum pairing. A learned routing analysis is outside the declared decision problem and is not added merely to optimise a different objective. |
| Overall 2 / key target 2, restricted advantage patterns and nonparallel contrasts | Accepted. Added E3, a clearly exploratory symmetric extension covering all four conditional advantage sign patterns at common ratios, budgets, confidence mixtures, and overlap positions. Original registered grid retained intact. Matched focal comparisons and nonparallel-design limitations added. |
| Overall 3 / key target 3, oracle weights/positivity/within-stratum selection | Accepted in part. E2 quantifies misspecified weights and the analytic condition covers cap-induced sign changes. Explicitly state conditional ignorability and positivity requirements and that no correction identifies an entirely unverified stratum without additional assumptions. Estimated-propensity models and every possible within-stratum selection mechanism are outside this scenario study; no robustness to them is claimed. |
| Overall 4 / key target 4, equal opportunities | Accepted. E1 compares all focal policies at fixed encounters, with expected labels and exact risks. Random and uniform-disagreement paired risks coincide at fixed opportunities. |
| Overall 5 / key target 5, behavioural evidence or computational development | Chose the permitted computational route. No new human data were collected. Added an exact finite-feedback risk formula and explicit boundary equation, narrowed behavioural interpretation to an unvalidated intervention, and improved the future model comparison. |
| Overall 6, usable weighting rule/grid magnitudes/cap boundary | Accepted computational development. Full machine-readable risk magnitudes already exist for all registered cells; matched tables, explicit cap-neutral point, and exact E3 summaries by sign pattern supplement counts. The paper provides conditional boundaries, not a universal deployable rule that assumes unknown true accuracies. |
| Detailed 1, what history stays fixed | Accepted. Histories are generated separately under assigned selection schedules and held fixed across display conditions within a schedule. |
| Detailed 2, which missing cases contribute zero | Accepted. Named agreements specifically; unverified disagreements are nonzero and their selection still matters. |
| Detailed 3, tolerance categories | Accepted. Define weighted-minus-paired differences below the negative tolerance, within inclusive bounds, or above the positive tolerance. |

The failed gpt-5.4 attempt did not produce scientific comments and does not count as another round. The full completed report and all reviewer criticism remain preserved even where the response declines an expansion of scope.

## Manuscript round 2 — Codex follow-up to coarse

Report: `reviews/coarse/r2_followup.md`. This was a bounded independent reassessment of the completed full coarse report, not a second full pipeline. Verdict: minor revision, no remaining substantive major issue within the constrained computational scope.

- **R2-1:** Move conditional random-verification assumption beside the selection equation. Accepted; the analytic section now states it immediately before defining the ratio.
- **R2-2:** Remove obsolete bibliography count in the source audit. Accepted; the current bibliography has thirteen entries.
- Residual limitations are retained: modest theoretical priority, symmetric scenario extension, known/conditionally ignorable sampling, fixed-source action space, and untested behaviour. The follow-up does not validate these assumptions or grant journal acceptance.

## Manuscript round 2 — Claude

Raw report: `reviews/manuscript/claude_r2.txt`, with runtime JSON retained. Verdict: minor-to-moderate revision, but three substantive major issues identified. Each is addressed before the final round.

| Comment | Response and disposition |
|---|---|
| 1. Known ratios are not necessary | Accepted. Added encounter-count estimation and the explicit post-stratified estimator, assumptions, empty-stratum problem, and the distinction between known-weight and estimated-weight finite-sample risks. The evaluated algorithm receives the true ratio; the manuscript no longer presents this information as a general requirement. Declined an additional estimator experiment: its encounter-level sampling and empty-cell rule require a separate design; no equality or universal direction of its risk is claimed. Independent Codex review confirms the estimator's feasibility and this limit. |
| 2. One-sided registered grid | Accepted. Methods and Results explicitly state its positive low-confidence/nonpositive high-confidence advantage pattern, why selection favours the human, and why reversals occur only among superior advisors. Other sign patterns are supported only by the narrow exploratory extension. |
| 3. Behavioural test source identity and benchmark | Accepted. The initial proposed test explicitly compares two described sources and supplies the baseline's marginal accuracy. Self-evaluation requires a separate replay/yoking design with participants' own judgements. Added the inequality needed for the absolute rule's below-chance prediction and an encounter-count condition for selection-aware learning. |
| 4. Abstract contrast differences | Accepted. Names the stronger selection ratio as well as smaller budget and reports that matched comparisons preserve the directions. |
| 5. Ignorability beside identity | Accepted. Both positive support and within-stratum independence of verification from which source is right appear beside the weighting claim. |
| 6. Identical E3 minima | Independently checked and confirmed, not an error. Mirrored score signs and global superiority at the maximum-overlap environments preserve each history's loss. Binomial verification and environment identities are in `reviews/code/e3_minima_check.md`; the manuscript explains the symmetry. |
| 7. Draft-history language | Accepted. Renamed the section Exploratory analyses and replaced rebuttal-style statements with current facts about the neutral cap, supplied benchmark, prespecified cap, and unrounded probabilities. |
| 8. Repetition/reporting | Accepted. Exact contrasts retained in the table instead of repeated sentences; grid subgroups and E3 ranges use compact tables; repeated introductory identity removed. |
| 9. Selection labels | Accepted. Table labels distinguish all cases from disagreements and state the ratio. |
| 10. Byline | Accepted. Added “draft; author approval pending” directly beside the intended author's name. |
| 11. Future submission requirements | Accepted as future actions. Human accountability, declarations, and persistent public archiving remain explicit; no certification or upload performed. |
| 12. References / review-log assessment | No requested bibliographic change. The reviewer did not verify references independently; our primary-source and registry audit remains the evidence. Their disagreement with the previous known-ratio response is resolved under comment 1. |

## Manuscript round 2 — Gemini 3.8 Flash (High)

Report: `reviews/manuscript/agy_r2.txt`. Verdict: accept with minor revisions; no substantive major issues identified. This is an AI review verdict, not journal acceptance.

| Comment | Response and disposition |
|---|---|
| 1. Binary decisions | Accepted. The analytic framework begins with two alternatives and exactly one correct response, and explicitly gives the disagreement relation. |
| 2. Integer increments | Accepted. Defined the positive scaling denominator and integer increments separately from raw scores, with sign invariance. |
| 3. Selection ratio | Accepted. Defined the high/low verification probability ratio beside the selection equation. |
| 4. Presentation order | Accepted. The future experiment counterbalances or pseudorandomises order; human order sensitivity is distinct from exchangeable computational summaries. |
| 5. Submission administration | Recorded as future requirements only, as for Claude 11. |

Gemini's narrative summary mistakenly prints a negative lower endpoint for the H2 Monte Carlo interval. The saved analysis and manuscript correctly give a wholly positive interval. Reviewer prose is retained unchanged as provenance and does not supply manuscript numbers.

## Manuscript round 3 — final reviews

Reports: `reviews/manuscript/claude_r3.txt` and `reviews/manuscript/agy_r3.txt`. Claude: minor revision, no substantive major issue within the declared scope. Gemini: accept pending human endorsement/administration, no substantive major issue. These are automated evaluations, not journal decisions. This is the third and final manuscript round; the minor corrections below do not initiate a fourth round.

### Claude comments

| Comment | Response and disposition |
|---|---|
| 1. Confidence during learning versus deployment | Accepted. Added the concrete case of an initial human evaluation phase followed by batch handoff without human initial judgements; confidence is then unavailable at deployment. |
| 2. Inputs to selection-aware prediction | Accepted. Restrict the prediction to disclosed schedules or encounter counts that identify selection; state that the stipulated account makes no prediction without either input. |
| 3. Ratio in paired prediction | Accepted. State the reversal-threshold condition and focal ratio explicitly. |
| 4. Mixed strategies | Accepted clarification. The proposed comparison concerns pure summary rules; reversal rejects that pure-rule account, not every mixture. A mixture analysis would require its own prospective specification. |
| 5. Misspecified-weight magnitudes | Accepted. Added exact regrets for all tested assumed weights in both focal settings, generated directly from the existing E2 CSV. No new analysis or selected-only comparison introduced. |
| 6. Fixed-encounter exact formula | Accepted. Added the encounter-category distribution and zero contribution for unaudited cases. The reviewer refers to Table 4 as fixed-encounter, but that table is correctly labelled fixed-label matched comparisons; only the E1 paragraphs use encounter budgets. |
| 7. Random all-case at fixed encounters | Accepted. Explicitly define it as verifying every encountered case. |
| 8. Inferior-advisor costs | Accepted. Connect these grid results to selection supporting the correct ranking and correction removing that support. |
| 9. Cap wording | Accepted. Combined prospective fixation and simple intermediate-rule rationale in Methods; removed the isolated defensive sentence. |
| 10. Table 1 layout | PDF checked: wrapped headers align correctly with all values. HTML tables retain semantic columns. The text-only review rendering is not the final layout. Additional PDF layout work keeps focal tables and captions together. |
| 11. Byline | Confirmed in PDF, HTML, TeX and editable frontmatter: intended author and draft/approval-pending status. The plain-text review copy omitted YAML metadata, not the delivered formats. |
| 12. Git history | Accepted. The archive plan retains the full unsquashed history, while explicitly preserving the lack of independent historical timestamp. No archive upload performed. |

### Gemini comments

| Comment | Response and disposition |
|---|---|
| 1. Table 3 subgroup budget | Accepted clarification that the subgroup rows describe the largest registered budget. Rejected calling it an “asymptotic regime”: it is a finite budget and does not establish a uniform asymptotic approximation. |
| 2. Tie extraction | Accepted. Explain that the constant coefficient is the exact score-tie probability and the half factor implements fair random choice. |
| 3. Empty-stratum examples | Accepted with limits. A preregistered prior or retaining the baseline until each stratum has feedback illustrates possible choices; each adds assumptions or changes the stopping policy and needs separate evaluation. No fallback is claimed to identify an unobserved stratum without assumptions. |
| 4. Compiled metadata | Confirmed full title, byline, and approval-pending status in the compiled formats. The review report's shorthand title does not change the manuscript title. |
| Future requirements | Retained human endorsement, declarations, and persistent archiving/reviewer access as future submission actions. No human approval, affiliation, public DOI or journal acceptance is fabricated. |

### Final review status

All actionable comments from the idea, code, manuscript and full coarse reviews have a recorded response. Remaining scientific limits are collected in `weaknesses.md`. No further review round is run. The completed full coarse report remains preserved with its original major-revision recommendation; the subsequent bounded Codex reassessment and final cross-model reviews assess the revised manuscript rather than altering that report.
