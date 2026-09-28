# Literature scoping: selective verification and advisor learning

Search date: 28 September 2026. This is a scoping review, not a systematic review. I searched primary article, publisher, institutional-repository, and arXiv records. I did not load individual-level data or run simulations. Crossref responses for the published references below are saved in `scoping/crossref_literature_agent.json`.

## Recommended contribution

A defensible contribution is to distinguish what disagreement-selected feedback can establish about **absolute advisor accuracy** from what it can establish about **relative advisor advantage**, and to investigate how the representation of identical feedback changes learning. The focal empirical prediction should concern a randomised display intervention: given the same disagreement-feedback sequence and an explicitly stated marginal human accuracy, an AI-only accuracy display versus paired human-and-AI accuracy display should produce different advisor evaluations and choices. The prediction can fail in future data if people spontaneously adjust for selection, already encode relative outcomes, ignore the display manipulation, or use other cues that outweigh it.

The formal sign result alone is not a substantial novelty claim. In binary tasks, agreement trials contribute zero to the paired correctness difference. Relative superiority therefore depends on the discordant cells, the elementary logic underlying matched binary comparisons. A simulation should quantify finite-horizon learning, the failure of the protection under confidence-dependent selection within disagreements, and the precision cost of weighting or random audits. No simulation should be described as empirical evidence that people actually use the proposed updating rules.

The initial broad idea, confidence-ranked auditing under correlated errors, is occupied unusually closely by a July 2026 preprint described below. The narrower comparison of feedback representations has better separation from that work and from older sampling accounts.

## Five closest published papers

### 1. Pescetelli, N., & Yeung, N. (2021)

**The role of decision confidence in advice-taking and trust formation.** *Journal of Experimental Psychology: General, 150*(3), 507–526. DOI: [10.1037/xge0000960](https://doi.org/10.1037/xge0000960).

Primary accessible source: [Oxford accepted manuscript and record](https://ora.ox.ac.uk/objects/uuid%3A5b00b576-d379-437d-bd71-91eeedd89f17). Crossref gives March 2021 publication; Oxford also records 2020 advance publication. Use 2021 consistently for the journal issue.

**Supported account:** The abstract and Experiment 2 explain that agreement weighted by one's own confidence can help estimate advisor accuracy without objective feedback when judgments are independent. Correlated judgments produce systematic trust distortions. The article also contains agent-based simulations of network-level trust and belief formation.

**What the proposed study adds:** Objective feedback is available but selected. The comparison is between absolute and paired evaluations made from the same selected outcomes, rather than agreement-in-confidence learning with versus without ground truth. Confidence affects which disagreements are verified, providing a boundary condition for the paired correction.

**Do not claim:** That this is the first computational account of confidence, correlated errors, and trust, or the first agent-based simulation of advice learning.

### 2. Jaquiery, M., & Yeung, N. (2024)

**Preferences for advisor agreement and accuracy.** *PLOS ONE, 19*(9), e0311211. DOI: [10.1371/journal.pone.0311211](https://doi.org/10.1371/journal.pone.0311211).

Primary full text: [PLOS](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0311211).

**Supported account:** The abstract and Discussion report experiments contrasting advisor accuracy and agreement, with and without objective feedback. In the direct accuracy-versus-agreement contrast, feedback produced a clear preference for accurate advice. Methods, “Task overview” and “Dates Task”, describe feedback after final responses in the relevant familiarisation conditions. Feedback was not experimentally selected according to participant–advisor disagreement.

**What the proposed study adds:** The presence of feedback alone is insufficient to characterise its informational value. The proposed study contrasts random and selectively revealed feedback while holding advisor performance fixed, and separates perceived absolute accuracy from relative usefulness.

**Do not claim:** These experiments establish a population-wide preference for agreeable over accurate advisors without feedback; their direct contrast showed substantial individual variation rather than a consistent average preference.

### 3. Fetchenhauer, D., & Dunning, D. (2010)

**Why so cynical? Asymmetric feedback underlies misguided skepticism regarding the trustworthiness of others.** *Psychological Science, 21*(2), 189–193. DOI: [10.1177/0956797609358586](https://doi.org/10.1177/0956797609358586).

Primary accessible copy: [author-hosted article](https://sites.lsa.umich.edu/wp-content/uploads/sites/275/2015/11/fetchdunnps10.pdf); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/20424043/).

**Supported account:** The abstract and experimental results show that feedback irrespective of one's own trust decision reduced cynicism compared with asymmetric feedback given only after trust was extended, or no feedback. The mechanism is missing evidence about partners who were not trusted.

**What the proposed study adds:** Advisor verification has a paired structure: the same ground truth evaluates both advisor and decision maker. Selection can bias an absolute evaluation while preserving the direction of a relative evaluation. Thus, some selective feedback can support an appropriate comparative decision without recovering absolute accuracy. This is a different, more conditional claim than “symmetric feedback corrects mistrust”.

**Do not claim:** The simulation explains these trust-game results, which involve interpersonal reciprocity rather than classification accuracy.

### 4. Honeycutt, D. R., Nourani, M., & Ragan, E. D. (2020)

**Soliciting Human-in-the-Loop User Feedback for Interactive Machine Learning Reduces User Trust and Impressions of Model Accuracy.** *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing, 8*(1), 63–72. DOI: [10.1609/hcomp.v8i1.7464](https://doi.org/10.1609/hcomp.v8i1.7464).

Primary publisher source: [AAAI](https://ojs.aaai.org/index.php/HCOMP/article/view/7464).

**Supported account:** The abstract reports an experiment using simulated object detection: providing interactive feedback reduced trust and perceived accuracy, whether or not model accuracy improved in response. This establishes that interaction intended to improve a model can have adverse consequences for impressions.

**What the proposed study adds:** A specific informational mechanism and remedial comparison: distinguish error-enriched outcome exposure from the representation of that exposure, compare absolute and paired trackers, and state when pairing does and does not protect the ranking. It does not establish that the selection mechanism caused Honeycutt et al.'s effects.

**Evidence scope:** Abstract/publisher summary inspected; do not cite for unverified details of its feedback-selection mechanism.

### 5. Fok, R., & Weld, D. S. (2024)

**In search of verifiability: Explanations rarely enable complementary performance in AI-advised decision making.** *AI Magazine, 45*(3), 317–332. DOI: [10.1002/aaai.12182](https://doi.org/10.1002/aaai.12182).

Primary full text: [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/aaai.12182); [author preprint](https://arxiv.org/abs/2305.07722).

**Supported account:** Abstract and Introduction argue that explanations improve decisions to the extent they permit verification, and distinguish complementary team performance from different meanings of appropriate reliance.

**What the proposed study adds:** Successful verification of individual cases can still produce an unrepresentative history for learning about an advisor. The study asks what a learner can infer from verified cases, and how that inferential task depends on whether the target is absolute reliability or comparative advantage.

**Do not claim:** The proposed model tests whether explanations enable verification; it assumes a verification channel and studies consequences of selection.

## Essential foundations beyond the five

- **Denrell, J., & March, J. G. (2001).** Adaptation as information restriction: The hot stove effect. *Organization Science, 12*(5), 523–538. [10.1287/orsc.12.5.523.10092](https://doi.org/10.1287/orsc.12.5.523.10092). Publisher abstract: adaptive repetition of successful actions can leave initially underestimated alternatives undersampled. This already supplies the broad explanation that adaptive sampling produces persistent mistaken impressions.
- **Denrell, J. (2005).** Why most people disapprove of me: Experience sampling in impression formation. *Psychological Review, 112*(4), 951–978. [10.1037/0033-295X.112.4.951](https://doi.org/10.1037/0033-295X.112.4.951). The article models how interaction contingent on current impressions stabilises negative impressions. The present target is a paired accuracy contrast under verification selection, not a new general sampling theory.

## Recent competing work that must be disclosed

### Zavattari, Tommasi, & Prencipe (2026), preprint

**One Human, N Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence.** [arXiv:2607.28317](https://arxiv.org/abs/2607.28317); [full text](https://arxiv.org/html/2607.28317v1).

The abstract and Model section directly cover budgeted noisy inspection, confidence-ranking policies, correlated errors, and a crossover to worse-than-random auditing. Related Work distinguishes allocating audits from learning to defer. The human allocates inspections; outcomes measure undetected error counts. This substantially pre-empts the original broad scoping idea. Our defensible difference is the psychological representation and estimation target of an individual's verified feedback history, not merely another confidence/correlation phase diagram. Its arXiv DOI is a DataCite DOI; do not falsely label it Crossref verified. This is a primary preprint, not peer-reviewed evidence.

### Li & Steyvers (2026), preprint

**Learning to Trust: How Humans Mentally Recalibrate AI Confidence Signals.** [arXiv:2603.22634](https://arxiv.org/abs/2603.22634); [full text](https://arxiv.org/html/2603.22634v1).

Abstract: a behavioural experiment tests learning across calibrated, overconfident, underconfident, and reverse-confidence mappings; an updating model adjusts baseline trust and confidence sensitivity. This makes “people learn AI reliability from repeated feedback” too broad a gap. The proposed contribution concerns selected ground truth and paired comparative learning. Again, arXiv registration must not be described as Crossref verification.

## Open data scoping

Jaquiery and Yeung's PLOS article states that its data are available as an R package at [Zenodo record 5543803](https://zenodo.org/record/5543803), and links the [analysis repository](https://github.com/oxacclab/advisor-choice-paper). The article is CC BY, but article licensing does not establish the dataset licence. I did not download the dataset or inspect outcomes. The Zenodo landing page could not be opened with the browsing tool in this pass, so the dataset licence and identifier status remain unverified. A secondary analysis should not proceed until both are checked. A simulation avoids this licensing uncertainty and allows the selective-feedback intervention to be defined directly; the source study did not randomise such an intervention.

## Search coverage and limits

Queries combined human/AI advice, confidence, correlated errors, selective verification/auditing, selective feedback, trust learning, disagreement, sampling bias, Denrell, and Fetchenhauer/Dunning. Targeted combinations “disagreement selective feedback advice” and “disagreement auditing trust selection bias” did not locate an exact behavioural test of the proposed absolute-versus-paired contrast. This absence is not proof of priority. The search identified current preprints that materially narrow the contribution; preserve them in novelty documentation even if the final manuscript relies on published, Crossref-indexed sources.

## Design safeguards

1. Call the sign identity an analytic property, not a falsifiable behavioural hypothesis.
2. Make behavioural predictions conditional on stated, distinguishable learning rules; randomise the display of identical feedback in the future test.
3. Keep an inferior-advisor condition so pairing cannot be evaluated solely by whether it increases advice acceptance.
4. Distinguish uniform selection within disagreements from confidence-targeted selection, where relative advantage can change between sampled and unsampled strata.
5. Compare methods under the same audit budget and distinguish accuracy estimation from policy learning; inverse-probability weights may improve bias while increasing finite-sample variance.
6. Do not conclude that reduced trust is inherently harmful. Selective feedback may reveal real weaknesses, and calibration refers to the right estimand.
