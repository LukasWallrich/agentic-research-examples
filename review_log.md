# Review log

Every reviewer comment and the response to it. Raw reviewer outputs are in `reviews/` (scoping critiques in `reviews/scoping/`, code review in `reviews/code/`, manuscript reviews in `reviews/manuscript/`). "Accepted" means the change was made; "Rejected" gives the reason.

## Round 0: Code and results review (codex, after the confirmatory analysis)

Source: `reviews/code/codex_answer_code_review_1.txt`. Codex confirmed that the preregistered rules produce the committed verdicts, that the inclusion rules reproduce the registered design counts, and that the models implement their stated equations.

| # | Severity | Comment | Response |
|---|---|---|---|
| C1 | Major | The external benchmark (Jacowitz & Kahneman's index of about .49) is a raw-scale quantity, but the calibration used a log-scale index. | Accepted as a sensitivity analysis. S1 (`R/05b_sensitivity.R`) recalibrates all models to a raw-scale index; the accepted parameter sets overlap almost completely and model survival is unchanged. The frozen predictions stay as preregistered; the manuscript reports both. |
| C2 | Major | M1R's parameter kappa does not have the meaning stated in the preregistration (the code multiplies sigma, not the 0.6 sigma spread of belief centres). | Accepted as a documentation correction (deviation D2). The code, and hence the predictions, are unchanged; the description in the manuscript follows the code. |
| C3 | Major | H3 compares a weighted mean index (simulation) with a multilevel intercept (observed). | Accepted (deviation D1). The observed level statistic now uses the same inverse-variance weighted mean as the simulation. Survival is decided by shape criteria and does not change. |
| C4 | Major | H1 rests largely on one study (13 of 20 cells); no study-level effect; R3 without Bahník is uninformative. | Accepted. Added S2: leave-one-study-out, a study random effect, and single-study fits. The manuscript presents study dependence as the first limitation and in the abstract ("mostly random anchors"). |
| C5 | Major | 870 of 987 gross errors come from one cell (Shanks et al., 2020, Study 3, Chicago) with a unit mismatch; the cell drops out. | Accepted. Documented in `deviations.md` and in the Method and Results; no change to the rule, which was applied as preregistered. |
| C6 | Minor | Stratum-level model simplifications (Q23 fallback) not logged. | Accepted; listed in `deviations.md` under contingency rules. |
| C7 | Minor | Operating characteristics use normal critical values and the full random structure, unlike Q22. | Accepted; described as approximations in `deviations.md`. The manuscript reports them as rounded shares (above 99%). |
| C8 | Minor | Rho CI uses a normal quantile while b and g use Satterthwaite t. | Accepted as a clarification (deviation D4); stated in the Method. |
| C9 | Minor | H2 has an extreme range of sampling variances; ten cells hold about 61% of the weight; participants appear in several cells. | Accepted. S3 adds study-clustered robust SEs, a fit without the ten most precise cells, and leave-one-study-out; the manuscript now says the across-cell slope is not robust. |
| C10 | Minor | H2 fallback did not check whether clubSandwich is installed. | Accepted; fixed in code (not triggered). |
| C11 | Minor | R2 fit has no convergence check; unlabelled warnings in the log. | Accepted; warnings from R2 and R3 are now labelled. The unlabelled convergence warning came from a fit that the preregistered fallback discarded. |
| C12 | Minor | Present the positive-leaning across-cell slope as an unresolved design difference, not a sign change within the same items. | Accepted; the Discussion describes two candidate explanations and says the data cannot separate them. |
| C13 | Nitpick | Misspelt task type "quantitity" in the inclusion list. | Accepted; removed (no analysed rows affected). |
| C14 | Nitpick | R4 silently drops cells with zero SE; MAD floor not registered. | Accepted as documentation: neither rule affected the observed cell set (noted in `deviations.md`, D3). |
| C15 | Nitpick | Data hash check used only the first 16 characters. | Accepted; now checks the full SHA-256. |

## Round 1: Manuscript review

### Reviewer: Gemini 3.8 Flash via agy (recommendation: major revision)

Source: `reviews/manuscript/agy_answer_r1.txt` (reviewed the first draft).

| # | Severity | Comment | Response |
|---|---|---|---|
| A1 | Major | Title, abstract and conclusion state the within-item decline as a general rule, although 83% of within-item estimates come from Bahník (2021), random anchors for lengths and heights; without it the estimate is uninformative. | Accepted. New neutral title; the abstract now gives the share from one study and its anchor type and ends with the open question for deliberate anchors; the conclusion names the evidence base. The first limitation already covered this. |
| A2 | Major | Practical advice to negotiators is an unwarranted extrapolation from random anchors and contradicts the positive-leaning across-cell slope. | Accepted. Removed the "diminishing returns for anyone choosing an anchor" sentence; the conclusion now says the data cannot answer the question for deliberate, informative anchors. The introduction's practical motivation remains, phrased as a question. |
| A3 | Major | M1 is a strawman; M1R "survived" only through a very wide rho interval while its g interval excluded the observed value; M3/M4 predicted g correctly. | Accepted in substance. The M1 paragraph now says M1 is not a defended theory but the mechanistic core of the resource-rational account with fixed adjustments (as in Lieder et al.'s fit with 29 adjustments). The H3 results and the abstract state that M1R's survival reflects wide predictions, that its g interval excluded the observed value, and that M3/M4 contained the observed g. We keep the preregistered survival rule and report its outcome as registered. |
| A4 | Major | E4 reported only the ratio specification, not the model with spread as a separate predictor, whose extremity slope stayed positive. | Accepted. Both specifications are now reported in Results and Discussion, with a note on ratio-predictor artefacts; the claim that E4 explains the across-cell pattern was removed. |
| A5 | Major | No descriptive table of the 20 within-item cells. | Accepted. Added Table 1 (study, item, true value, N, anchor levels, range of x, anchor type), generated by `R/05c_within_cells_table.R`. |
| A6 | Minor | The x|x| form implies a turning point (negative elasticity beyond |x| of about 3.7). | Accepted. The turning point is now stated, with the note that the piecewise robustness analysis has no turning point and shows the same flattening. |
| A7 | Minor | The random-anchor stratum's degrees of freedom jump to about 3,936 because the fallback dropped the curvature variance, making its p value anticonservative. | Accepted. Explained in the Results. |
| A8 | Minor | Precision of the cell index is coupled to anchor spread, so extreme cells get more weight. | Accepted. Noted in the H2 results; sensitivity analysis S3 (without the ten most precise cells) already addressed it. |
| A9 | Minor | Two different mean anchoring indices (0.42 and 0.241) are reported without explanation. | Accepted. The Results now explain that 0.42 is the multilevel intercept and 0.241 the inverse-variance weighted mean used only for the comparison with simulations. |
| A10 | Minor | Inconsistent labels: Imhoff & Barker 2022 vs 2023; Bahník 2021 vs 2021a; post-exclusion participant count. | Accepted. The Method now explains that the OpAQ labels ("Bahník, 2021a"; "Imhoff & Barker, 2022, Study 2") refer to Bahník (2021) and Imhoff & Barker (2023); Figure 2 and Table 1 use the publication labels. The preregistration keeps the OpAQ labels because it is frozen. Post-exclusion counts are in Table 1 and the Results. |
| A11 | Minor | Give a concrete example of what b and g mean. | Accepted. Added: for a true value of 100, doubling the anchor raises the estimate by 21% from 50, 17% from 200 and 11% from 500 (numbers computed inline). |

Rejected in part at round 1: we initially disputed A1's point that the well-resolved negative curvatures all came from random anchors, citing the fixed-anchor Cologne cathedral item. The citation check and codex (round 3, X3-1) showed that its authors describe those anchors as random, so A1 was right; the rejection was withdrawn in round 3 (see below).

### Reviewer: OpenAI Codex CLI (recommendation: major revision)

Source: `reviews/manuscript/codex_answer_r1.txt`. Codex reviewed the draft that already included the changes made in response to agy (the manuscript text was embedded in the prompt because two earlier codex runs stalled while exploring files).

| # | Severity | Comment | Response |
|---|---|---|---|
| X1 | Major | M1R is retained although the observed g lies outside its interval; report a joint check of b and g and call M1R inconclusive. | Accepted. Added a post-hoc joint check (R1a): no M1R replicate produced both b and g inside the observed CIs, compared with 33% of M3 and 4% of M4 replicates. The manuscript now describes M1R as not supported by the within-item data, while reporting that it passed the preregistered rule. |
| X2 | Major | The across-cell slope compares researcher-chosen items; failing to predict it should not count as decisive against a within-item process model. | Accepted. The H3 results now say that failure on d is weaker evidence than failure on g. The preregistered rule and its outcome are still reported as registered. |
| X3 | Major | H2 standard errors: give the formula and handle participants who answered under both anchors. | Accepted. The formula is now in the Method. No participant answered under both anchors of any cell (R1d), so the medians are independent. A participant bootstrap within studies gave a similar slope (reported with the caveat that it reflects participant sampling only). |
| X4 | Major | Scope of the primary inference; report study-specific estimates. | Accepted. Study-specific curvatures are now reported (R1c): negative for Bahník and for the Cologne cathedral item, imprecise for Frech et al., positive for Yoon et al. The abstract and conclusion restrict the claim to random anchors in the observed tasks. |
| X5 | Major | M2 is constant weight on the log scale; M3/M4 are particular implementations; frame rejections as applying to implementations. | Accepted. The model section now states that the models are specific log-scale implementations. We added an exploratory raw-scale constant-weight model (E6): it predicts the pooled curvature but a rising elasticity above the true value, which the data contradict. The Discussion now speaks of implementations, and M3 is attributed to Mussweiler & Strack (2001) and Epley & Gilovich (2006) with the note that the latter proposed it for self-generated anchors. |
| X6 | Major | Predictive intervals depend on parameter grids, sampling and assumptions; 300 relaxed draws do not show that no match exists; qualify "too steep". | Accepted. The Method states that parameters were drawn uniformly from accepted grid points; the relaxed-calibration text now says such settings are rare, not absent; the "too steep" statement is qualified as relative to the calibrated ranges. The raw-scale recalibration (S1) and the limitation on calibration remain. We did not run a further grid-weighting sensitivity analysis: the shape predictions of M1, M2, M3 and M4 follow from model structure, and the limitation is stated. |
| X7 | Minor | b is the elasticity at the true value, not an average; local elasticity is not the share of the gap carried into the estimate. | Accepted; definitions rewritten and the "carried 31% of its log distance" phrasing removed. |
| X8 | Minor | Report near and far slopes with intervals, not only their difference. | Accepted (R1b): near .31 [.25, .36], far .10 [.04, .17]. |
| X9 | Minor | Disclose in the manuscript that operating characteristics are approximations and that two safeguards were in the code but not the text. | Accepted; both are now in the Method. The repository link will be added before submission (placeholder in the Data availability statement). |
| X10 | Minor | The Chicago responses were valid answers in millions; say the whole cell was excluded and run a sensitivity check after conversion; distinguish design and analysed counts. | Accepted. The Method now says the whole cell was excluded because of inconsistent units; the converted-cell sensitivity analysis (R1e) gave a similar slope; the Method labels the design counts as "before exclusions". |
| X11 | Minor | Figure 3 caption: "precision" vs inverse-variance weight; reference formatting errors (HTML tags, Lieder author). | Accepted. Caption now says point area is proportional to 1/SE; the bibliography builder strips HTML tags and fixes the author entry. |

### Citation-support check (Claude subagent)

Source: `manuscript/citation_check.md` (57 claim-citation pairs; none unsupported, 12 partly supported). All 12 were addressed:

| # | Issue | Response |
|---|---|---|
| Q1 | Yoon et al. (2021) anchors were participants' own height or age, not random. | Accepted; described accurately in the Method, Table 1 caption and Limitations; the OpAQ coding was kept because it was preregistered. |
| Q2 | Imhoff & Barker's Cologne item: authors call the anchors random and found a linear raw-scale relation. | Accepted; both points reported, with the implication that this item alone cannot discriminate raw-scale averaging (led to E6). |
| Q3 | Epley & Gilovich proposed the plausible-boundary rule for self-generated anchors only. | Accepted; M3 now cites Mussweiler & Strack (2001) and states the extension. |
| Q4 | Strack & Mussweiler (1997) did not report a larger raw shift; implausible anchors were "at least as effective" in standardised estimates. | Accepted; rephrased. |
| Q5 | Mussweiler & Strack (2001) did not test that implausible-anchor estimates were no higher than plausible-high ones. | Accepted; rephrased to their finding that very different implausible anchors produced similar estimates. |
| Q6 | Schley & Weingarten's flag also covered "implausible" anchors. | Accepted; rephrased. |
| Q7 | Lieder et al. fitted a five-level demonstration with linear bias. | Accepted; stated. |
| Q8 | Turner & Schley's inverted U is between extremity and the size of the shift. | Accepted; rephrased. |
| Q9 | Bahník's objects were lengths, heights and distances. | Accepted. |
| Q10 | Lakens (2017) supports the procedure, not the bounds; 95% interval corresponds to α = .025. | Accepted; rephrased. |
| Q11 | Chapman & Johnson quote checked against the abstract only; add page. | Accepted; page 223 added. Full text not available (paywall); the quote is verbatim from the abstract. |
| Q12 | The Weber et al. corrigendum reference was missing or wrong. | Accepted; described in words as an unpublished 2026 corrigendum on the OpAQ project page. |

## Round 2: Manuscript review of the revised version

### Reviewer: OpenAI Codex CLI (recommendation: major revision)

Source: `reviews/manuscript/codex_answer_r2.txt`. Codex judged A2, A4, A5, X2, X3, X4 and X6 resolved, A1 largely resolved, and A3, X1 and X5 reported more fairly but needing interpretive changes.

| # | Severity | Comment | Response |
|---|---|---|---|
| X2-1 | Major | The conclusions describe the finding as a smaller "share of the distance between belief and anchor", but the measure is a local elasticity relative to the true value; beliefs were not measured. | Accepted. The abstract, Discussion opening and Conclusion now state the finding as a weaker response of estimates to changes in the anchor when the anchor is far from the true value. "Share of the gap" language is removed from the findings (it remains only in the description of how model M1 works). |
| X2-2 | Major | The conclusion says the result "supports" plausibility-based accounts, although the calibrated M3/M4 predictions miss ρ and the across-cell slope; no model explains the combined results. | Accepted. The Conclusion now says the result "is consistent with" plausibility-limited accounts and states that no calibrated model explained the combined results; the Discussion calls plausibility-limited influence "one possible account rather than an established mechanism". |
| X2-3 | Minor | State the exact H3 rule and why either curvature measure can qualify a model. | Accepted; the rule and its rationale (ρ lets a model with mis-calibrated anchoring strength pass on shape) are stated in the Results and in the Table 3 caption. |
| X2-4 | Minor | Specify the MAD convention. | Accepted; the Method states that the MAD is scaled by 1.4826 (R default). |
| X2-5 | Minor | "All 15 cells" item-by-item result sits uneasily beside the positive Yoon et al. curvature. | Accepted; the 15 cells are named and the difference in specification is explained. |
| X2-6 | Minor | Table 2 calls b "average elasticity"; repository link is a placeholder. | Heading corrected. The repository link is left as a placeholder: the goal forbids publishing or creating accounts, so the repository will be made public by the author before any submission. |

### Reviewer: Gemini 3.8 Flash via agy (recommendation: minor revision; no major issues remain)

Source: `reviews/manuscript/agy_answer_r2.txt`. Agy judged every round-1 major issue adequately resolved (A5 substantially).

| # | Severity | Comment | Response |
|---|---|---|---|
| A2-1 | Minor | Table 1 truncates the Cheops item (greedy regex) and lacks units. | Accepted; regex fixed, Unit column added, item capitalisation and unit labels harmonised. |
| A2-2 | Minor | "Average elasticity" survives in Table 2 and one Results sentence. | Accepted; both corrected. |
| A2-3 | Minor | The level-criteria sentence implies b lay inside only M1R's and M4's intervals. | Accepted; the sentence now lists the models whose interval contains b and, separately, those that contain both level statistics. |
| A2-4 | Minor | Table 3's "Retained" column hides that M3/M4 passed on g and M1R failed on g. | Accepted; the Table 3 caption now states this explicitly. |
| A2-5 | Minor | Post-exclusion participant count missing from the Results. | Accepted; added (1,491). |
| A2-6 | Minor | E5 omits M1R's two across-cell matches. | Accepted; added. |
| A2-7 | Minor | Hard-coded pre-exclusion count in the Limitations. | Accepted; now computed from the post-exclusion table. |
| A2-8 | Minor | Literal "&amp;" in a journal name. | Accepted; the bibliography builder now converts it. |

### Reviewer: coarse-review pipeline (full structured review; recommendation: major revision)

Source: `reviews/coarse/coarse_review_r2.md` (reviewed the version after round-1 revisions, before the codex/agy round-2 changes). Run with `coarse-ink` 1.4.0, host Claude, model claude-opus-4-6, effort high.

**Overall feedback**

| # | Comment | Response |
|---|---|---|
| K1 | The primary result depends on one study and one item domain; narrow the claims or add data. | Accepted (narrowing). The abstract and conclusion restrict the claim to random anchors in the observed tasks and state that deliberate anchors remain open; no other open multi-anchor data exist in OpAQ. New data collection is outside the remit of this study. |
| K2 | The binary survival rule rewards wide predictions; make the joint reproduction share the primary model-comparison metric. | Accepted in part. The preregistered rule is still reported as preregistered, but the Results now introduce the joint check as the more informative comparison and the abstract reports it (a plausible-boundary model reproduced the within-item pattern best; the resource-rational variant was too wide to test). We did not relabel the post-hoc check as primary, because it was not preregistered. |
| K3 | The within/across divergence is unresolved; engage with what would resolve it. | Accepted. The Discussion now proposes a design that separates the two explanations (informative and random anchors at many levels for the same items, with elicited unanchored estimates and plausible ranges), and reports the new analyses (E7, E10) that bear on it. |
| K4 | The quadratic form may impose the curvature; add a spline or multi-breakpoint specification. | Accepted. E9 fits five distance bands; slopes fall from 0.33 to about 0.12 and stay positive, without the reversal implied by the quadratic. |
| K5 | Calibration to a single benchmark; add a second calibration target such as the elasticity in a published random-anchor study. | Rejected, with reason: any additional calibration target from OpAQ studies would use outcome data that the predictions are tested against, and the only large published random-anchor study with many anchor levels (Bahník, 2021) is the main source of the test data. The limitation is stated in the Discussion and in `weaknesses.md`; the raw-scale recalibration (S1) and relaxed-calibration check (E5) show how much depends on the calibration. |
| K6 | The random-anchor stratum's fallback inflates precision; report item-level curvatures and a two-step estimate. | Accepted. E8 fits each cell separately and pools the 20 curvatures: γ = -0.046 [-0.068, -0.024], τ = 0.035, I² = 65%; 16 of 20 negative. |
| K7 | Test the model the Discussion motivates (plausibility discount with a floor). | Accepted. E7 simulates M4 with a weight floor: 36 of 400 draws reproduce the within-item b and γ, 62 the across-cell slope, none both. |
| K8 | Derive why Hedges' g rises mechanically under constant proportional pull. | Accepted. A short derivation is now in the Introduction. |
| K9 | Test whether curvature covaries with item uncertainty (the plausibility mechanism). | Accepted. E10: no relation across 18 cells (slope 0.012 [-0.136, 0.159]); reported in Results and Discussion as not supporting the mechanism, with its limits (few items; outcome-based spread). |
| K10 | Simulation assumptions too sparse in the text. | Accepted. A table in the Appendix (Table 4) lists every distributional assumption. |

**Detailed comments**

| # | Comment | Response |
|---|---|---|
| K-1 | Yoon anchor ranges are inconsistent with heights or ages. | Accepted after checking Yoon et al.'s Appendix A: participants entered their height in inches or age and compared the target with that number; the entered values (8-1,500; 6-279) suggest other units and errors. The Method now says so and explains why the values are analysed as anchors (they are the numbers participants compared against). H1 without Yoon et al. is unchanged (S2). |
| K-2 | H2 described as a null ("did not change detectably") instead of inconclusive. | Accepted; all such phrasings replaced by "inconclusive". |
| K-3 | Preregistration credibility: git is self-operated; state registry, temporal separation, and what was seen. | Accepted in part. The Method now states that the timestamp is local and not independently verifiable, that the repository and its history will be made public, and what was seen before the commit. Registering on an external registry was not possible within the constraints (no accounts may be created); `ai_disclosure.md` lists public deposit of the repository and its history as a step for the author before submission. |
| K-4 | Author role statement contradicts the instruction; add responsibility statement. | Accepted. The statement now distinguishes the constraints the author set from the choices the AI made within them, and says the author is accountable. We did not write that the author reviewed all analyses, because that has not happened yet (see `ai_disclosure.md`). |
| K-5 | M1R parameter deviation too vague; state which document governs. | Accepted; the parameter, both descriptions, and the rule that the committed code was treated as operative are now stated. |
| K-6 | Apply the metric critique to Schley & Weingarten as well. | Accepted; added. |
| K-7 | "Clarified" obscures whether the critical value was chosen post hoc. | Accepted; the text now states what the preregistration text said and that the preregistered code used the normal quantile for both simulation and analysis. |
| K-8 | Symbol g used for both Hedges' g and the curvature. | Accepted; the curvature is now γ throughout; Hedges' g is always named in full. |
| K-9 | Ambiguous metric for Strack & Mussweiler. | Accepted; "estimates z-standardised within each item". |
| K-10 | Fixed-anchor stratum composition is fragile under the disputed classification. | Accepted; a sentence states the composition if the Cologne item were counted as random. |
| K-11 | Chicago cell: clarify that no estimate entered any analysis. | Accepted; parenthetical added in the Results. |
| K-12 | The secondary test inherits the extremity-item confound. | Accepted; qualifier added in the Introduction. |

## Round 3 (final): Manuscript review of the round-2 version

### Reviewer: OpenAI Codex CLI (recommendation: major revision)

Source: `reviews/manuscript/codex_answer_r3.txt`. Codex judged most earlier major concerns addressed and the rejection of K5 (second calibration target) defensible.

| # | Severity | Comment | Response |
|---|---|---|---|
| X3-1 | Major | The Cologne cathedral item is used as evidence for fixed anchors although its authors describe the anchors as random; the round-1 rejection of A1 is therefore unpersuasive. | Accepted. The preregistered OpAQ-coded analysis is kept, but every claim that the decline was shown for fixed anchors was removed: the Results, Discussion, Limitations and Conclusion now state that all well-resolved within-item evidence comes from random or self-generated anchors, report the four remaining fixed-anchor items (Frech et al.) as imprecise, and say that the data contain no informative test for fixed, deliberately chosen anchors. The earlier rejection of A1 is withdrawn in the round-1 table. |
| X3-2 | Major | The repository link is a placeholder, so the audit trail for the preregistration cannot be inspected; the plan should be described as committed locally. | Accepted in part. The Method now says the preregistration was committed to a local git repository, not a public registry, and that the timestamp is not independently verifiable. Rejected in part, with reason: publishing the repository is outside what this project may do (no accounts may be created and nothing may be published); `ai_disclosure.md` lists public deposit of the repository and its full history as a step for the author before any submission. |
| X3-3 | Minor | The Schley & Weingarten inference assumes comparable response variability. | Accepted; condition added. |
| X3-4 | Minor | "No model reproduced both patterns" overstates finite simulations. | Accepted; now "None of the evaluated model simulations reproduced both patterns". |
| X3-5 | Minor | Gaussian proposals are unbounded, so "each step covers a bounded distance" is false. | Accepted; now "adjustment steps have a fixed typical size". |

### Reviewer: Gemini 3.8 Flash via agy (recommendation: accept with minor revision; no major issues remain)

Source: `reviews/manuscript/agy_answer_r3.txt`. Agy re-checked all numbers against `output/` and found them exact apart from item 1.

| # | Severity | Comment | Response |
|---|---|---|---|
| A3-1 | Minor | The Stephen King anchors range from 6 to 267, not 279 (279 was a back-calculation from a rounded value in a review comment). | Accepted; the ranges are now computed inline from the data. |
| A3-2 | Minor | The Method still describes the H3 rule in a way that contradicts the operational rule. | Accepted; the Method now states the rule exactly as coded (retain if d and at least one of γ and ρ lie inside). |
| A3-3 | Minor | The multi-band slopes at |x| ≥ 2 have CIs that include zero. | Accepted; qualified in the text. |
| A3-4 | Minor | Appendix table called "Table A1" in the review log but "Table 4" in the manuscript. | Accepted; review log corrected (Quarto numbers tables consecutively). |
| A3-5 | Minor | Repository link placeholder. | As X3-2: a step for the author before submission. |
