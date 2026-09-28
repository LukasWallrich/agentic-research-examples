# AI-use disclosure

This document is written to satisfy the AI-use policies of *Judgment and Decision Making* and Cambridge University Press ("research publishing ethics guidelines", https://www.cambridge.org/core/services/authors/publishing-ethics/research-publishing-ethics-guidelines-for-journals), which require that the use of AI-assisted technologies be disclosed and that AI systems are not listed as authors.

## What was done with AI assistance

- **Scoping and literature search.** AI agents searched Crossref and Europe PMC for candidate topics and for the closest prior work, and produced the crowding assessments in `scoping/`. All references were verified against Crossref by script (`analysis/scripts/verify_references.py`, output `manuscript/reference_audit.md`); no DOI was taken from memory.
- **Preregistration and analysis code.** The preregistration was drafted by the AI assistant under human-specified constraints and committed to git before the outcome variables were analysed. All analysis, simulation, and figure code was written by the AI assistant. The code is deterministic and reruns from the raw, openly licensed data with one command (`run_all.sh`).
- **Manuscript and cover letter.** Drafted by the AI assistant, then reviewed by independent AI reviewers (codex, agy, and the coarse-review pipeline). Reviewer comments and the responses to them are in `review_log.md`.
- **Independent second opinions.** Cross-model reviews (OpenAI codex, Google Gemini via agy) were used on the topic choice, the code and results, and the manuscript. Their outputs are retained in `reviews/` and summarised in `review_log.md`.

## What AI did not do

- No AI system is listed as an author. Authorship, affiliations, and responsibility rest with the human project owner.
- No AI system contacted any person, created any account, submitted any manuscript, or uploaded any artefact publicly.
- No AI system collected new data. The empirical component reuses the openly licensed (CC0) Confidence Database, and the simulation generates synthetic data from a committed configuration.

## Models and tools used

- The analyses were written and executed with an AI coding assistant (OpenRouter-hosted models via the OpenCode harness) using Python 3.12, NumPy, pandas, SciPy, and Matplotlib.
- Independent reviews used the OpenAI codex CLI and the Antigravity (agy) CLI with Gemini 3.8 Flash, plus the local coarse-review pipeline.
- No paid data-collection or human-participant services were used. The only external service costs were the review APIs on existing subscriptions.

## Human verification required before submission

The intended author must, before any submission: verify authorship criteria and affiliation; confirm every claim against the source it cites; confirm the analysis is correct and reproducible; and accept responsibility for the content. The author's own assessment of the paper's weakest points is in `weaknesses.md`.
