# Weaknesses: the five weakest points of this paper

My own assessment, revised after the corrected analysis (which turned several results against the paper). In order of how much they threaten it.

## 1. The paper's central empirical claim is a null and a negative result

The preregistered moderation (H5, that flatter calibration and higher shared error make confidence weighting worse) is **not supported**: both coefficients are near zero and non-significant, and the sign measure points the opposite way. The model-reproduction hypothesis (H6) is **rejected**: the calibrated simulation matches the data's sign for 37% of datasets on the decision measure, and 34% on the graded measure against a 79% trivial baseline. So the theoretical mechanism the paper proposes is not the one that governs the data. A reader may reasonably ask what the paper establishes beyond "confidence weighting does not help much", which was already suspected.

## 2. The theory contribution is a repackaging of known results, and its model fails

Shapley and Grofman (1984), Baharad and Ben-Yashar (2009), the forecast-combination puzzle, and Huang et al. (2024) already cover the ingredients: correlated errors change optimal weights, distorted competence inputs degrade them, estimated weights often lose to the average. The new elements are the psychometric parametrisation and the base rate. The simulation then fails to reproduce the data, which undercuts the parametrisation as a description of reality: a boundary can be shown to exist and still be the wrong boundary.

## 3. The empirical estimands are proxies, both of them

No dataset in the Confidence Database pairs several people with the same physical stimulus and a per-item ground truth. I define items as shared condition cells and a judge's vote as the sign of her recorded correctness; this measures how reweighting changes the crowd's estimate of a condition, not a controlled group decision. The graded measure, the leave-one-judge-out Brier score, predicts a held-out judge's correctness, not the item's truth, and it was added after the preregistered estimand proved ceiling-bound. The empirical leg therefore does not cleanly test the phenomenon the theory is about, and it is not confirmatory.

## 4. The analysis is small-effect and fragile to implementation choices

The central empirical effect is about six ten-thousandths of a Brier point. It is consistent in sign, but the earlier version of the pipeline, with two implementation bugs, produced a *significant* moderation that vanished once the bugs were fixed. That the headline can flip on sampling-with-versus-without-replacement and on whether the ICC is computed on trials or on the judge-item table is a real fragility, and it means the paper's conclusions are only as stable as the code, which is why the code is published.

## 5. The H6 test, while now fairer, rests on a crude mapping

The model-reproduction test maps each dataset to the nearest simulated cell using only two standardised inputs (calibration slope and error correlation). Nine datasets map to a single cell, seven have error correlations below the simulated range, and the mapping ignores group size and the item-difficulty distribution, which also govern the effect. The H6 failure is large enough that mapping crudeness is unlikely to explain it entirely, but the test is not a strong one, and the honest reading is "this particular account, under this coarse mapping, does not fit", not "no account fits".