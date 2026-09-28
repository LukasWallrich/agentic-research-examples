"""Simulation component: finite-sample boundary for confidence-weighted vs
equal-weighted aggregation (preregistration sections 4-5).

Generative model
----------------
For item i and judge j:
  delta_i ~ N(0,1)              item position; truth T_i = sign(delta_i)
  u_i     ~ N(0, tau^2)         shared within-item error
  a_j     ~ N(0, sigma_a^2)     judge ability (persistent)
  o_j     ~ N(0, 1)             judge overconfidence (persistent, independent of a)
  eps_ij  ~ N(0, sigma_eps^2)   trial-private noise
  s_ij    = delta_i + u_i + a_j + eps_ij
  correct_ij = 1[sign(s_ij) == T_i];  v_ij = 2*correct_ij - 1
  c_ij    = sigmoid(gamma * (T_i * s_ij) + phi * o_j) + N(0, omega^2), min-max normalised

phi is the overconfidence term: it raises confidence independently of accuracy,
which injects within-item noise into CW weights; tau is the shared-error term
that lowers the ceiling. Writes analysis/output/sim_cells.csv, sim_delta.csv,
sim_summary.json.

Deviation from prereg: the prereg's kappa (item-level shared shift) cannot
produce within-item miscalibration, so judge-level overconfidence phi replaces
it. Recorded in deviations.md.
"""
import json
import os

import numpy as np
import pandas as pd
from scipy import optimize

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "analysis", "output")
os.makedirs(OUT, exist_ok=True)

SEED = 20260928
N_ITEMS = 40000
MMAX = 65
M_LIST = [3, 5, 7, 9, 13, 17, 25, 41, 65]
LAM = np.round(np.arange(0, 1.0001, 0.05), 3)
SIGMA_A, SIGMA_EPS, OMEGA = 0.7, 1.0, 0.05
TAUS = [0.0, 0.3, 0.6, 1.0]
PHIS = [0.0, 1.0, 2.0, 4.0]
GAMMAS = [0.3, 0.6, 1.0]


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def logistic_slope(x, y):
    def nll(p):
        z = p[0] + p[1] * x
        return np.sum(np.logaddexp(0, z) - y * z)
    r = optimize.minimize(nll, [0.0, 1.0], method="BFGS")
    return float(r.x[1])


def icc_item(item_ids, correct):
    df = pd.DataFrame({"item": item_ids, "acc": correct})
    g = df.groupby("item")["acc"]
    n = g.size().values.astype(float)
    means = g.mean().values
    N = n.sum()
    grand = df["acc"].mean()
    ssb = np.sum(n * (means - grand) ** 2)
    ssw = np.sum((df["acc"] - df.groupby("item")["acc"].transform("mean")) ** 2)
    dfb, dfw = len(n) - 1, N - len(n)
    msb, msw = ssb / dfb, ssw / dfw
    k0 = (N - np.sum(n ** 2) / N) / dfb
    denom = msb + (k0 - 1) * msw
    return float((msb - msw) / denom) if denom > 0 else np.nan


def run_cell(tau, phi, gamma, seed):
    rng = np.random.default_rng(seed)
    delta = rng.normal(0, 1, N_ITEMS)
    truth = np.where(delta >= 0, 1.0, -1.0)
    u = rng.normal(0, tau, N_ITEMS)
    a = rng.normal(0, SIGMA_A, (N_ITEMS, MMAX))
    o = rng.normal(0, 1, (N_ITEMS, MMAX))
    s = delta[:, None] + u[:, None] + a + rng.normal(0, SIGMA_EPS, (N_ITEMS, MMAX))
    correct = (np.sign(s) == truth[:, None]).astype(float)
    v = 2 * correct - 1
    c = sigmoid(gamma * (truth[:, None] * s) + phi * o) + rng.normal(0, OMEGA, (N_ITEMS, MMAX))
    c = np.clip(c, 0.001, None)
    c = (c - c.min()) / (c.max() - c.min())
    c = c + 1e-6

    rows = []
    beta = logistic_slope(c[:, :10].ravel(), correct[:, :10].ravel())
    rho = icc_item(np.repeat(np.arange(N_ITEMS), 5), correct[:, :5].ravel())
    for m in M_LIST:
        vm, cm, corrm = v[:, :m], c[:, :m], correct[:, :m]
        ew = vm.mean(1)
        cw = (cm * vm).sum(1) / cm.sum(1)
        acc_ew = float(np.mean(ew > 0))
        acc_cw = float(np.mean(cw > 0))
        accs = [float(np.mean(((1 - lam) * ew + lam * cw) > 0)) for lam in LAM]
        lam_star = float(LAM[int(np.argmax(accs))])
        # leave-one-judge-out Brier improvement of CW over EW
        vsum, csum, cvsum = vm.sum(1), cm.sum(1), (cm * vm).sum(1)
        b_ew = b_cw = 0.0
        for t in range(m):
            denom = csum - cm[:, t]
            cw_loo = np.where(denom > 1e-9, (cvsum - cm[:, t] * vm[:, t]) / denom, ew)
            b_ew += np.mean(((1 + (vsum - vm[:, t]) / (m - 1)) / 2 - corrm[:, t]) ** 2)
            b_cw += np.mean(((1 + cw_loo) / 2 - corrm[:, t]) ** 2)
        brier_improvement = (b_ew - b_cw) / m
        rows.append(dict(m=m, acc_ew=acc_ew, acc_cw=acc_cw, delta=acc_cw - acc_ew,
                         brier_improvement=float(brier_improvement),
                         lam_star=lam_star, acc_lam_star=float(np.max(accs))))
    return rows, dict(beta=beta, rho=rho)


def main():
    cells, deltas = [], []
    seed = SEED
    for tau in TAUS:
        for phi in PHIS:
            for gamma in GAMMAS:
                seed += 1
                rows, ps = run_cell(tau, phi, gamma, seed)
                cell_mean = float(np.mean([r["delta"] for r in rows]))
                for r in rows:
                    deltas.append(dict(tau=tau, phi=phi, gamma=gamma, **r))
                cells.append(dict(tau=tau, phi=phi, gamma=gamma, beta=ps["beta"], rho=ps["rho"],
                                  mean_delta=cell_mean,
                                  min_delta=float(np.min([r["delta"] for r in rows])),
                                  mean_brier=float(np.mean([r["brier_improvement"] for r in rows])),
                                  min_brier=float(np.min([r["brier_improvement"] for r in rows])),
                                  any_negative=any(r["delta"] < 0 for r in rows)))
    pd.DataFrame(cells).to_csv(os.path.join(OUT, "sim_cells.csv"), index=False)
    pd.DataFrame(deltas).to_csv(os.path.join(OUT, "sim_delta.csv"), index=False)

    cd = pd.DataFrame(cells)
    dt = pd.DataFrame(deltas).sort_values(["tau", "phi", "gamma", "m"])

    def monotonic_violations(col, tol):
        v = 0
        for _, g in dt.groupby(["tau", "phi", "gamma"]):
            d = g[col].values
            v += int((np.diff(d) < -tol).sum())
        return v

    summary = dict(
        n_cells=len(cd),
        any_negative_cell_sign=int(cd["any_negative"].sum()),
        frac_negative_cells_sign=float(cd["any_negative"].mean()),
        any_negative_cell_brier=int((cd["min_brier"] < 0).sum()),
        frac_negative_cells_brier=float((cd["min_brier"] < 0).mean()),
        h2_sign_violations=monotonic_violations("delta", 0.002),
        h2_brier_violations=monotonic_violations("brier_improvement", 0.002),
        h2_total_steps=int(len(dt) - len(cd)),
        h3_cells_with_interior_lambda=int(
            dt[(dt["lam_star"] > 0.001) & (dt["lam_star"] < 0.999)]
            .groupby(["tau", "phi", "gamma"]).size().gt(0).sum()),
    )
    json.dump(summary, open(os.path.join(OUT, "sim_summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))
    print("\nCell mean delta (sign), gamma=0.3:")
    print(cd[cd.gamma == 0.3].pivot(index="tau", columns="phi", values="mean_delta").round(4))
    print("\nCell min brier improvement, gamma=0.3:")
    print(cd[cd.gamma == 0.3].pivot(index="tau", columns="phi", values="min_brier").round(5))


if __name__ == "__main__":
    main()