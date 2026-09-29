"""Scratch feasibility: can we recover a per-cell ground truth for a direct
crowd-accuracy test, and how many datasets support a leave-one-judge-out
correctness-prediction test?

STRUCTURAL ONLY: this checks reconstructability and cell coverage. It does not
evaluate confidence weighting or report any effect size.
"""
import glob
import os
import re

import numpy as np
import pandas as pd

SRC = "/tmp/jdm4scratch/confall"


def norm(cols):
    return {re.sub(r"[^a-z0-9]", "", str(c).lower()): c for c in cols}


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
    except Exception:
        continue
    m = norm(df.columns)
    subj, stim = pick(m, "Subj_idx", "subj_idx"), pick(m, "Stimulus")
    resp, corr = pick(m, "Response"), pick(m, "Accuracy", "Correct")
    conf = pick(m, "Confidence")
    if not (subj and corr and resp and conf):
        continue
    r = pd.to_numeric(df[resp], errors="coerce")
    acc = pd.to_numeric(df[corr], errors="coerce")
    respv = r.dropna().unique()
    is_binary = set(np.round(respv, 6)).issubset({0.0, 1.0, -1.0, 2.0}) and len(respv) <= 2
    # reconstruct truth for binary responses: truth = resp if correct else flip
    truth_ok = None
    if is_binary and len(respv) == 2:
        lo, hi = min(respv), max(respv)
        truth = np.where(acc == 1, r, np.where(r == lo, hi, lo))
        tdf = df.assign(_t=truth)
        if stim:
            g = tdf.groupby(stim)["_t"].nunique()
            truth_ok = float((g <= 1).mean())
    cov = None
    if stim:
        c = df.groupby(stim)[subj].nunique()
        cov = float(c.median())
    rows.append(dict(file=name, n_subjects=df[subj].nunique(), n_stim=df[stim].nunique() if stim else None,
                     binary=is_binary, cell_truth_unique_frac=truth_ok, median_judges_per_stim=cov))

out = pd.DataFrame(rows)
out.to_csv("scoping/conf_direct_test_feasibility.csv", index=False)
print("datasets with Accuracy+Confidence+Response:", len(out))
print("binary response:", int(out["binary"].sum()))
ok = out[(out["binary"]) & (out["cell_truth_unique_frac"].fillna(0) >= 0.9)]
print("binary & >=90% cells with unique truth:", len(ok))
print(ok[["file", "n_subjects", "n_stim", "median_judges_per_stim"]].to_string())