# Data sources and how to obtain them

All raw inputs are openly licensed and re-downloadable. They are excluded from git
by size but the analysis will re-download them if absent.

## Confidence Database (empirical component)

- Source: OSF node `s46pr`, https://osf.io/s46pr/
- DOI: https://doi.org/10.17605/OSF.IO/S46PR
- Licence: CC0 1.0 Universal
- Citation: Rahnev et al. (2020), *Nature Human Behaviour*, 4(3), 317-325,
  https://doi.org/10.1038/s41562-019-0813-1
- Files used: the 180 per-study `data_*.csv` files in the `Confidence Database`
  folder. Download listing:
  `https://api.osf.io/v2/nodes/s46pr/files/osfstorage/5e9ecb6da0ea43006254b422/?page%5Bsize%5D=100`
  (paginated). Each file's `data` link is a direct download. The analysis stores
  them under `data/confidence_database/`.

## No other data

The formal derivation and the simulation use no external data. The Good Judgment
Project and OpAQ data used in sibling papers are **not** used here.