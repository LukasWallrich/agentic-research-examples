"""Scratch feasibility check for the confidence-weighting study.

STRUCTURAL ONLY. This script counts items, judges per item, and detects which
correctness/response columns exist. It does NOT compute any aggregation outcome
(accuracy, confidence-weighted vs equal-weighted results) and does NOT use the
values of Accuracy/Correct/Confidence.

Inputs: confidence-database CSVs downloaded to /tmp/jdm4scratch/confall.
Output: scoping/conf_feasibility.csv
"""
import glob
import os
import re
import sys

import pandas as pd

SRC = "/tmp/jdm4scratch/confall"


def norm_cols(cols):
    m = {}
    for c in cols:
        k = re.sub(r"[^a-z0-9]", "", str(c).lower())
        m[k] = c
    return m


def pick(m, *names):
    for n in names:
        k = re.sub(r"[^a-z0-9]", "", n.lower())
        if k in m:
            return m[k]
    return None


rows = []
for f in sorted(glob.glob(os.path.join(SRC, "*.csv"))):
    name = os.path.basename(f)
    try:
        df = pd.read_csv(f, low_memory=False)
    except Exception as e:
        rows.append(dict(file=name, error=str(e)[:80]))
        continue
    m = norm_cols(df.columns)
    subj = pick(m, "Subj_idx", "subj_idx", "subject", "subjID")
    stim = pick(m, "Stimulus", "stimulus")
    resp = pick(m, "Response", "response")
    conf = pick(m, "Confidence", "confidence")
    corr = pick(m, "Accuracy", "Correct", "accuracy", "correct")
    n_sub = df[subj].nunique() if subj else None
    n_stim = df[stim].nunique() if stim else None
    # item x subject coverage (structural): distinct subjects per stimulus
    cover = None
    frac_ge2 = frac_ge3 = None
    if subj and stim:
        cov = df.groupby(stim)[subj].nunique()
        cover = float(cov.median())
        frac_ge2 = float((cov >= 2).mean())
        frac_ge3 = float((cov >= 3).mean())
    nresp = df[resp].nunique() if resp else None
    rows.append(dict(
        file=name, n_rows=len(df), n_subjects=n_sub, n_stimuli=n_stim,
        median_subj_per_stim=cover, frac_stim_ge2_subj=frac_ge2,
        frac_stim_ge3_subj=frac_ge3, has_correct=bool(corr),
        has_conf=bool(conf), n_response_levels=nresp,
        n_trials_per_subj=round(len(df) / n_sub, 1) if n_sub else None,
    ))

out = pd.DataFrame(rows)
out.to_csv("scoping/conf_feasibility.csv", index=False)
pd.set_option("display.width", 220)
print("datasets:", len(out))
print("with correctness column:", int(out["has_correct"].sum()))
elig = out[(out["has_correct"]) & (out["frac_stim_ge2_subj"].fillna(0) > 0.5) & (out["n_subjects"].fillna(0) >= 8)]
print("eligible (correct + >=50% stimuli with >=2 judges + >=8 subjects):", len(elig))
print(elig[["file", "n_subjects", "n_stimuli", "median_subj_per_stim", "frac_stim_ge2_subj", "n_response_levels"]].to_string())