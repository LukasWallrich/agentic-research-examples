# Weaknesses: the five weakest points of this paper

My own assessment, written before external review, in order of how much they threaten the paper.

## 1. The empirical estimand is a proxy, not a crowd decision

The Confidence Database was not built for crowd aggregation. Almost no dataset pairs several people with the same physical stimulus and a per-item ground truth. I therefore defined an item as a shared condition cell and a judge's vote as the sign of her recorded correctness, and I evaluate whether the crowd's aggregated estimate is correct. This measures how confidence reweighting changes the crowd's estimate of a condition, not a controlled group decision on a matched stimulus. A reviewer can reasonably say the empirical leg does not test the phenomenon the theory is about. The theory and simulation stand without it, but the paper's headline empirical numbers would need that caveat on every use.

## 2. The primary empirical estimand was changed after seeing the data

The preregistered estimand was the sign-accuracy gap. It hit a ceiling (equal-weighted crowd accuracy is 0.93 at three judges), so I added the leave-one-judge-out Brier comparison, which is the estimand the empirical narrative relies on, and disclosed it as a deviation. The preregistered result is reported and agrees in direction, but a strict reader will treat the Brier result as exploratory, which weakens the confirmatory status of the main empirical claim.

## 3. The formal contribution is a repackaging of known results

Shapley and Grofman (1984) already derived optimal weights under correlated votes; Baharad and Ben-Yashar (2009) already showed that distorted competence inputs degrade the optimal rule; the forecast-combination puzzle already shows that estimated weights often lose to equal weights. The genuinely new elements are the psychometric parametrisation of the gap and the base-rate estimate, not a new theorem. A reviewer who knows the committee-theory literature may see the formal section as a translation rather than an advance. I have not found a closed form for the general finite-sample gap, so the paper leans on the simulation.

## 4. The simulation is one model among many, and it was tuned to the data

The generative model, and especially the judge-level overconfidence term, was chosen to produce the empirically observed pattern; the preregistration's original mechanism could not generate within-item miscalibration, and I changed it and recorded the change. The simulation's within-item error correlations (0.09–0.30) are much larger than the empirical ones (median 0.02), so the simulated harmful region is more severe than the typical dataset. A different account of how confidence arises could move the boundary, and the 89% sign-reproduction is between a model and data the model was fit to describe, not an out-of-sample test.

## 5. Effect sizes are tiny and the practical stakes may be small

The central empirical effect is about eight ten-thousandths of a Brier point. It is consistent and statistically distinguishable from zero, but it is small enough that a reasonable reader will ask whether the choice between confidence weighting and equal weighting matters at all in practice. The honest answer is that for the coarse decision it usually does not, and for the graded estimate the difference is real but minor. The paper's value then rests on the boundary and the shrinkage guidance rather than on a large empirical effect, which may not be enough for a strong empirical outlet and is more suited to a Theory Article.
