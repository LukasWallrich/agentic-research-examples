"""Empirical component: confidence-weighted vs equal-weighted aggregation across
the Confidence Database, plus calibration and within-item error correlation.

Implements preregistration sections 3 and 6. Reads per-study CSVs from
data/confidence_database/ and writes:
  analysis/output/empirical_datasets.csv   one row per included dataset
  analysis/output/empirical_delta.csv      Delta(m) per dataset and group size
  analysis/output/moderation.json          H5 regression of mean Delta on beta, rho
  analysis/output/empirical_meta.json      random-effects meta-analysis of mean Delta
"""
import glob
import json
import os
import re

import numpy as np
import pandas as pd
from scipy import optimize

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "data", "confidence_database")
OUT = os.path.join(ROOT, "analysis", "output")
os.makedirs(OUT, exist_ok=True)

SEED = 20260928
R_DRAWS = 2000
M_LIST = [3, 5, 7, 9, 13, 17, 25, 40]
MAX_ITEMS = 64  # per draw, if a dataset has more items (computational bound; see deviations.md)

DESIGN_COLS = ["Contrast", "Coherence", "Difficulty", "SN", "SOA", "Orientation",
               "StimulusType", "Condition", "Task", "Category", "Temporal_distance", "Error"]


def norm_map(cols):
    return {re.sub(r"[^a-z0-9]", "", str(c).lower()): c for c in cols}


def pick(m, *names):
    for n in names:
        k = re.sub(r"[^a-z0-9]", "", n.lower())
        if k in m:
            return m[k]
    return None


def read_dataset(path):
    df = pd.read_csv(path, low_memory=False)
    m = norm_map(df.columns)
    subj = pick(m, "Subj_idx", "subj_idx", "subject")
    stim = pick(m, "Stimulus")
    resp = pick(m, "Response")
    conf = pick(m, "Confidence")
    corr = pick(m, "Accuracy", "Correct")
    if not (subj and stim and conf and corr and resp):
        return None
    # trial exclusion flags if present
    ex = pick(m, "trial_excl", "trial_excl_ind", "exclude")
    if ex is not None:
        df = df[~df[ex].astype(str).str.lower().isin({"true", "1", "yes"})]
    sub = pd.DataFrame({
        "subj": df[subj].astype(str),
        "stim": df[stim].astype(str),
        "conf": pd.to_numeric(df[conf], errors="coerce"),
        "acc": pd.to_numeric(df[corr], errors="coerce"),
    })
    # coerce string/boolean accuracy
    if df[corr].dtype == object:
        sub["acc"] = df[corr].astype(str).str.lower().map(
            {"true": 1.0, "false": 0.0, "1": 1.0, "0": 0.0, "yes": 1.0, "no": 0.0}).fillna(
            pd.to_numeric(df[corr], errors="coerce"))
    design_present = [c for c in DESIGN_COLS if c in df.columns]
    for c in design_present:
        sub[c] = df[c].astype(str).values
    sub = sub.dropna(subset=["conf", "acc"])
    sub = sub[sub["acc"].isin([0.0, 1.0])]
    if len(sub) == 0:
        return None
    sub["item"] = sub["stim"] + "|" + sub[design_present].agg("|".join, axis=1) if design_present else sub["stim"]
    return sub, design_present


def logistic_slope(x, y):
    """MLE slope of P(y=1) = sigmoid(b0 + b1 x)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.std() == 0:
        return np.nan

    def nll(p):
        z = p[0] + p[1] * x
        return np.sum(np.logaddexp(0, z) - y * z)

    r = optimize.minimize(nll, [0.0, 0.0], method="BFGS")
    return float(r.x[1])


def icc_item(sub):
    """One-way random-effects ICC of correctness grouped by item."""
    g = sub.groupby("item")["acc"]
    n = g.size().values.astype(float)
    if len(n) < 2:
        return np.nan
    means = g.mean().values
    N = n.sum()
    grand = sub["acc"].mean()
    ssb = np.sum(n * (means - grand) ** 2)
    ssw = np.sum((sub["acc"] - sub.groupby("item")["acc"].transform("mean")) ** 2)
    dfb = len(n) - 1
    dfw = N - len(n)
    if dfb <= 0 or dfw <= 0:
        return np.nan
    msb, msw = ssb / dfb, ssw / dfw
    k0 = (N - np.sum(n ** 2) / N) / dfb
    denom = msb + (k0 - 1) * msw
    return float((msb - msw) / denom) if denom > 0 else np.nan


def item_arrays(sub):
    """Per item: arrays of judge-level vote v and normalised confidence c."""
    conf = sub["conf"].values.astype(float)
    lo, hi = np.nanmin(conf), np.nanmax(conf)
    if not np.isfinite(lo) or not np.isfinite(hi) or hi <= lo:
        return None
    conf_n = (conf - lo) / (hi - lo)
    sub = sub.assign(v=2 * sub["acc"].values - 1, c=conf_n)
    items = []
    for _, g in sub.groupby("item"):
        j = g.groupby("subj").agg(v=("v", "mean"), c=("c", "mean")).values
        items.append((j[:, 0], j[:, 1]))
    return items


def delta_curves(items, m_list, rng):
    """Delta(m) = Acc_CW - Acc_EW via random group subsampling."""
    rows = []
    for m in m_list:
        eligible = [(v, c) for v, c in items if len(v) >= m]
        if not eligible:
            continue
        if len(eligible) > MAX_ITEMS:
            idx = rng.choice(len(eligible), MAX_ITEMS, replace=False)
            eligible = [eligible[i] for i in idx]
        ew_correct, cw_correct, total = 0.0, 0.0, 0
        for v, c in eligible:
            n = len(v)
            idx = rng.integers(0, n, size=(R_DRAWS, m))
            vs = v[idx]
            cs = c[idx] + 1e-9
            ew = vs.mean(axis=1)
            cw = (cs * vs).sum(axis=1) / cs.sum(axis=1)
            ew_correct += np.sum(ew > 0)
            cw_correct += np.sum(cw > 0)
            total += R_DRAWS
        rows.append(dict(m=m, n_items=len(eligible), acc_ew=ew_correct / total,
                         acc_cw=cw_correct / total, delta=cw_correct / total - ew_correct / total))
    return rows


def loo_brier(items):
    """Leave-one-judge-out Brier improvement of CW over EW.

    For each item and each target judge t, the crowd estimate from the other
    judges predicts t's correctness (1/0). Returns mean Brier(EW) - Brier(CW),
    so positive means confidence weighting predicts better.
    """
    b_ew, b_cw, n = 0.0, 0.0, 0
    for v, c in items:
        m = len(v)
        if m < 3:
            continue
        correct = (v + 1) / 2
        vsum, csum, cvsum = v.sum(), c.sum(), (c * v).sum()
        for t in range(m):
            ew = (vsum - v[t]) / (m - 1)
            denom = csum - c[t]
            cw = (cvsum - c[t] * v[t]) / denom if denom > 1e-12 else ew
            p_ew, p_cw = (1 + ew) / 2, (1 + cw) / 2
            b_ew += (p_ew - correct[t]) ** 2
            b_cw += (p_cw - correct[t]) ** 2
            n += 1
    return (b_ew - b_cw) / n if n else np.nan


def main():
    files = sorted(glob.glob(os.path.join(SRC, "*.csv")))
    ds_rows, delta_rows = [], []
    for f in files:
        name = os.path.basename(f)
        try:
            out = read_dataset(f)
        except Exception as e:
            ds_rows.append(dict(dataset=name, included=False, reason=f"parse_error:{str(e)[:60]}"))
            continue
        if out is None:
            ds_rows.append(dict(dataset=name, included=False, reason="missing_columns"))
            continue
        sub, design = out
        n_subj = sub["subj"].nunique()
        n_items = sub["item"].nunique()
        if n_subj < 8:
            ds_rows.append(dict(dataset=name, included=False, reason="lt8_subjects"))
            continue
        if sub["conf"].nunique() < 2:
            ds_rows.append(dict(dataset=name, included=False, reason="constant_confidence"))
            continue
        jpi = sub.groupby("item")["subj"].nunique()
        if (jpi >= 3).sum() < 2:
            ds_rows.append(dict(dataset=name, included=False, reason="lt2_items_ge3_judges"))
            continue
        items = item_arrays(sub)
        if items is None:
            ds_rows.append(dict(dataset=name, included=False, reason="confidence_scale_degenerate"))
            continue
        rng = np.random.default_rng(SEED + abs(hash(name)) % 100000)
        curves = delta_curves(items, M_LIST, rng)
        if not curves:
            ds_rows.append(dict(dataset=name, included=False, reason="no_eligible_groups"))
            continue
        conf_n = (sub["conf"] - sub["conf"].min()) / (sub["conf"].max() - sub["conf"].min())
        beta = logistic_slope(conf_n.values, sub["acc"].values)
        rho = icc_item(sub)
        for c in curves:
            delta_rows.append(dict(dataset=name, **c))
        mean_delta = float(np.mean([c["delta"] for c in curves]))
        dbrier = loo_brier(items)
        ds_rows.append(dict(dataset=name, included=True, n_subjects=n_subj, n_items=int(n_items),
                            n_trials=len(sub), n_design_cols=len(design),
                            mean_judges_per_item=float(jpi[jpi >= 3].mean()),
                            calibration_slope=beta, icc_rho=rho,
                            confidence_sd=float(conf_n.std()),
                            brier_improvement=dbrier,
                            mean_delta=mean_delta,
                            mean_delta_ge5=float(np.mean([c["delta"] for c in curves if c["m"] >= 5]))))
    pd.DataFrame(ds_rows).to_csv(os.path.join(OUT, "empirical_datasets.csv"), index=False)
    pd.DataFrame(delta_rows).to_csv(os.path.join(OUT, "empirical_delta.csv"), index=False)

    inc = pd.DataFrame([r for r in ds_rows if r.get("included")])
    print(f"included datasets: {len(inc)} of {len(files)}")
    if len(inc):
        meta = dict(n_datasets=len(inc))
        for key, label in [("mean_delta", "sign_accuracy"), ("brier_improvement", "loo_brier")]:
            d = inc[key].values.astype(float)
            d = d[np.isfinite(d)]
            bs = np.array([np.mean(np.random.default_rng(1000 + i).choice(d, len(d), replace=True))
                           for i in range(5000)])
            meta[label] = dict(mean=float(np.mean(d)),
                               ci95=[float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))],
                               frac_le0=float(np.mean(d <= 0)), frac_neg=float(np.mean(d < 0)))
        # H5 on the LOO-Brier improvement: Delta_brier ~ beta + rho
        meta["h5"] = {}
        for key in ("brier_improvement", "mean_delta"):
            X = inc[["calibration_slope", "icc_rho"]].values.astype(float)
            y = inc[key].values.astype(float)
            ok = np.isfinite(X).all(1) & np.isfinite(y)
            X, y = X[ok], y[ok]
            Xd = np.column_stack([np.ones(len(X)), X])
            coef, *_ = np.linalg.lstsq(Xd, y, rcond=None)
            resid = y - Xd @ coef
            n, k = Xd.shape
            XtXi = np.linalg.inv(Xd.T @ Xd)
            cov = XtXi @ (Xd.T @ (resid[:, None] ** 2 * Xd)) @ XtXi * n / (n - k)
            se_c = np.sqrt(np.diag(cov))
            meta["h5"][key] = dict(n=int(n), beta_coef=float(coef[1]), beta_se=float(se_c[1]),
                                   rho_coef=float(coef[2]), rho_se=float(se_c[2]))
        json.dump(meta, open(os.path.join(OUT, "empirical_meta.json"), "w"), indent=2)
        print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()