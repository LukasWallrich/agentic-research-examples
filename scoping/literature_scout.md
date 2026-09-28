# Literature scouting report: candidate JDM research questions answerable without new data

Date: 28 September 2026
Scouter: opencode (literature scout)
Output of: scoping task for `ai-jdm-paper4`

---

## 0. Scope and constraints

This report proposes research questions in judgment and decision-making (JDM) that are (a) plausibly understudied, (b) answerable by **secondary analysis of openly licensed data** or by a **falsifiable simulation**, and (c) not covered by the three sibling papers:

- **Paper 1** (`ai-jdm-paper`) — anchoring/proportionality, OpAQ meta-analysis. **Excluded: anchoring.**
- **Paper 2** (`ai-jdm-paper2`) — GJP forecasting, belief movement by horizon. **Excluded: probability forecasting, GJP, belief-movement.**
- **Paper 3** (`ai-jdm-paper3`) — selective feedback / comparative advisor evaluation. **Excluded: advisor verification, selective feedback, advice-weight learning.**

The sibling `novelty.md` files were read in full before scouting. Where a candidate is close to a sibling paper's statistical machinery (e.g. excess-movement statistics, model-simulation-on-frozen-design), that is noted.

## 1. Method

- Sources searched: OpenAlex API (`title.search`, `title_and_abstract.search`, `cites:`), Crossref REST API (`query.bibliographic`), and journal-level sweeps of recent works (2023–2026) in *Judgment and Decision Making*, *Journal of Behavioral Decision Making*, *Organizational Behavior and Human Decision Processes*, *Cognitive Psychology*, *Cognition*, *Psychological Science*, and *Management Science* (source IDs: `S179575189`, `S117214846`, `S64744539`, `S36783443`, `S88198767`, `S58854535`, `S33323087`).
- Recent-issue sweeps and gap checks were run to detect (i) existing meta-analyses, (ii) existing large-scale/open-data reanalyses, and (iii) the closest conceptual neighbours for each candidate.
- Every DOI in this report was checked against Crossref (`https://api.crossref.org/works/{DOI}`). Two non-Crossref identifiers are flagged explicitly.

**Caveats (read these as limits on all novelty claims).**

- OpenAlex `title_and_abstract.search` requires all query terms and is therefore very restrictive; a low count is **not** evidence that a topic is absent from the literature. Conversely a high count is often noise. Counts below are indicative only.
- Google Scholar could not be queried. Unpublished working papers, dissertations, and very recent (in-press) articles may be missed. Several relevant items turned out to be preprints (flagged).
- "First meta-analysis" claims are stated conservatively: "no published quantitative synthesis was located in Crossref/OpenAlex searches dated 28 Sep 2026", not "none exists".

---

## 2. Candidates

### C1. The sunk-cost effect: first general quantitative synthesis

**Question.** How large is the sunk-cost / escalation-of-commitment effect across the human literature, and which moderators (decision domain, real vs. hypothetical stakes, action/inaction framing, individual differences in cognitive ability) explain the heterogeneity?

**Why novel / closest work and its gap.** The sunk-cost effect is a 40-year-old textbook bias with ~600 works whose title mentions it, yet no general meta-analysis was located. The only quantitative synthesis is confined to **IT-project escalation** (Keil, Li, Mathur, & Tan, 2007, *Information Resources Management Journal*, https://doi.org/10.4018/irmj.2007070101), and the closest broad treatment is a **narrative** cross-species review (Arkes & Ayton's tradition; Ferreira et al., 2016, *JEAB*, https://doi.org/10.1002/jeab.202). Two subsequent critical pieces (Arkes & Blumer's original is 1985) raise the possibility that the effect is an artifact of framing or of measurement (e.g. "Evaluating the Sunk Cost Effect", 2021, *JEBO*, https://doi.org/10.1016/j.jebo.2021.03.029). Original anchor: Arkes & Blumer (1985), https://doi.org/10.1016/0749-5978(85)90049-4.

**Data / model needed.** Effect-size extraction from published studies (most are open-access or have OSF materials), plus any open raw datasets; where trial-level data are available, an individual-participant-data (IPD) two-stage meta-analysis with a multilevel model. A parallel **simulation** can show what design features (continuation vs. switching structure, scale of investment, whether "sunk" information is causally relevant) should moderate the effect, generating predictions that the meta-analysis then tests.

**Falsifiability.** Fully refutable. If the pooled effect is near zero after correcting for publication bias and selective reporting, or if moderators do not move it, the classic claim is weakened. The 2021 JEBO critique makes a null/small result a live possibility, which is exactly what makes the question worth answering.

**Feasibility risk.** Medium: requires manual effect-size coding rather than one clean open dataset. An IPD component depends on finding open raw data (many sunk-cost studies are now on OSF). This is the main candidate with a non-trivial extraction workload.

---

### C2. Overprecision (excessive precision in interval estimates): first quantitative synthesis

**Question.** How large is overprecision (confidence-interval hit rates below nominal coverage, and excessive narrowness), and how is it moderated by elicitation method (interval vs. distribution), incentives, item domain, and expertise?

**Why novel / closest work and gap.** Moore and Healy's (2008) *Psychological Review* paper, https://doi.org/10.1037/0033-295x.115.2.502, is a conceptual reconciliation and reported that overprecision is the most persistent of the three overconfidence forms, but it is not a meta-analysis. The comprehensive treatment remains a **book chapter** (Moore, Tenney, & Haran, 2015, "Overprecision in Judgment", https://doi.org/10.1002/9781118468333.ch6). Crossref/OpenAlex searches located **no quantitative meta-analysis** of overprecision; the closest recent items are preprints (e.g. "Overprecision in Estimates of Physical Constants", 2025, https://doi.org/10.31234/osf.io/26b5s_v1; "Conversational Principles in Cognitive Biases: the Case of Overprecision in Interval Estimation", 2026, https://doi.org/10.31234/osf.io/rsuzd_v1). At the same time, overconfidence is being actively revived as an individual-difference construct (see §3), so the field is hot but unsynthesised on this face.

**Data / model needed.** Coverage rates and interval widths are extractable or computable from published studies; many recent studies release raw interval responses. A simulation is useful for the known **scale-usage confound** (hit rate depends on nominal level and item difficulty) — showing which "remedies" (e.g. the 2010 "simple remedy", https://doi.org/10.1017/s1930297500001637) actually move the target quantity vs. only re-scale reports.

**Falsifiability.** Refutable: the pooled overprecision effect could shrink substantially once the hard–easy/scale-usage confound is modelled, or could be heterogeneous to the point of uninterpretability.

**Feasibility risk.** Medium: same extraction concern as C1, mitigated by the large volume of open interval-response data.

---

### C3. Bias versus noise in human judgment across domains

**Question.** Across decision domains, what fraction of judgment error is systematic bias versus unsystematic noise, and does aggregation reduce noise faster than bias (i.e. can groups be accurate while individuals are noisy-but-biased in different directions)?

**Why novel / closest work and gap.** The bias–noise decomposition was popularised by Kahneman, Sibony, and Sunstein (2021, *Noise*), but it has rarely been operationalised across multiple domains with a common model. The closest academic paper, "A unified explanation of variability and bias in human probability judgments" (2023, *JEP: General*, https://doi.org/10.1037/xge0001414), models variability and bias jointly but **only for probability judgments**, and it addresses the mean–variance signature rather than a cross-domain bias/noise share or an aggregation comparison.

**Data / model needed.** Open datasets containing **repeated judgments of the same objects** by multiple judges (e.g. essay/translation quality grading, image/radiology ratings, perceptual estimation crowds; the Confidence Database, https://doi.org/10.1038/s41562-019-0813-1, supplies many repeated-trial tasks). A hierarchical variance-decomposition model (judge × item variance components) computes the bias and noise shares; a simulation then derives when aggregation helps more via noise cancellation vs. bias reduction.

**Falsifiability.** Refutable: if noise is small relative to bias in most domains, aggregation's role is limited; if bias dominates and is shared, crowds will not fix it. Either outcome is informative.

**Feasibility risk.** High: requires locating several open repeated-judgment datasets that share enough structure to pool; data access (not modelling) is the bottleneck. GJP forecasting data must **not** be used (paper 2).

---

### C4. When does confidence-weighting harm collective accuracy? Boundary conditions

**Question.** Under what joint distribution of confidence and error does weighting judges by their confidence **hurt** crowd accuracy relative to simple averaging, and where do real crowds sit relative to those boundaries?

**Why novel / closest work and gap.** Confidence-weighting is widely recommended (e.g. "Wisdom of crowds benefits perceptual decision making across difficulty levels", 2021, *Scientific Reports*, https://doi.org/10.1038/s41598-020-80500-0), and recent work models correlated estimates (Aczél-type "Bayesian combination of correlated subjective probability estimates", 2026, *JDM*, https://doi.org/10.1017/jdm.2026.10035). What appears missing is a **formal sufficiency/boundary analysis**: weight by confidence improves accuracy only under conditions on the confidence–error covariance and on shared bias; with miscalibration or shared error, confidence-weighting can amplify a common bias. A 2025 preprint, "The Weighting Bias" (https://doi.org/10.2139/ssrn.5205685), is adjacent and worth monitoring.

**Data / model needed.** Derive the condition analytically, then run an agent-based simulation sweeping confidence–accuracy coupling, shared bias, and within-crowd correlation. Validate on open crowd datasets that include confidence (Confidence Database; perceptual crowds). This is closer to paper 3's mode (simulation with frozen predictions) but targets aggregation, not advisor verification — the estimand and the decision problem differ.

**Falsifiability.** Mathematical claims are provable/falsifiable directly; empirical claims are refutable if real crowds never fall in the harmful region, or if re-weighting with the derived correction never helps.

**Feasibility risk.** Low-to-medium: simulation is fully controllable; validation datasets exist but confidence data are less standard than accuracy data.

---

### C5. Are "risk preference" and "patience" cross-nationally comparable? Measurement invariance in the Global Preferences Survey

**Question.** Are the Global Preferences Survey (GPS) risk and time-preference modules measurement-invariant across countries and language groups, and how much of the headline cross-country variation survives a proper invariance model?

**Why novel / closest work and gap.** The GPS (Falk et al., 2018, *QJE*, https://doi.org/10.1093/qje/qjy013; replication data https://doi.org/10.7910/dvn/hh8dv4) is one of the most reused open preference datasets, yet OpenAlex searches of its citers located **no measurement-invariance / comparability test** of its modules; the closest is a 2025 working paper, "Measuring Economic Preferences with Surveys and Behavioral Experiments" (https://doi.org/10.2139/ssrn.5114896). Cross-national preference comparisons assume comparability; this is exactly the assumption a large validation literature (psychometrics, cross-cultural methods) has shown often fails.

**Data / model needed.** GPS respondent-level data (open for research via the Bonn portal / Dataverse) and multi-group confirmatory factor / item-response models (configural, metric, scalar invariance) across countries; a simulation quantifies how much attenuation/country-ranking reshuffling non-invariance induces in commonly reported GPS summaries (e.g. country means, correlations with income).

**Falsifiability.** Refutable: if scalar invariance holds, the existing GPS comparisons are validated; if it fails, published rankings must be qualified. Under an "approximate invariance" framing, results are quantitative rather than binary, but still falsifiable against pre-set thresholds.

**Feasibility risk.** Low: one clean open dataset and standard models. Risk is that GPS authors or citers have an unpublished invariance appendix.

---

### C6. Do models of intertemporal choice generalise across 100 open studies — and do process models beat choice-only models?

**Question.** Which computational models of intertemporal choice best predict out-of-sample choices when estimated across the newly released multi-study database, and does adding response-time (process) information systematically improve prediction over choice-only models?

**Why novel / closest work and gap.** A 2026 *Scientific Data* paper released **"A large-scale dataset of choice and response-time data in intertemporal choice"**: 100 studies, 11,852 subjects, 1,172,644 trials, with study-level methodological metadata (https://doi.org/10.1038/s41597-026-06947-4; preprint https://doi.org/10.31219/osf.io/nezgk_v2). The dataset paper explicitly frames its purpose as enabling new theory development, and no work has yet used it for **cross-study generalisation** of models. Existing model comparisons are within-study (e.g. Nagel et al., 2025, https://doi.org/10.3758/s13423-025-02709-2, compare attribute-wise vs. integrated models with a drift-diffusion framework in a single sample).

**Data / model needed.** The ITC database directly. Hierarchical Bayesian estimation of standard discounting models (exponential, hyperbolic, quasi-hyperbolic, attribute-wise) plus RT-enabled models (ddm/racing-diffusion), with study-level cross-validation and meta-regression on the provided metadata (incentivisation, procedure).

**Falsifiability.** Refutable: a single model might not generalise across studies (predicting failure of the "one best model" narrative), or process data might add nothing over choice data. Both are publishable outcomes.

**Feasibility risk.** Low-to-medium: the data are open and ready; the computational cost of hierarchical estimation over 1.17M trials is the main consideration. This is a strong, concrete candidate.

---

### C7. Is decision-strategy use domain-general or domain-specific?

**Question.** Do individuals who are best described by an "optimal" (expected-utility / Bayesian) strategy in risky choice also use optimal-style strategies in intertemporal choice, or is strategy use domain-specific and largely decoupled within person?

**Why novel / closest work and gap.** Model comparison in JDM is overwhelmingly **within-domain**. The closest cross-domain work compares ambiguity preferences and fits DDM across risk and time in a single large sample (Nagel et al., 2025, https://doi.org/10.3758/s13423-025-02709-2), and the largest risky-choice modelling effort (Peterson et al., 2021, *Science*, https://doi.org/10.1126/science.abe2629) is entirely within risky choice. No study appears to link individual-level strategy parameters **across** domains using large open datasets.

**Data / model needed.** CPC18 (Peterson et al., 2021; data/code released with the paper) for risky choice, and the ITC database (C6) for intertemporal choice. Estimate per-subject model parameters, then test cross-domain correlations and whether an "optimality" factor exists.

**Falsifiability.** Refutable and interesting either way: strong cross-domain correlations support a general decision-strategy factor; near-zero correlations support domain-specificity, challenging trait-like accounts of "decision competence".

**Feasibility risk.** Medium: CPC18 and the ITC database are separate samples (no within-person linkage), so the design is a between-sample comparison of parameter distributions unless a shared-sample open dataset is found. **Honest limitation:** some open datasets (e.g. Nagel et al., 2025) do contain both domains in one sample and should be checked for reuse rights first. Without within-person linkage this candidate is weaker; flag before committing.

---

### C8. Does the "inner crowd" gain depend on within-person error independence — or is it response noise?

**Question.** Does aggregating repeated judgments from a single person ("inner crowd") improve accuracy only when within-person errors are approximately independent, and how much of the reported gain is explained by response/scale noise rather than genuine "multiple perspectives"?

**Why novel / closest work and gap.** The inner crowd is claimed across several datasets (Herzog & Hertwig, 2017/2018, *Nature Human Behaviour*, https://doi.org/10.1038/s41562-017-0247-6; Herzog, von Helversen, & Hertwig, 2014, *TiCS*, https://doi.org/10.1016/j.tics.2014.06.009; for confidence judgments, 2020, *Decision*, https://doi.org/10.1037/dec0000119). The proposed mechanism is that repeated within-person samples are collectively more accurate because errors partly cancel. What appears missing is a direct **noise-structure test**: is the benefit driven by genuine independent samples, or by averaging out response noise/rounding/scale usage? A simulation can define the expected gain under independence vs. correlated errors, and existing open repeated-judgment datasets can test which regime real data resemble.

**Data / model needed.** Open datasets with repeated judgments by the same individuals (a subset of the Confidence Database; large calibration datasets with repeated items). Model within-person error covariance; simulate the inner-crowd gain as a function of that covariance.

**Falsifiability.** Refutable: if within-person errors are strongly correlated, the inner crowd should give little gain, contradicting some reports; if gains persist, that supports genuine sampling.

**Feasibility risk.** Medium: depends on repeated-judgment datasets with identifiable subjects; some are available, but pooling across tasks is non-trivial.

---

## 3. Directions checked and set aside (crowded or out of scope)

Recorded so the same ground is not re-trodden:

- **Anchoring, probability forecasting/GJP, advisor verification/selective feedback** — excluded by the brief (sibling papers).
- **Confidence Database reanalysis for domain-generality of metacognition** — crowded. The database (Rahnev et al., 2020, https://doi.org/10.1038/s41562-019-0813-1) already has a direct *meta-analysis of confidence–accuracy* (https://doi.org/10.3758/s13423-022-02063-7), plus domain-generality papers (https://doi.org/10.1177/17456916221075615; https://doi.org/10.1038/s44159-023-00245-1; https://doi.org/10.1037/xge0001197). Do not propose a generic Confidence Database question.
- **Overconfidence as an individual difference** — actively worked: *JDM* 2025 https://doi.org/10.1017/jdm.2025.11; *Cognition* 2026 https://doi.org/10.1016/j.cognition.2026.106665. (C2 targets overprecision *magnitude/moderation*, which is distinct, but cross-reference these.)
- **Choice overload, description–experience gap, identifiable victim effect, omission bias, status-quo bias (IS adoption), nudge/default effects** — meta-analyses already exist (choice overload: https://doi.org/10.1086/651235; description–experience: https://doi.org/10.1037/bul0000115; identifiable victim: https://doi.org/10.1080/15534510.2016.1216891; omission bias: https://doi.org/10.1177/01461672211042315; defaults: https://doi.org/10.1017/bpp.2018.43).
- **Serial dependence in perception** — heavily reviewed (https://doi.org/10.1146/annurev-psych-021523-104939), and a 2026 *Cognition* paper already covers serial effects in choice and confidence (https://doi.org/10.1016/j.cognition.2026.106643).
- **Hot-hand / gambler's-fallacy belief–reality correspondence** — attractive and plausibly under-tested as a **cross-domain** correspondence question (anchors: Gilovich et al., 1985, https://doi.org/10.1016/0010-0285(85)90010-6; Miller & Sanjurjo, 2018, https://doi.org/10.3982/ecta14943; MLB equilibrium, https://doi.org/10.1287/mnsc.2017.2804). Not promoted to a main candidate because it likely needs *belief* data across domains that may not exist openly (risk of requiring new data), but it is the strongest fallback if C7's within-person linkage cannot be secured.

---

## 4. Ranking summary

| # | Candidate | Open data / simulation | Novelty signal | Feasibility |
|---|---|---|---|---|
| C1 | Sunk-cost first general meta-analysis | Effect sizes + open raw (IPD) | High (no general meta located) | Medium (extraction) |
| C6 | ITC model generalisation across 100 studies | Open 1.17M-trial database | High (new dataset, unused) | Low–medium |
| C5 | GPS measurement invariance | Single clean open dataset | High (untested comparability) | Low |
| C4 | Confidence-weighting harm boundaries | Simulation + open crowd data | High (formal gap) | Low–medium |
| C2 | Overprecision first meta-analysis | Effect sizes + open raw | High (no meta located) | Medium |
| C8 | Inner-crowd noise-structure test | Open repeated-judgment data + simulation | Medium–high | Medium |
| C3 | Bias vs. noise across domains | Open repeated-judgment data | Medium–high | High (data access) |
| C7 | Cross-domain strategy consistency | CPC18 + ITC database | Medium (adjacent work exists) | Medium (no within-person link) |

## 5. Recommendation

The strongest combination of novelty and feasibility is **C1**, **C6**, **C5**, and **C4**: one clear "first-ever synthesis" (sunk cost), one large ready-made open dataset with a clean gap (intertemporal choice), one measurement-validity reanalysis (GPS), and one formal simulation with an empirical test (confidence-weighting). **C3** is the most scientifically interesting but the most data-constrained; **C7** must resolve the within-person linkage question before commitment.

## 6. Verification appendix

All DOIs below were resolved via Crossref on 28 September 2026 unless marked.

**Resolved (Crossref):** 10.1016/0749-5978(85)90049-4; 10.1016/j.jebo.2021.03.029; 10.1002/jeab.202; 10.1177/0956797617739368; 10.1016/0010-0285(85)90010-6; 10.3982/ecta14943; 10.1287/mnsc.2017.2804; 10.1038/s41562-017-0247-6; 10.1037/dec0000119; 10.1016/j.tics.2014.06.009; 10.1126/science.abe2629; 10.1093/qje/qjy013; 10.3758/s13423-025-02709-2; 10.1038/s41562-019-0813-1; 10.1037/0033-295x.115.2.502; 10.1002/9781118468333.ch6; 10.1017/s1930297500001637; 10.1037/xge0001414; 10.1177/2515245918810225; 10.1017/jdm.2026.10035; 10.1038/s41598-020-80500-0; 10.1017/jdm.2025.11; 10.1016/j.cognition.2026.106665; 10.1093/qje/qjaa043; 10.1038/s41597-026-06947-4; 10.1017/bpp.2018.43; 10.1086/651235; 10.1037/bul0000115; 10.1080/15534510.2016.1216891; 10.1177/01461672211042315; 10.1146/annurev-psych-021523-104939; 10.1016/j.cognition.2026.106643; 10.3758/s13423-022-02063-7; 10.1177/17456916221075615; 10.1038/s44159-023-00245-1; 10.1037/xge0001197; 10.4018/irmj.2007070101 (resolved via doi.org).

**Non-Crossref (flagged):** 10.7910/dvn/hh8dv4 (Harvard Dataverse / DataCite — resolves via doi.org, HTTP 202).
**Preprints (not peer-reviewed):** 10.31234/osf.io/26b5s_v1; 10.31234/osf.io/rsuzd_v1; 10.2139/ssrn.5205685; 10.2139/ssrn.5114896; 10.31219/osf.io/nezgk_v2.

## 7. Search provenance

Raw query outputs are retained in the session scratch directory. Key journal sweeps are in `jdm_recent.txt`, `jbdb_recent.txt`, `obhdp_recent.txt`, `cog_recent.txt`, `cogpsych_recent.txt`, `psci_recent.txt`. No hypothesis-bearing analysis of any candidate dataset was performed before writing this report.
