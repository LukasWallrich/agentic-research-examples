# Decision log

Autonomous decisions for `ai-jdm-paper4`, in order. Each entry states the decision, the reason, and (where relevant) what was rejected and why.

## D1. Project setup
- **Decision:** Initialise git in `/Users/lukaswallrich/Documents/Coding/ai-jdm-paper4`; use a `scoping/ prereg/ analysis/ manuscript/ reviews/` layout mirroring the three sibling papers.
- **Reason:** The brief requires a committed preregistration before analysis, rerunnable code, and a manuscript, so the layout must separate plan from execution.

## D2. Avoid duplicating the three sibling papers
- **Decision:** Exclude anchoring (paper 1), Good Judgment Project / probability forecasting / belief-updating (paper 2), and selective feedback / advisor verification (paper 3).
- **Reason:** Read all three siblings' `novelty.md`. The brief is to produce a *novel* paper; re-treading their territory would fail that test.

## D3. Topic: confidence-weighted vs equal-weighted aggregation of judgments
- **Decision:** Study when weighting judges by their reported confidence beats simple equal weighting in binary crowd aggregation, with a formal finite-sample boundary, a simulation, and an empirical mapping across open datasets.
- **Reason:** Scoping (two parallel agents) and an independent codex review of candidates. Codex ranked this first among the candidates and it is distinct from all three siblings (none is about aggregation weights). It is a core JDM question, has a crisp refutable structure, and needs no new data.
- **Rejected:** (a) cross-study intertemporal-choice model generalisation on the new ITC Database — codex flagged a live priority risk (the database creators presented a 2026 talk on exactly the response-time question) and Krajbich et al. (2015) already made the difficulty-adjustment point; (b) sunk-cost and overprecision "first meta-analyses" — both agents found existing systematic reviews; (c) GPS measurement invariance — agy reported prior invariance work and low JDM interest; (d) inner-crowd noise structure — crowded by van Dolder & van den Assem (2018) and data access is hard.

## D4. Confidence Database as the empirical substrate
- **Decision:** Use the Confidence Database (Rahnev et al., 2020; OSF `s46pr`; **CC0**) for the empirical component.
- **Reason:** Most permissive licence (public-domain dedication), 180 per-study CSVs, trial-level confidence + correctness + stimulus identifiers, no identifiers.

## D5. Empirical design: item = shared stimulus/condition cell; vote = signed correctness
- **Decision:** Define an "item" as a shared stimulus/condition cell (`Stimulus` plus available design columns), a judge's vote in an item as the mean of (2·Accuracy − 1) over their trials in it, and the crowd's decision as the equal-weighted or confidence-weighted mean of votes. Compare crowd-decision accuracy as a function of group size.
- **Reason:** Feasibility checks showed the database records correctness per trial, so no truth reconstruction from responses is needed; this makes the estimand general across datasets. It also matches the group-size question the theory addresses.
- **Consequence:** The empirical component is a **descriptive mapping / prevalence estimate**, not a clean randomised crowd experiment. Framed accordingly.

## D6. Make the paper theory/simulation-primary, empirical-secondary
- **Decision:** The formal finite-sample boundary and the boundary-surface simulation carry the paper; the Confidence Database analysis calibrates the theory's inputs and estimates the prevalence of the CW-harmful region.
- **Reason:** A focused novelty check found that the atomic claims (weighting can hurt; correlated-error optimal weights; miscalibration degrades optimal rules; confidence weighting beats majority in real crowds) are all published (Shapley–Grofman 1984; Baharad & Ben-Yashar 2009; Meyen et al. 2021; Huang et al. 2024). The defensible novel core is (i) the CW−EW gap written in psychometric coordinates (calibration slope, within-item error correlation, confidence dispersion), (ii) a preregistered boundary-surface simulation, and (iii) a descriptive base-rate estimate across real multi-judge datasets. So the paper must not lean on the empirical leg alone.

## D7. Independent consults before committing
- **Decision:** Obtained a codex second opinion (read-only) and an agy second opinion on the topic shortlist, and a dedicated novelty/crowding literature check.
- **Reason:** The brief asks for codex/agy review wherever helpful; the topic choice was the highest-stakes decision and the cheapest place to catch a fatal overlap.

## D8. Target journal (to confirm in Phase 4)
- **Decision:** *Judgment and Decision Making* (JDM).
- **Reason:** Open-access, exact scope match, and the intended outlet of sibling paper 3. Final justification (APC, AI policy, guidelines) to be recorded in Phase 4.

## D9. Honesty about what has been seen before preregistration
- **Decision:** Record in the preregistration exactly which data properties were inspected before writing it: file names and sizes, column headers, counts of rows/subjects/stimuli, whether `Response` has two levels, and the fraction of `Stimulus` cells whose reconstructed truth is unique. No accuracy, confidence, or choice aggregates were computed.
- **Reason:** The brief requires stating what has been seen for a secondary-data preregistration. Structural feasibility checks are necessary to design an analysable study, but must be disclosed.
## D10. Item and vote definitions in the empirical leg
- **Decision:** Define an item as a shared condition cell and a judge's vote as the sign of her recorded correctness, rather than reconstructing a per-item truth from responses.
- **Reason:** Feasibility checks showed most datasets code `Stimulus` as a coarse condition, not a unique shared stimulus, so truth reconstruction is unreliable. Using recorded correctness directly makes the estimand well-defined across heterogeneous datasets.
- **Consequence:** The empirical leg estimates how confidence reweighting changes the crowd's estimate of a shared condition, not a matched-stimulus group decision. Stated as the first weakness in `weaknesses.md`.

## D11. Fixed an item-key parsing bug and re-included two datasets
- **Decision:** After the first analysis run, fixed the item-key construction (pandas 3.0 preserves missing values through `astype(str)`), which had silently excluded two datasets as `parse_error`. Re-ran the full analysis; included datasets rose from 79 to 81.
- **Reason:** The parse error was a data-engineering bug, not a preregistered exclusion.
- **Recorded in** `deviations.md`. All manuscript numbers were regenerated from the corrected outputs.

## D12. Target journal: *Judgment and Decision Making* (JDM)
- **Decision:** Submit as a **Theory Article** to JDM.
- **Reason:** The journal's scope explicitly lists "advances in methods for improving JDM (e.g., wisdom-of-the-crowd)" and "development of new theories / modification or specification of existing theories", which match a formal-plus-simulation-plus-empirical paper on aggregation weights. It requires data and code availability, which the project already provides, and uses APA citation style, which the manuscript follows. Article length is unrestricted. The finance and AI policies were read (Cambridge research publishing ethics guidelines; see `ai_disclosure.md`).
- **Rejected:** *Decision* (APA) was a close second but the theory-first framing fits JDM's stated scope better; *Journal of Behavioral Decision Making* was less of a match for the wisdom-of-crowds framing.

## D13. Supporting documents
- **Decision:** Drafted `manuscript/cover_letter.md`, `ai_disclosure.md`, and `weaknesses.md`, and verified all 26 manuscript DOIs against Crossref (`manuscript/reference_audit.md`, zero failures).
- **Reason:** Required by the brief and by JDM's author instructions.

## D14. Review-driven revision and final framing
- **Decision:** After codex (two rounds), agy, and the coarse-review pipeline, the pipeline bugs were fixed, the preregistered hypotheses were reported with their outcomes (H1 supported, H2 not supported, H3 supported, H4 descriptive, H5 not supported, H6 rejected), and the paper was reframed around the divergence between the decision and judge-prediction objectives.
- **Reason:** The reviews found real errors (replacement sampling, unstable seeds, an ICC on trials, the H6 success rule, an even-`m` tie artefact) and a framing problem (the exploratory graded measure was leading while the preregistered decision measure was positive). Fixing them changed the H5 conclusion and the sign arbitration.
- **Consequence:** The manuscript now leads with the preregistered decision result, labels the graded measure exploratory, reports that estimated shrinkage does not beat equal weighting, reports minimum detectable effects for the moderation nulls, and softens the model-rejection claim to the resolution of the mapping.
- **Unresolved:** no general closed-form derivation of the boundary (a sign condition is given); the one-to-one stimulus-to-exemplar mapping is not recoverable from the corpus.
