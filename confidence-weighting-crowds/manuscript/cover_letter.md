> **AI-GENERATED DEMONSTRATION — NOT PEER REVIEWED — NOT FOR CITATION.** agentic-research-examples: AI-generated demonstration for the tutorial "Easing into agentic AI in research". See AI_GENERATED.md.

# Cover letter

To the Editors of *Judgment and Decision Making*,

We are submitting a Theory Article with an empirical component, "When does weighting by confidence hurt the crowd? A finite-sample boundary and a test across 81 judgment datasets", for consideration at *Judgment and Decision Making*.

**What the paper does.** Weighting judges by their confidence is often described as the optimal way to combine binary judgments, and the field has established that the rule is only conditionally optimal: correlated errors change the optimal weights, and miscalibrated competence inputs degrade it. The practical question that remains is how large the confidence-weighting advantage usually is and when its sign turns, stated in the quantities an aggregator can observe. We write the gap between confidence-weighted (CW) and equal-weighted (EW) aggregation as a function of the confidence–accuracy calibration slope, the within-item error correlation, and confidence dispersion, map the boundary of the harmful region in a preregistered simulation, and estimate where real judgment data sit.

**What we find.** Across 76 datasets from the Confidence Database (1.64 million trials) the two objectives diverge. On the preregistered crowd-decision measure, confidence weighting is a small but reliable improvement (+0.004, 95% CI [0.0003, 0.0083], and +0.007 on items the crowd does not already decide), and in a held-out item test it reaches 0.938 accuracy against 0.926 for equal weighting. On an exploratory graded measure that predicts a held-out judge's correctness rather than the item's truth, it is slightly worse (Brier improvement −0.0006, negative in 91% of datasets). Neither the calibration slope nor the within-item error correlation moderates either effect, and an estimated shrinkage weight beats equal weighting in only 24% of datasets. The simulation locates a real boundary, but a coarse two-input mapping of it does not reproduce the data.

**Why *JDM*.** The journal's scope explicitly includes advances in methods for improving judgment and decision making, including the wisdom of crowds, and the development or specification of existing theory. This paper is squarely within both. It is also a natural home for work that weighs the conditions under which a widely recommended aggregation rule helps, rather than assuming it does.

**Novelty and honesty about scope.** We do not claim that confidence weighting can hurt, that correlated error changes optimal weights, or that confidence-weighted voting sometimes beats majority voting; those are established, and we cite the work that established them (Shapley & Grofman, 1984; Baharad & Ben-Yashar, 2009; Huang et al., 2024; Meyen et al., 2021). The contributions are the psychometric parametrisation of the gap, the simulated boundary, the estimated base rate, and an honest negative result about the scope of a two-parameter account; we are explicit that the shrinkage recommendation is not supported by the held-out test. The empirical data are a reused corpus that was not designed for crowd aggregation; this and the other limitations are stated plainly in the manuscript and in the author's own weaknesses assessment.

**Open science.** The preregistration, committed before the outcome variables were analysed, the deviation log, the analysis code, and the simulated-data configuration accompany the manuscript. `run_all.sh` reproduces every number and figure from the openly licensed (CC0) raw data with one command. No new data were collected and no personal identifiers were used.

We confirm that this manuscript is not under consideration elsewhere, that no one has been contacted or any account created in its preparation, and that AI involvement is disclosed as required.

Yours sincerely,

The author(s) — names and affiliation to be supplied before submission
