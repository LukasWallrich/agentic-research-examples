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

Rejected in part: A1's suggestion that "100% of the items showing significant within-item curvature" used random anchors is incorrect; the one fixed-anchor item with 20 levels also showed negative curvature (S2), which the manuscript reports.
