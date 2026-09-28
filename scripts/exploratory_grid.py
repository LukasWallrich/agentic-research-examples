#!/usr/bin/env python3
"""E3: reviewer-requested exact risks across all stratum-advantage sign patterns.

This explicitly exploratory grid supplements, and never alters, registered
results. Reuses the independent verifier's rational joint tables and integer
score definitions. Convolution is exact up to floating probability arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import itertools
import json

import numpy as np
import pandas as pd

from independent_check import rational_probabilities, increments

ROOT = Path(__file__).resolve().parents[1]
LEARNERS = ("absolute", "paired", "ipw", "capped")
PATTERNS = (
    ("advisor_better_both", .65, .95),
    ("advisor_better_low_only", .65, .85),
    ("advisor_better_high_only", .55, .95),
    ("advisor_worse_both", .55, .85),
)


def multi_budget_risks(probabilities, steps, budgets, delta):
    """Convolve once through the largest budget, keeping prespecified budgets."""
    assert np.min(probabilities) >= 0
    assert abs(sum(probabilities)-1) < 1e-14
    low, high = int(steps.min()), int(steps.max())
    kernel = np.zeros(high-low+1)
    np.add.at(kernel, steps-low, probabilities)
    assert abs(kernel.sum()-1) < 1e-14
    distribution = np.ones(1)
    result = {}
    for n in range(1, max(budgets)+1):
        distribution = np.convolve(distribution, kernel)
        if n not in budgets:
            continue
        error = float(abs(distribution.sum()-1))
        assert error < 1e-11 and np.min(distribution) >= 0
        scores = np.arange(len(distribution))+n*low
        tie = float(distribution[scores == 0].sum())
        adoption = float(distribution[scores > 0].sum()+.5*tie)
        if delta == 0:
            ranking_error, regret = None, 0.0
        else:
            wrong = scores < 0 if delta > 0 else scores > 0
            ranking_error = float(distribution[wrong].sum()+.5*tie)
            regret = abs(float(delta))*ranking_error
        assert -.00000000001 <= adoption <= 1.00000000001
        assert 0 <= regret <= abs(float(delta))+1e-12
        result[n] = dict(adoption=adoption, tie_probability=tie,
                         ranking_error=ranking_error, regret=regret,
                         probability_mass_error=error)
    return result


def limiting_score(probabilities, steps, learner, schedule, human):
    if learner == "absolute":
        return float(probabilities @ steps / human.denominator)
    k = 1 if schedule == "random" else int(schedule[1:])
    low_weight = k if learner == "ipw" else min(k, 2) if learner == "capped" else 1
    denominator = probabilities @ np.repeat([float(low_weight), 1.0], 4)
    assert denominator > 0
    return float(probabilities @ steps / denominator)


def main():
    config = json.loads((ROOT/"config.json").read_text())
    rows, environments, checks = [], [], []
    budgets = tuple(config["budgets"])
    for index, ((pattern, a_low, a_high), p, r) in enumerate(itertools.product(
            PATTERNS, config["p_grid"], config["overlap_grid"])):
        env = dict(env_id=f"E3_{index:02d}", pattern=pattern, p=p, r=r,
                   a_low=a_low, a_high=a_high)
        environments.append(env)
        for schedule in config["schedules"]:
            probability, human, delta, audit_yield = rational_probabilities(env, schedule, config)
            assert 0 < audit_yield <= 1
            local_results = {}
            for learner in LEARNERS:
                steps = increments(learner, schedule, human)
                results = multi_budget_risks(probability, steps, budgets, delta)
                limit = limiting_score(probability, steps, learner, schedule, human)
                local_results[learner] = results
                for n in budgets:
                    rows.append(dict(**env, schedule=schedule,
                        k=1 if schedule == "random" else int(schedule[1:]), n=n, learner=learner,
                        human_accuracy=float(human), advisor_accuracy=float(human+delta),
                        delta=float(delta), delta_low=float(F(str(a_low))-F(str(config["h_low"]))),
                        delta_high=float(F(str(a_high))-F(str(config["h_high"]))),
                        true_superiority="advisor" if delta > 0 else "self" if delta < 0 else "tie",
                        audit_yield=audit_yield, limiting_score=limit,
                        limiting_direction="advisor" if limit > 1e-12 else "self" if limit < -1e-12 else "tie",
                        **results[n]))
            if schedule in ("random", "d1"):
                for n in budgets:
                    for learner in ("ipw", "capped"):
                        assert local_results[learner][n] == local_results["paired"][n]
                        checks.append(dict(env_id=env["env_id"], schedule=schedule, n=n,
                                           learner=learner, check="equal_weights_exact_equality", passed=True))
    frame = pd.DataFrame(rows)
    assert len(frame) == 36*5*3*4 and len(environments) == 36
    base = frame.pivot(index=["env_id", "schedule", "n"], columns="learner", values="regret")
    base["ipw_minus_paired"] = base.ipw-base.paired
    frame = frame.merge(base[["ipw_minus_paired"]].reset_index(), on=["env_id", "schedule", "n"], validate="many_to_one")
    assert frame.loc[frame.delta == 0, "regret"].eq(0).all()
    assert frame.loc[frame.delta == 0, "ranking_error"].isna().all()
    matched = frame[(frame.schedule == "d4") & (frame.n == 100) & (frame.learner == "ipw")]
    summaries = []
    for (pattern, r), part in matched.groupby(["pattern", "r"]):
        difference = part.ipw_minus_paired
        summaries.append(dict(pattern=pattern, r=float(r), schedule="d4", n=100,
            environments=len(part), ipw_minus_paired_min=float(difference.min()),
            ipw_minus_paired_max=float(difference.max()),
            lower_regret=int((difference < -1e-12).sum()),
            higher_regret=int((difference > 1e-12).sum()),
            equal_to_numerical_precision=int((abs(difference) <= 1e-12).sum())))
    pattern_ranges = []
    for pattern, part in matched.groupby("pattern"):
        pattern_ranges.append(dict(pattern=pattern, schedule="d4", n=100, environments=len(part),
            ipw_minus_paired_min=float(part.ipw_minus_paired.min()),
            ipw_minus_paired_max=float(part.ipw_minus_paired.max())))
    report = dict(status="E3 exploratory extension requested by full manuscript review round 1; specified before this extension ran",
        method="Rational joint probabilities and finite discrete convolution; no Monte Carlo",
        environment_count=len(environments), rows=len(frame), budgets=list(budgets),
        schedules=config["schedules"], human_accuracies=[config["h_low"], config["h_high"]],
        advantage_magnitudes=[-.05, .05], classifications=[p[0] for p in PATTERNS],
        checks_passed=True, equal_weight_checks=len(checks),
        maximum_probability_mass_error=float(frame.probability_mass_error.max()),
        tied_environment_count=int(frame.loc[frame.delta == 0, "env_id"].nunique()),
        sign_classification_tolerance=1e-12,
        matched_k4_n100_by_pattern_and_overlap=summaries,
        matched_k4_n100_pattern_ranges=pattern_ranges,
        environments=environments,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        independent_helper_sha256=hashlib.sha256((ROOT/"scripts/independent_check.py").read_bytes()).hexdigest())
    frame.to_csv(ROOT/"output/exploratory_grid.csv", index=False)
    (ROOT/"output/exploratory_grid.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k: report[k] for k in ("environment_count", "rows", "checks_passed", "equal_weight_checks",
        "maximum_probability_mass_error", "tied_environment_count", "matched_k4_n100_pattern_ranges")}, indent=2))


if __name__ == "__main__":
    main()
