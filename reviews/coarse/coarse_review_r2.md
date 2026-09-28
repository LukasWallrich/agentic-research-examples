# Anchor extremity and proportional anchor influence: A preregistered, model-based test in open trial-level data

**Date**: 09/28/2026
**Domain**: social_sciences/psychology
**Taxonomy**: academic/research_paper
**Filter**: Active comments

---

## Overall Feedback

Here are some overall reactions to the document.

**Outline**

This paper asks a well-defined question—whether an anchor's proportional influence changes with its extremity—and tackles it with preregistered, model-based predictions applied to openly available trial-level data. The approach is admirably transparent, and the separation of within-item and across-cell analyses is a genuine methodological contribution. The main concerns are that the primary finding rests almost entirely on one study with a narrow item domain, that the model comparison framework rewards uninformativeness, and that the divergence between the two analyses remains unresolved rather than explained.

The paper addresses a genuinely important gap: prior work conflated standardised effects with proportional pull, and disentangling these is valuable for both theory and practice. The preregistration discipline is strong, the transparency is exemplary, and the observation that Hedges' g rises with extremity while the anchoring index does not is a useful corrective for meta-analytic practice. The within-item curvature finding, though narrow in scope, is a real empirical contribution.

**The primary result depends on one study with one item domain**

Thirteen of 20 within-item cells and 83% of the within-item estimates come from Bahník (2021), a study in which Czech participants compared random anchors (integers 1–1000) with 13 lengths and heights. Without this study, the curvature estimate has the same sign but a confidence interval spanning zero (g = −0.045, [−0.36, 0.27]). The remaining cells contribute too little precision to support the main claim independently. This means the headline finding—declining proportional pull—is really a finding about random anchors applied to physical magnitudes in one sample. Lengths and heights have relatively tight prior distributions and well-defined true values, which may make plausibility boundaries unusually sharp. A revision should either obtain additional multi-anchor data from different item domains (e.g., populations, prices, counts) or substantially narrow the scope of the claims in the abstract and conclusion to match what the evidence actually supports. The current framing ('within items, extreme anchors pull estimates by a smaller share') reads as a general statement about anchoring, but the empirical base is a specific statement about one study's items.

**The model comparison rewards width: M1R survives by being uninformative**

The preregistered survival rule asks whether observed statistics fall inside each model's 95% predictive interval. M1R's interval for relative curvature spans [−0.37, 1.39]—nearly any outcome would fall inside it. The paper acknowledges this ('M1R passed only because its predictions were very wide'), and the post-hoc joint check shows that 0% of M1R replicates reproduced the observed b and g together. Yet M1R is the only model labelled 'retained' in Table 3, and the abstract reports this as the result. This framing gives readers the impression that resource-rational anchoring received empirical support, when it was simply not testable with these data. A more informative framework would report something like the proportion of each model's simulations that fall within the observed confidence region (the post-hoc analysis already does this: 33% for M3, 4% for M4, 0% for M1R). This should be the primary model-comparison metric, not the pass/fail rule that privileges imprecision. The revision should restructure the model-comparison conclusions around this joint calibration rather than the binary survival rule.

**The divergence between within-item and across-cell results is not resolved**

The within-item analysis finds declining proportional pull (negative curvature). The across-cell analysis finds no decline, with a positive point estimate. The paper offers two candidate explanations—researchers may place extreme anchors on uncertain items, and informative anchors may behave differently from random ones—but cannot distinguish between them. This is not a minor loose end; it is the central interpretive problem of the paper. If the pattern reverses when moving from random to researcher-chosen anchors, then the practical implication (whether negotiators gain from more extreme anchors) remains entirely open. The paper's own exploratory analysis scaling extremity by estimate spread gives contradictory results depending on specification. A revision needs to engage more directly with what it would take to resolve this divergence—for instance, by identifying cells in the across-cell set where anchor plausibility can be estimated, or by proposing a specific design that would discriminate the two explanations. As it stands, the paper's two analyses pull in opposite directions, and the discussion treats this as an open question rather than grappling with what the joint pattern implies.

**The quadratic log-scale specification may impose the curvature it detects**

The within-item model specifies y = a + bx + gx|x|, which forces the elasticity to be a linear function of |x|. This functional form has a mechanical turning point at |x| = b/(2|g|) = 3.78, beyond which the local elasticity goes negative. The paper notes this and offers a piecewise analysis as a check, which shows flattening but not reversal. However, the piecewise analysis compares only two bins (near vs. far), which cannot distinguish gradual saturation from a step change at some threshold. If the true anchor-response function has a kink or plateau rather than smooth curvature—plausible if plausibility boundaries are fairly sharp—the quadratic specification would spread that discontinuity across the entire range and produce a curvature coefficient that overstates the rate of decline for moderate anchors while understating it for extreme ones. Adding a spline or piecewise-linear specification with more breakpoints (the data from Bahník have hundreds of anchor values per item and could support this) would test whether the quadratic form is a reasonable approximation or is shaping the conclusions.

**Calibration to a single 30-year-old benchmark constrains model predictions asymmetrically**

All five models are calibrated to produce an anchoring index between 0.30 and 0.60, matching the value Jacowitz and Kahneman (1995) reported for 15th/85th-percentile anchors. This is a single empirical moment from one study with 15 items. The number of accepted parameter grid points varies dramatically across models (M3: 11; M1: 24; M4: 250; M1R: 56), meaning some models are represented by a thin slice of their parameter space while others are not. The preregistration computed the calibration index on the log scale, while Jacowitz and Kahneman computed theirs on the raw scale; the sensitivity analysis shows this made little difference for acceptance, but the mismatch means the calibration target is approximate. More importantly, calibrating to a single moment leaves the models' predictions for extreme anchors determined almost entirely by their structural assumptions rather than by empirical constraints on their parameters. A calibration that also matched, say, the average elasticity in a published random-anchor study would give tighter and more empirically grounded prediction intervals, particularly for M1R.

**Random-effects convergence failure inflates precision of the key estimate**

In the random-anchor stratum—the stratum that carries the result—the full mixed model did not converge, and the preregistered fallback removed the between-cell variance of the curvature. The curvature is then estimated as though it is identical across all 15 items, giving it 3,936 degrees of freedom. The paper notes that this makes the confidence interval narrower than one allowing item-varying curvature. This is a meaningful concern: if the curvature genuinely differs across items (as the exploratory item-by-item analysis suggests it does, with magnitudes ranging from −0.02 to −0.06 across Bahník's items), then the reported interval for g is anti-conservative. The revision should report the item-level curvature estimates and their heterogeneity, and consider whether a Bayesian specification or a two-step approach (estimate curvature per item, then meta-analyse) would avoid the convergence problem without collapsing item-level variation.

**The paper stops short of testing the model it motivates**

The discussion identifies the model class that best matches the data: 'a mixture in which the weight of an anchor falls gradually but does not vanish.' This is a specific, testable idea—a plausibility-discounted integration model with a floor on the weight, or equivalently M4 with a minimum-weight parameter. The paper declines to test it ('the data do not identify such a model, and we did not test one'). For a paper whose contribution is model-based discrimination, leaving the best-fitting model class unspecified and untested weakens the payoff. The data from Bahník (2021) have hundreds of anchor values per item and should be rich enough to fit a three-parameter model (intercept, slope, decay rate with floor) per item. A revision that fits even a simple version of this model—and shows whether it can jointly reproduce the within-item curvature and the across-cell null—would substantially strengthen the paper's contribution beyond ruling things out.

**No derivation that Hedges' g rises mechanically with constant proportional pull**

The paper's entire motivation rests on the claim that a standardised mean difference rises with anchor distance even when proportional influence is constant, making prior meta-analytic evidence uninformative about the extremity question. This is stated as fact in the introduction and confirmed empirically in the exploratory analysis, but the mathematical argument is never shown. For a paper whose contribution is precisely about choosing the right outcome metric, this needs a short derivation or worked numerical example. Suppose a constant log-scale elasticity of 0.3 and a fixed response standard deviation on the log scale: write out g as a function of anchor distance and show that it increases. Three equations would do it. Without this, a reviewer who does not immediately see why g must grow can question the premise, and the paper has nothing to point to except an assertion and a citation to Röseler and Schütz calling for better measures.

**Missing test of whether curvature covaries with item-level prior uncertainty**

The paper's theoretical conclusion is that anchor influence is limited by plausibility, and plausibility is a function of how uncertain people are about the quantity. This predicts a specific cross-item pattern: items with narrow prior distributions (well-known quantities like the Eiffel Tower's height) should show steep curvature, while items with wide priors (obscure lengths) should show shallower curvature because even extreme anchors remain somewhat plausible. The Bahník data span 13 items with different familiarity levels, and the item-level random-effect estimates from the mixed model already contain this information. The spread of unanchored or lightly anchored responses (estimates near |x| = 0) provides a proxy for prior uncertainty. Plotting item-level curvature against item-level response spread, or adding an interaction between the curvature term and a measure of item uncertainty, would test the plausibility mechanism directly rather than relying solely on the direction of the pooled curvature. As it stands, the link from negative curvature to plausibility is supported only by sign, which is necessary but not sufficient—the paper shows that influence declines but does not show that it declines because of implausibility.

**Simulation specification too sparse for readers to evaluate model predictions**

The model predictions are central to the paper's contribution, yet the distributional assumptions behind the simulations are given only in outline. The text says belief centres were 'drawn around the true value, with item-level bias and between-person spread,' that responses included 'response noise and a 2% share of gross errors,' and that belief uncertainty sigma was 'drawn from 0.3 to 1.2 log units per item.' It does not state the distributional form of the belief centre (normal on the log scale? uniform?), the distribution of item-level bias, the form and scale of response noise, or how the 2% gross errors were generated. These choices can affect the predicted curvature—for instance, heavy-tailed response noise would flatten far-anchor estimates and produce negative curvature even in M2. Readers who want to evaluate whether the model predictions are fair representations of each theory need these assumptions stated in the paper, not only recoverable from R/models.R. A specification table listing each distributional assumption, its support, and a brief justification would make the model comparison fully evaluable from the text alone.

**Recommendation**: Major revision. The core question is well-chosen, the preregistration is genuine, and the observation that standardised effects and proportional pull diverge is worth publishing. But the empirical base for the main claim is too narrow (one study, one item domain), the model-comparison framework rewards uninformativeness in a way that distorts the conclusions, and the divergence between the two analyses is unresolved. These are addressable problems, not fatal ones.

**Key revision targets**:

1. Narrow the scope of the abstract and conclusion to match the evidence (random anchors on physical magnitudes in one study), or obtain converging evidence from additional multi-anchor items in different domains.
2. Replace the binary survival rule with a model-comparison metric that penalises width (e.g., the proportion of simulations jointly reproducing the observed confidence region), and reframe M1R accordingly—it was not testable, not supported.
3. Test a plausibility-discount model with a weight floor (the model class the discussion identifies as most promising) and report whether it can jointly accommodate the within-item curvature and the across-cell null.
4. Report item-level curvature estimates and their heterogeneity to assess whether the pooled estimate from the convergence-fallback model is representative, and consider a two-step estimation approach that preserves item-level variation.
5. Add a flexible (spline or multi-breakpoint piecewise) specification for the within-item anchor-response function to check that the quadratic form is not imposing the curvature pattern.

**Status**: [Pending]

---

## Detailed Comments (12)

### 1. Yoon anchor ranges inconsistent with stated anchor source

**Status**: [Pending]

**Quote**:
> the anchors of the two Yoon et al. items were participants' own height or age

**Feedback**:
The x-ranges in Table 1 for the two Yoon items cannot be reconciled with heights or ages of adult participants. For the sofa bed item (true value 693), x = -4.5 implies an anchor of about 7.7 and x = 0.8 implies about 1,540; adult heights in centimetres span roughly 150-200, giving x from -1.5 to -1.2, and ages 18-70 give x from -3.6 to -2.3. Neither comes close to the observed range. For the Stephen King item (true value 51), x = 1.7 implies an anchor of about 279, which is not a plausible height or age in any unit. The pattern is suggestive of mixed-unit entries in the OpAQ anchor column (x = 0.8 for the sofa bed is consistent with heights in millimetres; x = -4.5 is consistent with heights in feet), but the text describes the source as a single quantity per participant. This matters because these two items are the only cells in which the exploratory analysis found positive curvature (g = 0.093), making them a potential counterexample to the main finding. If the anchor column mixes units or the source is mislabelled, the positive curvature may be an artefact. Verify the Yoon et al. (2021) design against the OpAQ data file and correct whichever element is in error.

---

### 2. H2 result described as a null finding rather than as inconclusive

**Status**: [Pending]

**Quote**:
> the anchoring index did not change detectably with extremity (slope 0.050, [-0.013, 0.113])

**Feedback**:
The abstract says the index 'did not change detectably,' and the Discussion says it 'showed no detectable decline.' Both phrasings suggest the data support stability. The results section classifies this outcome as 'inconclusive under the preregistered rule': the confidence interval spans -0.013 to 0.113, which includes zero but extends well past the equivalence bound of plus or minus 0.03, so the data cannot distinguish no change from a moderate positive slope. Calling it 'no detectable change' is the classic error of treating a non-significant result as evidence of no effect. The tension matters: the within-item curvature is negative while the across-cell point estimate is positive, and describing the latter as 'no change' rather than 'inconclusive' softens this tension for readers who see only the abstract. Replace 'did not change detectably' in the abstract and 'showed no detectable decline' in the Discussion with language matching the preregistered classification, such as 'showed no clear trend' or 'yielded an inconclusive result regarding extremity.'

---

### 3. Preregistration credibility needs a stronger commitment mechanism than self-operated version control

**Status**: [Pending]

**Quote**:
> The study was carried out by an AI system, Claude Opus 5.5 (Anthropic; model identifier claude-opus-5-5), running in Claude Code between 27 and 28 September 2026 under the instruction of the author.

**Feedback**:
The entire pipeline ran in roughly 24 hours: literature search, model specification, preregistration, analysis, manuscript. Preregistration gains credibility from a public timestamp on a tamper-resistant registry and a verifiable gap before data access. Here the mechanism is a git commit and a reader function that blocks one column, both operated by the same AI system in the same session. Git commits can be backdated, and no external registry with an independent timestamp is mentioned. A reader who wants to trust that the preregistration was genuinely locked before outcome data were seen has only the internal consistency of one agent's version-control history to rely on. The paper should also state which aspects of the OpAQ data were inspected before the preregistration was committed. The abstract and the model-predictions section already make clear that designs, anchor values, true values, and cell sizes were seen, but the Van den Akker et al. (2021) template this section cites as its framework asks authors to declare prior knowledge explicitly. Add a statement of where the preregistration was registered, how temporal separation was enforced, and what data were seen at the time of commitment.

---

### 4. Author role statement contradicts the described instruction

**Status**: [Pending]

**Quote**:
> The author did not direct the choice of question, methods or interpretation.

**Feedback**:
Two sentences earlier, the instruction is described as asking for 'a complete, preregistered study in judgement and decision making based on openly licensed data, with decisions recorded and reviews by other AI systems.' That instruction fixed the field, constrained the methodology to preregistered secondary data analysis, specified the data type, and required external AI review. These are consequential design decisions that shaped every downstream choice. Saying the author 'did not direct' question, methods, or interpretation is in tension with those constraints. Additionally, the paper attributes every intellectual contribution to the AI but names a single human author, leaving open who bears scientific responsibility if the analysis contains an error. Current norms require that listed authors take responsibility for the work. Two changes would resolve both issues. First, distinguish the constraints the author imposed from the specific choices the AI made within them: 'Within the constraints of the instruction, the author did not select the specific research question, statistical models, or interpretive framing.' Second, add a statement such as 'The author reviewed all analyses and interpretive claims and takes full responsibility for the content of the paper.'

---

### 5. M1R parameter deviation too vague to evaluate

**Status**: [Pending]

**Quote**:
> the preregistration described one M1R parameter incorrectly; the code, and therefore the predictions, were correct.

**Feedback**:
For a paper whose contribution rests on comparing model predictions, the correctness of those predictions is load-bearing. This sentence prevents readers from assessing whether the text-code mismatch was consequential. Which parameter was misdescribed, what did the preregistration text say, and what did the code implement? One sentence with the parameter name and both values would suffice. Separately, this deviation and deviation 3 (numerical safeguards in code but not text) both treat the code as authoritative over the written plan, but the paper never states which document is binding. Preregistration norms typically treat the written plan as the commitment. If undisclosed code features count as preregistered, a reader cannot evaluate the plan from its text, which weakens the transparency preregistration is meant to provide. State explicitly: when the preregistered text and code disagree, which governs?

---

### 6. Metric critique applied to one meta-analysis but not the other

**Status**: [Pending]

**Quote**:
> Schley & Weingarten (2026) coded extremity as a binary flag, mainly for anchors that the original authors described as extreme or implausible, and found no difference in effect size.

**Feedback**:
The section builds to the argument that standardised effects are uninformative about proportional pull, but applies this critique only to Roseler and Schutz's finding of increasing g. Schley and Weingarten's null result escapes scrutiny. If their 'extreme' anchors involve larger inter-anchor distances, then equal g across the two groups is actually more consistent with declining proportional pull than with constant pull: the greater distance should produce a larger raw shift under constant proportional influence, pushing g up. A null in g despite greater distance suggests the proportional pull fell enough to offset the distance advantage. The paper's own logic, applied symmetrically, turns the null into weak evidence for the paper's thesis. Note after describing the result that Schley and Weingarten's finding rests on the same metric limitation and, if anything, is compatible with declining proportional pull when extreme anchors are also farther from the truth.

---

### 7. 'Clarified' obscures whether the critical-value choice was made post hoc

**Status**: [Pending]

**Quote**:
> Fourth, we clarified that the relative-curvature interval uses a normal critical value.

**Feedback**:
'Clarified' is ambiguous. If the preregistration specified a different distributional basis (e.g., a t quantile) and the authors switched to a normal critical value, this is a deviation, not a clarification. If the preregistration was silent, then the choice was made after seeing the data—again not a clarification but a gap filled post hoc. The relative-curvature interval feeds directly into classifying H1. With thousands of degrees of freedom the practical difference between normal and t is negligible here, but the reporting still matters for preregistration transparency. State what the preregistration said (or did not say) and what was decided afterward.

---

### 8. Symbol g denotes both the standardised effect and the curvature parameter

**Status**: [Pending]

**Quote**:
> A meta-analysis of openly shared trial-level data from 90 anchoring studies estimated a pooled standardised effect of $g = 0.69$

**Feedback**:
The paper uses g for Hedges' g in the introduction and for the curvature coefficient throughout the results (e.g., g = -0.041). The entire argument turns on showing that Hedges' g is a misleading measure while the curvature g is informative, so having both share a symbol is actively confusing. A reader encountering 'g fell as anchors moved away' in the abstract may momentarily parse this as the standardised effect. Use a distinct symbol for one—rename the curvature to gamma or c, or refer to the standardised effect consistently as 'Hedges' g' with no bare-symbol shorthand.

---

### 9. Ambiguous outcome metric for Strack and Mussweiler

**Status**: [Pending]

**Quote**:
> Strack & Mussweiler (1997) found that implausible anchors were at least as effective as plausible ones in standardised estimates.

**Feedback**:
In a section whose whole point is that the choice of outcome metric determines the conclusion, 'standardised estimates' is doing unexplained work. It could mean standardised effect sizes, z-scored responses, or simply raw estimates from a standard paradigm. Strack and Mussweiler compared absolute estimates across anchor conditions; if their finding rested on raw differences, calling it 'standardised' risks implying they used the very metric the paragraph is about to criticise. Name the actual measure.

---

### 10. Fixed-anchor stratum composition fragile under disputed classification

**Status**: [Pending]

**Quote**:
> OpAQ codes five cells as using fixed anchors: four items with 10 high anchor levels each from unpublished data by Frech et al. (2021), contributed to OpAQ, and one item (the height of Cologne cathedral) with 20 anchor levels from a supplementary task in Imhoff & Barker (2023, Study 2), whose authors describe these anchors as random. We followed the OpAQ coding, as preregistered.

**Feedback**:
Following the preregistered coding is methodologically sound, but a consequence goes unstated. The Imhoff and Barker item contributes 786 of roughly 1,200 fixed-anchor estimates (about 65%). If its anchors are in fact random—as the study authors say—the residual fixed-anchor stratum is four items from one unpublished source, all with exclusively above-true-value anchors (x-ranges between 0.0 and 2.4) and just 104 participants each. Any stratum-specific curvature estimate for fixed anchors then rests on this narrow, one-sided subset. A sentence noting the compositional fragility would help readers weigh the fixed-anchor results appropriately.

---

### 11. Unit-mismatch cell: gross-error removal vs. full exclusion needs clearer sequencing

**Status**: [Pending]

**Quote**:
> 987 were removed as gross errors, 870 of them from the cell with the unit mismatch.

**Feedback**:
The deviations section says the Chicago cell 'was excluded in full' because all responses exceeded the gross-error limit, yet this sentence in the results reports 870 of 987 gross errors as coming from that cell. A reader encountering the results first (before the deviations section) will wonder whether the remaining responses from a cell with systematic unit confusion survived. The paper should state explicitly in the results, at the point where the 870 figure appears, that the cell was excluded in its entirety and that no estimates from it entered any analysis. One parenthetical would do.

---

### 12. Secondary test inherits the extremity-item confound

**Status**: [Pending]

**Quote**:
> Because anchor values in most studies were chosen by the original authors together with the items, a comparison across items confounds extremity with item properties. Our primary test is therefore within items

**Feedback**:
The paragraph identifies confounding of extremity with item properties as the motivation for the within-item design, then introduces the across-cell comparison as 'a secondary test' without noting that it is subject to the same confound. The anchoring index is computed within cells, but the second stage—regressing indices on extremity across cells—entangles extremity with item difficulty, paradigm, and researcher anchor-selection strategy. The word 'secondary' hints at lower evidential weight, but the specific reason goes unstated. Because the H2 result turns out inconclusive and may partly reflect this confound, readers benefit from knowing the limitation up front. A short qualifier would suffice—e.g., 'though still subject to this confound.'

---
