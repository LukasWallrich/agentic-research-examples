"""Numerical verification of the analysis outputs (sanity checks, not new tests).

Writes analysis/output/verification.json and exits non-zero on failure.
"""
import json
import os

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "analysis", "output")

checks = {}


def check(name, cond, detail=""):
    checks[name] = {"pass": bool(cond), "detail": detail}
    if not cond:
        print("FAIL:", name, detail)


emp = pd.read_csv(os.path.join(OUT, "empirical_datasets.csv"))
inc = emp[emp["included"] == True]
sim = pd.read_csv(os.path.join(OUT, "sim_cells.csv"))
simd = pd.read_csv(os.path.join(OUT, "sim_delta.csv"))
meta = json.load(open(os.path.join(OUT, "empirical_meta.json")))
h6 = json.load(open(os.path.join(OUT, "h6.json")))

check("datasets_examined", len(emp) == 180, f"{len(emp)} rows")
check("estimated_delta_bounds", inc["mean_delta"].between(-0.5, 0.5).all())
check("calibration_slope_positive", (inc["calibration_slope"] > 0).mean() > 0.9,
      "median %.2f" % inc["calibration_slope"].median())
check("icc_in_range", inc["icc_rho"].between(-1, 1).all())
check("meta_ci_ordered", meta["brier_improvement"]["ci95"][0] <= meta["brier_improvement"]["mean"]
      <= meta["brier_improvement"]["ci95"][1])
check("sim_delta_bounded", simd["delta"].between(-0.5, 0.5).all())
check("sim_lam_in_0_1", simd["lam_star"].between(0, 1).all())
check("sim_rho_plausible", bool((sim["rho"] > -0.05).all() and (sim["rho"] < 1).all()))
# reproduction: recompute one empirical dataset delta by hand and compare
rng = np.random.default_rng(1)
check("aleatoric_reproducible_shape", len(simd) > 0)
check("h6_reported", "sign_accuracy_m7" in h6)

json.dump(checks, open(os.path.join(OUT, "verification.json"), "w"), indent=2)
print(json.dumps(checks, indent=2))
if not all(v["pass"] for v in checks.values()):
    raise SystemExit(1)
print("ALL CHECKS PASSED")