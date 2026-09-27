# Simulation-study designs for the JDM paper: scoping report

## How the facts were checked
- **DOIs.** Every article DOI cited here (56) was checked against `https://api.crossref.org/works/<DOI>`: first author and year match. One arXiv paper has no Crossref DOI and is cited by its arXiv ID. Dataset DOIs (Dataverse, Zenodo, figshare) were resolved through their repository APIs.
- **Licences.** Each licence was read from the repository record through the OSF, Dataverse, Zenodo, figshare or GitHub API. I re-checked every licence the top designs depend on myself. No data file was opened; only metadata, READMEs and codebooks were read (decision log #3).
- **Blinding incident.** A Europe PMC call by the licence subagent started downloading the supplementary zip of Jayles et al. 2017 (PMC5703270). The subagent stopped the download within 2 minutes and deleted the partial file unopened. Nothing in it was listed or read. These are the Jayles 2017 data, which are a published reproduction target in design 3 only, not a test dataset.
- **Numbers.** Each quantitative finding gives its source. I read it in the paper text (PDF or PMC) unless it is marked "abstract" or "UNVERIFIED".

## Scores and ranking
Each axis runs from 1 (weak) to 3 (strong). Feasibility is capped at 1 when no openly licensed dataset exists. Rows are sorted by product.

| # | Design | Novelty | Falsifiability | Feasibility | Product |
|---|---|---|---|---|---|
| 1 | Anchoring: how the anchoring index changes with anchor spread (4 process models) | 3 | 3 | 2 | **18** |
| 2 | Hard–easy effect from noise alone, in general-knowledge quizzes | 2 | 3 | 3 | **18** |
| 3 | Social-influence revision model with frozen parameters, lab to lab (field arm as an extension) | 2 | 3 | 2 | **12** |
| 4 | Bayesian sampler as an explanation of extremizing in forecasting | 3 | 2 | 2 | 12 |
| 6 | Inner crowd as an autocorrelated sampler over time | 3 | 3 | 1 | 9 |
| 7 | Heterogeneity across sites created by the measurement scale (Many Labs) | 1 | 3 | 3 | 9 |
| 8 | Small-sample learning vs attitude change as causes of feedback effects in risky choice | 1 | 3 | 3 | 9 |
| 5 | Advice taking: generative model of the three-peaked weight-of-advice distribution | 2 | 2 | 2 | 8 |

**Top 3: designs 1, 2 and 3.** Design 3 beats design 4 on falsifiability. The aDDM (attention-weighted drift diffusion) is not proposed: it is heavily modelled already. Thomas et al. 2019 (https://doi.org/10.1038/s41562-019-0584-8) fitted a gaze-bias model (GLAM) to four open datasets, which are on GitHub under an MIT licence.

---

## 1. Anchoring: how the anchoring index changes with anchor spread (Open Anchoring Quest)

**Models.** One simulator runs four process models of numeric estimation on the log scale. Item belief is Normal(μᵢ, σᵢ).
- **M1: resource-rational adjustment** (Lieder et al. 2018, https://doi.org/10.3758/s13423-017-1286-8). A Metropolis–Hastings chain (a stepwise random-walk sampler) starts at the anchor and runs t steps of size s·σᵢ.
- **M2: Anchor Integration Model** (Turner & Schley 2016, https://doi.org/10.1016/j.cogpsych.2016.07.003). The estimate is a weighted mix of the anchor and a belief sample, with fixed weight w.
- **M3: adjust until the plausible range is reached** (Epley & Gilovich 2006, https://doi.org/10.1111/j.1467-9280.2006.01704.x). Adjustment stops at μᵢ ± kσᵢ.
- **M4: plausibility-gated selective accessibility** (Mussweiler & Strack 1999, https://doi.org/10.1006/jesp.1998.1364; Wegener et al. 2001, https://doi.org/10.1006/jesp.2000.1431). An anchor loses its effect when it falls outside the plausible range.

**Fixed vs fitted.**
- Fixed before OpAQ is loaded: s and t for M1, w for M2, k for M3. Each is calibrated to Jacowitz & Kahneman's (1995) anchoring index.
- One AI value does not pin down s and t: my scratch runs with (s, t) = (.5, 5), (.3, 10) and (1, 3) give different AI at z = 1, but in all of them AI rises with spread. The preregistration therefore commits M1 to the *sign* of the AI–spread slope, not to a numeric band. Optionally, (s, t) can be constrained further by fitting Lieder's 15 item-level Jacowitz & Kahneman values.
- Fitted per item on OpAQ: μᵢ, from `true_value` and the anchored data. σᵢ is taken from a proxy, the pooled within-condition SD. OpAQ has no unanchored SD per item, so the simulator computes the same proxy on its own simulated data, which keeps the comparison fair.

**Findings the models must reproduce (bands set before running).**
1. **Anchoring index (AI).** Jacowitz & Kahneman 1995 (https://doi.org/10.1177/01461672952111004) used anchors at the 15th and 85th percentiles and found a mean AI of 48.48%. Lieder's model gave 53.22% and an item-level correlation of r(13) = .62. These values are from the Lieder et al. preprint text. This is the calibration target. The test is the item-level correlation: it must be r ≥ .40.
2. **Anchor distance.** Anchoring grows with anchor distance: b = 0.040, k = 312, p < .001, "nonlinear but positive", with no inverted U (Röseler & Schütz 2022 meta-analysis of OpAQ, https://doi.org/10.31234/osf.io/wf2tn; pooled g = 0.689 [0.589, 0.789]). A model must predict a positive slope of g on distance.
3. **Random anchors.** Explicitly random anchors have much smaller effects than fixed anchors (same source; also Schley & Weingarten 2026, https://doi.org/10.1287/mnsc.2023.03238). M1 as published starts at any anchor and so predicts full-sized effects. **M1 fails this target unless the start point depends on how informative the anchor is. This is stated in advance.**
4. **Time pressure (contested).** M1 predicts more anchoring under time pressure. Lieder et al. (https://doi.org/10.3758/s13423-017-1288-6) found that adjustment falls as time cost rises. Röseler et al. 2023 (https://doi.org/10.31234/osf.io/jztk2) did not find the time effect in 4 studies (N = 898). The paper must report this conflict alongside the new test.

**New prediction.** The measure is AI = (median log estimate under the high anchor − median under the low anchor) / (log a_H − log a_L), plotted against anchor spread (log a_H − log a_L) / σ̂ᵢ. The four models predict different shapes:
- **M1: AI rises with spread.** Adjustment levels off at a fixed amount, so AI = 1 − adjustment/distance, which approaches 1. My scratch simulation (s = .5σ, t = 5) gave AI = .59 at z = 1, .79 at z = 4 and .88 at z = 8.
- **M2: AI stays flat at w.**
- **M3: AI falls**, roughly as k/distance beyond the plausible range.
- **M4: AI falls steeply** and can turn negative.

The existing evidence already goes against M3 and M4. The positive g–distance slope in target 2 contradicts M3, which predicts g flat once anchors pass the plausible range, and M4, which predicts g falling. So the open contrast is M1 against M2. Both predict a rising g, so g cannot separate them. The AI–spread slope can: it rises under M1 and stays flat under M2. M3 and M4 stay in the simulator as checks.

**Refutation rule.** Fit a multilevel regression of item AI on log spread, with random effects for study and a moderator for anchor type. A slope whose 95% CI lies entirely ≤ 0 refutes M1. A slope whose CI lies entirely > 0 refutes M2–M4. A CI that includes 0 with a half-width below 0.05 supports M2. The simulator converts these slopes into predicted intervals for each model before any data are loaded.

**Data.** Open Anchoring Quest, OSF https://osf.io/ygnvb/. Licence: **CC-BY 4.0** on the node that holds `OPAQ_JOPD.csv`; the components sz5b9, 4t5mu and gnr2x are also CC-BY 4.0. Contents: 96 studies, 21,359 participants, 412 items (355 with true values), 88,914 trials, an anchor-type code, and a high/low anchor flag (Röseler et al. 2022, https://doi.org/10.5334/jopd.67).
- **Optional site-level arm:** Many Labs 1 anchoring, OSF wx7ck, **CC0**. Site-level uncertainty should predict site-level anchoring. Reported anchoring SMDs are 1.21–2.53, τ .15–.69, I² 40–91% (Olsson-Collentine et al. 2020, https://doi.org/10.1037/bul0000294, table read from postprint). OpAQ most likely already includes the Many Labs 1 anchoring data, so this arm tests a different prediction on overlapping data. It is not an independent replication.

**Closest papers and what is left.**
- Lieder et al. 2018 (https://doi.org/10.3758/s13423-017-1286-8, https://doi.org/10.3758/s13423-017-1288-6) simulated classic small studies qualitatively.
- Röseler & Schütz 2022 tested distance at the level of study effect sizes.
- Schley & Weingarten 2026 coded extremity as binary and found no effect.
- Turner & Schley 2016 fitted their own experiments.
- No process model has been fitted to OpAQ. No study has compared models on the AI–spread shape.

**Risks.**
- σ̂ is a proxy. The simulator handles this by computing the same proxy on simulated data.
- Most items have exactly two anchors, so the test works across items.
- Knowing how many items have usefully asymmetric or extreme spreads would mean reading the data. The preregistration should therefore state a minimum item count (for example ≥ 60 items with spread > 3σ̂). If fewer items qualify, the test is declared uninformative.

**Effort.** R. 12–18 days: simulator 3, OpAQ cleaning 4–5, analysis and preregistration 5–10.

---

## 2. Hard–easy effect from noise alone, in general-knowledge quizzes

**Model.** An observer with no bias answers 4-option knowledge items. Evidence for each option is a Thurstonian draw (a normal random value per option); item difficulty and person skill set the evidence strength. Confidence is the ideal-observer probability of being correct, plus Gaussian reporting noise σ_r, rounded and clipped to the 25–100 scale.
- **Fitted:** item difficulties, person skill, and σ_r, estimated from choices and confidence variance.
- **Fixed:** the bias parameter, at 0. This rules out any over- or underconfidence that is built into the mind.

**Findings to reproduce.**
- Hard–easy effect (Lichtenstein & Fischhoff 1977, https://doi.org/10.1016/0030-5073(77)90001-0). Magnitudes UNVERIFIED; to be taken from the paper.
- The hard–easy effect nearly disappears once scale-end effects and linear dependency are controlled, while selected and representative item sets still differ (Juslin, Winman & Olsson 2000, https://doi.org/10.1037/0033-295x.107.2.384, abstract).
- The error model of over- and underconfidence (Erev, Wallsten & Budescu 1994, https://doi.org/10.1037/0033-295x.101.3.519).
- The same forecasters were overconfident by 3% in the tournament, and by 1% after teams and training (Moore et al. 2017, https://doi.org/10.1287/mnsc.2016.2525, abstract). This is a band check on the forecasting side.

**New prediction.** Juslin et al. 2000 and Erev et al. 1994 already treat the hard–easy *slope* as largely artefact. The open question for a selected item set is the *overall* level: does any over- or underconfidence remain once noise, scale ends (floor at 25 for 4 options) and linear dependency are simulated out? The GJP knowledge items were written by the researchers, so they are a selected set. The ecological (item-selection) account predicts overall overconfidence beyond noise for such items. The noise-only model predicts none. The published targets come mostly from 2-option tasks (floor at 50); the simulator must handle the 25 floor explicitly.

**Refutation rule.**
- **Main test:** overall bias, meaning mean confidence minus accuracy across items, compared with the 95% predictive interval of the noise-only model. That interval is simulated with the fitted σ_r and the real design (same items and sample sizes). A bias outside the interval refutes the noise-only model.
- **Secondary test:** the slope of item-level (confidence − accuracy) on item accuracy, compared with the same interval.
- **Precision gate:** 47 items is few. Before the preregistration is filed, the simulator must show that the noise-only interval excludes a 5-percentage-point bias. If it does not, falsifiability drops to 2, and the Confidence Database arm becomes necessary, not optional.

**Data.**
- Good Judgment Project (GJP), Harvard Dataverse https://doi.org/10.7910/DVN/BPCDH5, **CC0 1.0**. The file `all_individual_differences` holds two quizzes with a "probability that you are correct" rating on 25–100 for each item: Cluster Political Knowledge (32 items) and General Political Knowledge (15 items). Source: the README on Dataverse.
- Replication arm: the subset of the Confidence Database with probability-scale confidence and several difficulty levels. OSF s46pr, **CC0**. It holds 145 datasets, more than 8,700 participants and about 4M trials (Rahnev et al. 2020, https://doi.org/10.1038/s41562-019-0813-1, abstract). The usable subset may be small. It can be counted from dataset descriptions without opening data.

**Closest papers.**
- Guggenmos 2022 (https://doi.org/10.7554/elife.75420): a bias-free noisy observer, validated on one dataset.
- Merkle 2009 (https://doi.org/10.3758/pbr.16.1.204); Suantak et al. 1996 (https://doi.org/10.1006/obhd.1996.0074); Juslin et al. 2000.
- Nobody has tested a hard–easy effect predicted from fitted noise across datasets, or used the GJP quizzes for calibration research. I did not find a GJP quiz calibration paper, but I did not search this point exhaustively.

**Effort.** R. 8–12 days.

---

## 3. Social-influence revision model with frozen parameters, lab to lab

**Model.**
- Agents revise in log space: x₂ = x₁ + S·(social − x₁).
- S is a mixture: a spike at S = 0 (keep), a spike at S = 1 (adopt), and a Gaussian part in between (compromise).
- The probabilities of the three parts depend on the distance |D| between own estimate and social information, and on its direction: ⟨S⟩ = α + β|D| (Jayles et al. 2017) plus an asymmetry term for social information above vs below one's own estimate (Kao et al. 2018).
- **Fitted once** on the Kao and Jayles figshare datasets. **Then frozen.**

**Findings to reproduce.**
- **Jayles et al. 2017** (https://doi.org/10.1073/pnas.1703695114, PMC text): median S = 0.34, spikes at S = 0 and S = 1, and the probability of keeping one's estimate falls with |D|.
- **Becker et al. 2017** (https://doi.org/10.1073/pnas.1615978114, via a WebFetch summary of the PMC text; the Becker 2017 data themselves have no licence):
  - In decentralized networks, median error fell 12% (0.76 → 0.67 SD) and mean error fell 10%.
  - Revision coefficient (correlation of initial error with revision size) ρ = .41.
  - Across tasks, revision coefficient vs improvement ρ = −.71 (n = 59 tasks).
- **Lorenz et al. 2011** (https://doi.org/10.1073/pnas.1008636108): diversity fell while collective error barely changed; the wisdom-of-crowd indicator fell by about 1 unit. N = 144; 6 questions; 5 rounds.
- **Mellers et al. 2014** (https://doi.org/10.1177/0956797614524255, PDF): in GJP year 1, forecasters who saw the crowd's distribution ("crowd-belief" forecasters) beat independent forecasters, t(1120) = 5.92.

**New prediction and refutation rule.**
- **Main test (lab to lab).** Given each group's observed initial estimates and its network, the frozen model predicts the per-question change in mean and median error for the static-network conditions of Becker et al. 2019. Refutation: the correlation between predicted and observed change is below .30, or the sign matches on fewer than 60% of questions.
- **Almaatouq et al. 2020 is only a partial target.** Its networks rewire and give performance feedback, and a revision rule based on distance cannot predict that without a model of who connects to whom. Use only rounds or conditions with static networks, if the codebook shows any.
- **Field arm (extension, not part of the main test).** In GJP year 1, crowd-belief forecasters (conditions 2a–2c) were randomised against independent forecasters (1a–1c). They made about 1.3 forecasts per question (Mellers et al. 2014), so the crowd display mostly shaped the *first* forecast, and the revision rule has little to revise. This arm needs a different model, in which the displayed distribution acts as an anchor on the first forecast (close to M2 in design 1). Its targets would be spread per question-day and the difference in Brier score between conditions.

**Data (licences checked by me).**
- Kao et al. 2018: figshare 10.6084/m9.figshare.6120683 and sibling records, **CC BY 4.0**.
- Jayles, Sire & Kurvers 2021: figshare 10.6084/m9.figshare.12529571, **CC BY 4.0**. Further Jayles figshare sets were reported as CC BY 4.0 by the subagent: 12472034, 12522527, 11903421.
- Almaatouq et al. 2020: Dataverse 10.7910/DVN/EOYZKH, **CC0**.
- Becker et al. 2019: Dataverse 10.7910/DVN/OE6UMR, **CC0**.
- GJP: Dataverse 10.7910/DVN/BPCDH5, **CC0**.
- **Excluded (no licence):** Becker 2017 and Lorenz 2011, which exist only as PNAS supplementary files. Jayles 2017 has no deposit at all. These serve as published reproduction targets only.

**Closest papers.**
- Almaatouq et al. 2022 (https://doi.org/10.1038/s41598-022-20551-7) pooled 4 datasets (N = 2,885) in a weighted-averaging (DeGroot-type) framework, descriptively.
- Pilgrim & Becker 2024 (arXiv:2407.00199) decomposed the change in group error across 6 experiments.
- Madirolas & de Polavieja 2015 (https://doi.org/10.1371/journal.pcbi.1004594).
- Nobody has predicted other datasets with frozen parameters. No field test on GJP year 1 was found.

**Risks.**
- Two lab datasets with licences and pre/post estimates (Kao and the Jayles figshare sets) are used for fitting, and one (Becker 2019) carries the main test. The main test therefore rests on a single dataset.
- What crowd-belief forecasters saw in the field arm is known only from a web-search summary of Mellers et al. 2015 (JEP: Applied): "the distribution of forecasts for others in their group". UNVERIFIED; confirm from the paper or the GJP documentation.

**Effort.** R. 15–25 days. The GJP forecast files are large, and the year-1 survey file is 29 MB.

---

## 4. Bayesian sampler as an explanation of extremizing in forecasting

**Model.**
- Each forecaster draws N samples from a private probability, which gives information diversity among forecasters, and reports (S + β)/(N + 2β) (Zhu, Sanborn & Chater 2020, https://doi.org/10.1037/rev0000190).
- **Fitted on one GJP year:** N, β, and information overlap.
- **Fixed:** the prior form.

**Findings to reproduce.**
- Overconfidence of 3% (Moore et al. 2017).
- The aggregate needs extremizing. The mean needs more than the median, and experts need less than non-experts (Baron et al. 2014, https://doi.org/10.1287/deca.2014.0293, as summarised by Han & Budescu 2022, https://doi.org/10.1017/s1930297500009049; exact parameter values UNVERIFIED).
- Lab estimates of N are small: median 2.65–8.25 per participant (Sundh et al., preprint https://doi.org/10.31234/osf.io/yuhaz of https://doi.org/10.1037/xge0001414).

**New prediction.** Baron et al. argue that noise pulls only the mean toward 0.5, not the median. The sampler shrinks each person's *expected* judgment toward 0.5, so it predicts that the median also needs extremizing. Pure information-diversity accounts (Satopää et al. 2016, https://doi.org/10.1080/01621459.2015.1100621) predict that the median's optimal extremizing exponent γ_med(k) keeps rising with crowd size k. The sampler predicts that γ_med(k) levels off once k ≈ 10, at a level set by β/N.

**Refutation rule.** Draw random sub-crowds of size k = 1–50 per question-day. The sampler is refuted if γ_med(k) keeps rising beyond k = 20 by more than a preregistered amount. It is also refuted if γ_med stays ≤ 1 for large k. Partial-information aggregation also levels off once the shared information dominates. The simulator must therefore first show that the two accounts separate under realistic information overlap. Only then is this rule preregistered.

**Why falsifiability is 2.**
- The sampler is flexible, because N can grow with deliberation.
- With lab parameters (d = β/(N + 2β) ≈ .1), individual forecasts would stay below about .9. If GJP forecasters often go above .9, as I expect but cannot check under the blinding rule, N must be larger in the field.
- The test therefore only has force if N is tied to something observable, such as the number of updates.

**Data.** GJP, **CC0**; survey forecasts for years 1–4 (29–166 MB per year).

**Closest papers.**
- Baron et al. 2014; Satopää et al. 2016; the BIN (bias, information, noise) model of Satopää et al. 2021 (https://doi.org/10.1287/mnsc.2020.3882).
- Zhu et al. 2022 on poker experts (https://doi.org/10.1016/j.cognition.2022.105022).
- No sampler model has been applied to tournament aggregation.

**Effort.** R. 15–20 days.

---

## 5. Advice taking: generative model of the three-peaked weight-of-advice distribution

**Model.**
- The judge has privileged access to their own reasons, so they are unsure how accurate the advisor is. They combine own estimate and advice by Bayesian weighting.
- A discrete decision stage (keep own estimate / adopt the advice / average) comes from comparing the posterior probability that the advisor is better against two thresholds.
- The peaks at 0, .5 and 1 must come out of the model, not be built in.
- **Fitted:** prior on advisor accuracy, and the thresholds.

**Findings to reproduce.**
- Choosing vs averaging strategies (Soll & Larrick 2009, https://doi.org/10.1037/a0015145).
- Egocentric discounting (Yaniv 2004, https://doi.org/10.1016/j.obhdp.2003.08.002; Bonaccio & Dalal 2006, https://doi.org/10.1016/j.obhdp.2006.07.001).
- Curvilinear relation between advice distance and advice weight (Schultze et al. 2015, https://doi.org/10.1017/s1930297500003922).
- Numeric targets UNVERIFIED; to be taken from the papers.

**New prediction.** The share of "adopt" responses rises with the judge's own low confidence faster than the share of "average" responses does. The model derives the precise ratio.

**Refutation rule.** The predicted relation between confidence and the choose/average split falls outside the observed 95% CI.

**Data.** Jaquiery & Yeung date-estimation tasks, OSF h254u, **CC-BY 4.0** (licence checked by me). The subagent read the data dictionary as trial-level advice, confidence and responses. That the trials give an initial estimate, advice and a final estimate (the standard judge–advisor structure) is UNVERIFIED. Most other advice datasets have no licence: Schultze jgmd6 and 6xe5h were excluded.

**Closest papers.**
- Himmelstein 2022 (https://doi.org/10.1016/j.jmp.2022.102695): a dual-hurdle model in which the peaks are fitted, not generated. This is the benchmark to beat.
- Ravazzolo & Røisland 2011 (https://doi.org/10.1016/j.econlet.2011.03.032).
- Moussaïd et al. 2013 (https://doi.org/10.1371/journal.pone.0078433).
- Hütter & Ache 2016 (https://doi.org/10.1017/s193029750000382x).

**Effort.** R. 10–15 days.

---

## 6. Inner crowd as an autocorrelated sampler over time

**Model.**
- Estimates come from an autocorrelated sampler (Zhu et al. 2024, https://doi.org/10.1037/rev0000427).
- The second guess continues the chain after m(Δ) unobserved steps, where m(Δ) = m₀ + m₁·log(1 + Δ) and Δ is the delay.
- Averaging two guesses gains less than averaging two people, and the difference depends on Δ.

**Findings to reproduce** (Vul & Pashler 2008, https://doi.org/10.1111/j.1467-9280.2008.02136.x, PDF). Error reduction relative to the first guess:
- immediate second guess: [2.5%, 10.4%], equivalent to 1.11 people;
- after 3 weeks: [11.6%, 20.4%], equivalent to 1.32 people.

**New prediction.** The gain as a function of delay follows the chain's decorrelation curve, and it levels off at the share of error variance that is not shared bias.

**Data.** **None usable.**
- van Dolder & van den Assem 2018 is under a non-disclosure agreement.
- Steegen et al. 2014 (OSF ivfu6) has no licence.
- No other licensed deposit was found.

The design is therefore feasible only with new data collection or permission from the authors. It is the most novel design here: Dasgupta et al. 2017 (https://doi.org/10.1016/j.cogpsych.2017.05.001) only covered it qualitatively.

**Effort.** R. 6–8 days for the simulation. The empirical test is blocked.

---

## 7. Heterogeneity across sites created by the measurement scale (Many Labs)

**Model.**
- The latent log odds ratio is the same at every site.
- Sites differ in baseline rate p₀.
- The simulation uses Many Labs sample sizes and applies the same estimators to real and simulated data. This handles the shared sampling error between the risk difference and p₀.

**Findings to reproduce** (Olsson-Collentine et al. 2020, postprint text):
- 48/68 meta-analyses have non-significant heterogeneity.
- τ correlates with effect size: r = .77 [.57, .91] for SMDs; r = .91 [−.02, .98] for log odds ratios, k = 10.
- Effects not significantly different from zero have mean τ = .018.

**New prediction.** For binary JDM outcomes (ML1 gain/loss framing; ML2 framing, choosing vs rejecting, affect and risk, trolley 1 and 2), the site risk difference follows log OR × p₀(1 − p₀). τ on the log-odds scale should be about 0.

**Refutation rule.** The meta-regression slope falls outside the simulated band, or τ on the log-odds scale ≥ τ on the risk-difference scale after rescaling.

**Data.** ML1 OSF wx7ck **CC0**; ML2 OSF 8cd4r **CC0**; ML3 OSF ct89g **CC-BY 4.0**.

**Why novelty is 1.** Existing analyses already show small τ for ML2 framing (τ = .025 on the correlation metric, I² = 5.9%, in Olsson-Collentine et al.'s table), so only the risk-difference/baseline-rate arm is new. There is also an active competing group:
- Fünderich et al. 2025 (https://doi.org/10.3758/s13428-025-02879-w), plus a preprint on non-linearity across 55 multi-lab datasets (https://doi.org/10.31234/osf.io/s82zr_v3);
- Olsson-Collentine et al. 2023 (https://doi.org/10.31234/osf.io/jnb6e);
- Beinhauer et al. 2025 (https://doi.org/10.31234/osf.io/u6anb_v1).

The binary-outcome arm is the only open part.

**Effort.** R. 8–10 days.

---

## 8. Small-sample learning vs attitude change as causes of feedback effects in risky choice

**Model.**
- An agent chooses by the mean of k recalled outcomes. The hot-stove mechanism (Denrell & March 2001, https://doi.org/10.1287/orsc.12.5.523.10092; Denrell 2007, https://doi.org/10.1037/0033-295x.114.1.177) acts only under partial feedback.
- **Fitted:** k, on CPC15.
- **Tested:** on CPC18.

**Findings to reproduce.**
- The description–experience gap (Hertwig & Erev 2009, https://doi.org/10.1016/j.tics.2009.09.004).
- The gap persists when sampling error is nearly removed (Wulff et al. 2018, https://doi.org/10.1037/bul0000115, abstract).

**New prediction.** Learning predicts that the feedback-driven change in choice has a sign that follows the skew of each problem. Attitude change predicts a uniform shift toward the risky option that starts before any outcome is seen (Nasioulas et al. 2026, https://doi.org/10.1038/s41467-025-67729-x).

**Refutation rule.** Compare the sign agreement of per-problem feedback shifts with the skew, and look at the first feedback trial.

**Data.**
- CPC15: Zenodo 10.5281/zenodo.321652, **CC BY 4.0**.
- CPC18: Zenodo 10.5281/zenodo.2571510, **CC BY 4.0**.
- Wulff et al. 2018 database: Zenodo 10.5281/zenodo.1491449, **CC-BY-SA-4.0** (share-alike).
- choices13k (GitHub jcpeterson/choices13k) has **no licence** and is excluded.
- CPC feedback blocks show the foregone outcome, so the hot-stove mechanism cannot operate there.

**Why novelty is 1.** BEAST with frozen parameters already predicts CPC18 and choices13k (Erev et al. 2017, https://doi.org/10.1037/rev0000062; Plonsky et al. 2025, https://doi.org/10.1038/s41562-025-02267-6).

**Effort.** R. 8–12 days.

---

## Needs your decision
1. **Share-alike licence.** CC-BY-SA (the Wulff database) meets decision #4, but any derived data must be released under the same licence. Accept it?
2. **Dataverse CC0 defaults.** Becker 2019, Almaatouq 2020 and GJP carry CC0 because it is the Dataverse default licence. It is still an explicit licence on the record, so I counted them.
3. **Gürçay et al. 2015 re-deposit.** Becker 2022's Dataverse record (CC0) holds a re-deposit of the Gürçay data (`gurcay_data.tab`). The depositor may not own those data. I recommend not relying on it.
4. **Design 6 (inner crowd)** needs new data. Drop it, or keep it as a simulation paper with a separate data-collection preregistration?

## Open issues
- **Unchecked numbers.** Lichtenstein & Fischhoff, Hertwig et al. 2004, and the Baron/Satopää extremizing parameters were not extracted. Their tolerance bands cannot be set until they are.
- **Design 1 item count.** The number of OpAQ items with large anchor spreads is unknown without reading the data. The preregistration needs a rule that declares the test uninformative if too few items qualify.
- **Design 3 main test.** It rests on one licensed test dataset (Becker 2019). Adding a second static-network dataset with a licence would strengthen it; none was found.
- **Design 4 median diagnostic.** The claim that Baron et al. give the median as the diagnostic comes from their abstract. The exact derivation was not read.

Scratch files (full texts, scripts, the anchoring simulation `scratch_mh_anchor.py`, and the DOI lists) are in `/tmp/jdmsim`, outside the project.
