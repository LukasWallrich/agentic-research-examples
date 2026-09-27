# AI disclosure

## Summary

This study was conceived, designed, preregistered, coded, analysed, written and reviewed by AI systems. The human author, Lukas Wallrich, set the task and its constraints in a single instruction and did not intervene in the work that followed. He is accountable for the content under the policies of the target journal. The AI's role is disclosed here in full so that readers and editors can judge the work with that knowledge.

## What the human author did

- On 27 September 2026, gave one instruction: produce a complete, novel judgement-and-decision-making paper without collecting new data, working autonomously, recording decisions, preregistering before analysis, reviewing with other AI systems, and not submitting anything or contacting anyone.
- Provided the working environment (Claude Code with access to R, Quarto, the web, OpenAlex and Crossref, and the codex and agy command-line tools) and his writing style guide.
- Did not choose the research question, dataset, models, analyses or wording, and did not review the work before this record was written.

Before any submission, the author would need to read and verify the work, take responsibility for every claim, and decide whether to submit. None of that has happened yet.

## What the AI systems did

| System | Version | Access | Role |
|---|---|---|---|
| Claude (Anthropic) | Claude Opus 5.5 (model id claude-opus-5-5, 1M-token context), run in Claude Code | Anthropic API / Claude Code | Lead agent. Scoped the literature and datasets (through subagents running the same model), chose the study, wrote the preregistration, the simulation models and all R code, ran all analyses, made the figures, wrote the manuscript, cover letter and all project documents, and responded to reviews. Every decision and its reason is in `decision_log.md`. |
| Claude subagents | Claude Opus 5.5 | Claude Code Agent tool | Parallel literature searches, dataset licence checks, novelty checks, journal-policy extraction, citation-support checks. |
| OpenAI Codex CLI | codex-cli 0.155.1 (default model) | `codex exec`, read-only sandbox | Critique of the study shortlist; review of code and results; manuscript reviews. Outputs in `reviews/`. |
| Google Gemini via Antigravity CLI | Gemini 3.8 Flash (High) | `agy -p`, sandboxed | Critique of the study shortlist; manuscript reviews. Outputs in `reviews/`. |
| coarse-review pipeline | local Claude Code skill running Claude models headlessly | `coarse-review` skill | Full structured peer review of the manuscript. Output in `reviews/`. |

Dates of use: 27-28 September 2026.

## Safeguards

- **Preregistration before data contact.** The preregistration, frozen model predictions and analysis code were committed to git (tag `prereg-v1`, commit a40911b) before any outcome variable was read. The data reader (`R/read_opaq.R`) refuses to load the outcome column until the preregistration is committed. Only design columns were read before that commit; `prereg/preregistration.md` (Q18) lists them.
- **Numbers come from code.** Every number in the manuscript is computed inline from files in `output/`, which `run_all.sh` regenerates from the raw data.
- **References.** The bibliography was built by script from DOIs through doi.org content negotiation (Crossref and DataCite metadata); no reference was typed from memory. A separate agent checked each citation against the source text for support of the claim it is attached to (`manuscript/citation_check.md`).
- **Independent review.** Two non-Anthropic AI systems reviewed the design, code and manuscript; all comments and responses are in `review_log.md`.

## Known risks of AI authorship in this project

- The same model family that wrote the paper also judged which reviewer comments to accept. Rejected comments and the reasons are listed in `review_log.md` so that a human can second-guess them.
- Literature knowledge from model training may be out of date or wrong. Literature claims were therefore checked against retrieved texts, not recalled.
- The AI chose the research question under an instruction to produce a paper. Scoping reports (`scoping/`) and the decision log show the alternatives considered.

## Compliance with the target journal's policy

Judgment and Decision Making applies the Cambridge University Press policy (`scoping/journals/jdm.md`): AI tools may not be listed as authors; AI use in analysis is described in the Methods; AI-generated text is declared in the Acknowledgements; AI-generated figures are declared in their captions; each declaration names the tool and version, the dates, how others can access it, and a full description of the use. The manuscript follows these rules. No AI system is listed as an author.
