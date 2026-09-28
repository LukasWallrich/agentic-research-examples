# Novelty assessment before preregistration

Search completed 28 September 2026; primary sources, queries, metadata, and caveats are preserved in `scoping/literature_agent.md` and `scoping/journal_and_data.md`. This is a scoped search, not proof that no prior paper contains the same result. No hypothesis-bearing simulation or participant-level outcome was examined.

## Study contribution

The paper distinguishes two targets of learning from selectively verified advice: absolute advisor accuracy and the sign of the advisor's accuracy advantage over oneself. It derives the limits of paired comparison and quantifies finite-feedback decision loss when correction for confidence selection trades reduced bias for additional variance. A future randomised feedback-display experiment supplies refutable psychological predictions. The mathematical identity, inverse-probability weighting, and the general fact that selection biases learning are existing ideas, not claimed inventions.

## Five closest papers

1. **Pescetelli & Yeung (2021), The role of decision confidence in advice-taking and trust formation.** DOI: https://doi.org/10.1037/xge0000960. Their experiments and models concern confidence-weighted agreement as evidence of advisor reliability, including learning without objective feedback and distortion from dependent judgements. **Addition:** objective truth is available but selectively sampled; compare absolute and paired representations of the same verified cases and state their different estimands. This is not the first computational model of confidence and trust.

2. **Jaquiery & Yeung (2024), Preferences for advisor agreement and accuracy.** DOI: https://doi.org/10.1371/journal.pone.0311211. Their experiments distinguish agreement and accuracy with and without feedback; feedback supports preference for accuracy. **Addition:** distinguish feedback's presence from its selection mechanism; uniform disagreement feedback can remain adequate for relative ranking even when inappropriate for absolute assessment. No claim that their participants exhibited the proposed selection effect.

3. **Fetchenhauer & Dunning (2010), Why so cynical? Asymmetric feedback underlies misguided skepticism regarding the trustworthiness of others.** DOI: https://doi.org/10.1177/0956797609358586. Their trust experiments show that feedback conditional on trusting can sustain inaccurate negative impressions. **Addition:** advisor verification offers a paired contrast whose unobserved values on agreement are structurally zero, so missing feedback need not undermine the comparative decision. Reciprocity and classification accuracy are distinct tasks; this paper does not reproduce their experiment.

4. **Gao et al. (2021), Human-AI Collaboration with Bandit Feedback.** DOI: https://doi.org/10.24963/ijcai.2021/237. They use counterfactual policy learning to route cases between humans and machines under bandit feedback. **Addition:** a constrained global advisor-adoption decision, with fully verified paired labels on sampled cases, psychologically interpretable absolute/paired summaries, and finite-label cost of selection adjustment. IPW itself and learning from selectively observed outcomes are established; no general policy-learning advance is claimed.

5. **Zavattari, Tommasi, & Prencipe (2026), One Human, N Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence.** Primary preprint: https://arxiv.org/abs/2607.28317. It already models budgeted inspections, confidence selection, correlated errors, and worse-than-random auditing. **Addition:** learning comparative competence from a feedback history rather than allocating inspections to reduce remaining errors across a fleet; paired representation and the zero contribution of agreements are central. This is an unreviewed preprint, and its DOI belongs to DataCite rather than Crossref; registry coverage must not be misrepresented.

## Further overlap and limits

Denrell & March (2001) and Denrell (2005) already explain biased impressions through selective experience. Fok & Weld (2024) discuss verification and complementary performance. Honeycutt et al. (2020) show that interactive feedback can reduce trust and perceived accuracy. Li & Steyvers (2026, preprint) model learning AI confidence calibration. These precedents restrict the contribution to a particular representation-by-selection boundary and its finite-feedback consequences.

A transparent two-stratum scenario is intentionally limited. The paper cannot establish which summaries humans use, how often real verification follows the assumed policies, or that its numerical worlds describe deployed AI. It should be judged as a computational Theory Article with a testable behavioural extension, not as empirical evidence of algorithm aversion.
