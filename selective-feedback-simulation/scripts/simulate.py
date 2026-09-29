#!/usr/bin/env python3
"""Preregistered selective-feedback simulation; raw histories are category counts.

Categories repeat (both correct, human only, advisor only, both wrong)
for low then high human confidence. Within-history order is irrelevant to
all four registered learners, so counts preserve their complete input.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import itertools
import json
import platform
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
from scipy.stats import binom

ROOT = Path(__file__).resolve().parents[1]
LEARNERS = ("absolute", "paired", "ipw", "capped")
H_CORRECT = np.array([1, 1, 0, 0, 1, 1, 0, 0], dtype=float)
A_CORRECT = np.array([1, 0, 1, 0, 1, 0, 1, 0], dtype=float)
DIFFERENCE = A_CORRECT - H_CORRECT
DISAGREE = np.abs(DIFFERENCE)


def load_config(path=ROOT / "config.json"):
    return json.loads(Path(path).read_text())


def environments(config):
    result = []
    combos = itertools.product(config["p_grid"], config["a_low_grid"],
                               config["a_high_grid"], config["overlap_grid"])
    for i, (p, al, ah, r) in enumerate(combos):
        focal = abs(p-.5) < 1e-12 and abs(al-.8) < 1e-12 and abs(ah-.8) < 1e-12 and abs(r-.5) < 1e-12
        result.append(dict(env_id=f"e{i:03d}", p=p, a_low=al, a_high=ah,
                           r=r, grid=True, focal="crossing" if focal else ""))
    result.append(dict(env_id="control", **config["homogeneous_control"],
                       grid=False, focal="homogeneous"))
    return result


def joint_probabilities(env, config):
    h = np.array([config["h_low"], config["h_high"]])
    a = np.array([env["a_low"], env["a_high"]])
    lower, upper = np.maximum(0, h+a-1), np.minimum(h, a)
    q = lower + env["r"] * (upper-lower)
    conditional = np.column_stack([q, h-q, a-q, 1-h-a+q])
    if conditional.min() < -1e-12:
        raise FloatingPointError("Negative joint probability")
    # Algebraic structural zeros can acquire a last-bit negative representation.
    conditional[np.abs(conditional) < 1e-14] = 0
    probability = (conditional * np.array([env["p"], 1-env["p"]])[:, None]).ravel()
    if not np.isclose(probability.sum(), 1, atol=1e-12, rtol=0):
        raise FloatingPointError("Joint probabilities do not sum to one")
    return probability


def audit_distribution(probability, schedule):
    if schedule == "random":
        selection = np.ones(8)
    else:
        k = int(schedule[1:])
        selection = DISAGREE * np.repeat([1/k, 1.0], 4)
    selected = probability * selection
    audit_yield = selected.sum()
    if audit_yield <= 0:
        raise ValueError("Audit distribution undefined: zero yield")
    return selected / audit_yield, selection, float(audit_yield)


def learner_weights(schedule, config):
    k = 1 if schedule == "random" else int(schedule[1:])
    ipw = np.repeat([float(k), 1.0], 4)
    return {"paired": np.ones(8), "ipw": ipw,
            "capped": np.minimum(ipw, config["weight_cap"])}


def learner_scores(counts, schedule, human_accuracy, config):
    counts = np.asarray(counts, dtype=float)
    total = counts.sum(axis=-1)
    scores = {"absolute": counts @ A_CORRECT / total - human_accuracy}
    for learner, weights in learner_weights(schedule, config).items():
        scores[learner] = (counts @ (weights * DIFFERENCE)) / (counts @ weights)
    if any(not np.isfinite(score).all() for score in scores.values()):
        raise FloatingPointError("Nonfinite learner score")
    return scores


def adoption_probability(scores, config):
    tol = config["tie_tolerance"]
    return np.where(scores > tol, 1.0, np.where(scores < -tol, 0.0, 0.5))


def history_metrics(scores, delta, config):
    adoption = adoption_probability(scores, config)
    if abs(delta) <= config["tie_tolerance"]:
        return adoption, np.full_like(adoption, np.nan), np.zeros_like(adoption)
    wrong = 1-adoption if delta > 0 else adoption
    return adoption, wrong, abs(delta)*wrong


def se(values):
    return float(np.std(values, ddof=1) / np.sqrt(len(values)))


def exact_uniform_metrics(env, n, learner, config):
    """Exact binomial expectation for the uniform-disagreement audit."""
    prob = joint_probabilities(env, config)
    audit, _, _ = audit_distribution(prob, "d1")
    h, a = prob @ H_CORRECT, prob @ A_CORRECT
    wins = np.arange(n+1)
    pmf = binom.pmf(wins, n, audit @ A_CORRECT)
    score = wins/n-h if learner == "absolute" else (2*wins-n)/n
    adopt, wrong, regret = history_metrics(score, a-h, config)
    return {"adoption": float(pmf @ adopt), "regret": float(pmf @ regret),
            "ranking_error": None if abs(a-h) <= config["tie_tolerance"] else float(pmf @ wrong)}


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def generate(config, out):
    out.mkdir(parents=True, exist_ok=True)
    cells = []
    specs = list(itertools.product(environments(config), config["schedules"], config["budgets"]))
    children = np.random.SeedSequence(config["seed"]).spawn(len(specs))
    temporary = out / "raw_counts.tmp.npz"
    with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for index, ((env, schedule, n), child) in enumerate(zip(specs, children)):
            probability = joint_probabilities(env, config)
            audit, _, audit_yield = audit_distribution(probability, schedule)
            rng = np.random.Generator(np.random.PCG64(child))
            counts = rng.multinomial(n, audit, size=config["runs"]).astype(np.uint16)
            key = f"{env['env_id']}_{schedule}_n{n}"
            # Fix ZIP member metadata, making the raw archive byte-reproducible.
            member = zipfile.ZipInfo(key + ".npy", date_time=(1980, 1, 1, 0, 0, 0))
            member.compress_type = zipfile.ZIP_DEFLATED
            with archive.open(member, "w") as target:
                np.save(target, counts, allow_pickle=False)
            cells.append(dict(key=key, child_index=index, spawn_key=list(child.spawn_key),
                              environment=env, schedule=schedule, n=n,
                              audit_probability=audit.tolist(), audit_yield=audit_yield))
            if index % 150 == 0:
                print(f"Generated {index+1}/{len(specs)} cells", flush=True)
    temporary.replace(out / "raw_counts.npz")
    write_json(out / "cells.json", cells)
    return cells


def summarise(config, out):
    cells = json.loads((out / "cells.json").read_text())
    rows, contrasts = [], []
    with np.load(out / "raw_counts.npz", allow_pickle=False) as archive:
        for cell in cells:
            env, schedule, n = cell["environment"], cell["schedule"], cell["n"]
            counts = archive[cell["key"]]
            if counts.shape != (config["runs"], 8) or not np.all(counts.sum(axis=1) == n):
                raise AssertionError("Invalid raw history dimensions or totals")
            prob = joint_probabilities(env, config)
            audit, _, audit_yield = audit_distribution(prob, schedule)
            h, a = float(prob @ H_CORRECT), float(prob @ A_CORRECT)
            delta = a-h
            scores = learner_scores(counts, schedule, h, config)
            limits = learner_scores(audit, schedule, h, config)
            risks = {}
            reversed_sign = (abs(delta) > config["tie_tolerance"] and
                             float(limits["paired"])*delta < -config["tie_tolerance"])
            for learner in LEARNERS:
                adoption, wrong, regret = history_metrics(scores[learner], delta, config)
                risks[learner] = regret
                limit = float(limits[learner])
                row = dict(**env, schedule=schedule, k=1 if schedule == "random" else int(schedule[1:]),
                           n=n, learner=learner, runs=config["runs"], human_accuracy=h,
                           advisor_accuracy=a, delta=delta, disagreement=float(prob @ DISAGREE),
                           audit_yield=audit_yield, expected_opportunities=n/audit_yield,
                           population_reversal=bool(reversed_sign), adoption=float(adoption.mean()),
                           adoption_mcse=se(adoption), tie_probability=float(np.mean(np.abs(scores[learner]) <= config["tie_tolerance"])), regret=float(regret.mean()), regret_mcse=se(regret),
                           ranking_error=None if abs(delta) <= config["tie_tolerance"] else float(wrong.mean()),
                           score_mean=float(scores[learner].mean()), score_sd=float(scores[learner].std(ddof=1)),
                           limiting_score=limit,
                           limiting_direction="advisor" if limit > config["tie_tolerance"] else "self" if limit < -config["tie_tolerance"] else "tie")
                rows.append(row)
            hypothesis = ("H1" if env["focal"] == "crossing" and schedule == "d4" and n == 100
                          else "H2" if env["focal"] == "homogeneous" and schedule == "d8" and n == 20
                          else None)
            if hypothesis:
                diff = risks["ipw"]-risks["paired"]
                mean, mcse = float(diff.mean()), se(diff)
                low, high = mean-config["contrast_z"]*mcse, mean+config["contrast_z"]*mcse
                expected_sign = -1 if hypothesis == "H1" else 1
                outcome = ("supported" if (high < 0 if expected_sign < 0 else low > 0)
                           else "contradicted" if (low > 0 if expected_sign < 0 else high < 0)
                           else "unresolved")
                contrasts.append(dict(hypothesis=hypothesis, env_id=env["env_id"], schedule=schedule,
                                      n=n, contrast="regret_ipw_minus_paired", mean=mean, mcse=mcse,
                                      ci_low=low, ci_high=high, confidence_level=.975,
                                      predicted_sign=expected_sign, outcome=outcome))
    frame = pd.DataFrame(rows)
    frame.to_csv(out / "summary.csv", index=False)
    pd.DataFrame(contrasts).to_csv(out / "contrasts.csv", index=False)
    write_json(out / "contrasts.json", contrasts)
    grid = frame[frame.grid].pivot(index=["env_id", "schedule", "n", "population_reversal"], columns="learner", values="regret").reset_index()
    descriptions = []
    for (schedule, n, reversal), part in grid.groupby(["schedule", "n", "population_reversal"]):
        for learner in ("absolute", "ipw", "capped"):
            diff = part[learner]-part.paired
            descriptions.append(dict(schedule=schedule, n=int(n), population_reversal=bool(reversal),
                                     learner=learner, comparator="paired", environments=len(part),
                                     better=int((diff < -config["regret_tolerance"]).sum()),
                                     worse=int((diff > config["regret_tolerance"]).sum()),
                                     equal=int((abs(diff) <= config["regret_tolerance"]).sum()),
                                     tolerance=config["regret_tolerance"]))
    pd.DataFrame(descriptions).to_csv(out / "descriptive_grid.csv", index=False)
    write_json(out / "descriptive_grid.json", descriptions)
    all_env = frame.pivot(index=["env_id", "schedule", "n"], columns="learner", values="regret").reset_index()
    crossings = []
    for (env_id, schedule), part in all_env.groupby(["env_id", "schedule"]):
        lower = part.loc[part.ipw-part.paired < -config["regret_tolerance"], "n"]
        crossings.append(dict(env_id=env_id, schedule=schedule,
                              lowest_observed_n=None if lower.empty else int(lower.min()),
                              tolerance=config["regret_tolerance"]))
    pd.DataFrame(crossings).to_csv(out / "crossovers.csv", index=False)
    metadata = dict(config=config, python=sys.version, numpy=np.__version__, scipy=scipy.__version__,
                    pandas=pd.__version__, platform=platform.platform(),
                    generated_utc=datetime.now(timezone.utc).isoformat(),
                    environment_count=len(environments(config)), grid_count=81,
                    cells=len(cells), histories=len(cells)*config["runs"],
                    category_order=["low_both_correct", "low_human_only", "low_advisor_only", "low_both_wrong",
                                    "high_both_correct", "high_human_only", "high_advisor_only", "high_both_wrong"],
                    raw_dtype="uint16", rng="NumPy PCG64, SeedSequence child per cell",
                    hashes={name: sha256(out/name) for name in ["raw_counts.npz", "cells.json", "summary.csv", "contrasts.csv"]},
                    source_hashes={name: sha256(ROOT/name) for name in ["config.json", "scripts/simulate.py", "requirements.txt"]})
    write_json(out / "metadata.json", metadata)
    print(json.dumps(contrasts, indent=2), flush=True)
    return frame


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["run", "summarise"], nargs="?", default="run")
    parser.add_argument("--out", type=Path, default=ROOT / "output")
    args = parser.parse_args()
    config = load_config()
    if args.command == "run":
        generate(config, args.out)
    summarise(config, args.out)


if __name__ == "__main__":
    main()
