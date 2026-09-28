# Independent Codex code and results review

The implementation supports both preregistered computational conclusions. I found no major error in the joint distributions, feedback selection, adoption rules, primary contrasts, or reported Monte Carlo uncertainty. Independent exact calculations agree with the focal simulations. The package needs the minor reproducibility and documentation corrections listed below before final delivery.

Reviewer: independent Codex agent, 28 September 2026. This review examined the current scripts and saved outputs, not the prior project's deleted analysis or manuscripts. The review added `scripts/independent_check.py` and `output/independent_check.json`; it did not change the preregistration or production simulation.

## Findings requiring a response

| ID | Severity | Finding | Required response |
|:--|:--|:--|:--|
| C1 | Moderate, reproducibility | `scripts/build_manuscript.py` imports Matplotlib, but the reviewed `requirements.txt` lists only NumPy, SciPy, and pandas. A fresh environment satisfying that file cannot build the figures. | Include the tested Matplotlib dependency and ensure the one-command script executes both analysis and manuscript generation. |
| C2 | Minor, documentation | At review, `deviations.md` still stated that no preregistration existed and no hypothesis-bearing analysis had run. | Replace the stale statement with the completed analysis status, implementation clarifications, and this reviewer-requested verification. |
| C3 | Minor, verification provenance | The `verify.py` docstring describes its checks as independent, although it imports the production joint-table, score, and exact-binomial helpers. The checks are useful but could share an implementation error. | Describe those checks as internal/algebraic verification and include the separate independent convolution checker in the reproducibility command. |

No additional major or moderate scientific issue was identified. The review does not establish novelty, validate citation claims, or show that humans use the stipulated rules; those require the manuscript and source reviews.

## Independent quantitative verification

The new checker imports no production simulation functions. It reconstructs focal joint distributions using rational arithmetic, conditions them on each audit policy, and computes the exact distribution of each rule's integer score numerator by repeated discrete convolution. For the absolute rule, it multiplies the score by the rational human benchmark's denominator. For the paired rules, the positive normalising denominator cannot affect the adoption decision. Thus signs and ties are evaluated exactly as integers. Probability calculations use floating-point arithmetic, but the benchmark has no Monte Carlo approximation.

This checks all 120 focal learner cells: both focal environments, every schedule, every budget, and every learner. Independently evaluated saved histories reproduce every focal adoption rate, regret estimate, and regret Monte Carlo standard error. Every simulated focal regret lies within the registered verification tolerance of five Monte Carlo standard errors plus 0.0001. Both primary contrasts' exact values also lie within their reported 97.5% intervals.

| Hypothesis | Exact weighted-minus-paired regret | Simulated contrast | Simulation minus exact, in Monte Carlo SEs |
|:--|--:|--:|--:|
| H1 | −0.04343921809507949 | −0.043573749999999994 | −1.1745756253 |
| H2 | 0.010878183975226894 | 0.0111225 | 1.6671930400 |

These values come from `output/independent_check.json`. The registered Monte Carlo estimates remain the primary results. The exact checks are verification, not replacement analyses or new hypotheses. Run them with `python3 scripts/independent_check.py`.

## Preregistration and implementation audit

The working preregistration matches git commit `68c07e4ca1858f382b131a0ee990adf562a271b0`. The recorded local commitment precedes the saved analysis timestamp. This is evidence of local prospective versioning; it is not an independently certified registry timestamp. The configuration matches the committed numerical specification even though the configuration file itself was written after commitment.

The grid has the specified 81 scenarios and a separately labelled homogeneous control. Each joint table obeys the feasible bounds and correct marginal accuracies. Structural zeros are retained; last-bit floating-point zeros are normalised without altering a substantive probability. Feedback probabilities are correct: disagreements are sampled at rates 1/k and 1, and random audits include all cases. Conditional multinomial histories are valid because all registered learners depend only on category counts, not feedback order.

The specified seed, PCG64 generator, and deterministic SeedSequence child order are implemented. Cells have separate streams; learners share histories within a cell, which correctly allows paired contrast standard errors. The recorded internal check recreates three saved cells from their child seeds. No adaptive stopping, hypothesis selection, or outcome exclusion appears in the code.

Adoption ties are integrated as probability one-half, which gives the expected risk of fair random tie-breaking without adding avoidable Monte Carlo noise. Global accuracy ties have zero regret and missing ranking error. The source-selection loss correctly measures the expected accuracy cost relative to the better fixed source on fresh random cases. It does not measure realised future errors, cumulative regret, or a personalised delegation policy.

The inverse weights restore the contrast among all disagreements, Δ/d. They do not restore separate marginal accuracies, which cannot be recovered when agreements have zero inclusion probability. Positivity holds for both disagreement strata at every registered selection ratio. Agreement exclusions do not compromise the comparative sign because agreement cases contribute zero to A−H. The manuscript's interpretation of these facts is correct.

The primary means and standard errors use the within-history regret difference. The normal critical value matches a two-sided 97.5% interval, and the support rule matches the committed directional criterion. The family-wise coverage claim is appropriately approximate because the intervals use a normal approximation. These are numerical integration uncertainties, not behavioural confidence intervals. The two exact primary checks substantiate the reported directions without relying on that approximation.

The descriptive grid excludes the extra homogeneous control from grid frequencies, retains inferior advisors and global ties, and uses the specified regret tolerance. The lowest observed improvement budget is a thresholded grid description, not an estimated continuous crossover. Expected opportunities equal the verified-label budget divided by audit yield, as required for independent Bernoulli selection.

## Numerical manuscript audit

`build_manuscript.py` draws its focal contrasts, table entries, selected accuracies, limiting paired scores, grid counts, and expected opportunities from saved outputs. Percentage-point conversions multiply probability-scale regret by 100 correctly. Focal environment selection is asserted unique. The code retains a numerical provenance ledger and does not replace the primary estimates with the independent exact values.

The current template distinguishes conditional model results from human evidence, identifies the absolute rule's known benchmark, and states the extra information needed for weighting. Figure lines are identified as guides between tested budgets. No numerical claim inspected in the builder contradicts its source outputs. Author declarations, final rendering, references, and the final one-command execution remain outside this bounded code review.

## Follow-up: exploratory analyses and corrected package

I reviewed and reran `scripts/exploratory_checks.py`, inspected its saved JSON output, and checked the revised numerical builder and manuscript template. No new major, moderate, or minor correctness issue was identified. This follow-up is a bounded code audit; the final complete pipeline run remains a separate validation step.

The initial findings are addressed. C1: the requirements now pin Matplotlib and `run_all.sh` invokes manuscript generation. C2: the deviations document identifies the completed registered analysis and explicitly separates the later exploratory additions. C3: the original verifier now describes its checks as internal, and the pipeline invokes the independent convolution checker.

E1 correctly treats encountered opportunities as the fixed resource. The unverified probability mass contributes a zero increment, while the absolute rule subtracts the human benchmark only on verified cases. Consequently its sign still compares the observed advisor hit rate with the benchmark when any label is available. When no labels occur, the declared fair-tie convention is implemented. Expected labels are the encounter budget multiplied by audit yield; they are not substituted for a fixed realised label count. The claimed equality of random and uniform-disagreement paired risks at fixed encounters is correct because agreement outcomes contribute zero to either decision numerator.

I additionally verified both focal E1 contrasts using a separate decomposition: mix the independent fixed-label convolution risks over a binomial distribution for the realised number of verified labels. This checks the encounter calculation through a different construction. I checked every E2 row against the independent convolution implementation, using its assumed integer weight. Across these 64 checks, the maximum absolute regret discrepancy was 1.1796119636642288e−16. The exploratory script itself produces 180 rows and passed all its checks when rerun.

The E2 threshold follows from the weighted numerator per encounter, $p\delta_L w/k+(1-p)\delta_H$. In the crossing environment, a positive limiting comparison requires $w>k/2$; equality gives zero. Positive weights preserve the homogeneous control's correct limiting ordering, while finite-sample error can still change. The manuscript correctly distinguishes these limiting properties from finite-feedback optimality and labels E1 and E2 exploratory.

The confidence-stratum oracle chooses the better source within each confidence stratum using the stipulated stratum accuracies. It has no access to casewise correctness. Its reported accuracies, 0.85 for the crossing environment and 0.80 for the homogeneous control, are correct. The manuscript identifies it as an action-space benchmark and does not claim that a learned policy achieved these values.

The `capped_limits.limiting_numerator` field is the mean weighted numerator per audited label, not the normalised weighted score. Its name is accurate. The manuscript uses its zero/sign implication only; division by a positive expected weight cannot alter either. The stated neutral capped boundary is therefore correct. Likewise, the new `tie_probability` field in the core summary merely reports the fraction of existing scores within the registered tie tolerance. It does not change the adoption rule, random streams, generated histories, or primary contrasts.

The revised manuscript builder preserves the original Monte Carlo primary estimates and adds the independent exact contrasts as verification. Encounter contrasts, expected labels, oracle accuracies, matched focal comparisons, and the stratified grid counts are taken from the appropriate outputs. Percentage-point conversions remain correct. The manuscript makes no false equivalence between fixed opportunities and fixed labels, or between the global source oracle and confidence-contingent routing.

## Follow-up: E3 sign-pattern extension

The bounded audit of `scripts/exploratory_grid.py` and its JSON/CSV outputs found no new correctness issue. I reran the script and checked the four combinations of within-stratum advantages, each ±0.05, crossed with the three population shares and three overlap positions. The resulting 36 environments, five schedules, three budgets, and four learners produce the reported 2,160 rows. This is an explicitly exploratory extension, not an alteration to the registered grid.

The absolute rule uses the actual marginal human accuracy in each environment. When the low-confidence proportion is 0.25 or 0.75, the rational benchmark is respectively 33/40 or 27/40; at equal shares it is 3/4. Its integer score increments therefore scale by the applicable denominator rather than assuming a 0.75 benchmark everywhere. I checked all 540 absolute-rule risks against direct binomial probabilities with exact integer threshold and tie comparisons. The largest absolute regret discrepancy was 2.699229728619912e−15. The binomial comparison clips last-bit roundoff when recovering a probability from a saved limiting score at a structural boundary; it does not change the production calculations.

Fair score ties and global source ties are handled separately and correctly. The six environments with globally equal accuracy retain zero regret and undefined ranking error. The reported weight-equality checks pass. Positive normalising denominators yield the correct limiting score for paired, weighted, and capped rules, and the absolute limiting score uses the rational benchmark's denominator.

The matched ratio-4, budget-100 summaries select one weighted row per environment before taking contrasts. Each pattern-by-overlap summary spans the three population shares; each overall pattern range spans nine environments. I recomputed their minimum and maximum contrasts from the CSV and found agreement with the JSON summaries. Their numerical equality tolerance is explicitly reported as part of E3 and does not replace the registered descriptive tolerance.

The overlapping homogeneous-control environment reproduces all 60 corresponding independent exact risks, with a maximum discrepancy of 9.841845220737166e−17. File hashes before and after the E3 rerun confirm that the preregistration, configuration, primary contrasts, primary summary, and raw simulated histories did not change. No implementation changes were made during this review.
