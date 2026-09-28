"""H6: does the calibrated simulation reproduce the sign of each dataset's
confidence-weighting effect?

Each empirical dataset is mapped to the nearest simulation cell in standardised
(log calibration slope, error correlation) space; the cell's predicted sign is
compared with the dataset's observed sign for both the LOO-Brier improvement and
the sign-accuracy delta. Writes analysis/output/h6.json.
"""
import json
import os

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "analysis", "output")

emp = pd.read_csv(os.path.join(OUT, "empirical_datasets.csv"))
emp = emp[emp["included"] == True].dropna(subset=["calibration_slope", "icc_rho"])
sim = pd.read_csv(os.path.join(OUT, "sim_cells.csv"))


def zfit(v, ref):
    return (v - np.nanmean(ref)) / (np.nanstd(ref) + 1e-12)


features = [("beta", "calibration_slope"), ("rho", "icc_rho")]
sim_z = np.column_stack([zfit(sim[sf], pd.concat([sim[sf], emp[ef]])) for sf, ef in features])
emp_z = np.column_stack([zfit(emp[ef], pd.concat([sim[sf], emp[ef]])) for sf, ef in features])


def agree(pred_col, obs_col, tol=0.0):
    hits = 0
    for i, ez in enumerate(emp_z):
        j = int(np.argmin(((sim_z - ez) ** 2).sum(1)))
        pred = sim[pred_col].values[j]
        obs = emp[obs_col].values[i]
        if np.isfinite(obs) and np.sign(pred) == np.sign(obs):
            hits += 1
    return hits, len(emp_z)


res = {}
for pred_col, obs_col, name in [("mean_brier", "brier_improvement", "loo_brier"),
                                ("mean_delta", "mean_delta", "sign_accuracy")]:
    h, n = agree(pred_col, obs_col)
    res[name] = dict(sign_agreement=h / n, n_agree=h, n=n, supported=bool(h / n >= 0.6))

res["criterion"] = "H6 supported if sign agreement >= 0.60 for at least one measure"
res["supported"] = res["loo_brier"]["supported"] or res["sign_accuracy"]["supported"]
json.dump(res, open(os.path.join(OUT, "h6.json"), "w"), indent=2)
print(json.dumps(res, indent=2))