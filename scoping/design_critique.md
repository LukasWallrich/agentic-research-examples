# Design critique: finite feedback and global adviser selection

The model is mathematically coherent and can support a focused theory paper about learning which decision maker to use from selective feedback. Its most defensible contribution is the finite-label cost of correcting confidence-dependent selection, together with an explicit distinction between absolute accuracy feedback and paired performance feedback. Several proposed comparisons are mathematical identities or dominance results. They should be established before analysis and used as implementation checks, rather than presented as empirical discoveries or uncertain hypotheses.

This assessment uses symbolic reasoning only. No numerical calculations, hypothesis-testing simulations, outcome files, or existing analysis outputs were run or inspected. Literature searches were limited to public bibliographic material and abstracts. The calculations below assume binary labels, binary predictions, equally costly errors, independent audit draws, and deployment in the same environment as the source population.

## The quantities and what selection changes

Let strata have masses \(p_L=p\) and \(p_H=1-p\), human accuracies \(h_c\), adviser accuracies \(a_c\), and joint correctness \(q_c\). The four correctness states have probabilities

\[
P(1,1\mid c)=q_c,\quad P(1,0\mid c)=h_c-q_c,\quad
P(0,1\mid c)=a_c-q_c,\quad P(0,0\mid c)=1-h_c-a_c+q_c.
\]

The proposed Fréchet interpolation produces valid probabilities for \(r\in[0,1]\). Here \(r\) is an interpolation position, **not** the Pearson correlation of errors. Its relationship with correlation changes with the marginals.

Define \(\delta_c=a_c-h_c\), \(d_c=h_c+a_c-2q_c\), \(H=\sum_c p_ch_c\), \(A=\sum_c p_ca_c\), \(\Delta=A-H\), and \(D=\sum_c p_cd_c\). For binary predictions, disagreement occurs exactly when one decision maker is correct. This equivalence fails with multiclass predictions, where both can be wrong and disagree.

Under uniform sampling of disagreements, adviser accuracy and the paired contrast are

\[
A_D=\frac12+\frac{\Delta}{2D},\qquad
E[X_A-X_H\mid\mathrm{disagreement}]=\frac{\Delta}{D}.
\]

Therefore the paired contrast preserves the global ranking whenever \(D>0\). It estimates a rescaled contrast, not global \(\Delta\), unless multiplied by \(D\). For the ranking task, the positive scale is irrelevant. If \(D=0\), the two decision makers agree everywhere and \(\Delta=0\); a fixed-size disagreement audit cannot be drawn. Exclude such cells as undefined sampling designs, rather than retrying indefinitely.

Comparing disagreement-conditioned adviser accuracy with known deployment human accuracy gives

\[
A_D-H=\frac12-H+\frac{\Delta}{2D}.
\]

With the proposed human accuracies, \(H>1/2\). In expectation this rule selects the adviser only when \(\Delta>D(2H-1)\). It can therefore reject a genuinely better adviser. Under uniform disagreement sampling it cannot asymptotically select a worse adviser. Neither statement implies that the adviser accuracy estimate is universally biased downwards:

\[
A_D-A=\frac12-H+\Delta\left(\frac{1}{2D}-1\right),
\]

whose sign depends on the environment. Describe the problem as a comparison across different sampled populations, not a universal pessimism of disagreement feedback.

## Confidence-dependent sampling and weighting

Suppose the relative audit inclusion rates within disagreements are \(s_L=1\) and \(s_H=k>0\). Let \(Z=\sum_c p_cs_cd_c\). The audit stratum distribution is \(p_cs_cd_c/Z\), and the unweighted paired contrast has expectation

\[
\frac{p\delta_L+(1-p)k\delta_H}{Z}.
\]

This can reverse the global ranking when the stratum-specific advantages differ in sign. If both advantages favour the same decision maker, weighting cannot repair an asymptotic ranking reversal because no reversal exists. Include both mixed-sign and same-sign environments; report them separately.

For weights \(w_L=1\), \(w_H=1/k\), the unnormalised weighted mean has expectation \(\Delta/Z\). Its sign therefore identifies the desired ranking. The self-normalised ratio converges to \(\Delta/D\); the finite-sample ratio is not generally unbiased, though the positive denominator makes its ranking exactly the same as the unnormalised weighted sum. Avoid treating these as distinct ranking estimators.

For \(Y=X_A-X_H\), the weighted observation variance under this audit is

\[
\operatorname{Var}(wY)=
\frac{pd_L+(1-p)d_H/k}{Z}-\frac{\Delta^2}{Z^2}.
\]

This establishes why rare-stratum weights can impair finite-sample rankings without implying that they necessarily do so. Capping weights can trade systematic ranking error against sampling variability. If \(0<k\le1\), the cap is \(M\ge1\), and only the larger weight is capped, the capped numerator has expectation proportional to

\[
p\delta_L+(1-p)\min(1,kM)\delta_H.
\]

When the cap binds, consistency for the global ranking is no longer guaranteed. This exact limit should accompany finite-budget results.

If \(k>1\) is intended, define actual inclusion probabilities by dividing both rates by \(\max(1,k)\). Relative rates still determine the conditional audit distribution, but absolute sampling probabilities determine screening cost. A zero rate creates a positivity failure; do not claim weighting repairs it.

Disagreement-only labels generally cannot identify either decision maker's marginal accuracy separately, because agreement correctness remains unobserved. The relative difference is recoverable because its value on agreements is structurally zero. This distinction is a useful conceptual contribution and should be explicit.

## What is already determined analytically

Global deployment regret under a rule choosing one decision maker is \(|\Delta|\) times its probability of choosing the worse decision maker. Prespecify fair random tie-breaking; equivalent expected regret assigns half loss to ties. The regret is zero at \(\Delta=0\), regardless of ranking uncertainty.

Uniform disagreement auditing with a paired-majority rule weakly dominates random auditing with that same rule at equal label count. To see this, random auditing produces \(M\sim\mathrm{Binomial}(n,D)\) disagreements; agreements contribute zero. Conditional on \(M\), the random-audit decision is the same majority rule as an \(M\)-label disagreement audit. With fair ties, binomial majority error is nonincreasing in the number of informative draws. Since \(M\le n\), its expected error cannot be below that of the \(n\)-label disagreement audit. Equality is possible. This is a theorem under the stated assumptions, not evidence from simulated people.

For unselected audits, the paired observation variance is \(D-\Delta^2\); the adviser-only accuracy variance is \(A(1-A)\). Thus the paired estimator does not universally have lower variance than an adviser estimator compared with an exactly known human benchmark. The availability of known \(H\) gives the absolute-feedback comparator additional information and must be described as a benchmark assumption.

The finite-label comparisons with the strongest scientific room are consequently: weighting versus unweighted estimation under confidence-skewed disagreement sampling; capping versus full correction; absolute versus paired feedback in selective audits; and the dependence of these comparisons on heterogeneous advantage, disagreement frequency, and audit budget. A universal claim that correction lowers regret is not warranted by consistency alone.

## Improve the study within the fixed-sampling framework

1. **Give the loss function priority.** Use expected excess deployment error as the primary outcome. Report ranking error alongside it: an estimator can misrank frequently near indifference while incurring little practical loss. Avoid percent improvements when baseline regret is zero or nearly zero.
2. **Use exact probabilities where feasible.** Uniform-disagreement absolute/paired rules have binomial decision probabilities; random paired rules can be evaluated as a mixture over informative counts. Confidence-selected weighted rules have a small discrete support and can be checked through exact count enumeration or convolution for selected budgets. These calculations can independently verify a simulation implementation after preregistration.
3. **State the cost unit.** Equal labelled cases assumes observing both predictions and screening for disagreement is free. Report expected screening volume symbolically as \(n/D\), or \(n/Z\) after defining actual inclusion rates. An equal-screened-case interpretation is different and should not be implied.
4. **Fix the decision class.** Choosing one source globally cannot yield complementarity beyond the better marginal source. Describe it as source selection. Stratum-specific delegation is a richer policy class with a different oracle; adding it is optional and should not silently alter the estimand.
5. **Separate a normative result from human behaviour.** The rules are explicit information-processing policies, not estimated human learning models. A future feedback-display × audit-schedule experiment can test whether people use the proposed information and whether selection-aware feedback lowers deployment errors. Failure of those behavioural predictions would limit the model's psychological relevance even if its algebra remains correct.
6. **Choose interpretable regimes before results.** Include homogeneous advantage, opposing stratum advantages, nearly tied global performance, and clearly separated performance. State which regime a hypothesis concerns and report all regimes. Averages over an arbitrary grid are design summaries, not population estimates.

## Novelty and contribution risk

The sign identity is elementary conditioning, and inverse-probability weighting is established methodology. Neither should carry a priority claim. An especially relevant predecessor is *Human-AI Collaboration with Bandit Feedback*, whose abstracted discussion explicitly treats policy selection with selectively observed feedback and inverse-propensity weighting. The full paper needs checking before the final novelty statement. [Author-hosted paper](https://pages.ischool.utexas.edu/hai-files/files/publications/55/2021-IJCAI-BanditFeedback.pdf).

Recent work also formalises confidence-dependent human reliance and a trade-off between agreement at high human confidence and complementary expertise elsewhere. A comparison is needed with *Align When They Want, Complement When They Need! Human-Centered Ensembles for Adaptive Human-AI Collaboration*. Its visible framework concerns designing a model for confidence-dependent reliance; the proposed study instead concerns learning a global source ranking from a finite selectively labelled audit. [AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/download/38786/42748).

The useful claim is consequently modest but concrete: identify when feedback that is sufficient for choosing between two sources becomes misleading after confidence-dependent selection, and map the finite-label price of correction. A transparent analysis of where correction fails may be more informative than reporting its familiar asymptotic advantage. Publication value will depend on how clearly the final results add beyond standard missing-data weighting and how specifically they motivate a refutable JDM experiment.
