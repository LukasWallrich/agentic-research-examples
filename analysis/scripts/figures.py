"""Figures for the manuscript. Writes PNGs to analysis/output/figures/."""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "analysis", "output")
FIG = os.path.join(OUT, "figures")
os.makedirs(FIG, exist_ok=True)

plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})
C = {"ew": "#1f4e79", "cw": "#c0504d", "sim": "#7f7f7f", "acc": "#2e7d32"}

emp_delta = pd.read_csv(os.path.join(OUT, "empirical_delta.csv"))
emp = pd.read_csv(os.path.join(OUT, "empirical_datasets.csv"))
sim = pd.read_csv(os.path.join(OUT, "sim_cells.csv"))
sim_d = pd.read_csv(os.path.join(OUT, "sim_delta.csv"))

# Fig 1: empirical Delta(m) and Delta_Brier(m)
fig, ax = plt.subplots(1, 2, figsize=(8.5, 3.2))
g = emp_delta.groupby("m")
ax[0].errorbar(g["delta"].mean().index, g["delta"].mean().values,
               yerr=1.96 * g["delta"].sem().values, marker="o", color=C["cw"], capsize=3)
ax[0].axhline(0, color="k", lw=0.8, ls="--")
ax[0].set_xlabel("Group size $m$"); ax[0].set_ylabel(r"$\Delta$ crowd accuracy (CW $-$ EW)")
ax[0].set_title("(a) Sign-accuracy advantage", loc="left", fontsize=9)
incb = emp[emp["included"] == True]["brier_improvement"].dropna()
ax[1].hist(incb, bins=25, color=C["sim"], edgecolor="white")
ax[1].axvline(0, color="k", lw=0.8, ls="--")
ax[1].axvline(incb.mean(), color=C["cw"], lw=1.5)
ax[1].set_xlabel(r"$\Delta$ Brier (EW $-$ CW), leave-one-judge-out")
ax[1].set_ylabel("Datasets")
ax[1].set_title(f"(b) LOO-Brier, N={len(incb)} datasets", loc="left", fontsize=9)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig1_empirical.png"), dpi=200); plt.close(fig)

# Fig 2: simulated boundary surface, mean_brier over (tau, phi), gamma=0.3
fig, ax = plt.subplots(1, 2, figsize=(8.5, 3.2))
for k, (col, lab) in enumerate([("mean_brier", "(a) LOO-Brier improvement"), ("mean_delta", "(b) Accuracy $\\Delta$")]):
    sub = sim[sim.gamma == 0.3].pivot(index="tau", columns="phi", values=col)
    im = ax[k].imshow(sub.values, origin="lower", aspect="auto", cmap="RdBu_r",
                      vmin=-abs(sub.values).max(), vmax=abs(sub.values).max())
    ax[k].set_xticks(range(len(sub.columns)), sub.columns)
    ax[k].set_yticks(range(len(sub.index)), sub.index)
    ax[k].set_xlabel("Overconfidence $\\phi$"); ax[k].set_ylabel("Shared error $\\tau$")
    ax[k].set_title(lab, loc="left", fontsize=9)
    fig.colorbar(im, ax=ax[k], fraction=0.046)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig2_boundary.png"), dpi=200); plt.close(fig)

# Fig 3: empirical moderation
fig, ax = plt.subplots(1, 2, figsize=(8.5, 3.2))
ax[0].scatter(emp["calibration_slope"], emp["brier_improvement"], s=12, alpha=0.7, color=C["ew"])
ax[0].axhline(0, color="k", lw=0.8, ls="--")
ax[0].set_xlabel("Calibration slope $\\beta$"); ax[0].set_ylabel("LOO-Brier improvement")
ax[1].scatter(emp["icc_rho"], emp["brier_improvement"], s=12, alpha=0.7, color=C["acc"])
ax[1].axhline(0, color="k", lw=0.8, ls="--")
ax[1].set_xlabel("Within-item error correlation $\\rho$")
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig3_moderation.png"), dpi=200); plt.close(fig)

# Fig 4: shrinkage curve for a representative cell (large phi) and a well-calibrated one
fig, ax = plt.subplots(figsize=(4.2, 3.0))
LAM = np.round(np.arange(0, 1.0001, 0.05), 3)
for phi, col in [(0.0, C["ew"]), (2.0, C["cw"]), (4.0, C["sim"])]:
    sub = sim_d[(sim_d.gamma == 0.3) & (sim_d.tau == 0.0) & (sim_d.phi == phi)].sort_values("m")
    ax.plot(sub["m"], sub["lam_star"], marker="o", ms=3, color=col, label=f"$\\phi$={phi}")
ax.set_xscale("log"); ax.set_xlabel("Group size $m$"); ax.set_ylabel("Optimal shrinkage $\\lambda^*$")
ax.set_ylim(-0.02, 1.02); ax.legend(frameon=False, fontsize=8)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig4_lambda.png"), dpi=200); plt.close(fig)

print("figures written to", FIG)