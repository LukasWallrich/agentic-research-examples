"""Empirical component: confidence-weighted vs equal-weighted aggregation across
the Confidence Database, plus calibration and within-item error correlation.

Implements preregistration sections 3 and 6. Reads per-study CSVs from
data/confidence_database/ and writes:
  analysis/output/empirical_datasets.csv   one row per included dataset
  analysis/output/empirical_delta.csv      Delta(m) per dataset and group size
  analysis/output/empirical_meta.json      unweighted mean and bootstrap CI (see deviations)
"""
import glob
import json
import os
import re
import zlib

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
MAX_ITEMS = 64  # sampled items per group size when a dataset has more (see deviations.md)

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


def stable_seed(name):
    return SEED + zlib.crc32(name.encode("utf-8")) % 100000


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
    ex = pick(m, "trial_excl", "trial_excl_ind")
    if ex is not None:
        df = df[~df[ex].astype(str).str.lower().isin({"true", "1", "yes"})]
    sub = pd.DataFrame({
        "subj": df[subj].astype(str),
        "stim": df[stim].astype(str),
        "conf": pd.to_numeric(df[conf], errors="coerce"),
        "acc": pd.to_numeric(df[corr], errors="coerce"),
    })
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
    cols_for_item = ["stim"] + design_present
    key = sub[cols_for_item].astype("string").fillna("NA")
    sub["item"] = key.agg("|".join, axis=1)
    return sub, design_present


def logistic_slope(x, y, l2=0.05):
    """Ridge-penalised logistic slope via IRLS (robust to separation)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.std() == 0:
        return np.nan, False
    x = (x - x.mean()) / x.std()
    X = np.column_stack([np.ones_like(x), x])
    w = np.zeros(2)
    ok = False
    for _ in range(100):
        p = 1.0 / (1.0 + np.exp(-(X @ w)))
        W = np.clip(p * (1 - p), 1e-9, None)
        z = X @ w + (y - p) / W
        A = X.T @ (X * W[:, None]) + np.diag([1e-9, l2])
        b = X.T @ (W * z)
        w_new = np.linalg.solve(A, b)
        if np.max(np.abs(w_new - w)) < 1e-9:
            w, ok = w_new, True
            break
        w = w_new
    return float(w[1]), ok


def icc_item(ji):
    """One-way random-effects ICC on the judge-item correctness table."""
    g = ji.groupby("item")["acc"]
    n = g.size().values.astype(float)
    if len(n) < 2:
        return np.nan
    means = g.mean().values
    N = n.sum()
    grand = ji["acc"].mean()
    ssb = np.sum(n * (means - grand) ** 2)
    ssw = np.sum((ji["acc"] - ji.groupby("item")["acc"].transform("mean")) ** 2)
    dfb, dfw = len(n) - 1, N - len(n)
    if dfb <= 0 or dfw <= 0:
        return np.nan
    msb, msw = ssb / dfb, ssw / dfw
    k0 = (N - np.sum(n ** 2) / N) / dfb
    denom = msb + (k0 - 1) * msw
    return float((msb - msw) / denom) if denom > 0 else np.nan


def judge_item_table(sub):
    """Judge-level vote and confidence per item, plus min-max normalised confidence."""
    conf = sub["conf"].values.astype(float)
    lo, hi = np.nanmin(conf), np.nanmax(conf)
    if not np.isfinite(lo) or not np.isfinite(hi) or hi <= lo:
        return None
    ji = (sub.assign(v=2 * sub["acc"].values - 1, c=(conf - lo) / (hi - lo))
          .groupby(["item", "subj"], as_index=False)
          .agg(v=("v", "mean"), c=("c", "mean"), acc=("acc", "mean")))
    return ji


def draw_idx(rng, n, m, R):
    """R groups of m distinct judges (sampling without replacement)."""
    return np.argsort(rng.random((R, n)), axis=1)[:, :m]


def loo_brier(items):
    """Leave-one-judge-out Brier improvement of CW over EW (positive = CW better)."""
    b_ew = b_cw = n = 0
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
            b_ew += (((1 + ew) / 2) - correct[t]) ** 2
            b_cw += (((1 + cw) / 2) - correct[t]) ** 2
            n += 1
    return (b_ew - b_cw) / n if n else np.nan


def delta_curves(items, m_list, rng):
    rows = []
    for m in m_list:
        eligible = [(v, c) for v, c in items if len(v) >= m]
        if not eligible:
            continue
        if len(eligible) > MAX_ITEMS:
            idx = rng.choice(len(eligible), MAX_ITEMS, replace=False)
            eligible = [eligible[i] for i in idx]
        ew_correct = cw_correct = total = 0
        for v, c in eligible:
            idx = draw_idx(rng, len(v), m, R_DRAWS)
            vs = v[idx]
            cs = c[idx] + 1e-9
            ew = vs.mean(axis=1)
            cw = (cs * vs).sum(axis=1) / cs.sum(axis=1)
            ew_correct += int(np.sum(ew > 0))
            cw_correct += int(np.sum(cw > 0))
            total += R_DRAWS
        rows.append(dict(m=m, n_items=len(eligible), acc_ew=ew_correct / total,
                         acc_cw=cw_correct / total, delta=cw_correct / total - ew_correct / total))
    return rows


def loo_brier_m(items, m, rng, R=1000):
    """Leave-one-judge-out Brier improvement at a fixed group size m (subsampled)."""
    elig = [(v, c) for v, c in items if len(v) >= m]
    if not elig:
        return np.nan
    b_ew = b_cw = n = 0.0
    for v, c in elig:
        idx = draw_idx(rng, len(v), m, R)
        vs, cs = v[idx], c[idx]
        corr = (vs + 1) / 2
        vsum, csum, cvsum = vs.sum(1), cs.sum(1), (cs * vs).sum(1)
        for t in range(m):
            ew = (vsum - vs[:, t]) / (m - 1)
            denom = csum - cs[:, t]
            cw = np.where(denom > 1e-12, (cvsum - cs[:, t] * vs[:, t]) / denom, ew)
            b_ew += float(np.sum((((1 + ew) / 2) - corr[:, t]) ** 2))
            b_cw += float(np.sum((((1 + cw) / 2) - corr[:, t]) ** 2))
            n += R
    return (b_ew - b_cw) / n if n else np.nan


def calibration_decomposition(sub):
    """Within-item and between-judge linear-probability calibration slopes.

    The theory needs the within-item covariance of confidence with correctness;
    a pooled slope mixes it with the between-judge association.
    """
    t = pd.DataFrame({
        "item": sub["item"].values,
        "subj": sub["subj"].values,
        "c": sub["conf"].values.astype(float),
        "a": sub["acc"].values.astype(float),
    })
    c = (t["c"] - t["c"].min()) / (t["c"].max() - t["c"].min() + 1e-12)
    t["c"] = c
    # within-item: demean by item, then LPM slope
    t["cd"] = t["c"] - t.groupby("item")["c"].transform("mean")
    t["ad"] = t["a"] - t.groupby("item")["a"].transform("mean")
    v = t["cd"].var()
    beta_within = float(t["cd"].cov(t["ad"]) / v) if v > 1e-12 else np.nan
    # between-judge: subject means, then LPM slope
    sj = t.groupby("subj").agg(c=("c", "mean"), a=("a", "mean"))
    vv = sj["c"].var()
    beta_between = float(sj["c"].cov(sj["a"]) / vv) if vv > 1e-12 else np.nan
    return beta_within, beta_between


def contested_delta(items, m_list, rng):
    """Sign-accuracy gap restricted to items on which the crowd is not decided."""
    rows = []
    contested = [(v, c) for v, c in items if abs(v.mean()) < 0.5]
    if len(contested) < 2:
        return rows
    for m in m_list:
        elig = [(v, c) for v, c in contested if len(v) >= m]
        if not elig:
            continue
        ew_c = cw_c = tot = 0
        for v, c in elig:
            idx = draw_idx(rng, len(v), m, R_DRAWS)
            vs, cs = v[idx], c[idx] + 1e-9
            ew = vs.mean(1)
            cw = (cs * vs).sum(1) / cs.sum(1)
            ew_c += int(np.sum(ew > 0)) + 0.5 * int(np.sum(np.abs(ew) < 1e-12))
            cw_c += int(np.sum(cw > 0)) + 0.5 * int(np.sum(np.abs(cw) < 1e-12))
            tot += R_DRAWS
        rows.append(dict(m=m, n_items=len(elig), acc_ew=ew_c / tot, acc_cw=cw_c / tot,
                         delta=cw_c / tot - ew_c / tot))
    return rows


def lambda_test(items, rng, lam=0.5, R=300):
    """Held-out test of estimating the shrinkage lambda on a train half of items.

    Returns mean held-out accuracy for the estimated-lambda rule, EW, and CW.
    """
    grid = np.round(np.arange(0, 1.0001, 0.05), 3)
    arr_v = [v.mean() for v, _ in items]
    arr_cw = [np.sum(c * v) / np.sum(c) if np.sum(c) > 0 else v.mean() for v, c in items]
    n = len(items)
    if n < 4:
        return dict(acc_lambda=np.nan, acc_ew=np.nan, acc_cw=np.nan)
    acc_l = acc_e = acc_c = cnt = 0.0
    for _ in range(R):
        perm = rng.permutation(n)
        tr, te = perm[: n // 2], perm[n // 2:]
        lam_tr = 0.0
        best = -1
        for L in grid:
            acc = np.mean([(1 - L) * arr_v[i] + L * arr_cw[i] > 0 for i in tr])
            if acc > best + 1e-12:
                best, lam_tr = acc, L
        for i in te:
            acc_l += (1 - lam_tr) * arr_v[i] + lam_tr * arr_cw[i] > 0
            acc_e += arr_v[i] > 0
            acc_c += arr_cw[i] > 0
        cnt += len(te)
    return dict(acc_lambda=acc_l / cnt, acc_ew=acc_e / cnt, acc_cw=acc_c / cnt)


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
        n_subj, n_items = sub["subj"].nunique(), sub["item"].nunique()
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
        ji = judge_item_table(sub)
        if ji is None:
            ds_rows.append(dict(dataset=name, included=False, reason="confidence_scale_degenerate"))
            continue
        items = [(g["v"].values, g["c"].values) for _, g in ji.groupby("item")]
        m_max = int(np.floor(np.median(jpi.values)))
        m_list = [m for m in M_LIST if m <= m_max]
        if not m_list:
            m_list = [int(m_max)] if m_max >= 3 else []
        rng = np.random.default_rng(stable_seed(name))
        curves = delta_curves(items, m_list, rng)
        if not curves:
            ds_rows.append(dict(dataset=name, included=False, reason="no_eligible_groups"))
            continue
        brier_m7 = loo_brier_m(items, 7, np.random.default_rng(stable_seed(name) + 7)) \
            if any(len(v) >= 7 for v, _ in items) else np.nan
        conf_n = (sub["conf"] - sub["conf"].min()) / (sub["conf"].max() - sub["conf"].min())
        beta, conv = logistic_slope(conf_n.values, sub["acc"].values)
        rho = icc_item(ji)
        # robustness: clip confidence to 5th-95th percentile, renormalise
        lo, hi = np.percentile(conf_n.values, [5, 95])
        ji2 = ji.assign(c=np.clip(ji["c"], (lo - conf_n.min()) / (conf_n.max() - conf_n.min()),
                                  (hi - conf_n.min()) / (conf_n.max() - conf_n.min())))
        vals = ji2["c"].values
        ji2["c"] = (vals - vals.min()) / (vals.max() - vals.min() + 1e-12)
        items2 = [(g["v"].values, g["c"].values) for _, g in ji2.groupby("item")]
        beta_within, beta_between = calibration_decomposition(sub)
        cont = contested_delta(items, m_list, rng)
        lam = lambda_test(items, np.random.default_rng(stable_seed(name) + 11))
        for c in curves:
            delta_rows.append(dict(dataset=name, **c))
        ds_rows.append(dict(dataset=name, included=True, n_subjects=n_subj, n_items=int(n_items),
                            n_trials=len(sub), n_design_cols=len(design),
                            mean_judges_per_item=float(jpi[jpi >= 3].mean()),
                            logit_converged=conv,
                            calibration_slope=beta, beta_within=beta_within,
                            beta_between=beta_between, icc_rho=rho,
                            contested_mean_delta=float(np.mean([c["delta"] for c in cont]))
                            if cont else np.nan,
                            acc_lambda=lam["acc_lambda"], acc_ew_lambda=lam["acc_ew"],
                            acc_cw_lambda=lam["acc_cw"],
                            confidence_sd=float(conf_n.std()),
                            brier_improvement=loo_brier(items),
                            brier_improvement_clipped=loo_brier(items2),
                            brier_improvement_m7=brier_m7,
                            m_max=m_max,
                            mean_delta=float(np.mean([c["delta"] for c in curves]))))
    pd.DataFrame(ds_rows).to_csv(os.path.join(OUT, "empirical_datasets.csv"), index=False)
    pd.DataFrame(delta_rows).to_csv(os.path.join(OUT, "empirical_delta.csv"), index=False)

    inc = pd.DataFrame([r for r in ds_rows if r.get("included")])
    print(f"included datasets: {len(inc)} of {len(files)}")
    if len(inc):
        meta = dict(n_datasets=len(inc),
                    note="unweighted mean across datasets with a dataset bootstrap CI; "
                         "not a random-effects meta-analysis (see deviations.md)")
        for key in ("mean_delta", "brier_improvement"):
            d = inc[key].values.astype(float)
            d = d[np.isfinite(d)]
            bs = np.array([np.mean(np.random.default_rng(1000 + i).choice(d, len(d), replace=True))
                           for i in range(5000)])
            meta[key] = dict(mean=float(np.mean(d)),
                             ci95=[float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))],
                             frac_le0=float(np.mean(d <= 0)), frac_neg=float(np.mean(d < 0)))
        for key in ("brier_improvement", "brier_improvement_clipped"):
            d = inc[key].dropna().values.astype(float)
            meta[key + "_mean"] = float(np.mean(d)) if len(d) else None
            meta[key + "_frac_neg"] = float(np.mean(d < 0)) if len(d) else None
        meta["logit_nonconverged"] = int((~inc["logit_converged"]).sum())
        meta["h5"] = {}

        def fit_h5(predictors, key):
            X = inc[predictors].values.astype(float)
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
            out = dict(n=int(n), coefs=[float(x) for x in coef[1:]], ses=[float(x) for x in se_c[1:]])
            out["mde80"] = [float(2.802 * s) for s in se_c[1:]]
            return out

        for key in ("brier_improvement", "mean_delta"):
            meta["h5"][key] = fit_h5(["calibration_slope", "icc_rho"], key)
            meta["h5"][key + "_within"] = fit_h5(["beta_within", "icc_rho"], key)
        # contested-item and shrinkage summaries
        cd = inc["contested_mean_delta"].dropna().values.astype(float)
        meta["contested_items"] = dict(n=int(len(cd)), mean=float(np.mean(cd)) if len(cd) else None)
        lam = inc[["acc_lambda", "acc_ew_lambda", "acc_cw_lambda"]].dropna()
        meta["shrinkage_holdout"] = dict(
            n=int(len(lam)),
            acc_estimated_lambda=float(lam["acc_lambda"].mean()) if len(lam) else None,
            acc_ew=float(lam["acc_ew_lambda"].mean()) if len(lam) else None,
            acc_cw=float(lam["acc_cw_lambda"].mean()) if len(lam) else None,
            frac_lambda_beats_ew=float((lam["acc_lambda"] > lam["acc_ew_lambda"]).mean()) if len(lam) else None)
        json.dump(meta, open(os.path.join(OUT, "empirical_meta.json"), "w"), indent=2)
        print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()