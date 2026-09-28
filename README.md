# When does weighting by confidence help the crowd?

A Theory Article with an empirical test, produced without new data collection. It derives the finite-sample gap between confidence-weighted (CW) and equal-weighted (EW) aggregation of binary judgments, maps its boundary in a preregistered simulation, and tests it on 76 datasets from the Confidence Database.

**Headline result.** The two objectives diverge. On the preregistered crowd-decision measure, CW is a small but reliable improvement (+0.004, 95% CI [0.0003, 0.0083]; +0.007 on items the crowd does not already decide), and in a held-out item test it reaches 0.938 accuracy against 0.926 for EW. On an exploratory graded measure that predicts a held-out judge's correctness, CW is slightly worse (Brier improvement −0.0006, negative in 91% of datasets). Neither the calibration slope nor the within-item error correlation moderates either effect, and an estimated shrinkage weight beats EW in only 24% of datasets. A coarse two-input mapping of the calibrated simulation does not reproduce the data's signs.

## Read this first

- `manuscript/manuscript.pdf` (or `.html`, `.md`) is the paper. Target: *Judgment and Decision Making*, as a Theory Article.
- `manuscript/cover_letter.md` is the unsent cover letter.
- `prereg/preregistration.md` is the preregistration, committed at `03f4d3a` before any outcome analysis. `prereg/provenance.json` records its hash and commit.
- `deviations.md` lists every deviation and its effect; several changed the conclusions.
- `decision_log.md` records each decision with its reason. `novelty.md` gives the five closest papers. `review_log.md` records every reviewer comment and response. `ai_disclosure.md` and `weaknesses.md` are the AI-use disclosure and the author's own five weakest points.

## Reproduce

Run `./run_all.sh` from this folder. Prerequisites: `uv` and Python 3.12+. The script creates a local environment, installs pinned packages, downloads the CC0 Confidence Database if absent, and regenerates all simulated data, analyses, checks, figures, and numbers with one command. No credentials or paid APIs are needed after dependency installation.

Outputs are written to `analysis/output/` (per-dataset estimates, simulation grid, hypothesis summaries, verification, figures, and `manuscript_numbers.json`).

## Scope and integrity

All data are openly licensed (CC0) and contain no personal identifiers. No new data were collected. No manuscript was submitted, no person was contacted, no account was created, and no artifact was uploaded publicly. Reviews were produced by AI tools (codex, agy, and the coarse-review pipeline) on existing subscriptions; their text is retained in `reviews/` and is not human endorsement. Human authorship, affiliation, and responsibility require the project owner's assessment before any submission.