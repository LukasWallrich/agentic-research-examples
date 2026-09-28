"""Collate every number used in the manuscript from the analysis outputs.

Writes analysis/output/manuscript_numbers.json and manuscript/numbers.md.
"""
import json
import os

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "analysis", "output")
MAN = os.path.join(ROOT, "manuscript")
os.makedirs(MAN, exist_ok=True)

emp = pd.read_csv(os.path.join(OUT, "empirical_datasets.csv"))
inc = emp[emp["included"] == True]
dl = pd.read_csv(os.path.join(OUT, "empirical_delta.csv"))
sim = pd.read_csv(os.path.join(OUT, "sim_cells.csv"))
meta = json.load(open(os.path.join(OUT, "empirical_meta.json")))
h6 = json.load(open(os.path.join(OUT, "h6.json")))
ss = json.load(open(os.path.join(OUT, "sim_summary.json")))

g = dl.groupby("m")
n = {
    "n_datasets_examined": int(len(emp)),
    "n_datasets_included": int(len(inc)),
    "n_trials_analysed": int(inc["n_trials"].sum()),
    "median_calibration_slope": float(inc["calibration_slope"].median()),
    "median_icc_rho": float(inc["icc_rho"].median()),
    "median_judges_per_item": float(inc["mean_judges_per_item"].median()),
    "acc_ew_m3": float(g["acc_ew"].mean().loc[3]),
    "acc_ew_m40": float(g["acc_ew"].mean().loc[40]),
    "sign_delta": meta["mean_delta"],
    "loo_brier": meta["brier_improvement"],
    "loo_brier_clipped": dict(mean=meta["brier_improvement_clipped_mean"],
                              frac_neg=meta["brier_improvement_clipped_frac_neg"]),
    "loo_brier_m7": dict(median=float(inc["brier_improvement_m7"].median()),
                         frac_neg=float((inc["brier_improvement_m7"] < 0).mean())),
    "h5_loo_brier": meta["h5"]["brier_improvement"],
    "h5_sign_accuracy": meta["h5"]["mean_delta"],
    "h6": h6,
    "sim": ss,
}
json.dump(n, open(os.path.join(OUT, "manuscript_numbers.json"), "w"), indent=2, default=str)

lines = ["# Manuscript numbers (from analysis/output; do not edit by hand)", ""]
p = lambda k, v: lines.append(f"- **{k}**: {v}")
p("Datasets examined", n["n_datasets_examined"])
p("Datasets included", n["n_datasets_included"])
p("Trials analysed", f"{n['n_trials_analysed']:,}")
p("Median calibration slope (standardised)", round(n["median_calibration_slope"], 3))
p("Median within-item error correlation", round(n["median_icc_rho"], 3))
p("Median judges per item", round(n["median_judges_per_item"], 1))
p("EW accuracy m=3 / m=40", (round(n["acc_ew_m3"], 3), round(n["acc_ew_m40"], 3)))
p("Sign-accuracy gap", {k: (round(v, 4) if isinstance(v, float) else
                            [round(x, 4) for x in v] if isinstance(v, list) else v)
                        for k, v in n["sign_delta"].items()})
p("LOO-Brier improvement", {k: (round(v, 5) if isinstance(v, float) else
                                [round(x, 5) for x in v] if isinstance(v, list) else v)
                            for k, v in n["loo_brier"].items()})
p("LOO-Brier clipped", n["loo_brier_clipped"])
p("LOO-Brier m=7", n["loo_brier_m7"])
p("H5 LOO-Brier", n["h5_loo_brier"])
p("H5 sign", n["h5_sign_accuracy"])
p("H6", n["h6"])
p("Simulation summary", n["sim"])
open(os.path.join(MAN, "numbers.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))