---
author: Lukas Wallrich
bibliography: references.json
colorlinks: true
csl: apa.csl
fontsize: 11pt
geometry: margin=1in
lang: en-GB
linestretch: 1.15
title: Learning from disagreements when selective feedback helps and harms advisor evaluation
---

# Abstract

Outcome feedback can be accurate about the cases it reveals yet misleading about an advisor's overall competence. I distinguish estimating absolute advisor accuracy from deciding whether the advisor is more accurate than oneself. Uniformly sampled disagreements preserve the sign of the paired accuracy difference, although comparing the advisor's selected accuracy with one's marginal accuracy can favour the inferior source. Confidence-dependent verification can remove this protection. A prospectively specified simulation compared absolute, paired, inverse-probability-weighted, and capped-weight summaries at fixed feedback budgets. In the prespecified crossing-advantage scenario, weighting reduced deployment regret by 4.357 percentage points (97.5% Monte Carlo interval \[-4.383, -4.332\] for weighted minus paired regret). In a control with the same marginal source accuracies but a positive advisor advantage in both confidence strata, weighting increased regret by 1.112 points at the smaller budget. These results show that correcting selection can help or harm a finite-feedback decision. The model generates a refutable prediction for an experiment crossing feedback selection with the display of absolute or paired accuracy. Its behavioural interpretation remains untested: simulated decision makers implement stipulated estimators, and the study does not demonstrate how people learn from selective feedback.

**Keywords:** advice taking; selective feedback; confidence; comparative accuracy; simulation; inverse probability weighting

# Introduction

A person who verifies an advisor's recommendation learns whether that recommendation was correct. Across cases, however, verified recommendations need not represent the advice the person will receive next. Disagreements may be especially likely to attract scrutiny, and people may preferentially check disagreements when they feel confident in their own answer. The resulting feedback can answer a different question from the one used to decide whether to adopt the advisor. This paper asks when feedback that is selective in this way still supports a sound comparative judgement, and when correcting its selection improves the eventual decision.

The distinction matters because the practical question is often comparative. A person deciding whether to use an advisor may need to know whether its decisions are better than their own, without needing an unbiased estimate of either source's absolute accuracy. Conversely, an apparently low advisor hit rate need not justify rejecting it if one's own hit rate on those same cases is lower. I analyse this distinction in a deliberately constrained setting: after observing verified cases, a decision maker selects either their own initial judgements or the advisor for a new, randomly drawn set of cases. The model concerns this global adoption decision; it does not optimise which source to use on each individual case.

## What feedback makes available

Research on advice taking already distinguishes agreement from accuracy. Pescetelli & Yeung (2021) showed how decision confidence contributes to advice taking and trust formation, including how agreement and confidence can supply evidence when objective feedback is unavailable. Their account also exposes distortions when judgements are dependent. Jaquiery & Yeung (2024) experimentally separated preferences for agreement and accuracy; objective feedback supported a preference for accurate advice. These findings motivate attention to the evidence on which advisor judgements rest, but they do not establish how people interpret feedback selected from disagreements.

Selective experience can sustain inaccurate impressions without requiring intrinsically hostile attitudes. Denrell & March (2001) formalised how adaptive choices restrict later information, and Denrell (2005) applied experience sampling to impression formation. In interpersonal trust, Fetchenhauer & Dunning (2010) found that feedback supplied independently of the decision to trust reduced excessive scepticism. These studies establish the broader sampling problem. They do not imply that every comparative inference requires representative feedback: some comparisons remain identifiable because the missing cases contribute nothing to the difference of interest.

Verification and learning from verified cases are also distinct. Fok & Weld (2024) argue that explanations help human--AI decision making when they enable verification. Honeycutt et al. (2020) found that soliciting interactive feedback could reduce users' trust and impressions of model accuracy. Neither result implies the mechanism modelled here. The present analysis assumes that verification accurately reveals the truth and asks what can then be inferred from the selected history. It therefore concerns a downstream problem even when verification itself succeeds.

Recent computational work further limits the claim to priority. Gao et al. (2021) used inverse-probability weighting in learning human--AI routing from bandit feedback. Their problem involves selectively observed rewards and policies that exploit complementary performance. Zavattari et al. (2026), in a recent preprint, analyse allocation of a human audit budget across an agent fleet, including confidence dependence and updating after audits. Li & Steyvers (2026), also in a preprint, examine learning the relationship between AI confidence and accuracy. The contribution here is neither weighting nor learning advisor reliability in general. It is the comparison of absolute and paired feedback summaries for a global adoption decision, together with the finite-feedback consequences of correcting selection within disagreements.

## The present study

I first establish which comparative conclusions follow directly from the sampling mechanism. These are analytic properties rather than simulated discoveries. I then compare the decision losses induced by several summaries when only a finite set of verified outcomes is available. The computational hypotheses anticipate a benefit of weighting when confidence selection reverses the population comparison and a cost when selection instead favours informative comparisons. Finally, I specify a feedback-display experiment that could reject the proposed connection between these summaries and human judgement. No human outcome data are analysed, and no behavioural mechanism is considered confirmed by the simulation.

# Analytic framework

Let $A$ and $H$ indicate the correctness of the advisor's and human's initial binary responses. Let $D$ indicate disagreement between those responses, $d=P(D)$, $h=E[H]$, and $\Delta=E[A-H]$. On an agreement, $A-H=0$. Therefore, for $d>0$,

$$E[A-H\mid D]=\frac{\Delta}{d}.$$

Uniform disagreement feedback preserves the sign of the overall accuracy advantage. It does not recover its magnitude without $d$, nor does it identify either marginal accuracy. This is the familiar logic of paired discordant outcomes, not a new statistical identity. On a binary disagreement exactly one source is correct, so

$$E[A\mid D]=\frac{1+\Delta/d}{2}.$$

An absolute summary compared with the known marginal human benchmark favours the advisor only when $\Delta>d(2h-1)$. A paired summary instead favours it whenever $\Delta>0$. This comparison isolates an estimand mismatch: both the numerator and the benchmark must refer to the same selected cases. It is not a general claim that selected advisor accuracy must be biased downward.

Now distinguish low- and high-confidence strata with population proportions $p$ and $1-p$, and conditional advisor advantages $\delta_L$ and $\delta_H$. Suppose high-confidence disagreements are verified $k$ times as often as low-confidence disagreements. The sign of the selected paired comparison is then the sign of

$$p\delta_L+(1-p)k\delta_H.$$

Selection can reverse the global ordering when conditional advantages have opposite signs. If the advisor is better in both strata, positive reweighting cannot reverse the population sign. Inverse selection weights recover the sign of $\Delta$, provided both disagreement strata have positive sampling probability. With sample normalisation, the resulting score estimates the mean contrast among all disagreements, $\Delta/d$, rather than the unscaled global advantage. A capped weight generally targets a different selected contrast. Neither the unweighted nor the normalised weighted estimate is treated as a universally unbiased estimate of global accuracy difference.

Finite samples make the policy comparison less straightforward. Weights amplify contributions from rarely verified cases, potentially increasing decision error even when their limiting target is appropriate. Moreover, correcting a harmless selection can discard its informational advantage. The simulation quantifies these losses under explicit environments and feedback budgets. It does not require simulation to establish the preceding identities.

# Method

## Prospective specification and reproducibility

The hypotheses, environments, estimators, exclusions, and inference criteria were committed locally before hypothesis-bearing computation (git commit `68c07e4`). This provides a recoverable prospective record, not an independently timestamped public registration. Before that commitment, the workflow examined published articles, dataset documentation, and idea reviews, but no participant-level outcomes or hypothesis simulations. No existing dataset was used. A previous project remained in repository history; its deleted outcomes and manuscripts were not inspected.

The command `./run_all.sh` regenerates synthetic raw count histories, analyses, numerical checks, figures, and the manuscript. Saved count histories are sufficient for every estimator because feedback order is not used. Configuration, seeds, software versions, and hashes accompany the results. The main specification was followed; implementation clarifications and any later reviewer-requested analyses are documented in `deviations.md`. Full decisions, source audits, deviations, and reviewer responses accompany the manuscript.

## Environments and selection

Human correctness probabilities were 0.60 and 0.90 in low- and high-confidence strata. These are calibrated confidence categories by construction, not estimates from human ratings. The grid crossed low-confidence shares 0.25, 0.50, 0.75, advisor low-confidence accuracies 0.65, 0.80, 0.95, advisor high-confidence accuracies 0.70, 0.80, 0.90, and overlap positions 0.00, 0.50, 1.00, yielding 81 environments. An additional homogeneous-advantage control brought the total to 82.

For each stratum with marginal accuracies $h_c,a_c$, the probability of both sources being correct was

$$q_c=\max(0,h_c+a_c-1)+r\{\min(h_c,a_c)-\max(0,h_c+a_c-1)\}.$$

The four joint masses were $q_c,h_c-q_c,a_c-q_c,1-h_c-a_c+q_c$. Thus the dependence parameter $r$ locates the joint distribution within its feasible bounds; it is not a correlation coefficient. Truth can be taken as balanced, with symmetric decisions conditional on correctness. This makes the correctness table sufficient without modelling perception or generating identifiable records.

The focal crossing environment used equal stratum shares, midpoint overlap, and advisor accuracy 0.80 in both strata. The advisor was better at low confidence and worse at high confidence, while its marginal accuracy was 0.80 against human accuracy 0.75. The homogeneous control had advisor accuracies 0.65 and 0.95, retaining the same marginal accuracies but a positive advantage in both strata. These scenarios were selected in advance to contrast two mechanisms; they are not empirical prevalence estimates.

Feedback was either a random sample of all cases or a sample of disagreements with high-to-low verification ratios 1, 2, 4, 8. Under disagreement schedules, verification probabilities were $1/k$ at low confidence and unity at high confidence; agreements were never verified. Histories contained 20, 100, 500 independent verified outcomes. Matching verified outcomes holds the feedback budget constant but does not equate the number of cases encountered. I therefore also report audit yield and the expected opportunities needed to obtain each history.

## Summaries and adoption rule

The absolute learner subtracted known marginal human accuracy from observed advisor accuracy. The paired learner averaged $A-H$ on verified cases. The inverse-probability-weighted learner averaged the same difference using weights $k$ and unity in the low- and high-confidence disagreement strata, divided by their realised total. The capped learner limited these weights to 2. Under random feedback all weights were equal.

Each learner selected the advisor for a positive score and the human for a negative score. A numerical tie within 1e-12 was averaged over fair random selection. Learners within a condition used identical histories, permitting paired Monte Carlo contrasts. The known human benchmark gives the absolute learner information beyond the observed sample; it is a deliberate, favourable-information assumption, not a claim that people know their accuracy. The other learners require paired correctness on verified cases, and the weighted learner additionally requires the correct sampling ratio.

The outcome was expected deployment regret: the accuracy loss on a future random case relative to the better fixed source. It equals $|\Delta|$ multiplied by the probability of selecting the inferior source. This benchmark cannot establish complementary team performance and does not exploit confidence-contingent delegation. When marginal accuracies tie, regret is zero and ranking error is undefined; those environments remain in the output.

## Hypotheses and inference

**H1:** In the crossing environment with verification ratio 4 and 100 verified outcomes, weighted paired evaluation produces less regret than unweighted paired evaluation.

**H2:** In the homogeneous control with verification ratio 8 and 20 verified outcomes, weighted paired evaluation produces more regret than unweighted paired evaluation.

Each condition contained 20,000 independent histories generated with NumPy PCG64 and seed 20260928. Separate child streams were assigned to conditions in fixed order. For each hypothesis, I estimated weighted minus paired regret within the same histories and calculated a 97.5% normal Monte Carlo interval. The prespecified Bonferroni adjustment covers the 2 contrasts jointly at approximately 95%. A wholly predicted-side interval supports the computational prediction; a wholly opposite-side interval contradicts it; overlap with zero is unresolved. These intervals describe simulation precision, not uncertainty about human behaviour.

All scenarios, budgets, and learners were retained. Additional prespecified descriptions included adoption probabilities, limiting scores, capped correction, audit yields, and the lowest tested budget at which weighting improved estimated regret. Grid comparisons used the prespecified regret tolerance 0.0005; they are descriptions of a chosen design, not statistical generalisations to a population of tasks.

# Results

## Confirmatory comparisons

H1 was supported. In the crossing environment, weighted paired regret was 0.406 percentage points, compared with 4.763 for unweighted paired evaluation. The weighted-minus-paired contrast was -4.357 points (97.5% Monte Carlo interval \[-4.383, -4.332\]; Monte Carlo SE = 0.0115 points).

H2 was supported. In the homogeneous environment, weighted paired regret was 1.334 percentage points, compared with 0.221 for unweighted paired evaluation. The weighted-minus-paired contrast was 1.112 points (97.5% Monte Carlo interval \[1.079, 1.145\]; Monte Carlo SE = 0.0147 points).

  ----------------------------------------------------------------------------------------------
  Prediction     Weighted regret   Paired regret   Difference Monte Carlo interval   Outcome
  ------------ ----------------- --------------- ------------ ---------------------- -----------
  H1                       0.406           4.763       -4.357 \[-4.383, -4.332\]     supported

  H2                       1.334           0.221        1.112 \[1.079, 1.145\]       supported
  ----------------------------------------------------------------------------------------------

*Table 1. Prespecified regret contrasts. Regret and contrasts are percentage points of expected accuracy on a future random case. Intervals quantify Monte Carlo uncertainty, with the family-wise adjustment specified before computation.*

## What the selected cases imply

In the crossing environment, uniform disagreement feedback gave the advisor a limiting selected accuracy of 58.333%, against the known marginal human benchmark of 75.0%. The paired contrast was positive at 0.167, correctly favouring the advisor. With high-confidence verification ratio 4, the selected advisor accuracy became 41.667% and the paired contrast became -0.167. Weighting restored the limiting contrast to 0.167. These values instantiate the analytic selection boundary; they are not additional hypothesis tests.

  --------------------------------------------------------------------------------
  Environment   Selection       Labels   Absolute     Paired   Weighted     Capped
  ------------- ----------- ---------- ---------- ---------- ---------- ----------
  crossing      random             100      88.9%      81.9%      81.9%      81.9%

  crossing      1                  100       0.0%      95.4%      95.4%      95.4%

  crossing      4                  100       0.0%       4.7%      91.9%      49.2%

  crossing      4                  500       0.0%       0.0%      99.9%      49.9%

  homogeneous   8                   20      27.9%      95.6%      73.3%      91.0%

  homogeneous   8                  100       8.7%     100.0%      92.4%      99.9%

  homogeneous   8                  500       0.1%     100.0%     100.0%     100.0%
  --------------------------------------------------------------------------------

*Table 2. Advisor adoption probabilities in focal environments. Each row uses the same histories across summaries; selection refers to the high-to-low verification ratio among disagreements. The advisor is globally superior in both environments. Entries come from the prespecified simulation, including the random-feedback benchmark.*

![Expected deployment regret by feedback budget and summary. Panels show the crossing and homogeneous focal environments; lines show absolute, paired, weighted, and capped paired rules.](figures/focal_regret.png){width="95%"}

*Figure 1. Focal finite-feedback comparisons. Points are prespecified budgets; connecting lines guide the eye and do not estimate intermediate budgets. Errors concern global source adoption, not individual advice trials.*

## Prespecified grid and resource descriptions

The scenario grid included 54 superior-advisor environments, 24 inferior-advisor environments, and 3 exact marginal ties. At selection ratio 8 and 20 verified outcomes, weighting had lower regret than pairing in 44 grid environments, higher regret in 22, and a difference within the prespecified tolerance in 15. At selection ratio 8 and 500 verified outcomes, weighting had lower regret than pairing in 36 grid environments, higher regret in 9, and a difference within the prespecified tolerance in 36. The unweighted limiting paired sign reversed the global ordering in 24 grid environments at that ratio. Complete results, including capped correction, all dependence settings, and lowest observed improvement budgets, are supplied in the machine-readable tables. No grid frequency is interpreted as the frequency of such environments in practice.

In the crossing scenario, uniform disagreement selection verified 30.0% of encountered cases, requiring an expected 333.3 opportunities for 100 labels. Selection ratio 4 reduced yield to 15.0%, requiring 666.7 opportunities for the same label budget. In the homogeneous control, ratio 8 required 266.7 expected opportunities for 20 labels. Random all-case verification requires one opportunity per label. These are expected acquisition costs under independent cases, not realised waiting times.

Numerical checks verified the joint probability tables and margins, analytic sign properties, equivalent learners under uniform weighting, and exact binomial benchmarks for the focal uniform-disagreement conditions. The saved verification report records each comparison and its prespecified Monte Carlo tolerance. No history was excluded.

# Discussion

The prespecified simulation show that correcting selection can help or harm a finite-feedback decision. H1 was supported. In the crossing environment, weighted paired regret was 0.406 percentage points, compared with 4.763 for unweighted paired evaluation. The weighted-minus-paired contrast was -4.357 points (97.5% Monte Carlo interval \[-4.383, -4.332\]; Monte Carlo SE = 0.0115 points). H2 was supported. In the homogeneous environment, weighted paired regret was 1.334 percentage points, compared with 0.221 for unweighted paired evaluation. The weighted-minus-paired contrast was 1.112 points (97.5% Monte Carlo interval \[1.079, 1.145\]; Monte Carlo SE = 0.0147 points). The consequences depend on the advisor's conditional advantage and on what information the feedback policy selects; no summary was assumed to be a general cognitive model.

The first implication concerns the target of feedback. When advice and an initial judgement agree, the verified truth cannot favour one response over the other. Under uniform disagreement sampling, comparing the two sources on the same cases therefore retains the information required for global ranking. A low selected advisor hit rate can coexist with a useful advisor because the decision maker's own accuracy on those cases is lower still. This qualification complements sampling accounts of mistrust (Denrell, 2005; Fetchenhauer & Dunning, 2010): representativeness of observed outcomes is not equally necessary for every judgement.

The protection depends on which disagreements are seen. Confidence-dependent selection changes the balance between contexts in which each source has an advantage. Pairing removes a mismatch between samples, but it does not remove a mismatch between the verified sample and the target population. This explains why adding the human's own hit rate to a feedback display may sometimes suffice and sometimes fail. The inference is conditional on the joint accuracy structure, not on an assumption that increased advisor acceptance is inherently desirable. Inferior advisors and exact ties were retained in the grid precisely because greater reliance is not itself an improvement.

Weighting adds a further distinction between estimation and action. Recovering the right limiting contrast does not guarantee a better finite-feedback adoption decision. An unweighted score may be distorted in magnitude yet preserve the appropriate sign, and selective verification can concentrate informative comparisons. Conversely, where selection reverses the sign, gathering more cases under the same uncorrected rule can increase confidence in the wrong source. Capped weights are an interpretable compromise, but the reported grid does not identify a universal cap. The cap was fixed prospectively and evaluated, not optimised to the observed results.

## A behavioural test that could reject the account

The simulation does not establish that people use any of its summaries. Its psychological proposal is that feedback displays can change which comparative statistic guides a source-adoption judgement. A future experiment could hold each verified history fixed and randomise an advisor-only display, a paired display, or a selection-adjusted paired display. It would also randomise uniform versus high-confidence disagreement selection and provide an explicit marginal self-accuracy benchmark. Participants would then estimate the global advantage and choose a source for fresh random cases.

In the crossing scenario, the stipulated mapping predicts that a paired display improves adoption relative to an advisor-only display under uniform disagreement feedback, but loses that protection under confidence-selected feedback. A correctly adjusted display should restore adoption as feedback accumulates. The relevant test is the display-by-selection interaction, together with discrimination in an inferior-advisor control. Mere increases in trust would be insufficient. An experiment should also compare these rules with selection-aware inference and models that weight self and advisor errors asymmetrically.

The account is vulnerable to clear outcomes. If participants understand the displays but their choices do not show the predicted interaction, the proposed display-to-estimator mapping is inadequate. If they spontaneously adjust advisor-only summaries for selection, the absolute learner is a poor model. If choices depend mainly on itemwise confidence rather than global competence, the global adoption task misses the relevant decision. Such findings would reject or narrow the behavioural extension while leaving the probability identities intact. Sample size, quantitative behavioural bounds, comprehension criteria, and model comparisons require a separate prospective protocol; no human effect size is supplied by these simulation runs.

## Scope of the inference

The environments are stylised, not fitted to behavioural records or deployed systems. Discrete calibrated confidence strata omit noisy self-assessment and continuous difficulty. Correct feedback, stable source accuracies, known selection weights, and independent cases favour the statistical corrections. Estimated or misspecified sampling probabilities may substantially change their performance. The fixed, exogenous feedback schedule also omits the feedback loops studied in adaptive sampling accounts (Denrell & March, 2001). There is no evidence here about permanent abandonment, changes in trust over time, or why a person chooses to verify a case.

The resource comparison is equally specific. Equal label counts make sense when obtaining truth is the expensive step, but selective verification can require substantially more opportunities. Where time, delay, or opportunity costs dominate, equal-label comparisons alone do not establish the preferable policy. The model reports this cost rather than attaching an arbitrary exchange rate to labels and opportunities.

Finally, selection adjustment here is a benchmark available to a software display, not necessarily a plausible mental calculation. Its relation to human choice remains open, and the theoretical distinction may prove more useful for feedback design than for explaining existing behaviour. The resulting recommendation is correspondingly limited: evaluate advisor and self on matched cases, then establish whether those matched cases preserve the comparative ordering relevant to the next decision. Statistical correction is one possible response when they do not; its finite-feedback cost must also be assessed.

# Transparency and declarations

**Data and code availability.** No participant data were used. The local research package contains the prospective specification, synthetic count histories, configuration, complete scripts, machine-readable outputs, and manuscript source. `./run_all.sh` reproduces the analysis. Public archiving or journal upload has not been authorised or performed; the package can accompany a future submission.

**AI assistance.** OpenAI Codex (GPT-6 family, application and independent agents) carried out ideation, searching, design, coding, analysis, drafting, and checking on 28 September 2026. Claude via its authenticated CLI and Gemini 3.8 Flash (High) via agy reviewed ideas and drafts; Codex CLI reviewed code and ran the full coarse-ink 1.4.0 manuscript pipeline. Tool responses, settings available from the runtimes, source audits, and responses are retained. The initial Claude idea call used the CLI default and did not expose an exact model version. No AI is listed as an author. This autonomous draft requires the intended human author's assessment and approval before submission; no claim of completed human oversight is made.

**Acknowledgements and financial support.** Existing software subscriptions supported the automated workflow. No dedicated external funding was used by this workflow. The intended author's funding and competing-interest declarations require human confirmation before submission.

**Ethics.** This computational study collected no human data and processed no participant records or personal identifiers. It does not claim an institutional ethics determination.

# References {#references .unnumbered}

::::::::::::: {#refs .references .csl-bib-body .hanging-indent entry-spacing="0" line-spacing="2"}
::: {#ref-denrell2005 .csl-entry}
Denrell, J. (2005). Why Most People Disapprove of Me: Experience Sampling in Impression Formation. *Psychological Review*, *112*(4), 951--978. <https://doi.org/10.1037/0033-295x.112.4.951>
:::

::: {#ref-denrell2001 .csl-entry}
Denrell, J., & March, J. G. (2001). Adaptation as Information Restriction: The Hot Stove Effect. *Organization Science*, *12*(5), 523--538. <https://doi.org/10.1287/orsc.12.5.523.10092>
:::

::: {#ref-fetchenhauer2010 .csl-entry}
Fetchenhauer, D., & Dunning, D. (2010). Why So Cynical? Asymmetric Feedback Underlies Misguided Skepticism Regarding the Trustworthiness of Others. *Psychological Science*, *21*(2), 189--193. <https://doi.org/10.1177/0956797609358586>
:::

::: {#ref-fok2024 .csl-entry}
Fok, R., & Weld, D. S. (2024). In search of verifiability: Explanations rarely enable complementary performance in AI‐advised decision making. *AI Magazine*, *45*(3), 317--332. <https://doi.org/10.1002/aaai.12182>
:::

::: {#ref-gao2021 .csl-entry}
Gao, R., Saar-Tsechansky, M., De-Arteaga, M., Han, L., Lee, M. K., & Lease, M. (2021). Human-AI Collaboration with Bandit Feedback. *Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence*, 1722--1728. <https://doi.org/10.24963/ijcai.2021/237>
:::

::: {#ref-honeycutt2020 .csl-entry}
Honeycutt, D. R., Nourani, M., & Ragan, E. D. (2020). Soliciting Human-in-the-Loop User Feedback for Interactive Machine Learning Reduces User Trust and Impressions of Model Accuracy. *Proceedings of the AAAI Conference on Human Computation and Crowdsourcing*, *8*(1), 63--72. <https://doi.org/10.1609/hcomp.v8i1.7464>
:::

::: {#ref-jaquiery2024 .csl-entry}
Jaquiery, M., & Yeung, N. (2024). Preferences for advisor agreement and accuracy. *PLOS ONE*, *19*(9), e0311211. <https://doi.org/10.1371/journal.pone.0311211>
:::

::: {#ref-li2026 .csl-entry}
Li, Z., & Steyvers, M. (2026). *Learning to Trust: How Humans Mentally Recalibrate AI Confidence Signals* (Preprint 2603.22634). arXiv. <https://doi.org/10.48550/arxiv.2603.22634>
:::

::: {#ref-pescetelli2021 .csl-entry}
Pescetelli, N., & Yeung, N. (2021). The role of decision confidence in advice-taking and trust formation. *Journal of Experimental Psychology: General*, *150*(3), 507--526. <https://doi.org/10.1037/xge0000960>
:::

::: {#ref-zavattari2026 .csl-entry}
Zavattari, C., Tommasi, A., & Prencipe, G. (2026). *One Human, N Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence* (Preprint 2607.28317). arXiv. <https://doi.org/10.48550/arxiv.2607.28317>
:::
:::::::::::::
