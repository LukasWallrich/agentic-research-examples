# Novelty / crowding check: "When does weighting by confidence hurt the crowd?"

Date of search: 28 September 2026
Scope: read-only literature check for the proposed paper (formal boundary + simulation + Confidence Database mega-analysis on confidence-weighted vs. equal-weighted aggregation of binary judgments).
Sources searched: Crossref REST API (66 targeted `query.bibliographic` queries, ~500 records screened) and Europe PMC. **OpenAlex was unavailable** (daily budget exhausted for every key on this network; `Insufficient budget ... resets at midnight UTC`). Semanticscholar API returned HTTP 429. **Google Scholar was not consulted** (per brief).

All DOIs below were resolved through `https://api.crossref.org/works/{DOI}` and title/authors/year/venue confirmed (metadata also used to fill volume/pages). Two preprints are marked.

---

## 0. Blunt verdict (read this first)

**The proposed paper is a synthesis plus an empirical base-rate estimate; it is not a new theoretical result.**

The atomic claims are already in the literature, in three separate mature literatures that do not cite each other much:

1. **Committee / social-choice theory** already answers "when do weighted votes beat equal votes, and how does correlated error change the answer." Shapley–Grofman (1984), Nitzan–Paroush (1982) and Ben-Yashar–Nitzan (1997) derive the optimal weighted-majority rule; Shapley–Grofman and Ladha (1995)/Kaniovski (2010) handle *correlated* votes; Baharad–Ben-Yashar (2009) handle *distorted* (miscalibrated) competence probabilities fed into the optimal rule. The proposed "boundary as a function of shared error" is the correlated-votes result wearing a confidence-motivated parametrisation.
2. **Forecast-combination theory** already shows that *estimated* optimal weights often lose to equal weights (the "forecast combination puzzle": Smith–Wallis 2009; Claeskens et al. 2016), and Huang, Broomell & Golman (2024) - the closest single paper to the proposed title - already gives a hypothesis-test algorithm for deciding when weighting individual judgments reliably beats the simple average "or just adds noise."
3. **Crowd / metacognition empirics** already compare confidence weighting against equal/majority weighting. Meyen et al. (2021) do exactly confidence-weighted majority voting vs. majority voting for binary decisions; Saha Roy et al. (2021) compare a confidence-weighted average against majority pooling; Berger et al. (2025, preprint) compare confidence-based adaptive aggregation against static aggregators across seven datasets; Shirasuna & Honda (2021, preprint) test whether low-confidence individuals harm group accuracy.

**What is genuinely potentially novel** (and worthwhile if framed honestly):

- (i) Writing the *CW − EW expected-accuracy gap for binary counting/majority aggregation* explicitly as a function of the **confidence–accuracy calibration curve, the within-item error correlation, and confidence dispersion** - a psychometric, estimable parametrisation rather than abstract "competence." I did not find this exact decomposition.
- (ii) A **pre-registered simulation mapping the boundary surface** in those psychometric coordinates.
- (iii) A **descriptive prevalence estimate**: "in what fraction of real multi-judge datasets does CW actually lose to EW, and what moderates it?" I found **no prior mega-analysis of the Confidence Database comparing aggregation rules**, so this is the strongest novel component *if* the data support it.

**The honest positioning:** a bridging + empirical-instantiation paper, not a new theorem. Its value is connecting metacognition calibration research to the committee-theorem literature and attaching a real base rate to a known theoretical possibility.

---

## 1. The five closest papers

### 1.1 Meyen, S., Sigg, D. M. B., von Luxburg, U., & Franz, V. H. (2021). Group decisions based on confidence weighted majority voting. *Cognitive Research: Principles and Implications*, 6(1).
DOI: https://doi.org/10.1186/s41235-021-00279-0 (verified; journal-article)

**What it did.** Directly compares **confidence-weighted majority voting (CWMV)** with **unweighted majority voting (MV)** for binary group decisions, using formal cognitive modelling and by fitting simulated group responses to real group responses. It states the standard assumption explicitly: CWMV is theoretically optimal *if* confidence ratings are independent and accurate. It finds simulated CWMV matches real-group accuracy while simulated MV underperforms, but that real groups weight votes *more equally than CWMV prescribes*.

**Precise addition of the proposal.** Meyen et al. treat CWMV's optimality as conditional and then ask whether real groups behave like CWMV. They do **not** derive the condition for when CWMV is *worse* than MV, do not model shared error or miscalibration as parameters, and do not sweep a boundary surface. The proposal's addition is the negative-space result: the explicit region where the "theoretically optimal" rule loses, as a function of calibration and error correlation.

### 1.2 Huang, S., Broomell, S. B., & Golman, R. (2024). A hypothesis test algorithm for determining when weighting individual judgments reliably improves collective accuracy or just adds noise. *Decision*, 11(1), 7–34.
DOI: https://doi.org/10.1037/dec0000187 (verified; journal-article)

**What it did.** Develops a general statistical test for whether there are enough observed judgments to reject the simple average in favour of a weighted average as a *reliably* more accurate aggregation method, and shows (by simulation) the test beats cross-validation. This is the closest existing paper to the proposed question "when does weighting beat equal weighting."

**Precise addition of the proposal.** Huang et al. frame the risk of weighting as **finite-sample estimation noise in the weights** ("just adds noise"), not as a systematic property of miscalibration, shared bias, or confidence dispersion. The proposal's addition is the *bias/miscalibration* route to CW harm and a decision-theoretic closed form, plus an empirical prevalence estimate rather than a per-dataset test.

### 1.3 Shapley, L., & Grofman, B. (1984). Optimizing group judgmental accuracy in the presence of interdependencies. *Public Choice*, 43(3), 329–343.
DOI: https://doi.org/10.1007/BF00118940 (verified; journal-article)

**What it did.** Derives optimal weights for a weighted-majority/group-accuracy rule when voters' judgments are **statistically interdependent (correlated)** rather than independent. It is the foundational formal treatment showing that the optimal weighting scheme depends on the error-correlation structure, and that naive (equal or competence-proportional) weighting is not generally optimal once errors are shared.

**Precise addition of the proposal.** The proposal's "formal boundary as a function of within-item error correlation" is closely related to this result. What is not in Shapley–Grofman: expressing the weights as *subjective confidence* (a noisy, possibly miscalibrated proxy), the confidence-dispersion term, and any empirical test of how often real crowds fall in the harmful region. **This paper is the single biggest threat to the "first formal boundary" claim.**

### 1.4 Baharad, E., & Ben-Yashar, R. (2009). The robustness of the optimal weighted majority rule to probability distortion. *Public Choice*, 139(1–2), 53–59.
DOI: https://doi.org/10.1007/s11127-008-9378-7 (verified; journal-article)

**What it did.** Analyzes how the **optimal weighted majority rule degrades when the probability (competence) inputs it relies on are distorted** - i.e., when the weights are built from miscalibrated signals instead of true competences. This is the closest existing formal treatment of the *miscalibration* leg of the proposed boundary.

**Precise addition of the proposal.** Baharad–Ben-Yashar study distortion of abstract decisional skills in the committee model. The proposal's addition is to instantiate the distorted signal as *confidence* in a binary crowd, to add the confidence-dispersion term, and to quantify how often the distorted-weighting rule falls behind equal weighting in real data. The *mechanism* (miscalibrated weights hurt the optimal rule) is already established here.

### 1.5 Jin, S., Verhaeghen, P., & Rahnev, D. (2022). Across-subject correlation between confidence and accuracy: A meta-analysis of the Confidence Database. *Psychonomic Bulletin & Review*, 29(4), 1405–1413.
DOI: https://doi.org/10.3758/s13423-022-02063-7 (verified; journal-article)

**What it did.** The existing large-scale meta-analysis of the **Confidence Database** (Rahnev et al., 2020, https://doi.org/10.1038/s41562-019-0813-1, verified). It pools the database to estimate the *across-subject* confidence–accuracy correlation and its moderators.

**Precise addition of the proposal.** Jin et al. estimate a calibration/validity correlation, **not an aggregation-rule comparison**. The proposal's addition is the first (to my search) use of the Confidence Database to compare CW vs. EW item-level aggregation and estimate the prevalence of the CW-harmful region. **But the proposal must not bill itself as "the first mega-analysis of the Confidence Database"** - that already exists, and the database was not designed for item-level crowd aggregation (see §5).

---

## 2. Coverage by the brief's five sub-questions

| Sub-question | Closest verified prior art | Status |
|---|---|---|
| (a) CW worse than EW (boundary, not demo) | Huang et al. 2024 (estimation-noise boundary); Shapley & Grofman 1984 (correlated-vote optimal weights) | **Partially anticipated.** No paper found that derives the CW<EW condition jointly in (calibration, error correlation, dispersion). |
| (b) Miscalibration + correlated/shared error | Baharad & Ben-Yashar 2009 (probability distortion in optimal weighted majority); Trick et al. 2023, 2026 (Bayesian fusion *with* correlation); Ladha 1995; Kaniovski 2010 | **Largely anticipated** as separate results; the confidence-specific joint form is the gap. |
| (c) Empirical CW vs. simple averaging in crowds | Meyen et al. 2021; Saha Roy et al. 2021; Berger et al. 2025 (preprint, 7 datasets); Keuschnigg & Ganser 2017 (voting vs. averaging simulation); Larrick & Soll 2006; Soll & Larrick 2009; Mannes et al. 2014; Budescu & Chen 2015; Kurvers et al. 2016; Palley & Soll 2019 | **Demonstrations already numerous.** The gap is the *boundary + base rate*, not the demonstration. |
| (d) Mathematics of weighted majority with informative weights | Nitzan & Paroush 1982; Shapley & Grofman 1984; Ben-Yashar & Nitzan 1997; Berend & Paroush 1998; Grofman 1978; Smith & Wallis 2009; Claeskens et al. 2016 | **Fully covered territory.** Not novel. |
| (e) Prior Confidence Database aggregation mega-analysis | Jin et al. 2022 (different question: across-subject confidence–accuracy); Rahnev et al. 2020 (the database itself) | **No aggregation-rule mega-analysis found.** This leg is the most novel. |

### Second-tier prior art worth citing (all verified)

- **Nitzan, S., & Paroush, J. (1982).** Optimal Decision Rules in Uncertain Dichotomous Choice Situations. *International Economic Review*, 23(2), 289. https://doi.org/10.2307/2526438 — optimal weighted majority; weights ∝ competence log-odds.
- **Ben-Yashar, R. C., & Nitzan, S. I. (1997).** The Optimal Decision Rule for Fixed-Size Committees in Dichotomous Choice Situations: The General Result. *International Economic Review*, 38(1), 175. https://doi.org/10.2307/2527413
- **Berend, D., & Paroush, J. (1998).** When is Condorcet's Jury Theorem valid? *Social Choice and Welfare*, 15(4), 481–488. https://doi.org/10.1007/s003550050118
- **Ladha, K. K. (1995).** Information pooling through majority-rule voting: Condorcet's jury theorem with correlated votes. *Journal of Economic Behavior & Organization*, 26(3), 353–372. https://doi.org/10.1016/0167-2681(94)00068-p
- **Kaniovski, S. (2010).** Aggregation of correlated votes and Condorcet's Jury Theorem. *Theory and Decision*, 69(3), 453–468. https://doi.org/10.1007/s11238-008-9120-4
- **Grofman, B. (1978).** Judgmental competence of individuals and groups in a dichotomous choice situation. *The Journal of Mathematical Sociology*, 6(1), 47–60. https://doi.org/10.1080/0022250X.1978.9989880
- **Hogarth, R. M. (1978).** A note on aggregating opinions. *Organizational Behavior and Human Performance*, 21(1), 40–46. https://doi.org/10.1016/0030-5073(78)90037-5 — optimal number of judges and weights depend on inter-judge error correlation; more judges help only up to a point.
- **Einhorn, H. J., Hogarth, R. M., & Klempner, E. (1977).** Quality of group judgment. *Psychological Bulletin*, 84(1), 158–172. https://doi.org/10.1037/0033-2909.84.1.158 — group-judgment quality as a function of individual validity and inter-judge correlation.
- **Smith, J., & Wallis, K. F. (2009).** A Simple Explanation of the Forecast Combination Puzzle. *Oxford Bulletin of Economics and Statistics*, 71(3), 331–355. https://doi.org/10.1111/j.1468-0084.2008.00541.x
- **Claeskens, G., Magnus, J. R., Vasnev, A. L., & Wang, W. (2016).** The forecast combination puzzle: A simple theoretical explanation. *International Journal of Forecasting*, 32(3), 754–762. https://doi.org/10.1016/j.ijforecast.2015.12.005
- **Trick, S., Rothkopf, C. A., & Jäkel, F. (2023).** A normative model for Bayesian combination of subjective probability estimates. *Judgment and Decision Making*, 18. https://doi.org/10.1017/jdm.2023.39
- **Trick, S., Jäkel, F., & Rothkopf, C. A. (2026).** Bayesian combination of correlated subjective probability estimates. *Judgment and Decision Making*, 21. https://doi.org/10.1017/jdm.2026.10035 — explicitly models the correlation between forecasters' estimates and shows ignoring it is suboptimal.
- **Larrick, R. P., & Soll, J. B. (2006).** Intuitions About Combining Opinions: Misappreciation of the Averaging Principle. *Management Science*, 52(1), 111–127. https://doi.org/10.1287/mnsc.1050.0459
- **Soll, J. B., & Larrick, R. P. (2009).** Strategies for revising judgment. *Journal of Experimental Psychology: LMC*, 35(3), 780–805. https://doi.org/10.1037/a0015145
- **Mannes, A. E., Soll, J. B., & Larrick, R. P. (2014).** The wisdom of select crowds. *Journal of Personality and Social Psychology*, 107(2), 276–299. https://doi.org/10.1037/a0036677
- **Budescu, D. V., & Chen, E. (2015).** Identifying Expertise to Extract the Wisdom of Crowds. *Management Science*, 61(2), 267–280. https://doi.org/10.1287/mnsc.2014.1909
- **Kurvers, R. H. J. M., et al. (2016).** Boosting medical diagnostics by pooling independent judgments. *PNAS*, 113(31), 8777–8782. https://doi.org/10.1073/pnas.1601827113 — rests on the independence assumption the proposal interrogates.
- **Palley, A. B., & Soll, J. B. (2019).** Extracting the Wisdom of Crowds When Information Is Shared. *Management Science*. https://doi.org/10.1287/mnsc.2018.3047
- **Keuschnigg, M., & Ganser, C. (2017).** Crowd Wisdom Relies on Agents' Ability in Small Groups with a Voting Aggregation Rule. *Management Science*, 63(3), 818–828. https://doi.org/10.1287/mnsc.2015.2364 — agent-based simulation of voting vs. averaging aggregation.
- **Saha Roy, T., Mazumder, S., & Das, K. (2021).** Wisdom of crowds benefits perceptual decision making across difficulty levels. *Scientific Reports*, 11(1). https://doi.org/10.1038/s41598-020-80500-0 — confidence/neural weighted average beats majority pooling.
- **Prelec, D., Seung, H. S., & McCoy, J. (2017).** A solution to the single-question crowd wisdom problem. *Nature*, 541, 532–535. https://doi.org/10.1038/nature21054
- **Bahrami, B., et al. (2010).** Optimally Interacting Minds. *Science*, 329(5995), 1081–1085. https://doi.org/10.1126/science.1185718

### Preprints (not peer-reviewed)

- **Berger, J., Moussaïd, M., Hertwig, R., Herzog, S. M., & Kurvers, R. (2025).** *Making the wisdom of crowds efficient — with confidence.* Preprint. https://doi.org/10.31234/osf.io/j9t6p_v2 — develops three confidence-based adaptive crowd-stopping rules, tested against static aggregators in seven datasets across four domains (cancer diagnosis, false-news classification, criminology, forecasting). Closest empirical neighbour on the *mechanism* (use confidence to beat static aggregation); it optimizes *efficiency*, not the CW-vs-EW boundary.
- **Shirasuna, M., & Honda, H. (2021).** *Do low-confidence individuals decrease group judgments' accuracy?* Preprint. https://doi.org/10.31234/osf.io/xnk4p — behavioural experiments + simulation; low-confidence individuals generally do *not* hurt group accuracy in binary choice. Directly relevant to the "confidence weighting is unnecessary/harmful" intuition.

---

## 3. What is already known (the paper must not claim it)

1. **That weighting by a signal can hurt aggregation.** Established. See the forecast-combination puzzle (Smith–Wallis 2009; Claeskens et al. 2016) and Huang et al. (2024).
2. **That correlated/shared judgment errors bound the gains from aggregation and change optimal weights.** Established (Shapley–Grofman 1984; Ladha 1995; Kaniovski 2010; Hogarth 1978; Einhorn et al. 1977; Palley & Soll 2019).
3. **That miscalibrated/distorted competence inputs degrade the optimal weighted-majority rule.** Established (Baharad & Ben-Yashar 2009).
4. **The mathematics of weighted majority with informative weights.** Established and closed (Nitzan–Paroush 1982; Ben-Yashar–Nitzan 1997; Berend–Paroush 1998; Grofman 1978).
5. **That confidence-weighted aggregation empirically beats majority/equal weighting in real crowds.** Established (Meyen et al. 2021; Saha Roy et al. 2021; Berger et al. 2025 preprint), with the caveat that real groups weight more equally than CWMV prescribes (Meyen et al.).
6. **That the Confidence Database has already been meta-analysed.** Established (Jin et al. 2022).

## 4. What must NOT be claimed

- "We are the first to show that confidence weighting can be worse than equal weighting." False; the general result is in committee and forecast-combination theory.
- "We are the first to derive optimal/weighted aggregation under correlated errors." False; see Shapley–Grofman (1984) and the correlated-votes literature.
- "We are the first to examine miscalibration in weighted aggregation." False; Baharad–Ben-Yashar (2009).
- "This is the first empirical comparison of confidence weighting vs. averaging." False; Meyen et al. (2021), Saha Roy et al. (2021), Berger et al. (2025 preprint).
- "This is the first mega-analysis of the Confidence Database." False; Jin et al. (2022). Frame the database as *reused*, and cite Jin et al.
- Treating the CW-vs-MV optimality claim as new. Meyen et al. (2021) already state it and stress its independence/accuracy preconditions.

## 5. Prior art that could make each leg non-novel, and one feasibility risk

- **Formal boundary leg.** Non-novel in its ingredients. The correlated-votes optimal-weights result (Shapley–Grofman 1984) plus the probability-distortion robustness result (Baharad–Ben-Yashar 2009) jointly cover the proposed boundary. Novelty rests entirely on the *specific confidence parametrisation* (calibration curve + error correlation + dispersion) and on stating it for binary counting-style aggregation as a clean closed form.
- **Empirical mega-analysis leg.** No prior aggregation-rule mega-analysis of the Confidence Database was found, so this leg is the most defensible. **Feasibility risk:** the Confidence Database is a *single-subject* confidence corpus (Rahnev et al. 2020). Most studies use independently sampled stimuli per participant, so "the same item judged by multiple people" - required for a crowd-aggregation estimand - may hold in only a subset of datasets. The proposal's "~97 datasets" claim should be verified against the actual OSF files before commitment; if item-level overlap is thin, the mega-analysis is fragile and the paper leans almost entirely on the formal/simulation contribution (which is the less novel part). Jin et al. (2022) sidestepped this by using subject-level confidence–accuracy correlations.

## 6. Verified reference list

Every DOI above was resolved via Crossref on 28 September 2026 and matched on title, authors and year. Non-peer-reviewed items are marked *(preprint)*. The Confidence Database data descriptor is verified as Rahnev, D., et al. (2020), *Nature Human Behaviour*, 4(3), 317–325, https://doi.org/10.1038/s41562-019-0813-1 (CC0; OSF https://osf.io/s46pr/).

Search-provenance raw files: `scratch_crossref_cw.json`, `scratch_crossref_cw2.json`, `scratch_crossref_cw3.json`, `scratch_doi_verify.json` in this directory.