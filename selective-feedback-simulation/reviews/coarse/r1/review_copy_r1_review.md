# Learning from disagreements when selective feedback helps and harms advisor evaluation

**Date**: 09/28/2026
**Domain**: social_sciences/psychology
**Taxonomy**: academic/research_paper
**Filter**: Active comments

---

## Overall Feedback

Here are some overall reactions to the document.

The paired comparison is sound under the stated sampling conditions: agreements contribute zero to the accuracy difference, and uniform sampling of disagreements preserves its sign. The paper also reports the cost of weighting in a finite sample, rather than treating correction as automatically beneficial. Its main limits are the narrow set of environments and the gap between the simulated adoption rule and decisions people could make with confidence information.

**The deployment benchmark misses the value of confidence-based choice**

Section 8’s crossing environment gives the advisor 80% accuracy in both strata, while human accuracy is 60% at low confidence and 90% at high confidence. Choosing the advisor for low-confidence cases and oneself for high-confidence cases would yield 85% accuracy, compared with 80% for the better fixed source. Section 9 defines regret against that fixed source, so it assigns zero regret to a policy that gives up five percentage points available from the confidence information already in the model. This is a valid measure for a decision that must be made once for all future cases, but it limits the practical interpretation of H1. Add a confidence-contingent adoption analysis with regret against the best stratum-specific rule, or establish why the intended use requires a fixed source despite confidence being available.

**The grid gives limited coverage of advantage patterns**

In Section 8’s 81-environment grid, every advisor has a positive advantage in the low-confidence stratum; its high-confidence advantage is negative in 54 environments and zero in 27. The single added control is the only environment with a positive advantage in both strata, and the grid has no environment where the advisor is inferior in both. Moreover, H1 and H2 change the verification ratio and feedback budget as well as the advantage pattern, so their contrast cannot isolate why weighting helps in one case and harms in the other. Section 14’s counts describe this chosen grid accurately, but they do not show how often the finding survives other advantage patterns. Expand the grid to include positive and negative advantages in both strata, and compare those patterns at common ratios and budgets while reporting the resulting regret differences.

**The weighting result relies on an unusually well-known selection process**

The correction in Sections 5 and 9 requires positive, correctly known verification probabilities and selection that does not vary with correctness within each confidence stratum. The simulation supplies those conditions by construction: the smallest low-confidence verification probability is 1/8, and the learner receives the correct ratio. In an advisor evaluation setting, verification may also depend on perceived difficulty or other features associated with which source is right. Weighting by confidence alone would then fail to recover the population comparison, even with many labels. Test estimated and misspecified probabilities, sparse or unverified strata, and selection that varies within a stratum; where positivity fails, state what can still be bounded or add a small random-audit component.

**Equal label budgets leave the resource decision unresolved**

Sections 8 and 14 hold the number of verified outcomes fixed, but the policies require different numbers of encountered cases to obtain them. In the crossing environment, 100 labels require about 333 opportunities under uniform disagreement verification and 667 at ratio 4; random all-case verification requires 100. The paper reports these yields, yet H1 and the plotted regret comparisons remain comparisons at equal labels. If opportunities, delay, or a limited deployment period matter, the ranking of feedback policies may change. Repeat the policy comparison at fixed opportunity budgets and show regret against both labels used and opportunities required, so readers can see when the gain from selection correction pays for acquiring its feedback.

**The behavioural claim remains a proposed test**

Section 9 assigns learners complete paired correctness records, a known marginal human benchmark for the absolute learner, and the correct sampling ratio for the weighted learner. Section 16 proposes an experiment but provides no evidence that people use those inputs or map the displays onto the stipulated scores. The manuscript acknowledges this limit, which keeps the probability results intact; it also means the simulation cannot yet explain learning from selective feedback in people. For a behavioural contribution, run the proposed display-by-selection experiment with numerical advantage estimates and adoption choices, including an inferior-advisor condition, and test the predicted interaction. If the contribution is intended to remain computational, frame it as a decision-model result and develop the finite-sample analysis further.

**The reported grid does not yet give a usable weighting rule**

H1 and H2 in Sections 10–12 establish two predictions with precise Monte Carlo intervals, but those intervals measure simulation precision in the stipulated environments. Section 14 reduces the wider grid to counts of environments where weighting helps, harms, or falls within a tolerance; it does not show the size of those effects across budgets, ratios, overlap settings, or the capped rule. That matters because Section 13’s cap of 2 leaves the crossing environment near 50% advisor adoption even with 500 labels, consistent with a limiting score near a tie. Report regret magnitudes and Monte Carlo uncertainty across the grid, grouped by the conditional advantage pattern, and show where each cap changes the limiting adoption decision. An exact or numerically evaluated finite-sample decision boundary for the two-stratum model would turn the examples into guidance about when correction is worth its variance.

**Recommendation**: major revision. The analytic sign claim and the two stated simulation comparisons appear internally consistent. For a top venue, the paper needs broader evidence about when the decision result holds and a closer match between its deployment benchmark and the decisions its framing addresses; a behavioural interpretation also needs behavioural evidence.

**Key revision targets**:

1. Evaluate confidence-contingent deployment alongside fixed-source adoption, with regret against the best available rule for each decision.
2. Expand the environment grid to cover all conditional advantage patterns and compare them at shared verification ratios and feedback budgets.
3. Test weighting with estimated or misspecified verification probabilities, sparse strata, and zero-probability cases; report how weight caps affect the limiting decision.
4. Compare feedback policies at fixed opportunity budgets as well as fixed verified-label budgets.
5. Either test the proposed display-by-selection interaction in participants or develop a finite-sample decision boundary and frame the contribution as computational.

**Status**: [Pending]

---

## Detailed Comments (3)

### 1. Clarify what stays fixed in the proposed experiment

**Status**: [Pending]

**Quote**:
> A future experiment could hold each verified history fixed and randomise an advisor-only display, a paired display, or a selection-adjusted paired display. It would also randomise uniform versus high-confidence disagreement selection and provide an explicit marginal self-accuracy benchmark.

**Feedback**:
The predicted interaction requires the selection rules to reveal different sets of outcomes. Specify that each verified history is held fixed across display conditions within a selection condition, while the selection conditions generate their histories under their assigned rules. As written, “hold each verified history fixed” could also mean holding the revealed cases fixed across selection conditions.

---

### 2. Identify which missing cases contribute zero

**Status**: [Pending]

**Quote**:
> They do not imply that every comparative inference requires representative feedback: some comparisons remain identifiable because the missing cases contribute nothing to the difference of interest.

**Feedback**:
Only agreements necessarily contribute zero to the paired accuracy difference. An unverified disagreement contributes either +1 or −1. Name agreements here as the zero-contribution cases; the later result also depends on sampling disagreements uniformly. This distinction matters once the paper turns to selective verification within disagreements.

---

### 3. State how the grid applies its regret tolerance

**Status**: [Pending]

**Quote**:
> At selection ratio 8 and 20 verified outcomes, weighting had lower regret than pairing in 44 grid environments, higher regret in 22, and a difference within the prespecified tolerance in 15. At selection ratio 8 and 500 verified outcomes, weighting had lower regret than pairing in 36 grid environments, higher regret in 9, and a difference within the prespecified tolerance in 36.

**Feedback**:
The counts form three exclusive categories, but “lower” and “higher” could be read as including differences inside the stated tolerance. Define them using weighted minus paired regret: below −0.0005, within ±0.0005, and above 0.0005. The boundary matters at 500 labels, where 36 environments are classified as within tolerance.

---
