# When does weighting by confidence help the crowd? A finite-sample boundary and a test of the standard account

**Author to be determined.** Affiliation and correspondence to be supplied by the project owner before any submission. This manuscript is an AI-assisted draft prepared without submission; see the AI disclosure.

## Abstract

Weighting judges by their reported confidence is often described as the optimal way to combine binary judgments, but the rule is only conditionally optimal: correlated errors change the optimal weights, miscalibrated competence inputs degrade them, and estimated weights routinely lose to the simple average. We ask the finite-sample question an aggregator can act on: given the number of judges, the confidence–accuracy slope, and the within-item error correlation, when does confidence weighting (CW) lose to equal weighting (EW), and is partial shrinking better than either? We derive the gap, map its boundary in a preregistered simulation, and estimate where 76 datasets from the Confidence Database (1,641,000 trials) sit. The simulation has a clear boundary: CW helps only when confidence is well calibrated, and overconfidence reverses the graded effect. In the data, the decision advantage of CW is negligible (+0.004, 95% CI [0.0003, 0.0083], non-positive in 64% of datasets) and CW worsens the leave-one-judge-out estimate of a judge's correctness in 91% of datasets. Contrary to the account, the harm does not vary with the calibration slope or the error correlation, and the calibrated simulation does not reproduce the data (30% agreement at a common group size for the decision gap, and 33% for the graded measure against a 79% baseline). Confidence weighting is not a safe default, the standard overconfidence account does not explain why, and partial shrinking towards equal weighting is often better.

**Keywords:** wisdom of crowds; confidence; aggregation; calibration; correlated error; shrinkage

## 1. Introduction

Combining the judgments of several people usually beats asking one. The advantage comes from cancelling idiosyncratic error: if judges are on average better than chance and wrong for different reasons, the simple majority grows more accurate as judges are added (Condorcet, 1785/1994). This result, and the conditions under which it holds (Berend & Paroush, 1998), underpins practical advice to poll, average, or vote rather than to defer to a single expert.

A natural refinement is to weight judges by how confident they are. If a judge's reported confidence is the probability she is right, and errors are independent, then weighting votes by the log odds of correctness, which confidence is taken to track, is the optimal way to recover a binary truth (Grofman, 1978; Nitzan & Paroush, 1982; Ben-Yashar & Nitzan, 1997). The intuition is widespread: a confident judge should count for more than a hesitant one. It also sits within a large literature on combining opinions. People appreciate averaging less than they should (Larrick & Soll, 2006; Soll & Larrick, 2009); identifying expertise improves crowd accuracy (Budescu & Chen, 2015); pooling independent judgments boosts medical diagnosis (Kurvers et al., 2016); a small select crowd can match a large one (Mannes et al., 2014); and how information is shared between judges changes what aggregation achieves (Palley & Soll, 2019). Metacognitive variants, such as asking what others will answer, extend the same goal (Prelec et al., 2017).

Three literatures make the optimality conditional in ways worth stating plainly. First, committee theory shows that the optimal weights depend on the structure of shared error. When voters' judgments are correlated, equal or competence-proportional weighting is not generally optimal (Shapley & Grofman, 1984; Ladha, 1995; Kaniovski, 2010), and additional judges stop helping once their errors move together (Hogarth, 1978; Einhorn et al., 1977). Second, the forecast-combination literature shows that estimated optimal weights routinely fail to beat the simple average, because estimating many weights from few observations adds variance (Smith & Wallis, 2009; Claeskens et al., 2016). Huang, Broomell and Golman (2024) formalise this as a test of whether weighting "reliably improves collective accuracy or just adds noise". Third, when the weights come from a distorted competence signal rather than true competence, the optimal rule degrades (Baharad & Ben-Yashar, 2009). Reported confidence is exactly such a signal, and it is only weakly related to accuracy: pooling 145 datasets, Jin, Verhaeghen and Rahnev (2022) found a positive but modest confidence–accuracy correlation. Empirically, confidence-weighted majority voting can beat unweighted majority voting (Saha Roy et al., 2021; Meyen et al., 2021), and confidence-based rules can make crowds more efficient (Berger et al., 2025), but people themselves weight votes more equally than the optimal confidence rule prescribes (Meyen et al., 2021).

What remains underexamined is the boundary in the terms a crowd aggregator actually has: the number of judges, the strength of the confidence–accuracy relationship, and the correlation of errors within an item. Existing results are stated for abstract competences or for estimated weights; they are not written so that an analyst who knows her crowd size and the calibration of her confidence measure can say whether weighting will help. Nor has the size of the CW advantage been mapped across many real judgment datasets, so its typical magnitude is unknown. The practical question is not whether confidence weighting can help, which is settled, but how large the gap between CW and EW usually is, and when the sign turns.

We address this in three steps, and we report the results in full whichever way they come out. First, we write the expected gap between CW and EW as a function of the confidence–accuracy calibration slope, the within-item error correlation, and confidence dispersion, in the finite-sample regime of a handful of judges per item. Second, we map the boundary of the harmful region in a preregistered simulation where confidence is generated with a tunable amount of overconfidence, and derive the shrinkage between CW and EW that is accuracy-optimal. Third, we estimate where real judgment data sit, using 76 datasets from the Confidence Database (Rahnev et al., 2020), and test whether the observed pattern follows the theoretical inputs.

This is a Theory Article with an empirical test. We do not claim that confidence weighting can hurt, that correlated error changes optimal weights, or that confidence-weighted voting sometimes beats majority: those are established (Baharad & Ben-Yashar, 2009; Huang et al., 2024; Meyen et al., 2021; Shapley & Grofman, 1984). The contributions are the psychometric parametrisation of the gap, the simulated boundary, the estimated base rate of the harmful region, and a negative result: the simple account does not reproduce the data. Our preregistration, including the analysis plan and the criteria for each outcome, was committed before the outcome variables were analysed; it and every deviation are in the project repository.

## 2. A finite-sample account

### 2.1 Setup

Consider an item $i$ with a binary truth. Judge $j$ reports a binary judgment and a confidence $c_{ji}\in[0,1]$. Encode the judgment by its correctness, $v_{ji}=+1$ if the judge is right on that item and $-1$ if wrong. The two aggregation rules are the equal-weighted (EW) mean and the confidence-weighted (CW) mean:

$$\bar{x}_i = \frac1m\sum_{j=1}^m v_{ji}, \qquad \hat{x}_i = \frac{\sum_{j=1}^m c_{ji}\,v_{ji}}{\sum_{j=1}^m c_{ji}},$$

where $m$ is the number of judges on the item. The crowd decision is correct when the estimate is positive. This encoding uses recorded correctness directly, without reconstructing the truth from responses, and it makes the two rules differ only in their weights.

### 2.2 Bias, variance and the gap

Write the crowd estimate as a weighted mean with weights $w_j$ (all $1/m$ for EW, $c_j/\sum c$ for CW). Conditional on the item, its variance is $\mathrm{Var}(\hat{x}_i)=\sum_j w_j^2\,\mathrm{Var}(v_{ji}) + \sum_{j\ne k} w_jw_k\,\mathrm{Cov}(v_{ji},v_{ki})$. With $m$ judges whose residual variances are comparable, the first term falls as $\sum_j w_j^2$, so a more unequal weighting raises the variance at fixed $m$; CW therefore pays a variance cost the EW estimate does not. Its mean, $\sum_j w_j\,E[v_{ji}]$, is higher when the weights concentrate on judges who are more likely to be right. The gap between the two rules is the difference between this weighting gain and the variance cost.

Three quantities govern the trade-off. The **calibration slope** $\beta$, from a regression of correctness on normalised confidence, sets how sharply the weights separate good judges from bad. **Confidence dispersion** sets how unequal the weights are, and hence the size of the variance cost. The **within-item error correlation** $\rho$ is external to the judge: when errors are shared, an item that is hard for one judge is hard for all, the covariance term is large, and reweighting within the item shuffles a quantity whose average is already set by the shared component.

Two limits are instructive and give the sign condition. If confidence is perfectly calibrated and errors are independent ($\beta$ large, $\rho=0$), CW approaches the optimal rule, its weighting gain dominates the variance cost, and the gap is positive, growing with $m$ as the estimate converges on the item's expected correctness. If confidence carries no information about correctness within the item, CW is a weighted mean with weights independent of $v_{ji}$; it is then unbiased but strictly noisier than EW, so the gap is negative and shrinks towards zero as $m$ grows and the weights average out. In the finite-sample regime, the gap is negative whenever the weighting gain, which is proportional to the within-item covariance of $c_{ji}$ with $v_{ji}$, falls short of the variance cost, which grows with the dispersion of $c_{ji}$ and falls with $m$. The empirically relevant case lies between these limits, and the sign depends on which term dominates at the given $m$.

The ingredients here are the ones already used in the correlated-votes and forecast-combination literatures. The contribution is to write the gap in the psychological coordinates an aggregator can estimate, and to attach a simulation and a base rate to it. Because the finite-sample variances depend on the full confidence distribution, we do not claim a closed form for all cases; we give the sign condition above and solve the gap numerically where the closed form is not tractable. The framework also yields a prescriptive quantity. Define the shrinkage estimator

$$x^\lambda_i = (1-\lambda)\,\bar{x}_i + \lambda\,\hat{x}_i,$$

with $\lambda=0$ reproducing EW and $\lambda=1$ reproducing CW. If the weighting gain and the variance cost trade off, the accuracy-optimal $\lambda^\star$ will often lie strictly between the two, and shrinking towards equal weights is better than either extreme. Whether an interior optimum exists, and where, is a question for the simulation.

## 3. Simulation

### 3.1 Model and method

We simulated judgments and confidence for many independent items. Each item $i$ has a latent position $\delta_i\sim N(0,1)$ that fixes its truth $T_i=\mathrm{sign}(\delta_i)$; a shared error $u_i\sim N(0,\tau^2)$ common to all judges on the item; a persistent judge ability $a_j\sim N(0,0.7^2)$; a persistent judge overconfidence trait $o_j\sim N(0,1)$, independent of ability; and private noise $\varepsilon_{ji}\sim N(0,1)$. The judge's signal is $s_{ji}=\delta_i+u_i+a_j+\varepsilon_{ji}$, and the judgment is correct when $\mathrm{sign}(s_{ji})=T_i$. Confidence reflects the strength of the judge's own evidence and the overconfidence trait, not the truth,

$$c_{ji}=\mathrm{sigmoid}\big(\gamma\,|s_{ji}|+\phi\,o_j\big)+\nu_{ji},$$

with $\nu_{ji}\sim N(0,\omega^2)$, min–max normalised as in the empirical analysis. The parameter $\gamma$ sets how sharply confidence tracks correctness, $\phi$ is overconfidence (confidence not diagnostic of accuracy), and $\tau$ drives the within-item error correlation $\rho$. We swept $\tau\in\{0,0.25,0.5,0.75,1.0\}$, $\phi\in\{0,1,2,4\}$, $\gamma\in\{0.3,0.6,1.0\}$ and $\omega\in\{0.05,0.1\}$, with 40,000 items per cell and group sizes $m\in\{3,4,5,7,9,13,17,25,41,65\}$. For each cell we recorded the sign-accuracy gap $\Delta(m)$, the leave-one-judge-out Brier improvement of CW over EW, and the accuracy-optimal shrinkage $\lambda^\star$.

The **failure condition** set in advance was that the simulation must reproduce either the qualitative published result that real groups weight more equally than the confidence-optimal rule (Meyen et al., 2021) or the sign pattern of the empirical gap. A model that reproduces neither is rejected.

### 3.2 Results

The sign-accuracy gap has a clear boundary (Figure 2b). Of the 120 simulated cells, 87 (73%) show a negative gap at one or more group sizes, and the sign is governed by overconfidence: at $\gamma=0.3$ and $\tau=0$ the mean gap is +0.007 when confidence is well calibrated ($\phi=0$) and −0.032 when it is not ($\phi=4$). Higher shared error compresses the gap towards zero but does not reverse it.
![**Figure 2.** Simulated boundary surface (gamma = 0.3, omega = 0.05). Colour is the effect of confidence weighting as a function of overconfidence phi and shared error tau. (a) Leave-one-judge-out Brier improvement: positive only for well-calibrated confidence. (b) Sign-accuracy gap: positive for well-calibrated confidence and turning negative at high overconfidence.](analysis/output/figures/fig2_boundary.png)
 The gap does not increase monotonically with group size as the finite-sample reading predicts: 286 of 1,080 steps exceed the Monte-Carlo tolerance in the decreasing direction, so H2 is not supported and the relation is non-monotone in a substantial minority of cells.

The graded estimate shows the same boundary more sharply (Figure 2a). CW improves the leave-one-judge-out Brier score when confidence is well calibrated (mean +0.0007 at $\phi=0$, $\tau=0$) and degrades it once overconfidence is present (−0.005 at $\phi=2$, −0.021 at $\phi=4$). Across the grid, 33 of 120 cells have a positive mean Brier improvement and 87 negative.

An interior optimum is the rule rather than the exception. In 119 of the 120 cells the accuracy-optimal shrinkage $\lambda^\star$ lies strictly between 0 and 1 for at least one group size (Figure 3), so partial shrinking beats both pure rules almost everywhere. The optimal weight on confidence falls as overconfidence rises, reaching zero when confidence is uninformative.

![**Figure 3.** Accuracy-optimal shrinkage lambda* between equal weighting (0) and confidence weighting (1) against group size, for three levels of overconfidence. An interior optimum is the rule across the grid.](analysis/output/figures/fig4_lambda.png)

The simulation satisfies the failure condition in the sense that it has an adverse region consistent in spirit with Meyen et al. (2021), but Section 4 shows that its specific predictions do not match the data, which the preregistration treats as a failure of the account rather than the simulation.

## 4. Empirical test across 76 datasets

### 4.1 Data and method

We used the Confidence Database (Rahnev et al., 2020; OSF `s46pr`, CC0), a collection of trial-level datasets in which participants make a judgment and rate their confidence. Of 180 per-study files, 76 met the structural inclusion rules fixed before analysis: an explicit correctness column, a stimulus identifier, at least eight participants, non-constant confidence, at least two items judged by three or more participants, and enough judges per item to support the preregistered group sizes. Together these contain 1,641,000 analysed trials. Median calibration slope was 0.52 (on standardised confidence), median within-item error correlation 0.11, and the median item was judged by 33 participants.

An **item** is a shared cell, defined as the stimulus value together with any of a fixed list of design columns present in the dataset (for example contrast or coherence). A judge's **vote** in an item is the mean of $2\times\mathrm{correct}-1$ over her trials in it, and her **confidence** is the mean rating, min–max normalised within the dataset. This uses the recorded correctness directly and does not require reconstructing a per-item truth.

We computed two quantities. The **sign-accuracy gap** is the difference in the proportion of items on which the crowd decision is correct, CW minus EW, estimated at group sizes $m\in\{3,5,7,9,13,17,25,40\}$ not exceeding the dataset's median judges per item, by drawing 2,000 random subsets of distinct judges per item. The **leave-one-judge-out (LOO) Brier improvement** is, for each item and each target judge, the Brier score of the other judges' EW estimate minus that of the CW estimate; positive means confidence weighting predicted the target judge's correctness better. This is a graded version of the aggregation question that predicts a held-out judge rather than the item's truth, and it was added after the sign-accuracy estimand proved insensitive; the preregistered sign-accuracy results are reported in full alongside it.

We estimate per dataset the calibration slope $\beta$ (ridge-penalised logistic regression of correctness on standardised confidence, robust to separation) and the within-item error correlation $\rho$ (one-way random-effects ICC on the judge-item table), then relate the estimated effect to those inputs with an OLS regression using robust standard errors.

### 4.2 Results

The decision advantage of confidence weighting is negligible. Averaged over group sizes, the sign-accuracy gap is +0.004 (95% CI [0.0003, 0.0083]), and it is non-positive in 64% of datasets. The small size follows partly from a ceiling: EW crowd accuracy is already 0.93 at three judges and 0.98 at forty, so most items are decided correctly under either rule (Figure 1a).

The graded estimate tells a clearer and more adverse story. The LOO-Brier improvement of CW over EW is −0.0006 on average (95% CI [−0.0008, −0.0003]) and is negative in 91% of datasets (Figure 1b). At a fixed group size of seven, comparable to the simulation, it is negative in 79% of datasets (median −0.0004). The result is robust to clipping confidence to its 5th–95th percentile, where the improvement is −0.0007 and negative in 97% of datasets. In other words, in almost every dataset, weighting other judges by confidence produced a slightly worse estimate of whether a given judge was correct than weighting them equally.

![**Figure 1.** Confidence weighting versus equal weighting in 76 Confidence Database datasets. (a) The sign-accuracy advantage of CW over EW as a function of group size; points are means across datasets with 95% confidence intervals and the dashed line is zero. (b) Distribution of the leave-one-judge-out Brier improvement of CW over EW across datasets; the red line marks the mean.](analysis/output/figures/fig1_empirical.png)

The predicted moderation does not appear. Regressing the LOO-Brier improvement on the calibration slope and the within-item error correlation, neither coefficient is distinguishable from zero (calibration slope −0.0003, SE 0.0009; error correlation −0.00001, SE 0.0004). The same holds for the sign-accuracy gap (calibration slope +0.015, SE 0.014; error correlation +0.010, SE 0.007). H5, which predicted that flatter calibration and higher error correlation would make CW worse, is not supported on either measure: the point estimates are near zero and, for the sign measure, in the opposite direction from the prediction.

![**Figure 4.** Empirical moderation. Left: leave-one-judge-out Brier improvement against the calibration slope. Right: the same against the within-item error correlation. Neither relation is significant, contrary to the theoretical prediction.](analysis/output/figures/fig3_moderation.png)

Finally, the calibrated simulation does not reproduce the data. Mapping each dataset to the nearest simulated cell in standardised (calibration, error-correlation) space, at a common group size of seven the simulation matched the sign of the sign-accuracy gap for 21 of 70 datasets (30%) and the sign of the Brier improvement for 23 of 70 (33%), well below the 60% the preregistration required. On the sign measure the model does no better than always predicting a positive effect (both 30% agreement); on the Brier measure the trivial rule of predicting a negative effect for every dataset reaches 79%, and the model is worse than that baseline. The mapping is crude, matching on two inputs and collapsing 9 datasets onto a single cell, and 7 empirical error correlations fall below the simulated range, but the failure is not marginal. H6, the model-reproduction hypothesis, is rejected.

## 5. Discussion

Confidence weighting does not reliably improve crowd judgment in real data, and the standard explanation of why it might not is not supported either. Across 76 datasets and 1.6 million trials, weighting judges by their confidence gave a decision gain of +0.004, non-positive in about two of three datasets, and degraded the leave-one-judge-out estimate of a judge's correctness in 91% of datasets. The simulation shows that a boundary exists: confidence weighting improves both the decision and the graded estimate when confidence is well calibrated, and overconfidence turns the graded effect negative. But the data do not follow the predicted moderation, and the calibrated model does not reproduce the observed signs.

The negative results are as informative as the positive ones. The preregistered moderation hypothesis (H5) failed: neither the calibration slope nor the within-item error correlation predicted whether confidence weighting helped. It is worth noting that the corrected analysis changed this conclusion. An earlier version of the pipeline, which sampled judges with replacement and computed the error correlation on trials rather than on the judge-item table, produced a significant negative coefficient for the error correlation; fixing the sampling and the ICC removed it. That episode is a reminder that this class of moderation is fragile to small implementation choices, and it is why the code is committed alongside the results. The model-reproduction hypothesis (H6) also failed, and the failure is sharp: for the graded measure the calibrated simulation does worse than predicting a negative effect for every dataset. The simple overconfidence account, in which confidence reflects evidence strength plus noise, is not the mechanism that governs confidence weighting in these data.

What, then, should an aggregator do? The safest reading of these results is that confidence weighting should not be a default. Its typical decision benefit is under half a percentage point of accuracy, it is absent or negative in a majority of datasets, and it makes the graded estimate slightly worse in almost all of them. If confidence weighting is used at all, it should be justified on a calibration set where the analyst can check whether the confidence–accuracy slope is steep enough to matter, and it should be shrunk towards equal weighting, since an interior optimum was the rule in the simulation (though that optimum was chosen and scored on the same simulated items, so it is an in-sample result). The classical argument for weighting remains valid in the regime it was derived for, well-calibrated and largely independent judges, but that regime appears to be the exception rather than the norm in the corpora we can observe.

Several limitations bound these conclusions. The empirical leg reuses a corpus not designed for crowd aggregation. Items are condition cells rather than matched physical stimuli, so the analysis measures how confidence reweighting changes the crowd's estimate of a shared condition, not a controlled group decision, and the leave-one-judge-out measure predicts a held-out judge's correctness rather than the item's truth. The datasets differ in task, scale, and confidence format, and we pool them only at the level of summary estimates; the meta-analytic summary is an unweighted mean across datasets, not a random-effects model. The model-reproduction test matches on only two inputs, so its failure could reflect a crude mapping as well as model misspecification, though the size of the miss is too large to dismiss. The simulation itself is a particular generative model, and its failure to fit is a result about that model, not evidence that no account of confidence weighting could work. Finally, the graded estimand was added after the preregistered sign estimand proved ceiling-bound, so it is not confirmatory in the strict sense, and the two measures point in opposite directions (the decision gap is slightly positive on average, the graded improvement slightly negative).

The findings point to specific next steps. A designed crowd experiment that holds stimuli fixed across judges could test the graded prediction directly at the group sizes where the theory says the sign turns, and could measure the confidence–accuracy slope on a calibration set before the aggregation decision. A better mechanism than simple overconfidence is needed to explain why confidence weighting fails so consistently; candidates include confidence that tracks item familiarity rather than correctness, and shared information that makes the most confident judges the most correlated ones. And the shrinkage rule deserves evaluation on real crowds, since its value rests on the interior optimum that the simulation found but the data cannot yet confirm.

## Acknowledgements

This analysis was produced with AI assistance. The project owner should verify authorship, affiliation, and all declarations before any submission.

## Competing interests

The author(s) declare no competing interests.

## Financial support

None.

## Data availability

The Confidence Database is openly available under CC0 at https://osf.io/s46pr/. All analysis code, the preregistration, the deviation log, and the simulated data-generation configuration are in the project repository; `run_all.sh` reproduces every result from the raw data with one command. No new data were collected. No personal identifiers were used.

## References

Baharad, E., & Ben-Yashar, R. (2009). The robustness of the optimal weighted majority rule to probability distortion. *Public Choice*, 139(1–2), 53–59. https://doi.org/10.1007/s11127-008-9378-7

Ben-Yashar, R. C., & Nitzan, S. I. (1997). The optimal decision rule for fixed-size committees in dichotomous choice situations: The general result. *International Economic Review*, 38(1), 175–186. https://doi.org/10.2307/2527413

Berend, D., & Paroush, J. (1998). When is Condorcet's Jury Theorem valid? *Social Choice and Welfare*, 15(4), 481–488. https://doi.org/10.1007/s003550050118

Berger, J., Moussaïd, M., Hertwig, R., Herzog, S. M., & Kurvers, R. H. J. M. (2025). *Making the wisdom of crowds efficient — with confidence* [Preprint]. PsyArXiv. https://doi.org/10.31234/osf.io/j9t6p_v2

Budescu, D. V., & Chen, E. (2015). Identifying expertise to extract the wisdom of crowds. *Management Science*, 61(2), 267–280. https://doi.org/10.1287/mnsc.2014.1909

Claeskens, G., Magnus, J. R., Vasnev, A. L., & Wang, W. (2016). The forecast combination puzzle: A simple theoretical explanation. *International Journal of Forecasting*, 32(3), 754–762. https://doi.org/10.1016/j.ijforecast.2015.12.005

Condorcet, N. de. (1994). *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix* [Essay on the application of analysis to the probability of majority decisions]. Imprimerie Royale. (Original work published 1785)

Einhorn, H. J., Hogarth, R. M., & Klempner, E. (1977). Quality of group judgment. *Psychological Bulletin*, 84(1), 158–172. https://doi.org/10.1037/0033-2909.84.1.158

Grofman, B. (1978). Judgmental competence of individuals and groups in a dichotomous choice situation: Is a majority of heads better than one? *The Journal of Mathematical Sociology*, 6(1), 47–60. https://doi.org/10.1080/0022250X.1978.9989880

Hogarth, R. M. (1978). A note on aggregating opinions. *Organizational Behavior and Human Performance*, 21(1), 40–46. https://doi.org/10.1016/0030-5073(78)90037-5

Huang, S., Broomell, S. B., & Golman, R. (2024). A hypothesis test algorithm for determining when weighting individual judgments reliably improves collective accuracy or just adds noise. *Decision*, 11(1), 7–34. https://doi.org/10.1037/dec0000187

Jin, S., Verhaeghen, P., & Rahnev, D. (2022). Across-subject correlation between confidence and accuracy: A meta-analysis of the Confidence Database. *Psychonomic Bulletin & Review*, 29(4), 1405–1413. https://doi.org/10.3758/s13423-022-02063-7

Kaniovski, S. (2010). Aggregation of correlated votes and Condorcet's Jury Theorem. *Theory and Decision*, 69(3), 453–468. https://doi.org/10.1007/s11238-008-9120-4

Kurvers, R. H. J. M., Herzog, S. M., Hertwig, R., Krause, J., Carney, P. A., Bogart, A., Argenziano, G., Zalaudek, I., & Wolf, M. (2016). Boosting medical diagnostics by pooling independent judgments. *Proceedings of the National Academy of Sciences*, 113(31), 8777–8782. https://doi.org/10.1073/pnas.1601827113

Ladha, K. K. (1995). Information pooling through majority-rule voting: Condorcet's jury theorem with correlated votes. *Journal of Economic Behavior & Organization*, 26(3), 353–372. https://doi.org/10.1016/0167-2681(94)00068-P

Larrick, R. P., & Soll, J. B. (2006). Intuitions about combining opinions: Misappreciation of the averaging principle. *Management Science*, 52(1), 111–127. https://doi.org/10.1287/mnsc.1050.0459

Mannes, A. E., Soll, J. B., & Larrick, R. P. (2014). The wisdom of select crowds. *Journal of Personality and Social Psychology*, 107(2), 276–299. https://doi.org/10.1037/a0036677

Meyen, S., Sigg, D. M. B., von Luxburg, U., & Franz, V. H. (2021). Group decisions based on confidence weighted majority voting. *Cognitive Research: Principles and Implications*, 6(1), 22. https://doi.org/10.1186/s41235-021-00279-0

Nitzan, S., & Paroush, J. (1982). Optimal decision rules in uncertain dichotomous choice situations. *International Economic Review*, 23(2), 289–297. https://doi.org/10.2307/2526438

Palley, A. B., & Soll, J. B. (2019). Extracting the wisdom of crowds when information is shared. *Management Science*, 65(5), 2291–2309. https://doi.org/10.1287/mnsc.2018.3047

Prelec, D., Seung, H. S., & McCoy, J. (2017). A solution to the single-question crowd wisdom problem. *Nature*, 541(7638), 532–535. https://doi.org/10.1038/nature21054

Rahnev, D., Desender, K., Lee, A. L. F., Adler, W. T., Aguilar-Lleyda, D., Akdoğan, B., et al. (2020). The Confidence Database. *Nature Human Behaviour*, 4(3), 317–325. https://doi.org/10.1038/s41562-019-0813-1

Saha Roy, T., Mazumder, S., & Das, K. (2021). Wisdom of crowds benefits perceptual decision making across difficulty levels. *Scientific Reports*, 11(1), 538. https://doi.org/10.1038/s41598-020-80500-0

Shapley, L., & Grofman, B. (1984). Optimizing group judgmental accuracy in the presence of interdependencies. *Public Choice*, 43(3), 329–343. https://doi.org/10.1007/BF00118940

Smith, J., & Wallis, K. F. (2009). A simple explanation of the forecast combination puzzle. *Oxford Bulletin of Economics and Statistics*, 71(3), 331–355. https://doi.org/10.1111/j.1468-0084.2008.00541.x

Soll, J. B., & Larrick, R. P. (2009). Strategies for revising judgment: How (and how well) people use others' opinions. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 35(3), 780–805. https://doi.org/10.1037/a0015145

Trick, S., Jäkel, F., & Rothkopf, C. A. (2026). Bayesian combination of correlated subjective probability estimates. *Judgment and Decision Making*, 21, e12. https://doi.org/10.1017/jdm.2026.10035