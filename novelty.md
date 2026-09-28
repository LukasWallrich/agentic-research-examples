# Novelty: the five closest papers and what this study adds

Study: *When does weighting by confidence hurt the crowd? A finite-sample boundary, a simulation, and a descriptive base rate across open judgment datasets.*

Search basis: 28 September 2026. Crossref REST API (sixth targeted `query.bibliographic` sweeps, ~500 records screened), Europe PMC, and the citing-paper screens in `scoping/`. OpenAlex was unavailable on this network (daily budget exhausted until midnight UTC) and Google Scholar could not be queried, so "no prior work located" means "none located in Crossref/Europe PMC on this date", not proof of absence. The dedicated crowding report is `scoping/novelty_confidence_weighting.md`; every DOI below was resolved through `https://api.crossref.org/works/{DOI}` and matched on title, authors and year.

## Study contribution

The paper combines three components:

1. **Formal:** the expected-accuracy gap between confidence-weighted (CW) and equal-weighted (EW) aggregation of binary judgments, written explicitly as a function of three estimable psychometric quantities — the confidence–accuracy calibration slope, the within-item correlation of judgment errors, and confidence dispersion — in the finite-sample regime (few judges per item).
2. **Simulation:** a preregistered sweep of the boundary surface in those coordinates, with the optimal interior shrinkage between CW and EW, and a stated failure condition.
3. **Descriptive empirical:** the fraction of real multi-judge datasets in which CW does not beat EW, and how the CW advantage depends on group size, mapped across open datasets from the Confidence Database (Rahnev et al., 2020).

The atomic claims are not new (see below). The additions are the psychometric parametrisation of the gap and its simulated boundary, and the first descriptive base-rate estimate of the CW-harmful region across real judgment datasets.

## Five closest papers

| # | Paper | What it did | What this study adds |
|---|---|---|---|
| 1 | **Meyen, S., Sigg, D. M. B., von Luxburg, U., & Franz, V. H. (2021). Group decisions based on confidence weighted majority voting.** *Cognitive Research: Principles and Implications*, 6(1). https://doi.org/10.1186/s41235-021-00279-0 | Directly compared confidence-weighted majority voting (CWMV) with unweighted majority voting (MV) for binary group decisions, with formal modelling and fits to real group responses. Found simulated CWMV matched real groups better than MV, but real groups weighted votes *more equally* than CWMV prescribes; stated CWMV's optimality as conditional on independent, accurate confidence. | Does not derive when CWMV is *worse* than MV, does not parametrise shared error or miscalibration, and does not sweep a boundary. This study supplies the negative-space result: the explicit region where the "theoretically optimal" rule loses, as a function of calibration and error correlation. |
| 2 | **Huang, S., Broomell, S. B., & Golman, R. (2024). A hypothesis test algorithm for determining when weighting individual judgments reliably improves collective accuracy or just adds noise.** *Decision*, 11(1), 7–34. https://doi.org/10.1037/dec0000187 | Gave a statistical test for whether enough judgments exist to reject the simple average in favour of a weighted average as reliably more accurate; the closest single paper to the question "when does weighting beat equal weighting". | Huang et al. frame the risk of weighting as **finite-sample estimation noise in the weights**, not as a systematic property of miscalibration, shared bias, or confidence dispersion. This study derives the bias/miscalibration route and writes the gap in psychometric coordinates, then attaches a descriptive prevalence estimate rather than a per-dataset test. |
| 3 | **Shapley, L., & Grofman, B. (1984). Optimizing group judgmental accuracy in the presence of interdependencies.** *Public Choice*, 43(3), 329–343. https://doi.org/10.1007/BF00118940 | Derived optimal weights for group accuracy when voters' judgments are statistically interdependent; showed naive (equal or competence-proportional) weighting is not generally optimal once errors are shared. | The biggest threat to a "first formal boundary" claim. What is absent is a subjective-confidence instantiation (a noisy, possibly miscalibrated proxy with its own dispersion), the finite-sample form, and any empirical test of how often real crowds fall in the harmful region. |
| 4 | **Baharad, E., & Ben-Yashar, R. (2009). The robustness of the optimal weighted majority rule to probability distortion.** *Public Choice*, 139(1–2), 53–59. https://doi.org/10.1007/s11127-008-9378-7 | Analysed how the optimal weighted-majority rule degrades when the competence inputs it uses are distorted, i.e. when weights come from miscalibrated signals rather than true competences. | The *mechanism* (miscalibrated weights hurt the optimal rule) is already established here for abstract decisional skills. This study instantiates the distorted signal as reported confidence in a binary crowd, adds the confidence-dispersion term, and quantifies the empirical prevalence. |
| 5 | **Jin, S., Verhaeghen, P., & Rahnev, D. (2022). Across-subject correlation between confidence and accuracy: A meta-analysis of the Confidence Database.** *Psychonomic Bulletin & Review*, 29(4), 1405–1413. https://doi.org/10.3758/s13423-022-02063-7 | The existing large-scale meta-analysis of the Confidence Database (Rahnev et al., 2020); pooled datasets to estimate the *across-subject* confidence–accuracy correlation and its moderators. | Estimates a calibration/validity correlation, not an aggregation-rule comparison. This study reuses the same database for item-level crowd aggregation and estimates the prevalence of the CW-harmful region. It must **not** be billed as the first mega-analysis of the database — Jin et al. did that, on a different question. |

## Further overlap

- **Forecast-combination puzzle** (Smith & Wallis, 2009, https://doi.org/10.1111/j.1468-0084.2008.00541.x; Claeskens et al., 2016, https://doi.org/10.1016/j.ijforecast.2015.12.005): estimated optimal weights routinely lose to equal weights. This constrains what the empirical result can claim to discover.
- **Correlated-votes jury theory** (Ladha, 1995, https://doi.org/10.1016/0167-2681(94)00068-p; Kaniovski, 2010, https://doi.org/10.1007/s11238-008-9120-4) and **Hogarth (1978)**, https://doi.org/10.1016/0030-5073(78)90037-5: more judges help only up to a point when errors correlate.
- **Bayesian combination of correlated subjective estimates** (Trick, Jäkel & Rothkopf, 2026, *JDM*, https://doi.org/10.1017/jdm.2026.10035): models inter-forecaster correlation and shows ignoring it is suboptimal.
- **Crowd empirics** (Saha Roy et al., 2021, https://doi.org/10.1038/s41598-020-80500-0; Berger et al., 2025 preprint, https://doi.org/10.31234/osf.io/j9t6p_v2) already compare confidence-based aggregation with equal/majority pooling; Berger et al. optimise crowd *efficiency*, not the CW-vs-EW boundary.

## What this study must not claim

1. That weighting by a signal can hurt aggregation (established: forecast-combination puzzle; Huang et al., 2024).
2. That correlated errors bound aggregation gains and change optimal weights (Shapley–Grofman, 1984; Ladha, 1995).
3. That miscalibrated competence inputs degrade optimal weighted majority (Baharad & Ben-Yashar, 2009).
4. That confidence weighting beats majority/equal weighting in real crowds (Meyen et al., 2021; Saha Roy et al., 2021).
5. That this is the first mega-analysis of the Confidence Database (Jin et al., 2022).

## Honest scope limitation

The Confidence Database is a single-subject confidence corpus; whether the same item is judged by multiple people varies, and the empirical leg is a descriptive mapping rather than a designed crowd experiment. If the item-level overlap is thin, the empirical leg weakens and the contribution rests on the formal and simulation components — which are the less novel part. This is stated in the preregistration and in `weaknesses.md`.