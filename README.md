# Selective feedback and comparative advisor evaluation

This research package asks when selectively verified advice supports a sound choice between an advisor and one's own judgements. The simulation finds a prespecified benefit and a prespecified cost of inverse-probability weighting; exact exploratory extensions examine equal opportunities, misspecified weights, and all conditional advantage-sign patterns. It is a computational Theory Article with an untested behavioural extension, not evidence that people implement the stipulated rules.

Read `manuscript/manuscript.pdf` or `manuscript/manuscript.html`; editable sources are `manuscript/manuscript.template.md`, generated `manuscript/manuscript.md`, and `manuscript/manuscript.tex`. The unsent cover letter is `manuscript/cover_letter.md`. Intended target: *Judgment and Decision Making*.

## Reproduce

Run `./run_all.sh` from this folder. Prerequisites: uv, pandoc, and XeLaTeX or tectonic. The script creates a local Python 3.14 environment, installs pinned numerical/plotting packages, regenerates all synthetic raw histories, analyses, checks, figures, and manuscript formats. It requires no credentials, participant records, paid APIs, or network service after dependency installation. Package installation requires internet access on the first run.

To reanalyse the saved raw histories without simulating again: `.venv/bin/python scripts/simulate.py summarise`, then run the verification/build/render commands listed in `run_all.sh`. Raw histories are `output/raw_counts.npz`, with category order and child streams documented in `output/metadata.json` and `output/cells.json`. The compressed archive is intentionally excluded from git but present in this delivered folder and reproducible from the committed seed/configuration.

The prospective plan is `prereg/preregistration.md`, committed at `68c07e4ca1858f382b131a0ee990adf562a271b0` before simulations. Its file hash and git provenance are preserved in `prereg/provenance.json`. This was a local prospective commitment, not public preregistration. The untouched earlier repository history contains a different project whose working files were already deleted when this task began.

`output/contrasts.json` contains the two registered tests; `output/summary.csv` contains every condition and learner; `output/verification.json` and `output/independent_check.json` record numerical checks. `output/manuscript_numbers.json` maps generated manuscript numbers and result paragraphs to outputs. Reference metadata and claim support are audited separately in `manuscript/reference_audit.md` and `manuscript/citation_check.md`.

## Scope and review

All scenarios are synthetic and contain no personal identifiers. No external human dataset was used. The package records scoping of openly licensed alternatives, the five closest papers, all decisions and deviations, AI involvement, code and manuscript reviews, and the author's five weakest points. Three manuscript-review rounds were completed, including Claude, Gemini and the full coarse pipeline; final Claude and Gemini reviews identify no remaining major issue within the declared scope. Every response is in `review_log.md`. Reviewer text is retained under `reviews/`; it is not evidence of journal peer review or human endorsement.

No manuscript was submitted, no person contacted, no account created, and no artifact publicly uploaded. Human authorship, affiliation, declarations, and responsibility require the intended author's assessment before any future submission. Review APIs used authenticated subscriptions; coarse literature-search calls incurred an estimated cost below US$0.20; the reconciled estimate is in `decision_log.md`.
