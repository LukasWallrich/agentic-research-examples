"""H6: does the calibrated simulation reproduce the sign of each dataset's
confidence-weighting effect?

Primary, preregistered test: sign of the crowd-accuracy gap.
Secondary: sign of the leave-one-judge-out Brier improvement, compared at the
same group size on both sides (m = 7), with the trivial "predict negative for
all" baseline. Writes analysis/output/h6.json.
"""
import json
import os

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "analysis", "output")
KEYS = ["tau", "phi", "gamma", "omega"]

emp = pd.read_csv(os.path.join(OUT, "empirical_datasets.csv"))
emp = emp[emp["included"] == True].dropna(subset=["calibration_slope", "icc_rho"]).reset_index(drop=True)
sim = pd.read_csv(os.path.join(OUT, "sim_cells.csv"))
simd = pd.read_csv(os.path.join(OUT, "sim_delta.csv"))
sim7 = simd[simd["m"] == 7][KEYS + ["brier_improvement"]].merge(sim, on=KEYS)


def zfit(v, ref):
    return (v - np.nanmean(ref)) / (np.nanstd(ref) + 1e-12)


def map_indices(simdf):
    sz = np.column_stack([zfit(simdf["beta"], pd.concat([simdf["beta"], emp["calibration_slope"]])),
                          zfit(simdf["rho"], pd.concat([simdf["rho"], emp["icc_rho"]]))])
    ez = np.column_stack([zfit(emp["calibration_slope"], pd.concat([simdf["beta"], emp["calibration_slope"]])),
                          zfit(emp["icc_rho"], pd.concat([simdf["rho"], emp["icc_rho"]]))])
    return [int(np.argmin(((sz - e) ** 2).sum(1))) for e in ez]


res = {"criterion": "H6 (preregistered): sign agreement >= 0.60 on the crowd-accuracy gap"}
idx_acc = map_indices(sim)
hits = sum(np.sign(sim["mean_delta"].values[j]) == np.sign(emp["mean_delta"].values[i])
           for i, j in enumerate(idx_acc))
res["sign_accuracy"] = dict(n_agree=int(hits), n=int(len(emp)), agreement=float(hits / len(emp)),
                            supported=bool(hits / len(emp) >= 0.6))
mask7 = emp["brier_improvement_m7"].notna().values
emp7 = emp[mask7].reset_index(drop=True)
idx_b = map_indices(sim7)
hits_b = sum(np.sign(sim7["brier_improvement"].values[j]) == np.sign(emp7["brier_improvement_m7"].values[i])
             for i, j in enumerate(idx_b))
neg = int((emp7["brier_improvement_m7"] < 0).sum())
res["loo_brier_m7"] = dict(n_agree=int(hits_b), n=int(len(emp7)), agreement=float(hits_b / len(emp7)),
                           baseline_predict_negative=float(neg / len(emp7)),
                           note="simulated and empirical Brier compared at m = 7")
res["supported"] = res["sign_accuracy"]["supported"]
res["mapping"] = dict(n_mapped_to_one_cell=int(pd.Series(idx_acc).value_counts().iloc[0]),
                      n_below_min_sim_rho=int((emp["icc_rho"] < sim["rho"].min()).sum()))
json.dump(res, open(os.path.join(OUT, "h6.json"), "w"), indent=2)
print(json.dumps(res, indent=2))