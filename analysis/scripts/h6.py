"""H6: does the calibrated simulation reproduce the sign of each dataset's
confidence-weighting effect?

Both the primary (preregistered) crowd-accuracy test and the secondary Brier test
are compared at the same group size on both sides (m = 7), against the trivial
"predict negative" baseline. Writes analysis/output/h6.json.
"""
import json
import os

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "analysis", "output")
KEYS = ["tau", "phi", "gamma", "omega"]
M = 7

emp = pd.read_csv(os.path.join(OUT, "empirical_datasets.csv"))
dl = pd.read_csv(os.path.join(OUT, "empirical_delta.csv"))
emp7 = dl[dl["m"] == M][["dataset", "delta"]].rename(columns={"delta": "delta_emp"})
emp = emp[emp["included"] == True].merge(emp7, on="dataset", how="inner")
emp = emp.dropna(subset=["calibration_slope", "icc_rho"]).reset_index(drop=True)
sim = pd.read_csv(os.path.join(OUT, "sim_cells.csv"))
simd = pd.read_csv(os.path.join(OUT, "sim_delta.csv"))
sim7 = simd[simd["m"] == M][KEYS + ["delta", "brier_improvement"]].merge(sim, on=KEYS)
sim7 = sim7.rename(columns={"delta": "delta_sim"})


def zfit(v, ref):
    return (v - np.nanmean(ref)) / (np.nanstd(ref) + 1e-12)


def map_indices(simdf):
    sz = np.column_stack([zfit(simdf["beta"], pd.concat([simdf["beta"], emp["calibration_slope"]])),
                          zfit(simdf["rho"], pd.concat([simdf["rho"], emp["icc_rho"]]))])
    ez = np.column_stack([zfit(emp["calibration_slope"], pd.concat([simdf["beta"], emp["calibration_slope"]])),
                          zfit(emp["icc_rho"], pd.concat([simdf["rho"], emp["icc_rho"]]))])
    return [int(np.argmin(((sz - e) ** 2).sum(1))) for e in ez]


res = {"criterion": "H6 (preregistered): sign agreement >= 0.60 on the crowd-accuracy gap at m = 7"}
idx = map_indices(sim7)
hits = sum(np.sign(sim7["delta_sim"].values[j]) == np.sign(emp["delta_emp"].values[i])
           for i, j in enumerate(idx))
res["sign_accuracy_m7"] = dict(n_agree=int(hits), n=int(len(emp)), agreement=float(hits / len(emp)),
                               baseline_predict_negative=float((emp["delta_emp"] < 0).mean()),
                               supported=bool(hits / len(emp) >= 0.6))
mask = emp["brier_improvement_m7"].notna().values
empb = emp[mask].reset_index(drop=True)
idxb = map_indices(sim7)
hits_b = sum(np.sign(sim7["brier_improvement"].values[j]) == np.sign(empb["brier_improvement_m7"].values[i])
             for i, j in enumerate(idxb))
res["loo_brier_m7"] = dict(n_agree=int(hits_b), n=int(len(empb)), agreement=float(hits_b / len(empb)),
                           baseline_predict_negative=float((empb["brier_improvement_m7"] < 0).mean()))
res["supported"] = res["sign_accuracy_m7"]["supported"]
res["mapping"] = dict(n_mapped_to_one_cell=int(pd.Series(idx).value_counts().iloc[0]),
                      n_below_min_sim_rho=int((emp["icc_rho"] < sim["rho"].min()).sum()))
json.dump(res, open(os.path.join(OUT, "h6.json"), "w"), indent=2)
print(json.dumps(res, indent=2))