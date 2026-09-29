# Data provenance

No third-party participant dataset was downloaded or analysed. Open-data scoping was restricted to public documentation and licence records, with the exact exposure listed in `scoping/journal_and_data.md`. Published results read during literature review were used for context, not fitted numerical parameters.

The analysis inputs are generated synthetic categorical histories from `config.json`, with generation rules committed in `prereg/preregistration.md` before the first run. The compressed raw count archive is `output/raw_counts.npz`; cell keys, category order, random streams, and hashes are in `output/cells.json` and `output/metadata.json`. It contains no personal identifiers, respondents, prompts, or generated personal records. Each row represents one simulated feedback history.

The synthetic archive is regenerated with `./run_all.sh`; no external data licence, API credential, account, or network data download is required. Public literature metadata retained for citation checking is stored separately under `scoping/reference_metadata/`. Article copyrights are not represented as dataset licences, and full articles are not redistributed as study data.
