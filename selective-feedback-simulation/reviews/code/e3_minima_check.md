# E3 crossing-pattern minima and an observable poststratified alternative

The identical minima are genuine. They arise in `E3_17` (advisor better only at low confidence) and `E3_26` (advisor better only at high confidence), both with low-confidence share 0.75, maximal overlap, selection ratio 4, and 100 verified labels. No production code or primary output was changed for this check.

## Why the two risks coincide

At maximal overlap, each stratum's disagreements favour only its better source. In these worlds, both strata have disagreement probability 0.05. The marginal advisor advantage is +0.025 in E3_17 and −0.025 in E3_26. Audit selection is identical in the two worlds: low-confidence audited mass is 0.75 × 0.05 / 4, while high-confidence audited mass is 0.25 × 0.05. Thus the probability that an audited label comes from low confidence is 3/7 in both.

Let B be the number of low-confidence labels among 100 verified labels, so B has a Binomial(100, 3/7) distribution. In E3_17, the unweighted paired numerator is 2B−100 and the weighted numerator is 5B−100. In E3_26, both numerators change sign and the identity of the globally superior source also changes. Every realised history therefore incurs exactly the same loss under its corresponding rule in the two worlds. Fair treatment of ties preserves this equality.

I verified the resulting risks directly from binomial tail probabilities, independently of the E3 convolution:

$$R_{paired}=0.025\{P(B<50)+\tfrac12P(B=50)\},$$

$$R_{weighted}=0.025\{P(B<20)+\tfrac12P(B=20)\}.$$

The weighted-minus-paired contrast is approximately −0.0230994786452, or −2.30994786452 percentage points, in both worlds. The CSV reports this equality up to floating-point rounding. The equality concerns these symmetric boundary environments; it does not imply equal risk throughout the two crossing-pattern grids. The absolute rule is not sign-symmetric in this way because it compares advisor accuracy with a supplied human benchmark.

## Poststratification using encountered cases

A poststratified comparative estimator is feasible if the encounter log retains the human confidence stratum and both initial responses for every encountered case, including cases without verified outcomes. Disagreement can then be measured without observing the true outcome. With N encountered cases, let N_Dc count disagreements in stratum c. The proposed estimator can be written as

$$\widehat\Delta=\sum_c \frac{N_{Dc}}{N}\,\overline{(A-H)}_{verified\ D,c}
=\sum_c\widehat p_c\widehat d_c\,\overline{(A-H)}_{verified\ D,c}.$$

It targets the global advantage because $P(C=c,D)E[A-H\mid C=c,D]$ is each stratum's contribution and agreement cases contribute zero. It requires accurate verification, representative encountered cases, positive verification probability for every relevant disagreement stratum, and verification independent of comparative correctness within each stratum's disagreements. The stipulated constant stratum-specific audit probabilities meet that last condition. More selective verification within a stratum would require additional adjustment or a richer stratification.

This approach does not require the audit probability ratio to be known. It does require the unverified encounter log, which the primary fixed-label count histories do not contain. If a stratum has no verified disagreement, its conditional mean is undefined: a finite-sample implementation must specify what to do, and any exclusion, prior, pooling, or default can affect its bias and risk. Under suitable positivity and increasing observations in each stratum, the estimator is consistent. No general finite-sample unbiasedness claim is established here.

Its finite-sample source-selection risk is not automatically the same as the known-weight rule's risk. Estimated encounter proportions and disagreement rates are random; verified stratum counts and empty strata introduce additional variation, and shared records can make these quantities dependent. A fixed-label stopping rule also makes the number of encounters random. Although both procedures can consistently recover the same global ranking, their finite-sample decision risks require an explicitly specified encounter-and-verification model and a separate analysis. No new risk estimate or simulation is claimed in this note.
