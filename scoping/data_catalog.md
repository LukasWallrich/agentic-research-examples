# Openly licensed JDM / behavioural-decision datasets — scoping catalog

Date of scouting: 2026-09-28
Scope: de-identified, openly licensed datasets usable either for (a) a secondary JDM analysis or (b) validation of a decision-making simulation. Excludes OpAQ (anchoring) and Good Judgment Project (forecasting), per brief.
Method: OSF API v2 (`api.osf.io/v2/nodes/`), Zenodo REST API, Crossref, Europe PMC, GitHub API. Every URL below was opened and every license read from the repository's own license field. Anything not confirmed is marked **UNVERIFIED**.

License key: CC0 / CC-BY-4.0 / MIT = fully permissive for research reuse. CC-BY-NC-SA-4.0 = research reuse OK, no commercial use, share-alike. `none` = no license declared → **all rights reserved, do not reuse without written permission** (listed only to document the gap).

---

## A. Verified, openly licensed datasets

### A1. The Confidence Database
- **URL / DOI:** https://osf.io/s46pr/ — OSF DOI `10.17605/OSF.IO/S46PR`
- **Citation:** Rahnev et al. (2020), *The Confidence Database*, Nature Human Behaviour 4, 317–325. https://doi.org/10.1038/s41562-019-0813-1
- **License:** **CC0 1.0 Universal** (verified via OSF license id `563c1cf88c5e4a3877f9e96c`).
- **Size:** At publication: **145 datasets, >8,700 participants, ~4 million trials** (verified from the published abstract). The live OSF storage folder has since grown to **360 files / ~255 MB** (data CSVs + per-study readmes).
- **Variables:** trial-level **confidence rating**, **accuracy/correctness**, and task condition; many studies also carry response time, stimulus parameters, and demographics. Structured in a common format (one CSV + one readme per study).
- **Download:** direct per-file, e.g. https://osf.io/download/xkc7b/ (Database_Information.xlsx); individual study CSVs via the `osfstorage` folder. No registration.
- **Prior analyses / novelty headroom:** The original paper ran four exemplar aggregate analyses. It is a "database" project explicitly designed for reuse, so many secondary papers exist (individual-differences in metacognition, confidence–accuracy calibration, domain generality). **Low licence risk, moderate novelty headroom** — strongest as a large aggregated sample for a *new* question rather than confirming known confidence effects.

### A2. CPC2015 — Raw data (decisions under risk, ambiguity, and from experience)
- **URL / DOI:** https://zenodo.org/records/321652 — `10.5281/zenodo.321652`
- **Citation:** Erev, Ert & Plonsky (2017). CPC2015 choice prediction competition.
- **License:** **CC-BY-4.0** (verified via Zenodo API).
- **Size:** **>330,000 consequential choices** between two prospects; 3 experiment files (7 MB, 9 MB, 10 MB CSV) ≈ 26 MB.
- **Variables:** participant ID, location/gender/age, choice problem (two lotteries: outcomes × probabilities), condition (by-probability vs by-feedback / description vs experience), trial, **choice** (B), payoff, forgone payoff, block; **RT only in a subset**.
- **Download (direct):**
  - https://zenodo.org/records/321652/files/RawDataExperiment1sorted.csv/content
  - https://zenodo.org/records/321652/files/RawDataExperiment2sorted.csv/content
  - https://zenodo.org/records/321652/files/RawDataExperiment3sorted.csv/content
- **Prior analyses / novelty headroom:** Competition papers (Erev et al. 2010, 2017) and follow-up modelling papers. Substantially less re-analysed than CPC18 → **good novelty headroom**.

### A3. CPC18 — Calibration and full raw data
- **URLs / DOIs:**
  - Calibration set: https://zenodo.org/records/845873 — `10.5281/zenodo.845873` (510,750 choices, 45 MB CSV)
  - Full raw data: https://zenodo.org/records/2571510 — `10.5281/zenodo.2571510` (62 MB CSV, calibration + test sets)
- **Citation:** Plonsky, Erev & Ert.
- **License:** **CC-BY-4.0** (both records, verified).
- **Size:** Calibration: **510,750 consequential choices**; full raw adds the competition test set.
- **Variables (from the Zenodo dictionary PDF, verified):** `SubjID`, `Location`, `Gender`, `Age`, `Set`, `Condition`, `GameID`, lottery definitions (`Ha,pHa,La,LotShapeA,LotNumA` and B equivalents), `Amb` (ambiguity), `Corr` (correlation), `Order`, `Trial`, `Button`, **`B` (choice)**, `Payoff`, `Forgone`, **`RT` (response time, ms — only for Sets 6–7)**, `APay`, `BPay`, `Feedback`, `Block`.
- **Download (direct):** `.../files/All%20estimation%20raw%20data.csv/content`, `.../files/all%20CPC18%20raw%20data.csv/content`, plus dictionary PDF.
- **Prior analyses / novelty headroom:** Widely used as a modelling benchmark (Plonsky et al. 2019 *JDM*; many ML entries). **Moderate novelty headroom** but highest data quality/documentation for simulation validation.
- **Related OSF node:** CPC18 analysis materials, OSF node `dekt3` (https://osf.io/dekt3/), **MIT License**, includes `rawData_Comp_All.csv` (17.5 MB, direct: https://osf.io/download/4xk39/), train/test sets, and replication scripts.

### A4. ITC Database — large-scale intertemporal choice with response times
- **URL / DOI:** https://osf.io/3wsae/ — `10.17605/OSF.IO/3WSAE`
- **Descriptor:** "A large-scale dataset of choice and response-time data in intertemporal choice" (data-descriptor preprint included on the node).
- **License:** **CC-BY-NC-SA-4.0** (verified; research reuse permitted, no commercial use, share-alike).
- **Size:** **`all_data.csv` = 462 MB** (+ `all_data.RData` 8 MB).
- **Variables:** choice and **response time** in intertemporal-choice tasks across many studies, with the usual delayed-reward/SS–LL structure (inspect the descriptor PDF for exact columns).
- **Download (direct):** https://osf.io/download/69y5j/ (CSV), https://osf.io/download/98d6p/ (RData).
- **Prior analyses / novelty headroom:** Newly released data descriptor → **high novelty headroom**. Best fit for validating a simulation with both choice *and* RT.

### A5. Many Labs 3
- **URL / DOI:** https://osf.io/ct89g/
- **License:** **CC-BY-4.0** (verified).
- **Size:** two large files — `ML3 PPool and MTurk Data.csv` (5.0 MB) + `ML3 Task Order Data.csv` (0.1 MB); multiple sites, thousands of participants.
- **Variables:** replication outcomes across several classic effects, task order, response data, site; mostly cognitive/social rather than core JDM.
- **Download (direct):** via node files, e.g. https://osf.io/download/… (open `ct89g` storage).
- **Prior analyses / novelty headroom:** Published as Ebersole et al. (2016). **Moderate** JDM relevance; useful as a participant-pool/order-effect covariate source.

### A6. Many Labs 2
- **URL / DOI:** https://osf.io/ux3eh/
- **License:** **CC0 1.0** (verified).
- **Size:** large multi-site replication (Klein et al. 2018), 13 effects across 36 sites.
- **Variables:** effect estimates, site, sample; includes classic judgement-bias-adjacent effects. Not primarily JDM.
- **Download:** node storage (open).
- **Novelty:** mainly a methodological/robustness reference.

### A7. Psychological Science Accelerator COVID-19 Rapid Response (PSACR)
- **URL / DOI:** https://osf.io/3g7vq/
- **License:** **CC0 1.0** (verified).
- **Size:** very large multi-country sample; materials + data on node.
- **Variables:** pandemic attitudes/behaviour; not a core JDM choice paradigm but rich covariates for decision context.
- **Download:** node storage (open).
- **Novelty:** usable as a covariate/context dataset, not a primary JDM dataset.

### A8. Verbal Cognitive Reflection Test (CRT-V)
- **URLs / DOIs:**
  - OSF: https://osf.io/xehbv/ — **CC-BY-4.0** (verified), 8 study CSVs + codebook.
  - Zenodo mirror: https://zenodo.org/records/22916374 — `10.5281/zenodo.22916374`, **CC-BY-4.0**.
- **Citation:** LIRA Lab (CRT-V development/validation).
- **Size:** 8 studies; per-study CSVs (`Study1…Study8 CRT-V.csv`) + `Codebook Studies 1 to 8.txt`.
- **Variables:** CRT-V responses, maths-free cognitive-reflection items, sociodemographics (Study 5).
- **Download (direct):** e.g. https://osf.io/download/qxruy/ (Study 1), https://osf.io/download/ejda8/ (Study 6).
- **Prior analyses / novelty headroom:** Validation paper exists; **moderate** JDM relevance (individual differences in reflection/decision quality).

### A9. Advice source and belief revision under uncertainty
- **URL / DOI:** https://zenodo.org/records/22101889 — `10.5281/zenodo.22101889`
- **Title:** Data, Materials, and Analysis Code for "Human or AI? How Advice Source and Extremity Shape Belief Revision Under Uncertainty" (Lee, 2026).
- **License:** **CC-BY-4.0** (verified).
- **Size:** `MainStudy_N253_public.csv` + two pretests (N≈253 main).
- **Variables:** **advice source (human vs AI)**, advice extremity, prior beliefs, belief revision, uncertainty.
- **Download (direct):** https://zenodo.org/records/22101889/files/MainStudy_N253_public.csv/content
- **Prior analyses / novelty headroom:** Single recent study → **high novelty headroom** for advice-taking secondary analyses; small N.

### A10. Delay discounting: real vs hypothetical (adolescence)
- **URL / DOI:** https://osf.io/9zfm7/
- **License:** **CC-BY-4.0** (verified).
- **Size:** two Excel data files (`DATA-9-18-DDTASKS2025.xlsx`, `2026`), 33 KB each; User-Guide and Software folders.
- **Variables:** delay-discounting task choices (hypothetical vs real), likely demographics; see node user guide.
- **Download (direct):** on node (open).
- **Prior analyses / novelty headroom:** New → **high novelty headroom**; intertemporal + incentive-realism angle.

### A11. Decisions from experience — Hertwig group OSF nodes
- **Frey, Pedroni, Mata, Rieskamp & Hertwig (2017)** — https://osf.io/47kqs/ — license **GPL-3.0** (verified; unusual for data, but open). Analysis pipeline folders (`00_preparation` … `25_regressions`).
- **Lejarraga, Frey, Schnitzlein & Hertwig (2019)** — https://osf.io/5nj8s/ — **CC-BY-4.0** (verified). Contains modelling code (`lejarraga_2019/`) and an `objects/` folder; raw-trial data location on the node was **UNVERIFIED** (subfolder listings were empty via API — likely linked child nodes).
- **Note:** a companion node `w3zmr` (same title) is explicitly `license = none`; use only the CC-BY `5nj8s` version.
- **Variables (DFE):** sampling/experience trials, described vs experienced probabilities, choices, outcomes.
- **Novelty:** DFE remains active but Hertwig-group data is heavily modelled; **moderate** headroom.

### A12. Adolescent decision-making (polygenic risk, ADHD/anxiety)
- **URL / DOI:** https://osf.io/ca49h/
- **License:** **Academic Free License (AFL) 3.0** (verified; OSF-classified open licence — permissive but uncommon; read terms before reuse).
- **Size / data:** node storage listing showed only `SOM_Results.html` (5.9 MB) at time of check; **raw data availability UNVERIFIED**.
- **JDM relevance:** adolescent decision-making phenotypes; potentially valuable but treat as unverified.

### A13. Mouselab-MDP (process tracing / planning)
- **Code repo:** https://github.com/fredcallaway/Mouselab-MDP — **MIT License** (verified). Repository contains the JsPsych experiment plugin and `experiment/` code; **raw datasets are not in this repo (UNVERIFIED / not located here)**.
- **Companion:** `RationalityEnhancementGroup/mouselab-mdp-tools` (MIT) — analysis/simulation tools.
- **Relevance:** process-tracing of planning / information acquisition — excellent *paradigm* fit for a simulation, but data must be sourced from the associated experiment papers (Callaway et al.) separately. Mark data as **UNVERIFIED**.

---

## B. Datasets checked and NOT usable (documented gaps)

| Dataset | URL | Problem |
|---|---|---|
| Iowa Gambling Task, 617 healthy adults ("Many Labs") | https://osf.io/8t7rm/ | **license = none** (no reuse grant). Data originate from Steingroever et al. (2014); look for a separately licensed copy. |
| Frey et al. risk-preference specification-curve / typology data (`frey2021_jpsp`, `frey2023_jru`, 68 MB / 600 MB) | https://osf.io/b2fej/, https://osf.io/pjt57/ | **license = none**. Large and JDM-relevant, but cannot be reused as-is. |
| Framing effect among stock-market investors | https://osf.io/46u85/ | **license = none**; data = `Dados_tese_378.dta`. |
| Adolescent risky decision-making (hierarchical Bayesian mixture) | https://osf.io/4a38b/ | **license = none**. |
| Computational analysis of the CRT | https://osf.io/2vpha/ | **license = none**. |
| Human Choice Prediction (Shapira et al. 2025; language-based persuasion games, CPC2023-lineage) | https://github.com/eilamshapira/HumanChoicePrediction | Repo has code + `data/` but **no LICENSE file** (GitHub reports none). Request terms from authors. |
| Holter/CPC title collisions (OSF `dvkxp`, `u2ka3`, etc.) | — | Unrelated to choice-prediction competitions. |
| SOEP | — | Not openly licensed; requires a signed data-use agreement → out of scope. |
| "Basel" decision dataset | — | No openly licensed, de-identified JDM dataset identified under that name. **UNVERIFIED / not found.** |

---

## C. Ranked shortlist — 4 most usable

Ranked on (1) licence permissiveness, (2) direct downloadability, (3) JDM relevance to choice/confidence/RT simulation, (4) novelty headroom.

1. **CPC18 full raw data (Zenodo `2571510` + calibration `845873`) — CC-BY-4.0.**
   Direct 45–62 MB CSVs, documented variables including **choice, RT (subset), payoffs, ambiguity, correlation**, 510k+ consequential choices. Strongest benchmark-grade substrate for validating a stochastic choice simulation; combine with **CPC2015 (`321652`)** for a 330k-choice hold-out with higher novelty.

2. **The Confidence Database (OSF `s46pr`) — CC0.**
   The most permissive licence here (public-domain dedication), ~4M trials / 8,700+ participants / 360 files, trial-level **confidence + accuracy + task parameters (+ RT in many studies)**. Best for a large secondary analysis on judgement/confidence; novelty comes from the specific question, not the data.

3. **ITC Database (OSF `3wsae`) — CC-BY-NC-SA-4.0.**
   462 MB single CSV of **choice + response-time** data in intertemporal choice; newly released descriptor → **highest novelty headroom**. NC clause excludes commercial use only. Ideal for validating a simulation that predicts *both* choice and RT.

4. **CRT-V (OSF `xehbv`, Zenodo `22916374`) — CC-BY-4.0.** (tie with Many Labs 3, `ct89g`, CC-BY-4.0)
   8 studies with individual-difference measures (reflection, numeracy-adjacent, sociodemographics); clean, tiny, permissively licensed, and useful as a predictor/covariate for JDM simulation parameters and secondary individual-difference analyses.
   - *Alternative #4 if a large replication sample is preferred:* **Many Labs 3 (`ct89g`, CC-BY-4.0)**, though its core JDM relevance is weaker.

**Best single combination for the two stated goals:** use **CPC18 + CPC2015** to validate the simulation (choice/RT/risk/ambiguity/experience), and **Confidence Database** for the secondary JDM analysis (confidence/accuracy). Add **ITC Database** if intertemporal choice is in scope, or **CRT-V** if individual differences are.

---

## D. Verification ledger

- Licence + download links verified live via OSF API v2, Zenodo REST API, GitHub API on 2026-09-28.
- Confidence Database size (145 datasets / 8,700 participants / ~4M trials) verified from the published abstract (Europe PMC). Live node file count (360 files, ~255 MB) verified via OSF API.
- CPC18 variable dictionary verified by downloading and reading the Zenodo dictionary PDF.
- **UNVERIFIED / incomplete:** Mouselab-MDP raw data (not in the MIT repo); Lejarraga/Frey DFE raw-trial data location; adolescent ADHD dataset (`ca49h`) raw data; "Basel" and "Baby decision" datasets (no open, licensed, de-identified match found); Holt-Laury replication and "DOBBS" (no openly licensed, clearly named dataset located — searches returned unrelated records).
