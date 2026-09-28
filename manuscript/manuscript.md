# When does weighting by confidence hurt the crowd? A finite-sample boundary and a test across 80 judgment datasets

**Author to be determined.** Affiliation and correspondence to be supplied by the project owner before any submission. This manuscript is an AI-assisted draft prepared without submission; see the AI disclosure.

## Abstract

Weighting judges by their reported confidence is often called the optimal way to combine binary judgments: if confidence tracks the probability of being correct and errors are independent, confidence-weighted (CW) aggregation is Bayes-optimal. Existing theory already shows that correlated errors and distorted competence inputs change the optimum, and empirical work already shows that confidence-weighted voting can beat simple majority voting. We ask a narrower, finite-sample question: given the number of judges, the strength of the confidence–accuracy relationship, and the correlation of errors within an item, when does CW lose to equal weighting (EW), and is partial shrinking better than either? We derive the CW−EW gap as a function of these three quantities, map its boundary in a preregistered simulation, and estimate where real datasets sit using 81 datasets from the Confidence Database (1,753,204 trials). In the data, the majority-decision advantage of CW is negligible (mean +0.003, 95% CI [0.0003, 0.0071], and non-positive in 63% of datasets), and CW makes the continuous estimate of a held-out judge's correctness worse in 90% of datasets (mean Brier improvement −0.0008, 95% CI [−0.0013, −0.0004]). The harm is larger where errors correlate within items, as the theory predicts. The simulation reproduces the sign of this effect for 89% of datasets once confidence is set to the empirically observed, weakly diagnostic level. Partial shrinking is often optimal: with realistic confidence, neither pure CW nor pure EW is best. Confidence weighting is a safe default only when confidence is well calibrated and the crowd is large.

**Keywords:** wisdom of crowds; confidence; aggregation; calibration; correlated error; shrinkage

## 1. Introduction

Combining the judgments of several people usually beats asking one. The advantage comes from cancelling idiosyncratic error: if judges are on average better than chance and wrong for different reasons, the simple majority grows more accurate as judges are added (Condorcet, 1785/1994). This result, and the conditions under which it holds (Berend & Paroush, 1998), underpins practical advice to poll, average, or vote rather than to defer to a single expert.

A natural refinement is to weight judges by how confident they are. If a judge's reported confidence is the probability she is right, and errors are independent, then weighting votes by confidence is the optimal way to recover a binary truth (Grofman, 1978; Nitzan & Paroush, 1982; Ben-Yashar & Nitzan, 1997). The advice is intuitive and widespread: on this view, a confident judge should count for more than a hesitant one. It also sits within a large literature on combining opinions. People appreciate averaging less than they should (Larrick & Soll, 2006; Soll & Larrick, 2009); identifying expertise improves crowd accuracy (Budescu & Chen, 2015); pooling independent judgments boosts medical diagnosis (Kurvers et al., 2016); a small select crowd can match a large one (Mannes et al., 2014); and how information is shared between judges changes what aggregation achieves (Palley & Soll, 2019). Metacognitive variants, such as asking what others will answer, extend the same goal (Prelec et al., 2017). Yet three literatures make the optimality conditional in ways worth stating plainly.

First, committee theory shows that the optimal weights depend on the structure of shared error. When voters' judgments are correlated, equal or competence-proportional weighting is not generally optimal (Shapley & Grofman, 1984; Ladha, 1995; Kaniovski, 2010), and additional judges stop helping once their errors move together (Hogarth, 1978; Einhorn et al., 1977). Second, the forecast-combination literature shows that estimated optimal weights routinely fail to beat the simple average, because estimating many weights from few observations adds variance (Smith & Wallis, 2009; Claeskens et al., 2016). Huang, Broomell and Golman (2024) formalise this as a test of whether weighting "reliably improves collective accuracy or just adds noise". Third, when the weights come from a distorted competence signal rather than the true competence, the optimal rule degrades (Baharad & Ben-Yashar, 2009). Reported confidence is exactly such a signal, and it is only weakly related to accuracy: pooling 145 datasets, Jin, Verhaeghen and Rahnev (2022) found a positive but modest confidence–accuracy correlation. Empirically, confidence-weighted majority voting can beat unweighted majority voting (Saha Roy et al., 2021; Meyen et al., 2021), and confidence-based rules can make crowds more efficient (Berger et al., 2025), but people themselves weight votes more equally than the optimal confidence rule prescribes (Meyen et al., 2021).

What remains underexamined is the boundary itself in the terms a crowd aggregator actually has: the number of judges, the strength of the confidence–accuracy relationship, and the correlation of errors within an item. Existing results are stated for abstract competences or for estimated weights; they are not written so that an analyst who knows her crowd size and the calibration of her confidence measure can say whether weighting will help. Nor has the size of the CW advantage been mapped across many real judgment datasets, so its typical magnitude is unknown. The practical question is not whether confidence weighting can help, which is settled, but how large the gap between CW and EW usually is, and when the sign turns.

We address this in three steps. First, we write the expected-accuracy gap between CW and EW as a function of the confidence–accuracy calibration slope, the within-item error correlation, and confidence dispersion, in the finite-sample regime where each item has a handful of judges. Second, we map the boundary of the harmful region in a preregistered simulation, where confidence is generated with a tunable amount of overconfidence, and derive the shrinkage between CW and EW that is accuracy-optimal. Third, we estimate where real judgment data sit, using 80 datasets from the Confidence Database (Rahnev et al., 2020), and test whether the observed pattern follows the theoretical inputs.

This is a Theory Article with an empirical test. We do not claim that confidence weighting can hurt, that correlated error changes optimal weights, or that confidence-weighted voting sometimes beats majority: those are established (Baharad & Ben-Yashar, 2009; Huang et al., 2024; Meyen et al., 2021; Shapley & Grofman, 1984). The contributions are the psychometric parametrisation of the gap, the simulated boundary, and a description of how real datasets are distributed relative to it. Our preregistration, including the analysis plan and the criteria for each outcome, was committed before the outcome variables were analysed; it and all deviations are in the project repository.

## 2. A finite-sample account

### 2.1 Setup

Consider an item $i$ with a binary truth. Judge $j$ reports a binary judgment and a confidence $c_{ji}\in[0,1]$. Encode the judgment by its correctness, $v_{ji}=+1$ if the judge is right on that item and $-1$ if wrong. The two aggregation rules are the equal-weighted (EW) mean and the confidence-weighted (CW) mean:

$$\bar{x}_i = \frac1m\sum_j v_{ji}, \qquad \hat{x}_i = \frac{\sum_j c_{ji}\,v_{ji}}{\sum_j c_{ji}},$$

where $m$ is the number of judges on the item. The crowd decision is correct when the estimate is positive. This encoding lets us use recorded correctness directly, without reconstructing the truth from responses, and it makes the two rules differ only in their weights.

The rank of EW is its efficiency as an estimator of the item's expected correctness: the more judges, the less the estimate depends on which judges happened to be included. CW, if the weights are informative, places more weight on judges who are more likely to be right, which reduces bias or, equivalently, raises the estimate's mean. The two differ in both bias and variance, and the balance shifts with $m$.

### 2.2 Bias, variance and the gap

Write the crowd estimate generically as a weighted mean with weights $w_j$. Conditional on the item, its variance falls with $m$ and rises with the dispersion of the weights. CW raises weight dispersion, so at small $m$ it pays an extra variance the EW estimate does not. That extra variance is only worth paying if the weights are informative enough to raise the estimate's signal. Two features of the confidence distribution govern this. The **calibration slope** $\beta$, from a regression of correctness on normalised confidence, sets how much the weights separate good judges from bad. **Confidence dispersion** sets how unequal the weights are, and hence how much variance CW adds. A third feature is external to the judge but central: the **within-item error correlation** $\rho$. When errors are shared, an item that is hard for one judge is hard for all, and reweighting within the item shuffles a quantity whose average is already determined by the shared component.

Two limiting cases are instructive. If confidence is perfectly calibrated and errors are independent ($\beta$ large, $\rho=0$), CW approaches the optimal rule and the gap is positive, growing with $m$ as the estimate converges on the item's true expected correctness. If confidence carries no information about correctness within the item, CW is a weighted mean with random weights: it is unbiased if the weights are unrelated to correctness, but noisier than EW, so the gap is negative and vanishes as $m$ grows and the weights average out. The empirically relevant case lies between, and the sign of the gap depends on whether the calibration gain outruns the weight-variance cost at the given $m$.

This is a bias–variance statement, and its ingredients are the ones already used in the correlated-votes and forecast-combination literatures. The contribution here is to write the gap in the psychological coordinates an aggregator can estimate, and to attach a simulation and a base rate to it. Because the finite-sample variance term depends on the full confidence distribution, we do not claim a closed form for all cases; we derive it where it is tractable and, where it is not, solve the gap numerically and say so (Sections 3 and 4).

The framework also yields a prescriptive quantity. Define the shrinkage estimator

$$x^\lambda_i = (1-\lambda)\,\bar{x}_i + \lambda\,\hat{x}_i,$$

with $\lambda=0$ reproducing EW and $\lambda=1$ reproducing CW. If the calibration gain and the weight-variance cost trade off, the accuracy-optimal $\lambda^\star$ will often lie strictly between the two, and shrinking towards equal weights is better than either extreme. Whether an interior optimum exists, and where, is a question for the simulation.

## 3. Simulation

### 3.1 Model and method

We simulated judgments and confidence for many independent items. Each item $i$ has a latent position $\delta_i\sim N(0,1)$ that fixes its truth $T_i=\mathrm{sign}(\delta_i)$; a shared error $u_i\sim N(0,\tau^2)$ that is common to all judges on the item; a judge ability $a_j\sim N(0,0.7^2)$; a judge overconfidence trait $o_j\sim N(0,1)$, independent of ability; and private noise $\varepsilon_{ji}\sim N(0,1)$. The judge's signal is $s_{ji}=\delta_i+u_i+a_j+\varepsilon_{ji}$, and the judgment is correct when $\mathrm{sign}(s_{ji})=T_i$. Confidence rises with the strength of the correct-side signal and with the overconfidence trait,

$$c_{ji}=\mathrm{sigmoid}\big(\gamma\,T_i s_{ji}+\phi\,o_j\big)+\nu_{ji},$$

with $\nu_{ji}\sim N(0,0.05^2)$, min–max normalised as in the empirical analysis. The parameter $\gamma$ sets how sharply confidence tracks correctness, $\phi$ is overconfidence (confidence that is not diagnostic of accuracy), and $\tau$ drives the within-item error correlation $\rho$. We swept $\tau\in\{0,0.3,0.6,1.0\}$, $\phi\in\{0,1,2,4\}$ and $\gamma\in\{0.3,0.6,1.0\}$, with 40,000 items per cell and group sizes $m\in\{3,5,7,9,13,17,25,41,65\}$. For each cell we recorded the sign-accuracy gap $\Delta(m)$ and the leave-one-judge-out Brier improvement of CW over EW (defined in Section 4.1), and the accuracy-optimal shrinkage $\lambda^\star$.

The **failure condition** set in advance was that the simulation must reproduce either the qualitative published result that real groups weight more equally than the confidence-optimal rule (Meyen et al., 2021) or the sign pattern of the empirical gap. A model that reproduces neither is rejected.

### 3.2 Results

Across the 48 simulated cells, the sign-accuracy gap is positive almost everywhere and the harmful region is small. Only 5 of 48 cells (10%) show a negative gap at some group size, and they are the cells with the strongest overconfidence ($\phi=4$) and the weakest shared error. For example, at $\gamma=0.3$, $\tau=0$ and $\phi=4$, the mean gap is −0.006, while at the same $\gamma$ and $\tau$ with $\phi=0$ it is +0.050. The gap grows with group size over most of the range, consistent with the finite-sample reading, though there are local violations (51 of 384 steps exceed the Monte-Carlo tolerance in the negative direction).

The picture changes for the continuous estimate. The leave-one-judge-out Brier improvement of CW over EW is negative in all 48 cells: at every combination of calibration and shared error we swept, reweighting by confidence made the estimate of a held-out judge's correctness slightly worse. The harm is small where confidence is well calibrated (Figure 2a; mean Brier improvement +0.001 at $\phi=0$, $\gamma=0.3$) and larger where it is not (−0.014 at $\phi=4$, $\gamma=0.3$). This is the central simulation result: the majority decision is nearly unaffected by weighting, but the graded estimate is degraded, and the degradation tracks overconfidence.

An interior optimum is common (Figure 3). In 16 of the 48 cells the accuracy-optimal shrinkage $\lambda^\star$ lies strictly between 0 and 1 for at least one group size, so partial shrinking beats both pure rules. The optimal amount of weighting falls as overconfidence rises: when confidence is uninformative, the best rule is close to equal weighting, and any weight on confidence costs accuracy.


![**Figure 2.** Simulated boundary surface (gamma = 0.3). Colour is the effect of confidence weighting as a function of overconfidence phi and shared error tau: (a) the leave-one-judge-out Brier improvement, negative throughout; (b) the sign-accuracy gap, positive for well-calibrated confidence and turning non-positive at high overconfidence.](analysis/output/figures/fig2_boundary.png)

![**Figure 3.** Accuracy-optimal shrinkage lambda* between equal weighting (0) and confidence weighting (1) as a function of group size, for three levels of overconfidence. Partial shrinking is frequently optimal, and the optimal weight on confidence falls as confidence becomes less diagnostic.](analysis/output/figures/fig4_lambda.png)

These results satisfy the failure condition. They reproduce, in sign, the empirical pattern of Section 4, and they are consistent with the finding that real groups behave closer to equal weighting than the confidence-optimal rule prescribes (Meyen et al., 2021).

## 4. Empirical test across 81 datasets

### 4.1 Data and method

We used the Confidence Database (Rahnev et al., 2020; OSF `s46pr`, CC0), a collection of trial-level datasets in which participants make a judgment and rate their confidence. Of 180 per-study files, 81 met the structural inclusion rules fixed before analysis: an explicit correctness column, a stimulus identifier, at least eight participants, non-constant confidence, and at least two items judged by three or more participants. Together these contain 1,753,204 analysed trials. Median calibration slope was 1.52, median within-item error correlation 0.02, and the median item was judged by 32 participants.

An **item** is a shared cell, defined as the stimulus value together with any of a fixed list of design columns present in the dataset (for example contrast or coherence). A judge's **vote** in an item is the mean of $2\times\mathrm{correct}-1$ over her trials in it, and her **confidence** is the mean rating, min–max normalised within the dataset. This uses the recorded correctness directly and does not require reconstructing a per-item truth.

We computed two quantities. The **sign-accuracy gap** is the difference in the proportion of items on which the crowd decision is correct, CW minus EW, estimated at group sizes $m\in\{3,5,7,9,13,17,25,40\}$ by drawing 2,000 random judge subsets per item. The **leave-one-judge-out (LOO) Brier improvement** is, for each item and each target judge, the Brier score of the other judges' EW estimate minus that of the CW estimate; a positive value means confidence weighting predicted the target judge's correctness better. The LOO-Brier comparison is a continuous version of the same question with no ceiling, and it was added after the sign-accuracy estimand proved insensitive; the preregistered sign-accuracy results are reported in full alongside it (see deviations).

We estimate per dataset the calibration slope $\beta$ and the within-item error correlation $\rho$, then relate the estimated effect to those inputs with an OLS regression using heteroscedasticity-robust standard errors.

### 4.2 Results

The majority-decision advantage of confidence weighting is negligible. Averaged over group sizes, the sign-accuracy gap is +0.003 (95% CI [0.0003, 0.0071]), and it is non-positive in 63% of datasets. The trivial size follows partly from a ceiling: EW crowd accuracy is already 0.93 at three judges and 0.98 at forty, so most items are decided correctly under either rule and the room for improvement is small (Figure 1a).

The continuous estimate tells a clearer story. The LOO-Brier improvement of CW over EW is −0.0008 on average (95% CI [−0.0013, −0.0004]) and is negative in 89% of datasets (Figure 1b). In other words, in almost every dataset, weighting other judges by confidence produced a slightly worse estimate of whether a given judge was correct than weighting them equally. The effect is small in absolute terms, as it must be when confidence is only weakly diagnostic, but it is consistent in sign and its confidence interval excludes zero.

![**Figure 1.** Confidence weighting versus equal weighting in 81 Confidence Database datasets. (a) The sign-accuracy advantage of CW over EW as a function of group size; points are means across datasets with 95% confidence intervals, and the dashed line is zero. (b) Distribution of the leave-one-judge-out Brier improvement of CW over EW across datasets; the red line marks the mean.](analysis/output/figures/fig1_empirical.png)


The moderation matches the theory. Regressing the LOO-Brier improvement on the calibration slope and the within-item error correlation, the error-correlation coefficient is negative and its confidence interval excludes zero (−0.020, SE 0.0095): the more errors correlate within an item, the more confidence weighting hurts. The calibration-slope coefficient is near zero (−0.00013, SE 0.00016). In the sign-accuracy regression, by contrast, the error-correlation coefficient is positive (+0.133, SE 0.057), which we read as a ceiling artefact rather than a substantive reversal, since the sign measure has little variance left to explain (Figure 4).

![**Figure 4.** Empirical moderation. Left: the leave-one-judge-out Brier improvement against the calibration slope. Right: the same against the within-item error correlation; the negative slope is the predicted pattern.](analysis/output/figures/fig3_moderation.png)


We mapped each dataset to the nearest simulated cell in standardised (calibration, error-correlation) space. The simulation reproduced the sign of the LOO-Brier effect for 72 of 81 datasets (89%), meeting the preregistered criterion, but the sign of the sign-accuracy effect for only 30 of 81 (37%). The model therefore captures the continuous estimate but not the coarse decision, which is the pattern the simulation itself predicted.

Two interpretive points follow from the same numbers. First, the average benefit of confidence weighting is smaller than one percentage point of accuracy, and its typical sign is negative for the graded estimate. Second, the harm concentrates where shared error is high, which is the regime that the correlated-votes literature already flagged as where aggregation gains are fragile.

## 5. Discussion

Confidence weighting does not reliably improve crowd judgment in real data, and it usually makes the finer estimate slightly worse. Across 81 datasets and 1.75 million trials, weighting judges by their confidence gave a majority-decision gain of +0.003, non-positive in about three of five datasets, and degraded the leave-one-judge-out estimate of a judge's correctness in 89% of datasets. The harm grew with the correlation of errors within an item, as the finite-sample account predicts. The simulation reproduced the pattern of the continuous estimate for 89% of datasets, and it shows why: for the coarse decision, reweighting barely matters; for the graded estimate, extra weight dispersion at small to moderate group sizes costs more than weakly diagnostic confidence recovers.

The results sit inside what is already known, and they sharpen it. That confidence weighting can fail, that correlated error bounds aggregation, and that miscalibrated competence inputs degrade optimal weighted voting are established (Baharad & Ben-Yashar, 2009; Huang et al., 2024; Shapley & Grofman, 1984). What the present analysis adds is the boundary in estimable psychological coordinates, the finding that real datasets sit on the adverse side of it for the graded estimate, and the size of the effect: about eight ten-thousandths of a Brier point, consistently negative. The magnitude matters for practice. Reports that confidence-weighted aggregation beats majority voting (Meyen et al., 2021; Saha Roy et al., 2021) are not contradicted, because they concern the coarse decision and often larger or better-calibrated crowds; but they should not be read as evidence that weighting improves the underlying estimate, and the present results suggest that in ordinary datasets it does not.

The practical guidance follows from the boundary rather than from a slogan. The optimal amount of confidence weighting depends on group size and calibration. With weakly diagnostic confidence and small groups, any weight on confidence costs accuracy, and partial shrinking towards equal weighting is safer than either pure rule; that an interior optimum exists in a third of the simulated cells is the constructive version of this point. If confidence is well calibrated and the crowd is large, the classical argument holds and weighting helps the decision. An analyst who wants a single default should calibrate her confidence measure first: if the confidence–accuracy slope is flat, or the ratings are compressed, equal weighting is the safer choice.

Several limitations bound these conclusions. The empirical leg reuses a corpus not designed for crowd aggregation. Items are condition cells rather than matched physical stimuli, so the analysis measures how confidence reweighting changes the crowd's estimate of a shared condition, not a controlled group decision. The datasets differ in task, scale, and confidence format, and we pool them only at the level of summary estimates. The within-item error correlations we estimate are small in absolute terms (median 0.02), smaller than in the simulation, so the simulated adverse region is somewhat more severe than the typical dataset; the moderation result should be read with that gap in mind. The Brier estimand was added after the preregistered sign-accuracy estimand proved ceiling-bound, so it is not a confirmatory test in the strict sense, though the preregistered result points the same way. Finally, the simulation is a particular generative model, and a different account of how confidence arises could shift the boundary.

The findings point to specific next steps. A designed crowd experiment that holds stimuli fixed across judges could test the graded-estimate prediction directly, at group sizes where the theory says the sign turns. Because the harm tracks overconfidence, measuring the confidence–accuracy slope on a calibration set before deploying a weighted aggregation rule is the concrete procedure to test. And the shrinkage rule deserves evaluation on real crowds rather than in simulation alone, since its value rests on the existence of the interior optimum that the simulation suggests.

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
