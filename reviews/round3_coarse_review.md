# When does weighting by confidence help the crowd? A finite-sample boundary and a test of the standard account

**Date**: 09/28/2026
**Domain**: social_sciences/psychology/judgment_and_decision_making
**Taxonomy**: academic/research_paper
**Filter**: Active comments

---

## Overall Feedback

Here are some overall reactions to the document.

**Outline**

The paper asks a well-motivated practical question—when does confidence weighting help crowd aggregation?—and brings useful structure to the answer via a finite-sample gap framework, a simulation boundary, and a large empirical test. But several design choices weaken the empirical conclusions substantially. The primary graded measure (LOO-Brier) answers a different question than the one the theory poses, the sign-accuracy gap is ceiling-bound by construction, and the simulation-to-data mapping is too coarse to support the strong claim that the standard account fails. The paper is honest about many of these limitations individually but does not adjust its conclusions to match their cumulative force.

The paper tackles a genuinely important practical question and does so with an unusual degree of preregistration discipline and transparency. The simulation boundary (Figures 2–3) is the paper's strongest contribution—it gives aggregators a concrete map of when confidence weighting pays off. The honest reporting of negative results, including the note about the earlier pipeline bug, is commendable. The writing is clear and the theoretical framing is well-situated in the literature.

**The LOO-Brier measure answers a different question than the theory poses**

The theoretical setup asks when confidence weighting better recovers the item's binary truth. The LOO-Brier measure instead asks whether CW better predicts a held-out judge's correctness. These are different objectives, and the difference matters most exactly when errors are correlated—which is one of the paper's key parameters. When judges share errors on an item, the best predictor of whether judge j is correct is close to the base rate of correctness on that item, which EW approximates well. CW could still be better at recovering truth while being worse at predicting a held-out judge, because the held-out judge's error is partly shared with the other judges whose confidence is doing the weighting. The paper acknowledges this mismatch in one sentence of the limitations (Section 5) but then treats the LOO result as telling 'a clearer and more adverse story' than the sign-accuracy gap and builds the headline conclusions around it (91% of datasets, the abstract). The theoretical derivation in Section 2 is about recovering truth, and the simulation evaluates both truth-recovery and LOO prediction; the empirical test should make the distinction between these two objectives explicit and not let the LOO result carry conclusions about truth recovery.

**Ceiling effects render the sign-accuracy gap uninformative rather than informative**

EW crowd accuracy is 0.93 at m=3 and 0.98 at m=40. The maximum possible improvement from any reweighting is bounded by the EW error rate, which is 2–7%. The observed gap of +0.004 is small in absolute terms but is being compared against a ceiling that is itself small. The paper acknowledges the ceiling but treats the negligible gap as evidence that CW is unhelpful. A more informative analysis would condition on items where the crowd actually disagrees (the items where weighting could change the decision), or report the gap as a fraction of the available improvement. As it stands, the Confidence Database tasks are overwhelmingly easy for crowds, and the sign-accuracy result tells us more about task difficulty than about the merits of confidence weighting. If these results are to support claims about CW as a general aggregation strategy, the paper needs either harder tasks or an explicit argument that most real-world crowd-aggregation settings have similarly high base rates.

**Item definition does not match the theoretical setup**

The theory in Section 2 assumes m judges evaluate the same item i. The empirical analysis defines an item as a condition cell—the stimulus value plus design columns. Different judges within a condition cell may have seen different specific trials (different exemplars at the same contrast level, for instance). This means 'within-item error correlation' in the data is not the same quantity as ρ in the simulation, where all judges literally see the same stimulus. If judges in a condition cell face different physical stimuli, their errors are less correlated by construction, and confidence tracks stimulus-specific difficulty that is irrelevant for other judges in the cell. This could explain both the low empirical error correlations (median 0.11) and the failure of CW: confidence may be informative about each judge's specific trial but not about the shared condition. The paper should report how many of the 76 datasets have a one-to-one mapping between stimulus identifiers and physical stimuli, and test whether CW performs differently in those datasets.

**The strongest empirical conclusions rest on a post-hoc outcome**

The LOO-Brier measure was added after the preregistered sign-accuracy estimand proved ceiling-bound (Section 5 states this explicitly). The 91% figure and the Brier-based moderation tests are therefore exploratory, not confirmatory. Yet the abstract and discussion lead with the LOO-Brier result and use it to reject the standard account. The preregistered sign-accuracy gap is actually positive on average, with a CI excluding zero, which is—if anything—weakly supportive of CW. Presenting an exploratory measure as the primary evidence while the confirmatory measure is equivocal is a framing problem. The paper should either foreground the preregistered result and treat the LOO analysis as supplementary, or explicitly reframe the entire empirical section as exploratory.

**The simulation-to-data mapping is too crude to support the model-rejection claim**

The model-reproduction test (H6) maps each dataset to the 'nearest simulated cell' in a two-dimensional space of calibration slope and error correlation, then checks whether the simulation predicts the correct sign. Nine datasets collapse onto a single cell, seven empirical error correlations fall below the simulated range, and the mapping ignores group size, confidence dispersion, the shape of the confidence distribution, and task-specific features. Failing to reproduce the data under this crude projection does not warrant the conclusion that 'the standard overconfidence account does not explain why' CW fails. It warrants the weaker conclusion that a two-parameter summary of the standard account, evaluated at a coarse grid, does not predict dataset-level signs. The paper should either refine the mapping (e.g., simulate each dataset's actual parameter estimates rather than snapping to a grid) or soften the model-rejection language to match the resolution of the test.

**Calibration slope β conflates between-judge and within-item variation**

The theoretical gap depends on the within-item covariance of confidence with correctness: does a judge who is more confident on item i tend to be more accurate on that item? The empirical β comes from a ridge-penalized logistic regression of correctness on standardized confidence pooled across all judges and items. This estimate mixes a between-judge component (some judges are both more confident and more accurate overall) with the within-item component the theory requires. If the between-judge association is positive but the within-item association is flat, the estimated β would be positive even though CW gains nothing on any single item. The moderation analysis in Section 4.2 could find no relationship between β and the CW advantage precisely because β does not isolate the relevant signal. A within-item or within-judge decomposition of the calibration slope would be more appropriate and would provide a sharper test of the theory.

**Shrinkage is evaluated in simulation but not tested against estimation noise in data**

The simulation shows that an interior λ* between EW and CW is almost always optimal (119/120 cells). This is presented as practical advice: 'partial shrinking towards equal weighting is often better.' But the simulation knows the population parameters and can compute the optimal λ* exactly. In practice, λ* would need to be estimated from the same finite sample, reintroducing the estimation-noise problem the paper rightly identifies for CW weights themselves. The paper does not evaluate whether estimated shrinkage actually beats EW in the 76 empirical datasets—it says 'the data cannot yet confirm' this. Without that test, recommending shrinkage is premature: the cure may have the same disease as the treatment. A leave-one-item-out or split-sample evaluation of estimated λ on the real data would substantially strengthen or appropriately weaken this recommendation.

**The gap parametrisation is described but never written as an equation**

The paper's first stated contribution is 'the psychometric parametrisation of the expected gap between CW and EW as a function of the confidence–accuracy calibration slope, the within-item error correlation, and confidence dispersion.' Section 2.2 describes the ingredients and gives limiting behavior in prose, but no equation for the gap itself appears. The sign condition is stated verbally ('the gap is negative whenever the weighting gain falls short of the variance cost'), and the paper concedes it does not have a closed form for all cases. Even so, a theory article whose headline contribution is a parametrisation should display at least the expression it is parametrising — even if it holds only under a simplifying assumption (e.g., equal judge ability, symmetric confidence distribution) or is written as an inequality that gives the sign. Without it, readers cannot check the derivation, verify the simulation against the analytic result, or use the framework for their own setting. The paper should write out the gap $\Delta(\beta, \rho, \sigma_c^2, m)$ explicitly under the simplest non-trivial case — say, $m$ exchangeable judges with common accuracy and beta-distributed confidence — and show that the simulation recovers the analytic value in that case.

**No practical procedure for computing the recommended shrinkage**

The paper recommends partial shrinkage toward equal weighting as the practical takeaway and shows that the oracle-optimal $\lambda^*$ is interior in 119 of 120 simulation cells. But it provides no method an aggregator could use to estimate $\lambda^*$ from a finite sample. The recommendation is actionable only if a practitioner knows how to get from data to a shrinkage parameter: a plug-in formula, a cross-validation scheme, a minimum calibration-set size, or a default value that is safe across the observed range. The first-pass review noted that estimated shrinkage is not tested against EW on the real data; the deeper gap is that no estimation procedure exists to test. The paper should specify at least one concrete method — for instance, leave-one-item-out cross-validation of $\lambda$ on the CW–EW mixture — report its performance on the 76 datasets, and state what sample size is needed for the estimate to be stable. Without this, 'shrink toward equal weighting' is advice without a recipe.

**No power analysis for the moderation nulls that drive the negative conclusion**

The rejection of the standard account (H5, H6) rests partly on the finding that neither the calibration slope nor the error correlation predicts whether CW helps, with coefficients near zero in OLS regressions on 76 datasets. The paper treats this as a substantive negative result — 'the harm does not vary with the calibration slope or the error correlation' — but does not report or discuss whether these tests had adequate power to detect moderation of the size the theory predicts. With 76 observations, restricted ranges of $\beta$ and $\rho$ (median 0.52 and 0.11 respectively, with many $\rho$ values near zero), and the outcome compressed by ceiling effects on sign accuracy, the detectable effect size may be large. If the simulation predicts moderation of, say, 0.01 per unit of $\beta$ and the standard error is 0.009, the null is uninformative rather than informative. The paper should compute the minimum detectable moderation effect at conventional power (80%) for these sample sizes and predictor distributions, and compare it to the moderation magnitude the simulation predicts. If the test could not have detected the predicted effect, the negative conclusion needs qualification.

**Recommendation**: Major revision. The paper addresses a well-defined practical question with a transparent, preregistered design, and the simulation boundary is a genuine contribution. But the empirical test has structural problems—the primary graded outcome measures the wrong target, the confirmatory outcome is ceiling-bound, and the model-rejection claim rests on a crude mapping—that together make the negative conclusions stronger than the evidence supports. A revision that fixes the outcome-target mismatch, properly conditions on task difficulty, and refines the simulation-data comparison could produce a convincing paper.

**Key revision targets**:

1. Separate the LOO-Brier analysis (predicting a held-out judge) from the truth-recovery question, either by constructing a truth-recovery graded measure or by explicitly restricting conclusions from the LOO analysis to the judge-prediction objective. If LOO-Brier is retained, explain formally why its sign should agree with the truth-recovery gap under the paper's own model.
2. Address the ceiling effect by conditioning the sign-accuracy analysis on items where the EW crowd is not already unanimous, or by reporting the gap as a proportion of available improvement. Discuss whether the Confidence Database tasks are representative of settings where CW is typically recommended.
3. Refine the model-reproduction test: simulate each dataset at its own estimated parameters (including confidence dispersion and group size) rather than snapping to a coarse grid, and report a continuous measure of fit rather than a binary sign match.
4. Decompose the calibration slope into within-item and between-judge components and test whether the within-item component predicts the CW advantage, as the theory requires.
5. Evaluate estimated shrinkage (with λ chosen on held-out data) against EW and CW in the empirical datasets, or remove the shrinkage recommendation from the abstract and conclusions.

**Status**: [Pending]

---

## Detailed Comments (16)

### 1. Positive significant CI contradicts 'negligible' characterization

**Status**: [Pending]

**Quote**:
> the decision advantage of CW is negligible (+0.004, 95% CI [0.0003, 0.0083], non-positive in 64% of datasets)

**Feedback**:
The abstract's own CI excludes zero on the positive side, making the decision advantage statistically significant by conventional standards. Calling this 'negligible' and then concluding CW is 'not a safe default' creates a tension the reader will notice: by the preregistered measure, CW is on average significantly better, not worse. The 64% non-positive figure is consistent with a small true positive effect plus high between-dataset variability — under a zero true effect with sampling noise, you would expect about 50%, so 64% is only modestly elevated. Arguing the effect is too small to matter practically is fine, but it needs an equivalence-testing framework or an explicit practical-significance threshold — the word 'negligible' applied to a CI that excludes zero does not do the job. Rewrite to something like: 'the decision advantage of CW is small and positive on average (+0.004, 95% CI [0.0003, 0.0083]), though non-positive in 64% of datasets' — then let the LOO-Brier result carry the negative conclusion while noting it is post-hoc.

---

### 2. Additive ability term functions as criterion bias, not sensitivity

**Status**: [Pending]

**Quote**:
> a persistent judge ability $a_j\sim N(0,0.7^2)$; a persistent judge overconfidence trait $o_j\sim N(0,1)$, independent of ability; and private noise $\varepsilon_{ji}\sim N(0,1)$. The judge's signal is $s_{ji}=\delta_i+u_i+a_j+\varepsilon_{ji}$, and the judgment is correct when $\mathrm{sign}(s_{ji})=T_i$.

**Feedback**:
For an item with truth +1 ($\delta_i = d > 0$), judge j is correct with probability $\Phi((d + a_j)/\sigma)$; for truth -1, correctness is $\Phi((d - a_j)/\sigma)$. Because $\Phi$ is strictly concave for positive arguments, adding $a_j \neq 0$ always lowers average accuracy across the two truth classes. Numerically: at $d = 0.5$, $\sigma = 1$, $a_j = 0.7$, average accuracy is $(\Phi(1.2) + \Phi(-0.2))/2 = 0.653$, versus $\Phi(0.5) = 0.691$ at $a_j = 0$. This is the signature of a criterion shift, not improved sensitivity — accuracy is maximized at $a_j = 0$. The downstream consequence matters more: since confidence depends on $|s_{ji}|$ and $a_j$ pushes $s$ away from zero for one truth class, judges with large $|a_j|$ report high confidence precisely when they are systematically wrong. This creates a structural negative association between mean confidence and accuracy at the judge level, penalizing CW beyond what genuine sensitivity heterogeneity would produce. A multiplicative formulation ($s_{ji} = k_j \delta_i + u_i + \varepsilon_{ji}$, $k_j > 0$) would give symmetric accuracy across truth values. Note that $a_j$ operates as a criterion shift and discuss whether the resulting confidence–accuracy structure limits the scope of the simulation's conclusions.

---

### 3. Calibration slope coefficient is in the predicted direction on the sign measure

**Status**: [Pending]

**Quote**:
> H5, which predicted that flatter calibration and higher error correlation would make CW worse, is not supported on either measure: the point estimates are near zero and, for the sign measure, in the opposite direction from the prediction.

**Feedback**:
H5 predicts that steeper calibration should make CW better (positive coefficient on the gap) and higher error correlation should make CW worse (negative coefficient). The sign-accuracy gap coefficient for calibration slope is +0.015 — positive, which is exactly the predicted direction. Only the error correlation coefficient (+0.010) is in the wrong direction (positive when it should be negative). Saying both are 'in the opposite direction from the prediction' mischaracterizes the calibration-slope result. Rewrite the clause to distinguish the two predictors: the calibration slope is in the predicted direction but far from significant (+0.015, SE 0.014), while the error-correlation coefficient runs weakly in the wrong direction (+0.010, SE 0.007).

---

### 4. Calibration-check advice contradicts the H5 finding

**Status**: [Pending]

**Quote**:
> of them. If confidence weighting is used at all, it should be justified on a calibration set where the analyst can check whether the confidence–accuracy slope is steep enough to matter, and it should be shrunk towards equal weighting, because an interior optimum was the rule in the simulation.

**Feedback**:
Two paragraphs earlier, the paper reports that neither the calibration slope nor the error correlation predicted whether CW helped (H5 failed). One paragraph earlier, it rejects the overconfidence mechanism. Advising practitioners to check whether the calibration slope is 'steep enough to matter' presupposes exactly the relationship that H5 found no evidence for. If the calibration slope did not predict CW success across 76 datasets spanning a range of slopes, a practitioner who measures it on a calibration set has no empirically supported threshold to apply. Rewrite as: 'it should be justified on a calibration set by directly comparing CW and EW accuracy, since the calibration slope alone did not predict the CW advantage in our data.' This removes the reliance on the rejected mechanism and gives advice grounded in the paper's own findings.

---

### 5. 'Exception rather than the norm' relies on the mechanism just rejected

**Status**: [Pending]

**Quote**:
> The classical argument for weighting remains valid in the regime it was derived for, well-calibrated and largely independent judges, but that regime appears to be the exception rather than the norm in the corpora we can observe.

**Feedback**:
This sentence explains CW's poor empirical performance by saying well-calibrated, independent judges are rare. That is precisely the account the previous paragraphs rejected: if calibration and independence governed CW success, H5 should have shown that higher calibration slope and lower error correlation predicted a larger CW advantage. It did not. The paper cannot simultaneously argue (a) that calibration and error correlation do not predict CW success and (b) that CW fails because calibration is insufficient and errors are too correlated. Rewrite as: 'but our data did not confirm that departures from that regime explain the failure of confidence weighting (H5), so additional mechanisms are likely at work.' This aligns the explanatory claim with the empirical finding.

---

### 6. Shrinkage universality claim rests on a very weak criterion

**Status**: [Pending]

**Quote**:
> In 119 of the 120 cells the accuracy-optimal shrinkage $\lambda^\star$ lies strictly between 0 and 1 for at least one group size (Figure 3), so partial shrinking beats both pure rules almost everywhere.

**Feedback**:
The qualifier 'for at least one group size' makes the 119/120 count far less informative than it sounds. A cell with 10 tested group sizes where the optimal shrinkage is interior for only one of them does not support the conclusion that 'partial shrinking beats both pure rules almost everywhere.' The criterion selects the weakest possible evidence within each cell. A more informative summary would report the median fraction of group sizes per cell where the optimum is interior, or the number of cells where it is interior across all tested group sizes. Without this, readers will infer near-universal superiority of shrinkage when the finding might be much more limited.

---

### 7. Dataset composition changes across group sizes, confounding the m-trend

**Status**: [Pending]

**Quote**:
> The **sign-accuracy gap** is the difference in the proportion of items on which the crowd decision is correct, CW minus EW, estimated at group sizes $m\in\{3,5,7,9,13,17,25,40\}$ not exceeding the dataset's median judges per item, by drawing 2,000 random subsets of distinct judges per item.

**Feedback**:
Because m cannot exceed a dataset's median judges per item, the set of contributing datasets changes at each group size. Datasets with fewer available judges drop out at higher m. Task difficulty, domain, and calibration quality likely covary with the number of available judges, so any trend of the gap across m confounds group size with dataset characteristics. This matters for interpreting Figure 1a and for the prediction in Section 2.2 that the gap grows with m under favorable calibration. State whether results are also reported within the subset of datasets that support all evaluated m values, or at minimum note the confound.

---

### 8. Step-level evidence does not support the cell-level characterization of non-monotonicity

**Status**: [Pending]

**Quote**:
> 289 of 1,080 steps exceed the Monte-Carlo tolerance in the decreasing direction, so H2 is not supported and the relation is non-monotone in a substantial minority of cells.

**Feedback**:
The evidence is at the step level (289 of 1,080 pairwise transitions between adjacent group sizes), but the conclusion is drawn at the cell level ('non-monotone in a substantial minority of cells'). If those 289 decreasing steps are spread across 100 of the 120 cells, non-monotonicity is pervasive, not a 'substantial minority.' If concentrated in 30 cells, the characterization holds. The 'so' in this sentence makes an inferential jump that the data do not support without the cell-level count. Report how many cells (out of 120) exhibit at least one decreasing step exceeding Monte-Carlo tolerance.

---

### 9. Between-person correlation cited as evidence for within-item claim

**Status**: [Pending]

**Quote**:
>  Reported confidence is exactly such a signal, and it is only weakly related to accuracy: pooling 145 datasets, Jin, Verhaeghen and Rahnev (2022) found a positive but modest confidence–accuracy correlation. Empi

**Feedback**:
The paper's own reference list gives the title of Jin et al. (2022) as 'Across-subject correlation between confidence and accuracy.' This is a between-subject association — some people are both more confident and more accurate overall — not the within-item discrimination that determines whether CW helps on any given item. A strong within-item relationship can coexist with a weak between-person correlation when individual calibration styles add noise to the cross-person summary. Citing the between-subject metric as evidence that confidence 'is only weakly related to accuracy' in a paragraph motivating the failure of CW elides this distinction. Specify what level of analysis the Jin et al. correlation captures and note whether it speaks to the within-item confidence–accuracy relationship that CW actually requires.

---

### 10. Cell-averaging of trials changes the estimand from the single-trial theory

**Status**: [Pending]

**Quote**:
> judge's **vote** in an item is the mean of $2\times\mathrm{correct}-1$ over her trials in it, and her **confidence** is the mean rating, min–max normalised within the dataset. This uses

**Feedback**:
Section 2 assumes each judge makes one binary judgment per item and reports one confidence rating. Here, both the vote and the confidence are means over potentially many trials by the same judge in the same condition cell. When the number of within-cell trials is large, the vote becomes near-continuous in [-1, 1] rather than binary, and the confidence becomes a smoothed average rather than a per-judgment report. This is a separate concern from whether judges share the same physical stimulus — the averaging changes the statistical problem even if every trial in the cell presents an identical stimulus. How much this matters depends on the number of trials per judge per cell, but that quantity is never reported. Add the distribution of trials per judge per item (median and IQR across datasets) so readers can assess how far the empirical setup departs from the single-trial theory.

---

### 11. 'Points the same way' mischaracterises the divergence between the two measures

**Status**: [Pending]

**Quote**:
> the preregistered result is reported throughout and points the same way

**Feedback**:
The preregistered sign-accuracy gap has a positive mean with a CI excluding zero: by this measure, CW helps on average. The exploratory LOO-Brier result is negative in 91% of datasets: by that measure, CW hurts almost universally. Saying the preregistered result 'points the same way' conflates the dataset-level majority (64% non-positive) with the average effect (significantly positive). The two measures give opposite answers to 'does CW help on average,' and readers relying on this sentence will underestimate how much the headline conclusion depends on the exploratory measure. Rewrite as: 'the preregistered result is reported throughout; its average is weakly positive but non-positive in 64% of datasets, consistent with a negligible practical benefit even though the two measures diverge on the average sign.'

---

### 12. Variance cost presentation omits how correlation modulates it

**Status**: [Pending]

**Quote**:
> With $m$ judges whose residual variances are comparable, the first term falls as $\sum_j w_j^2$, so a more unequal weighting raises the variance at fixed $m$; CW therefore pays a variance cost the EW estimate does not.

**Feedback**:
Under the exchangeable setup the paper describes, the CW-minus-EW variance cost is $(1-\rho)(\sum w_j^2 - 1/m)\sigma^2$, which is positive for $\rho < 1$ but shrinks linearly in $\rho$ and vanishes at $\rho = 1$. The paragraph attributes the variance cost to the diagonal term and then discusses the error correlation only via the gain channel ('reweighting within the item shuffles a quantity whose average is already set by the shared component'). The qualitative conclusion is correct — CW does pay a positive variance cost when $\rho < 1$ — but the incomplete picture could mislead readers about how correlation enters the trade-off. Add a clause noting that the cost is modulated by $(1-\rho)$: the off-diagonal covariance is smaller for more unequal weights, partly offsetting the diagonal increase, so the net variance cost vanishes as $\rho \to 1$.

---

### 13. Symmetric trait distribution models miscalibration, not directional overconfidence

**Status**: [Pending]

**Quote**:
> The parameter $\gamma$ sets how sharply confidence tracks correctness, $\phi$ is overconfidence (confidence not diagnostic of accuracy), and $\tau$ drives the within-item error correlation $\rho$.

**Feedback**:
With $o_j \sim N(0,1)$, roughly half the judges have inflated confidence and half have deflated confidence. The parameter $\phi$ scales this symmetric spread, degrading CW by making weights noisy rather than systematically biased upward. Population-level overconfidence — confidence systematically exceeding accuracy — would require $E[o_j] > 0$ or a skewed distribution. The abstract then generalizes 'overconfidence reverses the graded effect' from a mechanism (symmetric miscalibration adding weight noise) to a phenomenon (directional overconfidence) that the model does not implement. Min-max normalization partly absorbs the mean of $o_j$, so the practical gap between symmetric and asymmetric miscalibration may be smaller than it first appears. Still, the label should match the mechanism. Rewrite '$\phi$ is overconfidence' as '$\phi$ scales confidence miscalibration' and note once — here or in the discussion — that the simulation tests symmetric miscalibration rather than directional overconfidence.

---

### 14. Ridge penalty and unit of observation are unspecified

**Status**: [Pending]

**Quote**:
> We estimate per dataset the calibration slope $\beta$ (ridge-penalised logistic regression of correctness on standardised confidence, robust to separation)

**Feedback**:
The ridge penalty directly controls how much the calibration slope is shrunk toward zero, so different values produce materially different estimates of β. These β values feed into the moderation analysis testing whether calibration predicts the CW advantage (H5), so the penalty choice affects the downstream conclusions. The unit of observation — individual trial, judge–item cell, or judge-level aggregate — is also left unstated, though each implies a different effective sample size and standard-error structure. State the penalty value (or the selection rule, e.g., 10-fold cross-validation of the deviance) and the unit of observation.

---

### 15. '79% baseline for the graded measure' is ambiguous in the abstract

**Status**: [Pending]

**Quote**:
> the calibrated simulation does not reproduce the data (36% agreement with the decision gap, against a 79% baseline for the graded measure)

**Feedback**:
The parenthetical is hard to parse. A reader unfamiliar with the paper cannot tell whether '79%' means (a) the simulation correctly predicts the graded measure's sign in 79% of datasets, (b) the graded measure is negative in 79% of datasets, making majority-class prediction a trivially achievable baseline, or (c) some other reference point. From Section 4.2, interpretation (b) appears correct — 'the trivial rule of predicting a negative effect for every dataset reaches 79%' — but the abstract does not say this. If (b) is the meaning, then the 36% agreement on the decision gap should be compared against its own baseline too. State plainly what both numbers represent: e.g., 'the simulation predicts the sign of the decision gap in 36% of datasets (chance: X%) and the sign of the graded gap in Y% (trivial-rule baseline: 79%).'

---

### 16. Clipping analysis reveals a pattern, not just robustness

**Status**: [Pending]

**Quote**:
> The result is robust to clipping confidence to its 5th–95th percentile, where the improvement is −0.0007 and negative in 97% of datasets.

**Feedback**:
The paper frames this as confirming robustness, but the result is actually stronger after clipping: the share of datasets where CW hurts goes from 91% to 97%, and the mean Brier improvement shifts from -0.0006 to -0.0007. Clipping removes the most extreme confidence values, which should reduce any weight-estimation noise from outliers — if anything, this should give CW a better shot under the overconfidence account. The fact that CW does slightly worse after clipping suggests the disadvantage lives in the body of the confidence distribution, not just its tails. One sentence interpreting the direction of the change — not just noting that the sign persists — would sharpen what this robustness check tells the reader about mechanism.

---
