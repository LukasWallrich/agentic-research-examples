# Deviations from the preregistration

Each deviation states what changed, when it was decided, whether it was decided before or after seeing the relevant outcome, and its effect on interpretation.

## V1. Simulation mechanism: judge-level overconfidence replaced the prereg's κ term

- **Preregistration (§4):** confidence miscalibration was modelled as an item-level shift, `c_ji = Φ(γ·(s_ji + κ·u_i)) + ν_ji`.
- **Change:** the implemented model makes confidence depend on a judge-level overconfidence trait, `c_ji = sigmoid(γ·(T_i·s_ji) + φ·o_j) + ν_ji`, and drops κ.
- **Reason:** with κ, the shared error `u_i` is constant across judges within an item, so a confidence term depending on `u_i` shifts all judges' confidence together and cannot produce *within-item* miscalibration. Because confidence-weighted aggregation only changes the outcome through within-item reweighting, the κ specification cannot by construction generate the harmful region the paper is about. A judge-level trait is the minimal mechanism that can.
- **Decided:** before the final simulation was run; while calibrating the model, after confirming (from the prereg's own algebra, not from data) that κ was inert for within-item weighting.
- **Effect:** the simulation now has a well-defined harmful region. The substantive claim (confidence that is not diagnostic of accuracy hurts weighting) is unchanged; only the parameterisation is.

## V2. Added a leave-one-judge-out Brier estimand (V2a: empirical; V2b: simulated)

- **Preregistration (§6):** the primary empirical quantity was the sign-based crowd-accuracy difference Δ(m), and H4/H5 referred to it.
- **Change:** added `Δ_Brier = Brier(EW) − Brier(CW)` for predicting a held-out judge's correctness from the other judges, computed both empirically and in the simulation, and report it alongside the sign-based Δ(m).
- **Reason:** the sign-based estimand is ceiling-bound. Mean EW crowd accuracy is 0.93 at m = 3 and 0.98 at m = 40, so the sign-based Δ is compressed toward zero by construction and cannot discriminate the hypotheses. The Brier comparison is a continuous version of the same question ("does confidence weighting improve the crowd's estimate of whether a judge is correct?") with no ceiling.
- **Decided:** **after** observing the sign-based ceiling. This is disclosed explicitly. The preregistered sign-based results are still reported in full; the Brier results are the better-powered test and are labelled as an extension throughout.
- **Effect:** the empirical leg rests mainly on the Brier comparison. A reader who discounts the post-hoc estimand still has the preregistered sign-based result (a small, mostly non-significant positive Δ) and the simulation.

## V3. Computational bounds: fewer draws and an item cap

- **Preregistration (§6):** R = 5,000 random judge subsets per group size and dataset.
- **Change:** R = 2,000; and, for datasets with more than 64 eligible items, 64 items are sampled per draw.
- **Reason:** runtime bound at 1.17 M-trial scale; sampling 2,000 groups changes the Monte-Carlo error of Δ to ~0.001, below the reported effects. The item cap affects only a few large datasets (notably Rausch 2014 with 360 items).
- **Decided:** before running the final empirical analysis.
- **Effect:** negligible on estimates; increases Monte-Carlo noise slightly.

## V4. Item design-column list fixed in code

- **Preregistration (§3):** items are `Stimulus` plus any present column from the design list D.
- **Change:** none in substance; the list D was implemented exactly as specified. Noted here only because the effective item granularity differs across datasets depending on which columns exist, which limits pooling.
- **Decided:** before analysis.
- **Effect:** the empirical leg is a set of per-dataset estimates with heterogeneous item definitions, not a single pooled item set. This is stated as a limitation.

## V5. ICC estimation for within-item error correlation

- **Preregistration (§6):** `ρ` is the intraclass correlation of correctness among judges within items.
- **Change:** implemented as a one-way random-effects ICC on the judge-item correctness table with the standard unequal-group-size correction. No change to the definition.
- **Decided:** before analysis.

## Summary for the reader

The only deviation that changes what is reported as the headline empirical test is **V2** (the Brier estimand, chosen after seeing that the preregistered sign-based estimand was ceiling-bound). The preregistered sign-based results are reported in full and are consistent in direction. **V1** changes the simulation's mechanism, not its conclusion, and was forced by the prereg's own algebra. **V3** is a computational bound. None of the deviations changes the qualitative conclusions.