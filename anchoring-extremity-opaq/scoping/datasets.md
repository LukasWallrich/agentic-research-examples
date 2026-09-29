# Scoping: openly licensed JDM datasets

Produced by a scoping subagent on 2026-09-27. No data files were opened; only repository metadata, licence fields, papers, READMEs and codebooks were read. Citation counts are OpenAlex `cited_by_count` of the source paper on 2026-09-27.

## Candidates with an explicit open licence

| # | Dataset | Source paper | Repository | Licence (where seen) | N / structure | Reuse |
|---|---|---|---|---|---|---|
| 1 | Good Judgment Project | Mellers et al. 2014, Psych Sci, 10.1177/0956797614524255 | doi:10.7910/DVN/BPCDH5 | CC0 1.0 (Dataverse API) | Forecast-level data, 4 years, thousands of forecasters, conditions, cognitive battery | High (329 cites) |
| 2 | CPC18 raw data | Erev et al. 2017, Psych Rev, 10.1037/rev0000062 | zenodo.org/records/2571510 | cc-by-4.0 (Zenodo API) | 694,500 trial-level choices, 210 problems, 30 games x 25 trials per person | Very high at problem level |
| 3 | Open Anchoring Quest (OpAQ) | Röseler et al. 2022, JOPD, 10.5334/jopd.67 | osf.io/ygnvb | CC-By Attribution 4.0 International (OSF API) | v2022: 21,359 participants, 96 studies, 412 items, 88,914 estimates | Low (4 cites) |
| 4 | Winton Centre Numeracy Dataset | none yet (Zenodo, Kerr et al., 11 Sep 2026) | doi:10.5281/zenodo.22699877 | cc-by-4.0 (Zenodo API) | N = 75,688, 59 surveys, 14 countries, item-level BNT, Schwartz numeracy, CRT, AOT | None |
| 5 | Confidence Database | Rahnev et al. 2020, NHB, 10.1038/s41562-019-0813-1 | osf.io/s46pr | CC0 1.0 Universal (OSF API) | 180 trial-level datasets | Moderate-high |
| 6 | Basel-Berlin Risk Study | Frey et al. 2017, Sci Adv, 10.1126/sciadv.1701381 | osf.io/rce7g | CC-BY 4.0 (OSF API) | N = 1,507, 39 risk measures | High; possible DOB fields |
| 7 | PSACR-001 framing | Dorison et al. 2022, Affective Science, 10.1007/s42761-022-00128-3 | osf.io/gvw56 | CC-BY 4.0 (OSF API) | N = 15,929, 84 countries | Low |
| 8 | Description-experience gap data | Wulff et al. 2018, Psych Bull, 10.1037/bul0000115 | zenodo.org/records/1491449 | cc-by-sa-4.0 | Choice-level data, 28 publications | Moderate-high |
| 9 | Many Labs 2 | Klein et al. 2018, AMPPS, 10.1177/2515245918810225 | osf.io/8cd4r | CC0 1.0 | ~15,000 participants, 125 samples | Very high |
| 10 | Many Labs 1 | Klein et al. 2014, Soc Psych, 10.1027/1864-9335/a000178 | osf.io/wx7ck | CC0 1.0 | ~6,344, 36 samples | Very high |
| 11 | Adaptive social networks | Almaatouq et al. 2020, PNAS, 10.1073/pnas.1917687117 | doi:10.7910/DVN/EOYZKH | CC0 1.0 | Networked estimates | Moderate |
| 12 | Wisdom of partisan crowds | Becker et al. 2019, PNAS, 10.1073/pnas.1817195116 | doi:10.7910/DVN/OE6UMR | CC0 1.0 | Estimates before/after exposure | Moderate |
| 13 | Psych-101 | Binz et al. 2025, Nature, 10.1038/s41586-025-09215-4 | huggingface.co/datasets/marcelbinz/Psych-101 | apache-2.0 (re-licenses third-party data) | 160 experiments as text | Rising |
| 14 | IGT many-labs pool | Steingroever et al. 2015, JOPD, 10.5334/jopd.ak | osf.io/8t7rm | CC BY-SA 4.0 in article only | N = 617 | Moderate |
| 15 | Kao et al. wisdom of crowds | Kao et al. 2018, JRSI, 10.1098/rsif.2018.0130 | figshare c.4064342 | CC BY 4.0 | N = 812 | Small |
| 16 | Climate megastudy | Vlasceanu et al. 2024, Sci Adv, 10.1126/sciadv.adj5778 | zenodo.org/records/10345806 | cc-by-4.0 | N = 59,440 | Weak JDM fit |

## Excluded (no open licence on the data record)

Ruggeri et al. 2020 prospect theory (osf.io/esxc4); Ruggeri et al. 2022 temporal discounting (osf.io/njd62); choices13k (GitHub, no licence; aggregates only); Becker et al. 2017 (PNAS supplement, no licence); repliCATS (no licence); van Dolder & van den Assem 2018 (proprietary).

## OpAQ variable list (from the JOPD data paper, not from the data file)

participant_id, sex, age, anchoring_item, true_value, anchor, anchorhigh, anchortype, comparative_question, estimate, incentive, preregistered, sampletype, scaletype, stimulitype, tasktype, adjustment, score.

## CPC18 variable list (from the dictionary PDF)

SubjID, Location, Gender, Age, problem parameters (Ha, pHa, La, LotShape, LotNum, Amb, Corr, ...), Order, Trial, Block, B (choice), Payoff, Forgone, RT (sets 6-7), Feedback.
