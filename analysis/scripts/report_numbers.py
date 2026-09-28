"""Collate every number used in the manuscript from the analysis outputs.

Writes analysis/output/manuscript_numbers.json (machine) and
manuscript/numbers.md (human-readable, for the drafting step).
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
simd = pd.read_csv(os.path.join(OUT, "sim_delta.csv"))
meta = json.load(open(os.path.join(OUT, "empirical_meta.json")))
h6 = json.load(open(os.path.join(OUT, "h6.json")))
ss = json.load(open(os.path.join(OUT, "sim_summary.json")))

g = dl.groupby("m")
n = {
    "n_datasets_examined": int(len(emp)),
    "n_datasets_included": int(len(inc)),
    "exclusion_reasons": emp[emp["included"] != True]["reason"].value_counts().to_dict()
    if "reason" in emp.columns else {},
    "n_trials_analysed": int(inc["n_trials"].sum()),
    "median_calibration_slope": float(inc["calibration_slope"].median()),
    "median_icc_rho": float(inc["icc_rho"].median()),
    "median_confidence_sd": float(inc["confidence_sd"].median()),
    "median_judges_per_item": float(inc["mean_judges_per_item"].median()),
    "acc_ew_m3": float(g["acc_ew"].mean().loc[3]),
    "acc_ew_m40": float(g["acc_ew"].mean().loc[40]),
    "acc_cw_m3": float(g["acc_cw"].mean().loc[3]),
    "sign_delta": meta["sign_accuracy"],
    "loo_brier": meta["loo_brier"],
    "h5_loo_brier": meta["h5"]["brier_improvement"],
    "h5_sign_accuracy": meta["h5"]["mean_delta"],
    "h6": h6,
    "sim": {
        "n_cells": ss["n_cells"],
        "frac_negative_sign_cells": ss["frac_negative_cells_sign"],
        "n_negative_sign_cells": ss["any_negative_cell_sign"],
        "frac_negative_brier_cells": ss["frac_negative_cells_brier"],
        "h3_interior_lambda_cells": ss["h3_cells_with_interior_lambda"],
        "h2_sign_violations": ss["h2_sign_violations"],
        "h2_brier_violations": ss["h2_brier_violations"],
        "h2_total_steps": ss["h2_total_steps"],
    },
    "sim_phi0_gamma03_mean_brier": float(
        sim[(sim.phi == 0) & (sim.tau == 0) & (sim.gamma == 0.3)]["mean_brier"].iloc[0]),
    "sim_phi4_gamma03_mean_delta": float(
        sim[(sim.phi == 4) & (sim.tau == 0) & (sim.gamma == 0.3)]["mean_delta"].iloc[0]),
    "sim_phi0_gamma03_mean_delta": float(
        sim[(sim.phi == 0) & (sim.tau == 0) & (sim.gamma == 0.3)]["mean_delta"].iloc[0]),
}
json.dump(n, open(os.path.join(OUT, "manuscript_numbers.json"), "w"), indent=2, default=str)

lines = ["# Manuscript numbers (from analysis/output; do not edit by hand)", ""]


def p(k, v):
    lines.append(f"- **{k}**: {v}")


p("Datasets examined", n["n_datasets_examined"])
p("Datasets included", n["n_datasets_included"])
p("Trials analysed", f"{n['n_trials_analysed']:,}")
p("Median calibration slope beta", round(n["median_calibration_slope"], 3))
p("Median within-item error correlation rho", round(n["median_icc_rho"], 3))
p("Median judges per item", round(n["median_judges_per_item"], 1))
p("EW accuracy at m=3", round(n["acc_ew_m3"], 3))
p("EW accuracy at m=40", round(n["acc_ew_m40"], 3))
p("Sign-accuracy delta (mean [CI], frac<=0)", n["sign_delta"])
p("LOO-Brier improvement (mean [CI], frac<0)", n["loo_brier"])
p("H5 LOO-Brier ~ beta, rho", n["h5_loo_brier"])
p("H6", n["h6"])
p("Simulation summary", n["sim"])
open(os.path.join(MAN, "numbers.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))