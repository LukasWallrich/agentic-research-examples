### 1. Novelty, Closest Existing Work, and the Precise Gap

#### Is it novel and publishable in a strong JDM outlet?
**Theoretically, no; mega-analytically, yes.** 
If framed as the discovery that "trial difficulty drives RT in intertemporal choice," this paper will be rejected. Mathematical psychologists and neuroeconomists have treated this as a settled baseline for over a decade. However, if framed as an **authoritative empirical audit of the dual-process "impulsive is fast / patient is slow" dogma across the published literature**, it is publishable in top-tier outlets (*Cognition*, *Judgment and Decision Making*, *Decision*, or *JEP: General*).

#### Closest Existing Work
1. **Krajbich, Bartling, Su, & Fehr (2015, *Nature Communications*, [10.1038/ncomms8455](https://doi.org/10.1038/ncomms8455)):** *"Rethinking fast and slow based on a critique of reaction-time reverse inference."* 
   * *What they showed:* The canonical critique of using RT to infer cognitive systems. They showed theoretically and empirically (in social and intertemporal choice) that raw RT differences between choice types are an artifact of choice discriminability (trial difficulty) and stimulus menu design.
2. **Chabris, Laibson, Morris, Schuldt, & Taubinsky (2009, *AER P&P*):** *"The Allocation of Time in Decision-Making."*
   * *What they showed:* Decision time in intertemporal choice is an inverted-U function of subjective value difference ($|SV_{LL} - SV_{SS}|$), explaining over 50% of the variance in deliberation time.
3. **Sequential Sampling / DDM in ITC:**
   * **Rodriguez, Turner, & McClure (2014, *PLoS ONE*):** Modeled intertemporal choice as evidence accumulation (LBA), linking drift rates to discounted subjective values.
   * **Dai & Busemeyer (2014, *Psych Review*):** Dynamic dual-process vs. accumulation models in ITC.
4. **The Dataset Itself:**
   * **Pongratz & Schoemann (March 2026, *Scientific Data*, [10.1038/s41597-026-06947-4](https://doi.org/10.1038/s41597-026-06947-4)): Published the database as an open data descriptor to spur process modeling. 

#### The Precise Gap
While theorists know that difficulty confounds raw RT differences, hundreds of empirical behavioral papers continue to casually interpret fast choices as "impulsive/automatic" and slow choices as "deliberative/controlled." 
Existing methodological critiques (like Krajbich et al., 2015) used **1 to 3 targeted experiments** to make a conceptual proof-of-concept. **No one has evaluated this across the entire empirical corpus (100 studies, 1.17M trials).** 
The open empirical questions are:
1. Across the published literature, does a consistent raw within-subject LL-SS RT difference actually exist, or is its sign and magnitude entirely an artifact of study-specific choice menus?
2. When controlling for difficulty, does any residual RT difference survive, or is the dual-process signature 100% accounted for by value discriminability?

---

### 2. Critique of Hypotheses (H1–H3) & Proposed Refinements

* **H1 (Within-subject RT difference is reliably non-zero and consistent in sign across studies):**
  * *Fatal flaw:* **The sign will almost certainly NOT be consistent across studies.** The raw sign depends directly on whether a study’s menu features easy LL options (e.g., $10 now vs $1,000 in a week $\rightarrow$ fast LL) or easy SS options (e.g., $50 now vs $51 in a year $\rightarrow$ fast SS). 
  * *Correction:* Reframe H1 as a test of **between-study heterogeneity**: Test whether the conventional claim (SS is faster than LL) holds on average, and quantify between-study variance ($\tau^2$).
* **H2 (A substantial fraction is attributable to difficulty; attenuates after conditioning):**
  * *Methodological danger:* **Circularity.** If you estimate each participant's discounting parameter ($k$) using their choices and then compute difficulty as $|SV_{LL} - SV_{SS}|$, you are conditioning RT on a transformation of the dependent variable. If the discounting model is misspecified, you get artifactual residuals.
  * *Correction:* You must compute difficulty either (a) **out-of-sample** (fit $k$ on odd trials, test RT attenuation on even trials), or (b) use **model-free difficulty proxies** (e.g., choice entropy, group-level choice proportion $|P(LL) - 0.5|$, or normalized trade-off ratios: $\Delta \$ / \Delta \text{Delay}$).
* **H3 (RT adds out-of-sample predictive value beyond a stimulus-only model):**
  * *Fatal flaw:* **Trivial and already answered.** It is a mathematical truism of any drift-diffusion or sequential sampling process that RT correlates with choice confidence and improves out-of-sample likelihood (e.g., Chabris et al., 2009; Clithero, 2018; Webb, 2019). Reviewers will dismiss H3 as an uninformative benchmark.
  * *Correction:* Replace H3 with a **process-model architecture test (Drift Diffusion Model decomposition)**:
    * Does the data require a **starting-point bias** toward SS ($z < 0.5$, which formalizes the dual-process "impulsive default" hypothesis), or is starting evidence unbiased ($z = 0.5$) with RT differences driven purely by drift rate asymmetries?

---

### 3. Likely Fatal Weaknesses & Mitigation

1. **RT Heterogeneity Across 100 Environments:**
   * *Problem:* Studies range from lab tachistoscopes and E-Prime setups to unmoderated online surveys (MTurk, Prolific) with different input modalities (touch, mouse, keyboard). Baseline RTs will vary from 600 ms to 5,000+ ms.
   * *Mitigation:* Do not use raw ms. Use within-subject log-RT standardization ($z$-scores) or hierarchical DDM parameters, where non-decision time ($T_{er}$) isolates hardware/motor latencies across studies.
2. **Paradigm Artifacts (Multiple Price Lists vs. Discrete Trials vs. Titration):**
   * *Problem:* In Multiple Price Lists (MPL), participants often sweep down a column with rapid rhythmic clicking (heavy temporal autocorrelation). In adaptive titration tasks (e.g., adjusting amount), almost all trials cluster near indifference ($SV_{SS} \approx SV_{LL}$). In fixed random designs, difficulty varies widely.
   * *Mitigation:* Code task paradigm (MPL vs. Discrete Trial vs. Adaptive Titration) as a primary pre-registered moderator.
3. **Data Cleaning & Trimming Biases:**
   * *Problem:* Each original author used idiosyncratic RT cutoffs (e.g., dropping $<200$ ms, $<500$ ms, or $>3$ SD).
   * *Mitigation:* Apply a uniform, transparent exclusion protocol across all 100 datasets (e.g., drop RT $<250$ ms and $>10$ s), and report a specification curve across multiple cutoffs.
4. **The "Stimulus Set Asymmetry" Confound:**
   * *Problem:* If Study A finds LL is slower than SS, is it because LL requires self-control, or because the researcher picked SS amounts that were close to indifference and LL amounts that were obvious?
   * *Mitigation:* Explicitly compute the **Menu Asymmetry Index** for each study: $\text{Mean}(|\Delta SV| \mid \text{Choice}=LL) - \text{Mean}(|\Delta SV| \mid \text{Choice}=SS)$. Test whether study-level menu asymmetry predicts study-level raw RT difference.

---

### 4. Evaluation of Alternative Topics

* **(a) First meta-analysis of sunk-cost effect:**
  * **FATAL FLAW: It is NOT the first.** Stefan Roth, Thomas Robbert, and Lennart Straus published *"On the sunk-cost effect in economic decision-making: a meta-analytic review"* in 2015 (*Business Research*, 98 effect sizes). Furthermore, Sleesman et al. (2012) published a massive meta-analysis on escalation of commitment. Submitting a "first meta-analysis of sunk cost" will result in immediate desk rejection.
* **(b) First meta-analysis of overprecision:**
  * Feasible conceptually, but **does not meet the zero-data-collection / low-friction constraint**. It requires manually identifying hundreds of papers, extracting confidence intervals, resolving elicitation differences (SPI vs. TPI vs. fractiles), and dealing with severe reporting heterogeneity.
* **(c) Confidence-weighting harm boundaries:**
  * Testing when confidence-weighting degrades judgment aggregation relative to simple averaging is a solid JDM question. However, your group’s Paper 2 was already a secondary analysis of Good Judgment Project (GJP) forecasting data. Doing another forecasting aggregation study risks pigeonholing the group and appearing derivative.
* **(d) Global Preferences Survey (GPS) measurement invariance:**
  * Several studies have already conducted measurement invariance / DIF analyses on the GPS (confirming metric and partial scalar invariance across many countries). Testing psychometric invariance on a 2-item preference scale is dry, psychometrically narrow, and of low interest to behavioral JDM researchers.
* **(e) Inner-crowd noise-structure test:**
  * The debate over whether dialectical bootstrapping works via independent stochastic sampling or regression to the mean was thoroughly addressed by van Dolder & van den Assem (2018, *Nature Human Behaviour*). Finding open datasets with repeated within-subject estimates that offer new traction is difficult.

---

## Answer

### Recommendation
**Choose the Candidate Topic (ITC Database), but execute a strategic pivot in its theoretical framing and hypothesis structure.**

Do **NOT** pursue alternative (a) (sunk cost), as meta-analyses by Roth et al. (2015) and Sleesman et al. (2012) already exist. Alternatives (b), (d), and (e) are either labor-prohibitive from scratch, saturated, or outside core behavioral JDM interest; alternative (c) overlaps too closely with your group's Paper 2.

The ITC Database (Pongratz & Schoemann, 2026; OSF 3wsae) is a high-value asset: 100 studies, 1.17M trials, unanalyzed as a consolidated mega-dataset, zero data collection cost, and distinct from your group's prior papers (anchoring meta-analysis, GJP forecasting, advisor simulation).

### Required Pivot for the Candidate Topic
To avoid immediate rejection by reviewers who cite Krajbich et al. (2015) and Chabris et al. (2009), **reframe the paper from an exploratory RT analysis into an authoritative mega-analytic audit of the dual-process paradigm in intertemporal choice.**

#### Recommended Paper Title & Framing
* **Title:** *"Is the 'Impulsive is Fast, Patient is Slow' Signature Real? A 100-Study Mega-Analytic Test of Dual-Process vs. Evidence-Accumulation Accounts of Intertemporal Choice."*
* **Core Argument:** For decades, behavioral science has relied on the premise that choosing smaller-sooner rewards is intuitive/fast while choosing larger-later rewards requires deliberative self-control. While decision theorists have argued that RT is merely a function of trial difficulty, this critique has never been tested across the empirical literature. We test whether the purported LL-SS RT difference is an empirical constant or a spurious artifact of experimental menu design.

#### Restructured Hypotheses & Analyses
1. **H1 (The Menu-Asymmetry Hypothesis — replaces raw H1):** Across 100 studies, the raw within-subject LL-SS RT difference is highly heterogeneous. The sign and magnitude of a study's raw RT effect are predicted by that study's **Menu Asymmetry Index** (i.e., whether the experimenter's design placed LL or SS options closer to the subjective indifference point).
2. **H2 (Cross-Validated Difficulty Attenuation — replaces H2):** In an out-of-sample cross-validation framework (estimating discounting parameters $k$ on fold $K_1$ and evaluating RT on fold $K_2$), conditioning on trial difficulty ($|SV_{LL} - SV_{SS}|$) attenuates the within-subject LL-SS RT gap toward zero across paradigms.
3. **H3 (Starting Bias vs. Drift Rate in Hierarchical DDM — replaces H3):** When fitting a hierarchical Drift Diffusion Model across trials, the data will support an **unbiased starting point** ($z = 0.5$) with drift driven by value difference, refuting the dual-process prediction of an inherent starting-point bias toward immediate reward ($z < 0.5$).
4. **Synthetic Null Simulation:** Simulate an agent with zero choice bias ($z = 0.5$) run through the exact stimulus sets of all 100 studies. Demonstrate that difficulty alone generates the exact empirical distribution of "fast SS" and "fast LL" studies observed in the literature.
