# Anchor extremity and proportional anchor influence: A preregistered, model-based test in open trial-level data

**Date**: 09/28/2026
**Domain**: social_sciences/psychology
**Taxonomy**: academic/research_paper
**Filter**: Active comments

---

## Overall Feedback

Here are some overall reactions to the document.

**Outline**

This paper asks whether anchors lose proportional influence as they become more extreme, tests predictions from five process models against trial-level data from the Open Anchoring Quest, and finds declining within-item elasticity but an inconclusive across-cell pattern. The approach is unusually transparent and the preregistered model-comparison framework is commendable. However, the empirical base is narrow, the log-scale specification carries more weight than the paper acknowledges, the model comparison framework rewards imprecision, and the disconnect between the two analyses is not adequately resolved.

The paper tackles a genuinely important question — the functional form of anchor influence — that has been obscured by decades of reliance on standardised effect sizes. The idea of deriving shape predictions from process models and preregistering them against existing open data is creative and well-executed in its procedural transparency. The writing is clear and the limitations section is unusually honest. These are real strengths.

**The within-item finding is effectively a single-study result**

Thirteen of 20 cells and 83% of the within-item estimates come from Bahník (2021). Without this study, the curvature estimate is -0.045 with a confidence interval of [-0.36, 0.27] — completely uninformative. The paper's main empirical claim therefore rests on one experiment with random anchors for lengths, heights, and distances in Czech landmarks. The other contributing studies add little: Frech et al. provides four items with only high anchors and 104 participants each (failing the preregistered gate), Yoon et al. provides two items that show the opposite pattern (positive curvature), and the Cologne cathedral item from Imhoff & Barker is a single supplementary item. Presenting this as a 20-cell, multi-study analysis overstates the evidential breadth. The paper should foreground that the declining-elasticity finding has been observed clearly in one study and is consistent with one additional item, and frame replication as a necessary next step rather than a caveat.

**Random anchors may engage qualitatively different processing than researcher-chosen anchors**

The within-item set is dominated by random anchors (15 of 20 cells), while the across-cell set consists entirely of fixed or relevant anchors. Participants in Bahník (2021) were told the anchor was a random number between 1 and 1,000 — they had every reason to discount it, and more reason to discount it as it became more extreme. This is consistent with the declining elasticity but does not tell us much about the kind of anchoring that matters in practice: opening offers, suggested prices, sentencing demands, and other deliberately informative anchors. The paper's title and abstract frame the finding as about anchoring in general ('anchor extremity and proportional anchor influence'), but the evidence speaks almost exclusively to the random-anchor case. The two Yoon et al. items, where anchors were participants' own height or age, show positive curvature — the opposite direction. This heterogeneity by anchor type deserves more than an exploratory footnote. The paper should either restrict its claims to random anchors or provide a more substantive theoretical account of why the pattern should or should not generalise.

**The log-scale specification is doing heavy inferential lifting without adequate justification**

The paper's central argument is that standardised effects are misleading and log-scale elasticity is the right metric. This reframing is the engine of the entire contribution — it converts a literature of rising standardised effects into one consistent with declining proportional influence. But the log-scale specification is itself an assumption about how people represent and combine magnitudes, not a neutral measurement choice. The paper's own exploratory analysis shows that constant weighting on the raw scale also produces negative curvature on the log scale. The paper rules out raw-scale weighting based on side-specific curvature (negative below the true value, positive above for the raw-scale model, versus negative on both sides in the data), but this side-specific test is exploratory and has less statistical power than the pooled test. If anchoring operates on the raw scale for some items or item types, the log-scale curvature could be partly a scale artifact. The paper needs a principled argument for the log scale — ideally a model-selection exercise comparing log-linear and raw-linear specifications — rather than treating it as obviously correct because magnitudes are roughly log-normal.

**The model comparison framework rewards imprecision and cannot support the stated conclusions**

The preregistered survival rule retains a model if the observed across-cell slope falls inside its 95% predictive interval and at least one curvature statistic does. M1R survived only because its predictive interval for relative curvature spanned [-0.37, 1.39] — so wide it would accommodate nearly any empirical value. The paper acknowledges this openly, but the framing still treats model survival as informative ('H3: Model adequacy'). A model that cannot be rejected because it predicts everything has not passed a test; it has avoided one. Meanwhile, M3 and M4, which actually predicted the sign and approximate magnitude of the within-item curvature, were rejected because they predicted a falling across-cell slope that the data could not confirm or deny. The survival rule thus penalises models that make sharp predictions and rewards those that do not. Top journals in this area expect quantitative model comparison — Bayes factors, cross-validation, or proper scoring rules that reward calibration, not just coverage. Directional preregistered tests with wide predictive intervals are not a substitute. A post-hoc joint check (what fraction of replicates reproduce both b and gamma) is reported and is more informative, but it should be the primary comparison, not a supplementary one.

**Mismatch between within-item and across-cell results is left theoretically unresolved**

The within-item analysis shows declining elasticity; the across-cell analysis shows a positive (though inconclusive) point estimate. The paper offers two candidate explanations — different operationalisations of extremity, and different anchor types — but does not develop either into a testable prediction. This matters because the paper claims that 'no model reproduced both patterns,' which sounds like a strong negative result. But the two patterns come from different data structures (continuous within-item variation vs. two-anchor contrasts across studies), different anchor types (mostly random vs. all fixed/relevant), and different levels of statistical precision. The mismatch could simply reflect insufficient power in the across-cell analysis, researcher selection of anchor pairs that happen to be more extreme for easier items, or genuine heterogeneity by anchor type. Without resolving which of these is at work, the claim that no model fits both patterns carries little theoretical weight. The paper would be stronger if it dropped the across-cell analysis to a secondary descriptive role and built the argument around the within-item evidence, or if it developed a formal account of why the two analyses should or should not agree.

**Calibration to a single 30-year-old benchmark constrains model predictions in untested ways**

All five models were calibrated to reproduce the anchoring index reported by Jacowitz and Kahneman (1995) for anchors at the 15th and 85th percentiles of unanchored estimates (about 0.49), accepting parameters that yielded an index between 0.30 and 0.60. This calibration determines the parameter space that generates the predictions, so the 'model predictions' are really predictions conditional on matching this one benchmark. If the benchmark does not represent the anchoring strength in the OpAQ data — and the observed weighted mean index was 0.241, below the calibration window's lower bound — then the model predictions are anchored (so to speak) to a mismatched baseline. The sensitivity analysis using raw-scale recalibration retained most of the same parameter points, which shows the calibration is not very constraining, but that is itself a problem: if calibration barely constrains parameters, the predictive intervals reflect prior parameter ranges more than empirical calibration. A more informative approach would calibrate each model to a subset of the OpAQ data and test on the remainder, or use the Jacowitz and Kahneman data as a prior and update with OpAQ.

**Preregistration after reading design columns provides weaker protection than implied**

The paper emphasises its preregistered design — predictions were committed to version control before estimates were read. But the authors had already read the design columns: study identifiers, item names, true values, anchor values, anchor types, and participant identifiers. This is substantial information. Knowing which items have many anchor levels, how those levels are distributed, what the true values are, and which studies dominate the data allows an analyst to anticipate the shape of the anchor-response function before seeing any estimates. For instance, knowing that Bahník's random anchors span up to 6.9 log units from the true value, combined with general knowledge about how people respond to absurdly extreme random numbers, makes declining elasticity a reasonable prior guess. The paper's commit-timestamp verification is also acknowledged as 'not independently verifiable in the way a registry timestamp is.' These points do not invalidate the preregistration, but the paper should be more explicit about what the preregistration does and does not protect against. It protects against analytic flexibility (choice of estimator, exclusion rules, decision thresholds) but not against hypothesis selection informed by design knowledge.

**No analytical derivation of why each model implies its curvature sign**

The paper says it 'derived the shape of the anchor-response function from five process models,' but the derivations exist only in simulation code (R/models.R), not in the text. For M1, the paper gives an informal argument about bounded step sizes and notes that Lieder et al.'s geometric approximation implies constant pull, but never shows mathematically why the full Metropolis-Hastings chain departs from the approximation in the direction of positive curvature. For M3 and M4, the verbal intuitions are clear (plausibility limits pull), but there is no formal statement of the form 'under M3, the local elasticity is [expression], which is decreasing in |x| because [reason].' A paper whose core contribution is testing five models' predictions against data should let the reader verify that the predictions follow from the model structure, not just from a particular simulation run with particular nuisance parameters. An analytical appendix that derives the curvature sign for each model — even approximately, as Lieder et al. did for the geometric case — would make the theoretical argument self-contained and let readers see which structural features of the models drive the predictions, independently of the simulation assumptions in Table 4.

**Sensitivity of model predictions to simulation distributional assumptions is unexplored**

Table 4 specifies the simulation's distributional assumptions: belief uncertainty drawn Uniform(0.3, 1.2), response noise Normal(0, 0.3σ), a 2% gross-error rate, and so on. The curvature predictions in Table 2 are conditional on these choices, but the paper never examines how they change if the assumptions shift. For instance, if response noise were 0.5σ instead of 0.3σ, would the predictive intervals for M3 and M4 widen enough to overlap the observed curvature and relative curvature jointly? If the gross-error rate were 5%, would M1's positive curvature prediction weaken? The relaxed-calibration analysis (drawing model parameters from wider ranges) addresses sensitivity to model parameters but not to the shared simulation scaffolding. A table or figure showing how each model's predicted γ and ρ vary when belief uncertainty, response noise, and gross-error rate are each perturbed would tell the reader whether the model comparison depends on these modelling choices or is robust to them.

**No power or detectable-effect analysis for the across-cell test (H2)**

The across-cell slope is reported as inconclusive (0.050, 95% CI [-0.013, 0.113]), and this result enters the model-adequacy evaluation: M3 and M4 are rejected partly because they predict a clearly negative across-cell slope that the data do not confirm. But the paper never reports what slope H2 had the power to detect. With 128 cells, heterogeneity across 40 studies, and precision weights that concentrate on a few cells (the ten most precise cells carry 61% of the weight), the effective sample size for detecting a trend may be small. If the minimum detectable slope at 80% power were, say, 0.08, the inconclusive finding would carry little weight against M3 and M4, whose predicted slopes are around -0.08 to -0.10. Computing the detectable effect size — or at minimum the effective number of independent cells — is standard when an inconclusive result is used to adjudicate between models, and its absence leaves the reader unable to judge how much the across-cell analysis adds to the model comparison.

**Recommendation**: Major revision. The paper's core finding — declining within-item elasticity — is interesting and potentially important, but it is effectively a single-study result that applies to random anchors for physical magnitudes, presented with a model comparison framework that cannot support its stated conclusions. The log-scale specification, which drives the entire reframing of the anchoring literature, needs stronger justification. The paper is commendably transparent, which makes these limitations visible rather than hidden, but they need to be addressed rather than merely acknowledged.

**Key revision targets**:

1. Replace the directional survival rule with a quantitative model comparison (e.g., Bayes factors or a scoring rule that penalises imprecision) so that M1R does not survive by making predictions too wide to test, and M3/M4 are not penalised for making sharp predictions that happen to miss on the across-cell slope.
2. Provide a formal justification for the log-scale specification — ideally a model selection comparing log-linear and raw-linear response functions across items — and discuss explicitly under what conditions the negative curvature finding would be a scale artifact rather than a psychological phenomenon.
3. Reframe the paper's claims to match the evidential base: the main finding is a single-study result for random anchors, not a multi-study finding about anchoring in general. Develop a clear theoretical account of whether and why the pattern should generalise to informative anchors, or restrict the title and abstract accordingly.
4. Resolve the within-item vs. across-cell mismatch by either (a) conducting a power analysis showing that the across-cell analysis was too imprecise to detect a decline of the observed within-item magnitude, or (b) developing a formal model of researcher anchor selection that predicts a different across-cell pattern, or (c) demoting the across-cell analysis to a descriptive supplement.

**Status**: [Pending]

---

## Detailed Comments (19)

### 1. Yoon items violate stated self-generated anchor exclusion

**Status**: [Pending]

**Quote**:
> Estimates entered the analysis if the anchor was explicitly random, fixed, or relevant to the target (self-generated and incidental anchors were excluded); the response scale was open; the quantity was a positive ratio-scale magnitude

**Feedback**:
The Yoon participants typed in their own height or age, then compared the target with that number. These are self-generated anchors by any ordinary reading. The treatment is also asymmetric: another study was excluded because its anchors were computed from participants' own estimates, overriding its OpAQ code, while the Yoon items stay in because OpAQ codes them as 'random.' If the operative distinction is that the excluded study's anchors were estimates of the target quantity whereas Yoon's come from a different domain (height used as anchor for sofa prices), that is a meaningful distinction in anchoring theory — but it does not appear in the inclusion criteria as written. A reader who takes the text at face value would expect both sets of participant-derived anchors to be excluded. Rewrite the exclusion criterion to specify the rule that was actually applied, e.g., 'self-generated anchors whose value depended on the target question were excluded; participant-derived values unrelated to the target (coded as random in OpAQ) were retained.' Name the excluded study for reproducibility.

---

### 2. AI training data weakens preregistration and independence claims

**Status**: [Pending]

**Quote**:
> The AI tools used no data other than the openly licensed OpAQ file and published literature.

**Feedback**:
This describes runtime data access, but LLMs draw on training corpora that likely include published anchoring studies, their effect sizes, and possibly analyses of the OpAQ dataset itself. The system that 'chose the research question' and derived predictions may have been shaped by memorised empirical patterns — including the direction and approximate magnitude of the curvature it predicted. The preregistration protects against analytic flexibility (the commit log shows predictions preceded analysis code), and the reader-function safeguard ensures the analysis code was not outcome-informed. But it does not guarantee that the predicted curvature direction was derived purely from model structure rather than from training-corpus knowledge of the empirical regularities being tested. Distinguish runtime data access from training-corpus exposure, and note that the epistemic position of this preregistration differs from one arising from a researcher who has genuinely never encountered the relevant results.

---

### 3. Rescaling of M1R's agent-uncertainty parameter unquantified

**Status**: [Pending]

**Quote**:
> the preregistration described M1R's parameter $\kappa$ as the agent's uncertainty relative to the spread of belief centres across people, whereas the code defines it relative to the item's belief uncertainty $\sigma$ (the spread of belief centres is $0.6\sigma$)

**Feedback**:
The two definitions differ by a factor of 1/0.6, roughly 1.67. A given kappa value under the textual definition implies about 60% of the agent uncertainty implied under the code's definition. This is not innocuous: M1R survived the preregistered tests solely because its predictive interval for relative curvature was very wide ([-0.37, 1.39]), driven partly by parameter settings that produce almost no anchoring. Had the textual definition been implemented instead, the calibration filter (Jacowitz-Kahneman index in [0.30, 0.60]) would have accepted different grid points, and the predictive intervals could have shifted enough to change whether M1R survived. State the scaling factor explicitly and report whether the grid under the textual definition yields materially different predictive intervals. Better still, report M1R's intervals under both definitions so the reader can judge.

---

### 4. Weber et al. sensitivity result and its theoretical implications underexplored

**Status**: [Pending]

**Quote**:
> excluding the second made the across-cell slope positive and significant

**Feedback**:
Two things here. First, the paper retains Weber et al. in the primary analysis despite a corrigendum flagging likely coding errors, while it excluded the Shanks cell for a unit mismatch. What principle distinguishes the two cases? If the coding errors are uncertain, say so; if the data are retained out of conservatism, state that rationale. Without it, the asymmetric treatment looks arbitrary. Second, the sentence buries what may be an important result. Removing one study with suspected errors makes the across-cell slope significantly positive — the opposite sign from the within-item curvature. If taken at face value, this deepens the tension between H1 and H2 and tightens the challenge for any single-process model. One or two additional sentences acknowledging this implication would help the reader gauge how much the H1-H2 mismatch depends on data quality.

---

### 5. Accountability claim in tension with disavowal of intellectual choices

**Status**: [Pending]

**Quote**:
> within these constraints, the author did not select the research question, the dataset, the models or the interpretation. The author is accountable for the content of the article.

**Feedback**:
Scientific accountability normally implies having exercised judgment over the claims and their interpretation. These two sentences sit in direct tension: the first says the author chose neither the question nor the interpretation; the second asserts accountability for the content. What does 'accountable' mean here? Did the author verify the numerical results independently? Evaluate whether the model specifications are reasonable? Endorse the Discussion's framing? If so, the disavowal overstates the author's distance from the work. If not, the accountability is nominal rather than operative. Add one or two sentences specifying what the author verified or endorsed before submission, so the reader can judge the depth of accountability.

---

### 6. Model equivalence across anchor types is structural, not theoretical

**Status**: [Pending]

**Quote**:
> The models make the same shape predictions for both, but it is possible that informative anchors lose less pull with extremity than anchors people know to be random.

**Feedback**:
None of the five models includes a parameter or mechanism that distinguishes random from informative anchors. Saying they 'make the same shape predictions for both' sounds like a substantive theoretical claim, as though the models evaluated the distinction and found it immaterial. In fact, the predictions are identical by construction — the models are simply silent about anchor type. The next clause then introduces the possibility that informative anchors behave differently, which amounts to acknowledging the models are misspecified for at least one type. Make the limitation explicit: 'None of the five models distinguishes anchor types, so they generate identical predictions by construction. If informative anchors lose less pull with extremity, the models are misspecified for one type, and a single parameter set should not be expected to fit both the within-item and across-cell data.'

---

### 7. Discussion blends exploratory and preregistered findings without distinction

**Status**: [Pending]

**Quote**:
> The decline appeared on both sides of the true value, in every item with enough near and far anchors, and in the one fixed-anchor item with many anchor levels.

**Feedback**:
Each claim in this sentence draws on exploratory or sensitivity analyses, not on the preregistered model. 'Both sides' comes from the exploratory side-specific analysis. 'Every item with enough near and far anchors' comes from item-level exploratory fits — the preregistered model estimated curvature as common across cells after the full model failed to converge, so it cannot establish item-level universality. The fixed-anchor item is from the sensitivity section. A reader of this summary paragraph would reasonably take these as preregistered results. The qualifier 'with enough near and far anchors' compounds the issue by leaving the selection criterion unstated, which could exclude items showing the opposite pattern (the Yoon items have positive curvature) on unspecified grounds. Either label each claim's evidential source or add a sentence noting that the item-level and side-specific results are from exploratory analyses.

---

### 8. Standardised-effect critique would resolve apparent conflict in early literature

**Status**: [Pending]

**Quote**:
> Chapman & Johnson (1994) found that "implausibly extreme anchors had a proportionally smaller effect than anchors close to the expected value" [p. 223] in lottery valuations. Strack & Mussweiler (1997) found that implausible anchors were at least as effective as plausible ones, in estimates z-standardised within each item.

**Feedback**:
These two studies anchor the 'mixed results' framing. Two paragraphs later, the paper shows that standardised metrics grow with anchor distance even under constant proportional pull. Z-standardisation introduces the same confound: if implausible anchors are further from the true value, constant proportional pull already predicts equal or larger z-standardised effects — exactly what Strack & Mussweiler found. The apparent conflict between a proportional measure (Chapman & Johnson, declining effect) and a standardised one (Strack & Mussweiler, no decline) may therefore be a measurement artifact, not a genuine disagreement. The paper applies this reframing to the Röseler & Schütz and Schley & Weingarten meta-analyses but never circles back to Strack & Mussweiler. Doing so would actually strengthen the argument: the early literature is more coherent than it appears once the measurement issue is recognised.

---

### 9. Schley & Weingarten inference depends on an unverified conditional

**Status**: [Pending]

**Quote**:
> By the same logic, the null result of Schley & Weingarten (2026) is, if anything, more compatible with declining proportional influence: if the anchors flagged as extreme were also further apart, equal standardised effects imply a smaller proportional pull.

**Feedback**:
The directional claim rests entirely on 'if the anchors flagged as extreme were also further apart.' Schley & Weingarten coded extremity as a binary property of individual anchors — mainly whether original authors described them as extreme or implausible — not as a measure of inter-anchor spacing. A study could pair one very extreme anchor with one moderate anchor, producing high individual-anchor extremity without proportionally wider spacing. The hedge 'if anything' is too casual for a conditional that carries the whole inference. Either verify from the Schley & Weingarten data that extreme-flagged studies had wider anchor spacing, or rewrite to: 'could be compatible with declining proportional influence, depending on whether extreme-flagged studies also had wider anchor spacing — a question the binary coding does not directly answer.'

---

### 10. Simulation bias defense uses generic distributions, not measured item-specific beliefs

**Status**: [Pending]

**Quote**:
> the simulations included item-level bias to account for this, and the curvature was negative on both sides of the true value.

**Feedback**:
The simulations drew item-level bias from Normal(m, 0.3) with m ~ Uniform(-0.3, 0.3) per replicate — a generic prior over hypothetical items. This shows that small, symmetrically distributed biases do not eliminate the curvature, but it does not address the actual pattern of over- and underestimation for the specific Czech landmarks that supply 83% of the data. If Czech respondents systematically overestimate the length of the Petřín funicular by, say, a factor of three, the 'true value' origin is misplaced for that item in a way the generic distribution may not capture. The next sentence nearly makes this point by calling for unanchored estimates, but the gap between 'assumed generic bias' and 'actual item-specific bias' should be stated directly rather than papered over with 'the simulations included item-level bias.' The defense is weaker than the phrasing implies.

---

### 11. Banded analysis too coarse to adjudicate reversal

**Status**: [Pending]

**Quote**:
> The slope thus fell over the first two log units and then stayed low but positive, without the reversal that the quadratic term implies beyond $|x| \approx 3.78$.

**Feedback**:
At |x| = 3, the quadratic itself predicts a local slope of 0.31 - 2(0.041)(3) = 0.064. The final band lumps everything above |x| = 3, and observations almost certainly thin out at extreme distances, so the band's average slope of 0.06 is dominated by data near |x| = 3 — where the quadratic predicts essentially the same value. The band average is therefore consistent with the quadratic rather than evidence against it. The broader observation that the slope appears to level off rather than follow a continued parabolic decline is reasonable, but the specific claim about absence of reversal goes beyond what the binning resolves. Rewrite to: 'the final band (|x| > 3) is too coarse to confirm or rule out the reversal the quadratic implies at |x| ≈ 3.78; the levelling-off across the last three bands suggests the quadratic may overstate the rate of decline at large distances.'

---

### 12. 18-item null framed as evidence against plausibility mechanism

**Status**: [Pending]

**Quote**:
> We also found no evidence that items with a wider spread of estimates near the true value showed flatter curvature, as a plausibility mechanism would predict if spread reflects uncertainty; this test had only 18 items and an outcome-based measure of spread.

**Feedback**:
With 18 items, a correlation needs to exceed roughly r = 0.47 to reach significance at conventional power. This test can barely detect anything. Reporting 'no evidence' here, even with the sample-size qualifier in the trailing clause, risks reading as evidence of absence — particularly in a paragraph weighing the plausibility account. The qualifier follows rather than leads, so the reader encounters the negative finding first. Report the observed effect size and confidence interval to show how uninformative the estimate is, or restructure so the power limitation leads: 'With only 18 items, the test lacked precision to detect a plausible association between spread and curvature (observed slope 0.012, 95% CI [-0.136, 0.159]).'

---

### 13. Item-domain description inconsistent between abstract and limitations

**Status**: [Pending]

**Quote**:
> Bahník (2021), in which participants compared 13 random anchors with 13 different lengths and heights

**Feedback**:
The abstract says 'lengths, heights and distances.' Here the Limitations section drops distances. Table 1 includes distance items (subway tracks, longest ship). Both sections describe the same dataset, so one is wrong. Reconcile them — most likely by adding 'and distances' in the Limitations.

---

### 14. Spread-scaled result leads before its endogeneity problem

**Status**: [Pending]

**Quote**:
> When we scaled extremity by the spread of estimates, the across-cell slope turned negative, as the within-item analysis and the plausibility accounts predict

**Feedback**:
The paragraph first reports the result aligning with plausibility accounts, then discloses — only afterward — that spread is endogenous to anchoring, making both versions of the analysis hard to interpret. A reader who skims or stops before the qualification walks away thinking this result supports the plausibility explanation. Restructure so the identification problem leads: 'The spread of estimates is itself affected by anchoring, so scaling extremity by spread does not cleanly measure subjective implausibility. The scaled slope was negative (consistent with the within-item result), but when spread entered as a separate predictor the extremity slope remained positive and imprecise. Neither specification resolves whether the across-cell pattern reflects plausibility limits or researcher placement of anchors.'

---

### 15. "Many different anchors" overstates the inclusion criterion

**Status**: [Pending]

**Quote**:
> in studies that presented many different anchors for the same question, we asked how the proportional pull changes as the anchor moves away from the true value.

**Feedback**:
The actual gate was 'at least three distinct anchor values' per cell. Three is the minimum for fitting a curve and does not qualify as 'many.' The characterisation is accurate for Bahník's data (hundreds of distinct anchor values per item) but misleading for the Frech et al. cells (10 levels) or any cell near the threshold. Replace 'many' with 'multiple' or 'at least three' to match the actual criterion. Readers encountering this before the method section will otherwise picture uniformly dense within-item coverage.

---

### 16. Barrera-Lemarchand description conflates model specification and empirical finding

**Status**: [Pending]

**Quote**:
> Barrera-Lemarchand et al. (2024) modelled the anchored crowd mean as a weighted average of anchor and crowd mean, with a weight that decays exponentially with the distance between anchor and truth, and found that this weight fell with distance across 30 percentage questions.

**Feedback**:
The sentence says the model uses 'a weight that decays exponentially with the distance' and then reports that the weight 'fell with distance.' The decay is already in the specification, so the finding sounds redundant. If Barrera-Lemarchand estimated a decay parameter that could have been zero and found it significantly positive, the empirical contribution is that estimate, not the direction of the relationship. Separate specification from result: 'modelled the weight as an exponential function of anchor-truth distance and found the estimated decay rate significantly above zero' — or, if they compared a decaying-weight model against a constant-weight alternative, report the comparison.

---

### 17. Erroneous Yoon anchor entries retained without robustness check

**Status**: [Pending]

**Quote**:
> The entered values range from 8 to 1,500 and from 6 to 279, which suggests entries in other units and some errors; because participants compared the target with the number they had entered, we analysed these values as anchors.

**Feedback**:
A height of 1,500 inches or an age of 279 is a data-entry error, not a self-report. The rationale for keeping them is psychologically reasonable, but these entries sit at the extreme ends of the anchor range where they exert the most leverage on the curvature estimate. With only 85 and 86 observations per Yoon item, and those items showing positive curvature — the opposite sign of the pooled result — a handful of high-leverage observations could shift the item-level estimates. Report how many entries fall outside plausible ranges (e.g., height > 84 inches, age > 100) and whether trimming them changes the item-level curvature.

---

### 18. Floor model's 9% hit rate needs characterisation of the search space

**Status**: [Pending]

**Quote**:
> A plausibility discount with a floor, in which an anchor's weight falls but never reaches zero, can reproduce the within-item pattern (36 of 400 exploratory draws), but none of these draws also reproduced the across-cell slope.

**Feedback**:
Thirty-six of 400 draws is a 9% hit rate. Whether this is promising depends on the breadth of the parameter sweep: a wide uniform grid over three free parameters will produce many misses by construction, while a targeted sweep around calibrated values would make 9% more meaningful. The paper says 'wide ranges' but gives no specifics about the ranges or sampling scheme. Characterise the search space — how broad each parameter's range was relative to calibrated values — so the reader can distinguish 'the floor model works under moderate tuning' from 'it works in a narrow corner of a large space.'

---

### 19. Uniqueness of model-discriminating test overstated

**Status**: [Pending]

**Quote**:
> the shape of the relation between anchor extremity and anchor influence is one of the few places where they can be tested against each other.

**Feedback**:
The anchoring literature has identified other empirical signatures distinguishing the leading models: self-generated versus experimenter-provided anchors (Epley & Gilovich, 2001, 2006), knowledge moderation (Mussweiler & Strack, 2000), response-time patterns, and effects of accuracy incentives. What is genuinely distinctive about the extremity question is that it yields different quantitative predictions testable in existing archival data. Rewrite 'one of the few places where they can be tested against each other' as something like 'a domain where they yield distinct quantitative predictions testable in existing multi-anchor data' — this characterises the contribution precisely without overstating its uniqueness.

---
