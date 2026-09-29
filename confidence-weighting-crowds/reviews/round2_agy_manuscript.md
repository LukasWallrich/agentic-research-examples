## Review of "When does weighting by confidence help the crowd? A finite-sample boundary and a test of the standard account"

**Journal:** *Judgment and Decision Making* (JDM)  
**Recommendation:** Major Revision / Reject with Invitation to Resubmit  

---

### Overview

The manuscript examines an important, longstanding question in judgment aggregation and the "wisdom of crowds": when does weighting binary judgments by self-reported confidence outperform simple equal weighting (majority voting), and when does it hurt? The authors frame their contribution around three elements:
1. Formulating a finite-sample bias–variance trade-off between equal weighting (EW) and confidence weighting (CW) parameterized by psychometric inputs (calibration slope $\beta$, within-item error correlation $\rho$, and group size $m$);
2. A generative simulation demonstrating parameter boundaries where CW underperforms EW and where intermediate shrinkage ($\lambda^*$) is optimal; and
3. An empirical meta-analysis across 76 datasets from the Confidence Database (1.64 million trials) testing whether CW helps, whether the benefit is moderated by calibration and error correlation, and whether the generative simulation reproduces real-world outcomes.

The paper is engagingly written, commendably transparent about preregistered hypotheses and subsequent deviations, and tackles a foundational problem of direct interest to the readers of *Judgment and Decision Making*. However, under close scrutiny, the paper suffers from deep theoretical gaps, critical empirical construct mismatches, post-hoc metric shifting, and severe statistical overstatements. 

Below is an evaluation structured around the six focal areas requested, followed by a ranked list of major and minor issues.

---

### 1. Novelty and Framing

**Is the contribution real, and is the framing honest?**

The authors correctly acknowledge prior foundational work: Condorcet (1785), Grofman (1978), Nitzan & Paroush (1982), Shapley & Grofman (1984), Ladha (1995), Baharad & Ben-Yashar (2009), the forecast-combination puzzle (Smith & Wallis, 2009; Claeskens et al., 2016), Huang, Broomell, and Golman (2024), and Meyen et al. (2021). 

However, the framing significantly overstates the novelty and scope of what the paper actually accomplishes:
- **Prior Knowledge vs. Paper Claims:** That weighted majority voting degrades or falls behind equal weighting when weights are noisy, distorted, or miscalibrated is precisely the core theorem of Baharad & Ben-Yashar (2009). That estimating or assigning weights adds sample variance that often exceeds the reduction in bias is the exact definition of the forecast-combination puzzle and the core premise of Huang et al. (2024).
- **The "Derived Boundary" Claim:** The paper repeatedly asserts in the title, abstract, and introduction that it "derives a finite-sample boundary." Yet no closed-form boundary, analytical proof, or exact inequality is ever derived. The theoretical section (§2.2) provides only a qualitative bias–variance heuristic and states that a closed form is intractable. Running a numerical simulation on an arbitrary grid is *mapping a simulation surface*, not *deriving a boundary*.
- **The Empirical Base Rate:** While aggregating across 76 datasets appears impressive, the datasets are almost exclusively psychophysics/perceptual experiments (visual detection, motion discrimination, contrast sensitivity) from the Confidence Database. Framing this as a general empirical base rate for "crowd aggregation" is misleading; these are not forecasting tournaments, political judgments, or general-knowledge crowds.

---

### 2. Theory: Bias–Variance Account and Derivation

**Is the bias–variance account correct and sufficiently derived?**

The theoretical section (§2) contains severe mathematical and conceptual shortcomings:
1. **Mathematical Imprecision of the Variance Formula:** In Section 2.2, the crowd estimate variance is written as:
   $$\mathrm{Var}(\hat{x}_i) = \sum_j w_j^2 \mathrm{Var}(v_{ji}) + \sum_{j \neq k} w_j w_k \mathrm{Cov}(v_{ji}, v_{ki})$$
   This formula treats the weights $w_j = c_{ji} / \sum_k c_{ki}$ as fixed constants. But the weights are *random variables* that are explicitly and deliberately *correlated* with the individual judgments $v_{ji}$! In ratio estimators of random variables, $\mathrm{Var}\left(\frac{\sum c_j v_j}{\sum c_j}\right)$ cannot be decomposed as if $w_j$ were deterministic constants. The covariance between the weights and the votes is the very engine that generates the weighting benefit.
2. **0–1 Loss vs. Squared Error Loss:** The crowd decision rule is defined as a sign-threshold decision: $\mathrm{sign}(\bar{x}_i)$ vs $\mathrm{sign}(\hat{x}_i)$. Classification accuracy under 0–1 loss does not obey the standard additive bias–variance decomposition of squared error (Friedman, 1997). In 0–1 loss, variance reduction only improves accuracy if the decision is on the correct side of the boundary; if the group mean is negative, increasing variance can actually increase the probability of a correct majority vote! The paper conflates continuous estimation variance with discrete classification accuracy.
3. **Absence of Closed Form:** The lack of an analytical closed form is a critical weakness because the paper bills itself as providing an actionable boundary for an aggregator. Without an analytical expression or parametric approximation, an analyst who knows $m, \beta,$ and $\rho$ still cannot determine where the boundary lies without running the authors' simulation script.

---

### 3. Empirical Design and Estimands

**Is the item/vote definition defensible? Does LOO-Brier test the claim? Is H6 meaningful? Is the moderation sound?**

1. **Fatal Construct Mismatch in the Item/Vote Definition:**
   - In Section 4.1, an "item" is defined as a condition cell (e.g., a specific stimulus value combined with contrast, coherence, or difficulty level). A judge's "vote" $v_{ji}$ is defined as the *mean accuracy* of that judge over multiple trials in that cell, transformed to $[-1, +1]$.
   - This completely undermines the crowd-decision setting. In perceptual psychophysics experiments, subjects typically operate well above chance (e.g., 70–90% correct across trials). Consequently, almost every judge's vote $v_{ji}$ in a condition cell is strictly positive ($v_{ji} > 0$).
   - When all $v_{ji} > 0$, any weighted average with positive weights $c_{ji} \ge 0$ is *guaranteed* to be strictly positive! Thus, $\mathrm{sign}(\bar{x}_i) = +1$ and $\mathrm{sign}(\hat{x}_i) = +1$ mechanically coincide on almost every item. This is why the baseline equal-weighted accuracy is 93.3% at $m=3$ and 98.0% at $m=40$, leaving essentially zero room for CW and EW to differ. The authors are not aggregating independent judgments on discrete binary problems; they are averaging condition-level psychometric functions.
2. **The Post-Hoc LOO-Brier Estimand:**
   - Because the preregistered sign-accuracy gap was ceiling-bound, the authors introduced the leave-one-judge-out (LOO) Brier improvement post-hoc.
   - However, LOO-Brier answers an entirely different question: *how well do the other $m-1$ judges predict the correctness of a held-out judge?* It does NOT measure whether the crowd correctly identifies the state of the world. In crowds, an individual judge's response is noisy; an aggregation rule that correctly tracks the ground truth will frequently disagree with an errant held-out judge. Penalizing CW for failing to predict a held-out judge's idiosyncratic error distorts the concept of crowd wisdom.
   - Crucially, as disclosed in `deviations.md` (V2), the preregistered sign-accuracy gap is *positive* on average (+0.0036), whereas the LOO-Brier improvement is *negative* (−0.0006). Pivoting to the negative LOO-Brier score to conclude that "confidence weighting hurts" is a post-hoc shift in primary outcome.
3. **The H6 Model Reproduction Test:**
   - The H6 test (requiring $\ge 60\%$ sign agreement between the simulation and empirical datasets) is conceptually flawed. In the simulation, 72.5% of cells show negative Brier improvement; in the empirical data, 78.9% of datasets show negative Brier improvement at $m=7$. 
   - A completely trivial baseline predicting a negative effect for every dataset achieves 78.9% agreement. Yet the authors' calibrated model achieved only 34.2% agreement (26 of 76 datasets). 
   - The authors interpret this failure as refuting the psychological account of overconfidence. But when a model achieves less than half the accuracy of a trivial zero-information baseline and worse than a coin flip, the failure reflects severe model misspecification, an inadequate parameter grid, and a flawed mapping procedure (9 datasets collapsed to a single cell, and 7 empirical datasets had $\rho$ falling outside the simulated range).
4. **Moderation Analysis (H5):**
   - The regression of dataset-level effects on $\beta$ and $\rho$ treats 76 vastly heterogeneous datasets as exchangeable points in an unweighted OLS regression.
   - As shown in Figure 3, the data contain extreme leverage points (e.g., an extreme negative outlier at LOO-Brier $\approx -0.009$, while all others are near 0).
   - More fundamentally, $\beta$ and $\rho$ are estimated with considerable sampling error across datasets. Running OLS with noisy regressors causes severe *errors-in-variables attenuation bias*, driving regression coefficients directly toward zero. The authors confuse "failure to reject the null" with evidence that calibration and error correlation do not matter.

---

### 4. Statistics, Power, and Ceiling Effects

1. **Misrepresentation of the Primary Effect:**
   - The abstract and text emphasize that the sign-accuracy gap is "non-positive in 64% of datasets."
   - According to `output/manuscript_numbers.json`, only 44.7% of datasets have a strictly negative gap (`frac_neg: 0.447`). About 20% of datasets have a gap of *exactly zero* due to discrete ceiling effects.
   - More importantly, the mean sign-accuracy gap is **+0.0036, with a 95% bootstrap confidence interval of [0.0003, 0.0083]**. This confidence interval *strictly excludes zero*! By conventional statistical standards, confidence weighting produces a statistically significant *improvement* in crowd accuracy across the 76 datasets. Describing this result as "CW loses to EW in 64% of datasets" and concluding that CW harms accuracy is a misleading gloss over a statistically significant positive effect.
2. **Ceiling Problem Handling:**
   - At 98% baseline accuracy, observing a tiny absolute difference (+0.0036) is mathematically inevitable. The authors fail to apply transformed scales (such as log-odds or $d'$) or restrict the analysis to difficult items/datasets where crowd accuracy is off the ceiling.
3. **Overstatement of Shrinkage Optimality (H3 / Figure 4):**
   - The authors state: "In 119 of the 120 cells the accuracy-optimal shrinkage $\lambda^*$ lies strictly between 0 and 1 for at least one group size (Figure 3), so partial shrinking beats both pure rules almost everywhere."
   - Looking directly at Figure 4 (`fig4_lambda.png`), the $\lambda^*$ curves display erratic jumps and blatant Monte Carlo instability (e.g., for $\phi=0$, $\lambda^*$ is 1.0 at $m=3$, drops near 0 at $m=4$, jumps back to 1.0 at $m=5$, and stays flat at 1.0). For $\phi=4$, it hovers at 0 across nearly all group sizes except for noisy spikes.
   - Registering H3 to be supported if $\lambda^*$ is interior for *a single swept cell*, and then asserting that shrinking beats pure rules *almost everywhere*, is an indefensible leap.

---

### 5. Clarity, Structure, and Fit to *Judgment and Decision Making*

- **Fit to JDM:** The core question—evaluating whether metacognitive signals improve collective choice—is an ideal fit for JDM. JDM has a rich tradition of publishing foundational work on the wisdom of crowds, averaging, and calibration.
- **Tone and Skepticism:** The authors deserve credit for transparency regarding the bug fixes that overturned earlier results (`deviations.md`, V6). However, the manuscript adopts an overly confident, revolutionary tone ("the standard account fails", "confidence weighting is not a safe default") that is simply not supported by the heavily compromised empirical substrate.
- **Figure and Caption Scrambling:** In the manuscript draft, Figure citations and image files are out of sync:
  - Text line 64 cites Figure 2, pointing to `fig2_boundary.png`.
  - Text line 71 cites Figure 3, but embeds `fig4_lambda.png`.
  - Text line 93 cites Figure 1, pointing to `fig1_empirical.png`.
  - Text line 97 cites Figure 4, but embeds `fig3_moderation.png`.
  This must be cleaned up and properly ordered.

---

## Answer

### Ranked Major Issues

#### 1. Inappropriate Item and Vote Definition on Psychophysics Data
- **Problem:** Defining an "item" as an experimental condition cell and a "vote" as a participant's average accuracy over repeated trials within that condition creates a severe artificial ceiling (EW accuracy 93% to 98%). Because participants are well above chance in almost all conditions, almost all votes are positive, ensuring that EW and CW agree on virtually 100% of items. This does not represent crowd decision making on binary problems.
- **Is it fixable?** **Partially.**
- **How to fix:** The authors must determine whether any subset of the Confidence Database features shared, identical stimuli presented across different subjects on individual trials. If not, the authors must openly acknowledge that they are analyzing condition-level psychometric aggregations, not discrete binary voting. Ideally, they should test their framework on genuine crowd-judgment or forecasting datasets (e.g., the Good Judgment Project, binary general knowledge questions, or cognitive benchmark sets) where items have ground-truth answers and diverse error patterns.

#### 2. Lack of Analytical Derivation of the "Finite-Sample Boundary"
- **Problem:** The title, abstract, and introduction promise a "derived finite-sample boundary," but Section 2 contains only a qualitative heuristic. The variance formula in Section 2.2 incorrectly treats endogenous, vote-correlated confidence weights as fixed constants and fails to connect continuous variance to 0–1 classification loss.
- **Is it fixable?** **Yes.**
- **How to fix:** Either provide a formal mathematical derivation—for example, using a bivariate normal signal detection framework or a Taylor series approximation for the ratio estimator to derive the sign condition for $E[\mathrm{Acc}_{\mathrm{CW}}] > E[\mathrm{Acc}_{\mathrm{EW}}]$ as a function of $(m, \beta, \rho)$—or drop the claim of having "derived a boundary" throughout the manuscript, reframing the contribution as a simulation-based exploration.

#### 3. Post-Hoc Pivot to LOO-Brier and Mischaracterization of the Primary Result
- **Problem:** The preregistered primary outcome—the sign-accuracy gap—is statistically significantly positive (+0.0036, 95% CI [0.0003, 0.0083]). Emphasizing that CW is "non-positive in 64% of datasets" conceals that 20% are exact zeros and that strictly positive datasets outnumber strictly negative ones. Shifting the primary negative narrative onto the post-hoc LOO-Brier metric (which asks whether the crowd predicts a noisy individual judge, not the true state) constitutes an unprincipled post-hoc outcome shift.
- **Is it fixable?** **Yes.**
- **How to fix:** Keep the preregistered sign-accuracy gap front and center. Honestly report that CW produces a statistically significant, though practically tiny (+0.36%), improvement in accuracy. Present the LOO-Brier score strictly as an exploratory, secondary diagnostic of probability calibration, clearly distinguishing the goal of predicting the true state of the world from the goal of predicting a held-out judge's response.

#### 4. Flawed Model Validation and Interpretation of H6
- **Problem:** The simulation achieved only 34.2% sign agreement with the data on LOO-Brier, performing far worse than a trivial baseline (78.9%) and worse than chance. Interpreting this failure as evidence that "the standard overconfidence account does not explain the data" is an overreach; the failure is driven by an arbitrary simulation grid, coarse 2D nearest-neighbor mapping, and severe dataset-to-simulation domain mismatch.
- **Is it fixable?** **Yes.**
- **How to fix:** Retract the broad claim that the overconfidence account is refuted. Instead, state clearly that the specific generative model failed to reproduce the empirical data due to structural mismatches. Replace the uninformative raw sign-agreement test with continuous error metrics (e.g., RMSE, correlation) or standard posterior predictive checks, accounting for base-rate prevalence.

#### 5. Severe Overstatement of Shrinkage Optimality (Figure 4 / H3)
- **Problem:** The claim that "partial shrinking beats both pure rules almost everywhere" is based on an unfalsifiable preregistered criterion ($\lambda^*$ interior in at least one cell) and contradicted by Figure 4, which shows extreme Monte Carlo instability and boundary solutions ($\lambda^* = 0$ or $1$) across most group sizes.
- **Is it fixable?** **Yes.**
- **How to fix:** Increase the Monte Carlo draws in the simulation by an order of magnitude to eliminate optimization noise. Plot smooth $\lambda^*(m)$ curves with standard error bands. State accurately what proportion of the parameter space genuinely benefits from intermediate shrinkage, rather than declaring it an "interior optimum almost everywhere."

#### 6. Methodological Deficiencies in Moderation Analysis (H5)
- **Problem:** The moderation OLS regressions treat heterogeneous datasets as exchangeable and ignore severe errors-in-variables attenuation bias arising from noisy estimation of $\beta$ and $\rho$. Claiming that calibration slope and error correlation do not moderate aggregation effectiveness based on non-significant OLS slopes is a classic acceptance of the null hypothesis.
- **Is it fixable?** **Yes.**
- **How to fix:** Implement a formal meta-regression model (e.g., random-effects meta-regression weighting datasets by inverse variance). Explicitly discuss the impact of measurement error and attenuation bias. Remove or control for the massive outlier visible in Figure 3, and report the statistical power/minimum detectable effect size for the moderation tests.

---

### Ranked Minor Issues

1. **Scrambled Figure Citations and Captions:**
   - *Problem:* As detailed in Section 5, text references to Figures 1–4 do not match the embedded file paths and caption numbers.
   - *Fix:* Ensure figures are numbered sequentially and match the corresponding text and file references.

2. **Uncertain Group Size Support at $m=40$:**
   - *Problem:* In Figure 1a, the point at $m=40$ has zero error bar and sits at 0.000. It appears only a single dataset possessed $\ge 40$ median judges.
   - *Fix:* Display sample sizes ($N$ datasets) at each group size $m$ along the x-axis, and omit or clearly indicate points where the sample collapses to a trivial number of datasets.

3. **Inconsistent Brier Improvement Sign Notation:**
   - *Problem:* In Section 4.1, Brier improvement is defined as $\mathrm{Brier}(\mathrm{EW}) - \mathrm{Brier}(\mathrm{CW})$, meaning positive values indicate CW superiority. Yet in Figure 1b, the axis is labeled $\Delta \mathrm{Brier} (\mathrm{EW} - \mathrm{CW})$, but negative numbers are plotted and interpreted as CW being worse.
   - *Fix:* Standardize the notation and explicitly label the axis direction: "Negative values favor EW; positive values favor CW."

4. **Missing or Inaccessible Reproduction Script:**
   - *Problem:* Section 127 states that `run_all.sh` reproduces all results from the root repository, but the script is not present at the stated root path.
   - *Fix:* Verify that the reproduction script and all companion files are correctly packaged and located in the referenced directory structure.

5. **Clarity of Prior Theoretical Context:**
   - *Problem:* While Baharad & Ben-Yashar (2009) and Shapley & Grofman (1984) are cited, the manuscript does not explain how its conceptual trade-off mathematically differs from Baharad & Ben-Yashar's theorems on probability distortion.
   - *Fix:* Add 1–2 paragraphs in the Introduction/Theory section explicitly contrasting the paper's formulation with Baharad & Ben-Yashar's analytical framework.
