# Reference metadata and claim-support audit

Audit date: 28 September 2026. All thirteen manuscript references were queried directly through the Crossref works API. Eleven resolved. The two arXiv DOIs returned HTTP 404 because they are registered with DataCite; their titles, authors, dates, and primary URLs were verified against DataCite and the arXiv version-one primary pages. This is an explicit registry exception, not a claim that those references were verified by Crossref. Both are explicitly identified as preprints in the manuscript and bibliography.

Raw responses and the two Crossref failure-status records are in `scoping/reference_metadata/`. `manuscript/references.json` is CSL JSON rebuilt from those records with `python scoping/reference_metadata/build_csl.py`. These files concern references and published findings, not the study's analysis outcomes. The audit distinguishes verified source claims from the present study's interpretations. The current template contains sixteen citation occurrences, all covered by this audit and `citation_check.md`.

## Metadata verification

| CSL key | Authors and year | Exact title | DOI and registry result |
|---|---|---|---|
| `pescetelli2021` | Niccolò Pescetelli; Nicholas Yeung (2021) | The role of decision confidence in advice-taking and trust formation | [10.1037/xge0000960](https://doi.org/10.1037/xge0000960), Crossref 200 |
| `jaquiery2024` | Matt Jaquiery; Nick Yeung (2024) | Preferences for advisor agreement and accuracy | [10.1371/journal.pone.0311211](https://doi.org/10.1371/journal.pone.0311211), Crossref 200 |
| `fetchenhauer2010` | Detlef Fetchenhauer; David Dunning (2010) | Why So Cynical? Asymmetric Feedback Underlies Misguided Skepticism Regarding the Trustworthiness of Others | [10.1177/0956797609358586](https://doi.org/10.1177/0956797609358586), Crossref 200 |
| `denrell2005` | Jerker Denrell (2005) | Why Most People Disapprove of Me: Experience Sampling in Impression Formation | [10.1037/0033-295X.112.4.951](https://doi.org/10.1037/0033-295X.112.4.951), Crossref 200 |
| `honeycutt2020` | Donald R. Honeycutt; Mahsan Nourani; Eric D. Ragan (2020) | Soliciting Human-in-the-Loop User Feedback for Interactive Machine Learning Reduces User Trust and Impressions of Model Accuracy | [10.1609/hcomp.v8i1.7464](https://doi.org/10.1609/hcomp.v8i1.7464), Crossref 200 |
| `denrell2001` | Jerker Denrell; James G. March (2001) | Adaptation as Information Restriction: The Hot Stove Effect | [10.1287/orsc.12.5.523.10092](https://doi.org/10.1287/orsc.12.5.523.10092), Crossref 200 |
| `fok2024` | Raymond Fok; Daniel S. Weld (2024) | In search of verifiability: Explanations rarely enable complementary performance in AI-advised decision making | [10.1002/aaai.12182](https://doi.org/10.1002/aaai.12182), Crossref 200 |
| `gao2021` | Ruijiang Gao; Maytal Saar-Tsechansky; Maria De-Arteaga; Ligong Han; Min Kyung Lee; Matthew Lease (2021) | Human-AI Collaboration with Bandit Feedback | [10.24963/ijcai.2021/237](https://doi.org/10.24963/ijcai.2021/237), Crossref 200 |
| `zavattari2026` | Cesare Zavattari; Alessandro Tommasi; Giuseppe Prencipe (2026) | One Human, N Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence | [10.48550/arXiv.2607.28317](https://doi.org/10.48550/arXiv.2607.28317), Crossref 404; DataCite 200; arXiv v1 dated 30 July 2026 |
| `li2026` | ZhaoBin Li; Mark Steyvers (2026) | Learning to Trust: How Humans Mentally Recalibrate AI Confidence Signals | [10.48550/arXiv.2603.22634](https://doi.org/10.48550/arXiv.2603.22634), Crossref 404; DataCite 200; arXiv v1 dated 23 March 2026 |
| `einhorn1978` | Hillel J. Einhorn; Robin M. Hogarth (1978) | Confidence in judgment: Persistence of the illusion of validity | [10.1037/0033-295X.85.5.395](https://doi.org/10.1037/0033-295X.85.5.395), Crossref 200 |
| `mcnemar1947` | Quinn McNemar (1947) | Note on the sampling error of the difference between correlated proportions or percentages | [10.1007/BF02295996](https://doi.org/10.1007/BF02295996), Crossref 200 |
| `elwin2007` | Ebba Elwin; Peter Juslin; Henrik Olsson; Tommy Enkvist (2007) | Constructivist coding: Learning from selective feedback | [10.1111/j.1467-9280.2007.01856.x](https://doi.org/10.1111/j.1467-9280.2007.01856.x), Crossref 200 |

Metadata conventions: Pescetelli and Yeung appeared online in 2020, but Crossref identifies the journal issue as March 2021, volume 150(3), 507–526; the bibliography uses 2021. Crossref supplies “Nicholas” for this paper and “Nick” for Jaquiery and Yeung. Fetchenhauer and Dunning's subtitle is a separate Crossref field and has been included. Honeycutt and Ragan's middle initials and issue 1 are supplied by the primary publisher page because Crossref omits them. Fok and Weld's correct pagination is 317–332 in volume 45(3). Gao et al. appear on pages 1722–1728 of the Thirtieth IJCAI proceedings. Dollar signs around N in arXiv's title are TeX formatting and are removed from CSL display text. Minor case and hyphen typography differences do not change titles.

## Claim-to-source audit

### Pescetelli and Yeung (2021)

**Claim supported:** Confidence-weighted agreement can inform advisor evaluations without feedback, but correlated judgments undermine its validity.

**Source and location:** [Oxford primary accepted manuscript and bibliographic record](https://ora.ox.ac.uk/objects/uuid%3A5b00b576-d379-437d-bd71-91eeedd89f17), abstract and Experiment 2. The record explicitly describes feedback versus feedback-free comparisons and agent-based simulations.

**Boundary:** This already models confidence, dependence, and trust. It does not establish the consequences of revealing ground truth selectively on disagreements, or the proposed absolute-versus-paired display intervention. No source-based numerical estimate is carried into the manuscript from this audit.

### Jaquiery and Yeung (2024)

**Claim supported:** Advisor choice reflects both accuracy and agreement; objective feedback strengthens preference for accuracy in their experimental contrasts.

**Source and location:** [PLOS primary full text](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0311211), Abstract; Materials and methods, Task overview and Dates Task; Discussion. Methods describe feedback at the end of trials in the relevant conditions, rather than a manipulation selecting feedback by disagreement.

**Boundary:** Do not assert that accuracy lost to agreement on average in their no-feedback direct comparison. The paper instead reports wide individual differences. Our distinction concerns which completed cases generate labelled feedback.

### Fetchenhauer and Dunning (2010)

**Claim supported:** Giving feedback regardless of participants' trust decisions reduced their underestimation of others' trustworthiness relative to asymmetric or absent feedback.

**Source and location:** [Author-hosted primary article](https://sites.lsa.umich.edu/wp-content/uploads/sites/275/2015/11/fetchdunnps10.pdf), abstract and experiment; Crossref abstract independently confirms the comparison.

**Boundary:** The outcome is interpersonal reciprocity. This supports the broader relevance of selected experience, not the claim that the present classification model empirically explains their participants.

### Gao et al. (2021)

**Claim supported:** Human–AI policy learning under bandit feedback uses inverse-propensity weighting to address action selection in logged outcomes and to optimise routing between humans and an algorithm.

**Source and location:** [Primary proceedings PDF](https://www.ijcai.org/proceedings/2021/0237.pdf), §2 Counterfactual Policy Optimization (p. 1723); §3 Counterfactual Risk Minimization, equations 2–3, and Collaboration Objective, equation 4 (p. 1724). §1 explains that rewards are observed only for actions actually taken. §2 explicitly distinguishes the system from human–machine interaction.

**Boundary:** IPW and the general selective-outcome problem are established methods, not contributions of this study. Gao et al. learn policies from action-dependent rewards. The present model compares representations of selectively labelled classification cases, where one revealed ground-truth label evaluates both already-made predictions. It neither solves their general bandit problem nor estimates missing causal rewards.

### Zavattari et al. (2026), preprint

**Claim supported:** The preprint studies how to allocate a limited audit budget across an agent fleet with miscalibrated confidence and correlated errors, comparing audit policies by residual undetected errors.

**Source and location:** [Primary arXiv full text, v1](https://arxiv.org/html/2607.28317v1), §2 “Scoping: deferral allocates instances; we allocate audits”; §3 “Audit and risk” and “Policies”. §3 specifies that audits reveal error indicators with noise and describes posterior updates; thus it would be inaccurate to say their model contains no learning.

**Boundary:** The separation is the estimand and representation of the learner's evidence: absolute advisor accuracy versus paired comparative advantage from selected labelled cases. The present study must not claim to introduce confidence-based auditing, error dependence, audit-learning effects, or confidence-policy reversal in general.

### Denrell and March (2001)

**Claim supported:** Adaptive repetition can leave alternatives that initially appear unattractive undersampled and perpetuate inaccurate evaluations.

**Source and location:** [Primary publisher page](https://pubsonline.informs.org/doi/10.1287/orsc.12.5.523.10092), abstract; also saved Crossref abstract.

**Boundary:** Cite for the established mechanism of restricted experience. Do not present adaptive sampling bias as a new general mechanism established here.

### Denrell (2005)

**Claim supported:** Impression-dependent interaction can make early negative impressions more persistent by reducing further interaction.

**Source and location:** [Primary article DOI](https://doi.org/10.1037/0033-295X.112.4.951), abstract and model overview; author-uploaded article text supplies the model overview. Bibliographic identity was independently verified through Crossref.

**Boundary:** This is a foundation for the role of experience sampling, not direct evidence about AI verification displays.

### Honeycutt et al. (2020)

**Claim supported:** Providing feedback in a simulated object-detection interaction lowered reported trust and perceived accuracy, whether or not system accuracy improved.

**Source and location:** [Primary AAAI publisher page](https://ojs.aaai.org/index.php/HCOMP/article/view/7464), Abstract; saved Crossref abstract.

**Boundary:** This audit verified the published abstract, not every experimental design detail. Do not identify disagreement-selected feedback as the demonstrated cause of the effect.

### Fok and Weld (2024)

**Claim supported:** The authors argue that explanations support complementary decision performance insofar as they permit verification of predictions.

**Source and location:** [Primary publisher full text](https://onlinelibrary.wiley.com/doi/10.1002/aaai.12182), Abstract and Introduction; [author preprint](https://arxiv.org/abs/2305.07722).

**Boundary:** This is a theoretical argument, not a universal empirical demonstration that every useful explanation works only through verification. The present study assumes a successful verification channel and examines what its selected history permits a learner to infer.

### Li and Steyvers (2026), preprint

**Claim supported:** Participants can learn mappings between AI confidence and correctness across repeated labelled feedback, and the authors model adjustment of baseline trust and confidence sensitivity.

**Source and location:** [Primary arXiv full text, v1](https://arxiv.org/html/2603.22634v1), Experiment, Materials and Procedure; Cognitive Modeling, Linear-in-Log-Odds Calibration and Rescorla–Wagner Learning Rule. The latter explicitly states that correctness feedback follows every trial.

**Boundary:** Their learning model concerns calibration with trialwise feedback. The present selective-feedback model does not show that their estimated parameters generalise to missing labels, nor establish the proposed paired tracker as a human cognitive mechanism.

### Einhorn and Hogarth (1978), `einhorn1978`

**Verified metadata:** Hillel J. Einhorn and Robin M. Hogarth. *Confidence in judgment: Persistence of the illusion of validity.* *Psychological Review, 85*(5), 395–416. DOI [10.1037/0033-295X.85.5.395](https://doi.org/10.1037/0033-295X.85.5.395). Crossref HTTP 200; raw response saved.

**Narrow supported claim:** Learning about one's judgement depends on task structure, which action outcomes can be observed, and how feedback is coded and interpreted. The authors explain how action-contingent observation can obstruct disconfirmation and maintain confidence.

**Primary evidence:** [Published article PDF hosted by an academic lab](https://worthylab.org/wp-content/uploads/2020/12/einhorn_hogarth_1978.pdf), pp. 396–398, “Task Structure and Psychological Process”, including the hiring example where rejected candidates' outcomes are unavailable. This supports the foundational distinction between experience and useful evidence, not a claim that the present feedback-display intervention was tested in 1978.

### McNemar (1947), `mcnemar1947`

**Verified metadata:** Quinn McNemar. *Note on the sampling error of the difference between correlated proportions or percentages.* *Psychometrika, 12*(2), 153–157. DOI [10.1007/BF02295996](https://doi.org/10.1007/BF02295996). Crossref HTTP 200; raw response saved.

**Narrow supported claim:** Comparison of correlated proportions has a classical statistical foundation in McNemar's paper. The primary publisher abstract describes significance formulas and their chi-square connection.

**Primary evidence and access limit:** [Springer primary record](https://link.springer.com/article/10.1007/BF02295996), Abstract. The original full text was subscription restricted; this audit does not claim direct inspection of its discordant-cell formula. In the manuscript, cite as historical grounding for correlated-proportion comparisons, while deriving the agreement-zero identity directly. Do not say McNemar studied selective verification or advisor learning.


### Elwin et al. (2007), `elwin2007`

**Verified metadata:** Ebba Elwin, Peter Juslin, Henrik Olsson, and Tommy Enkvist. *Constructivist coding: Learning from selective feedback.* *Psychological Science, 18*(2), 105–110. DOI [10.1111/j.1467-9280.2007.01856.x](https://doi.org/10.1111/j.1467-9280.2007.01856.x). Crossref HTTP 200, with subtitle joined correctly; raw response saved.

**Primary evidence:** [Publisher abstract](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2007.01856.x) and full published PDF obtained through [Olsson's public author publication page](https://www.olssonresearch.com/publications), [linked PDF](https://drive.google.com/file/d/1KF_AnkW0QudPerzrK81kb6N9e10dc6bu/view). The article's “Selective Feedback” and coding subsections (pp. 105–106) distinguish recording observed outcomes from reconstructing missing outcomes through task knowledge. Method (p. 107) describes decision-contingent feedback in an investment task and approximately equates feedback counts by increasing training opportunities. Results, Coding (p. 108), and Discussion (p. 109) report no demonstrated performance impairment from selective feedback and better fit of constructivist than naive observed-outcome coding.

**Supported use:** Selective feedback need not impair decision performance, and how people represent missing and observed experience matters. The authors' task supplies direct empirical reason not to treat the present absolute-summary rule as a default human learner.

**Boundary:** Their experiment does not establish equivalence of selective and complete feedback across tasks or validate our paired source-comparison model. Our distinctive analysis concerns paired accuracy differences under disagreement sampling, not the broad insight that representation or task knowledge can preserve performance with selected feedback.

## Scope and conclusion

All thirteen references have verified bibliographic identity. Eleven resolve in Crossref; `zavattari2026` and `li2026` return Crossref HTTP 404 and resolve in DataCite. These two registry exceptions are retained explicitly. Primary evidence supports the limited claims attached to all sixteen citation occurrences. Metadata identity and substantive claim support were assessed separately.

The manuscript distinguishes existing empirical findings, established statistical ideas, its own model deductions, and an untested behavioural extension. McNemar is cited only for the historical comparison of correlated proportions because the original full text was unavailable. Honeycutt et al.'s narrow claim is supported by the primary abstract; no uninspected mechanism is attributed to it. Source statistics were read during literature review; no participant-level outcome file was downloaded or analysed for this audit.

CSL display titles use sentence case while preserving AI, LLM, and the mathematical N. Raw registry titles remain in the saved metadata.
