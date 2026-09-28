#!/usr/bin/env python3
"""Exploratory reviewer-requested sensitivity analyses using exact distributions.

E1 fixes encountered opportunities, including opportunities yielding no label.
E2 fixes verified labels and varies assumed inverse-selection weights.
No Monte Carlo draws; all risks follow finite discrete score convolutions.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
H = (1, 1, 0, 0, 1, 1, 0, 0)
A = (1, 0, 1, 0, 1, 0, 1, 0)


def focal_worlds():
    return [dict(environment="crossing", p=F(1, 2), h_low=F(3, 5), h_high=F(9, 10),
                 a_low=F(4, 5), a_high=F(4, 5), overlap=F(1, 2)),
            dict(environment="homogeneous", p=F(1, 2), h_low=F(3, 5), h_high=F(9, 10),
                 a_low=F(13, 20), a_high=F(19, 20), overlap=F(1, 2))]


def joint_table(world):
    probabilities = []
    for mass, human, advisor in ((world["p"], world["h_low"], world["a_low"]),
                                  (1-world["p"], world["h_high"], world["a_high"])):
        lower = max(F(0), human+advisor-1)
        upper = min(human, advisor)
        both = lower+world["overlap"]*(upper-lower)
        probabilities.extend(mass*x for x in (both, human-both, advisor-both, 1-human-advisor+both))
    assert min(probabilities) >= 0 and sum(probabilities) == 1
    return probabilities


def selected_masses(probabilities, schedule):
    if schedule == "random":
        return probabilities.copy()
    k = int(schedule[1:])
    assert k > 0
    return [mass*(F(1, k) if c < 4 else F(1)) if H[c] != A[c] else F(0)
            for c, mass in enumerate(probabilities)]


def score_steps(learner, schedule, assumed_weight=None):
    k = 1 if schedule == "random" else int(schedule[1:])
    if learner == "absolute":
        return [4*correct-3 for correct in A]
    low = (assumed_weight if assumed_weight is not None else k if learner == "ipw"
           else min(k, 2) if learner == "capped" else 1)
    assert low > 0
    return [(a-h)*(low if c < 4 else 1) for c, (a, h) in enumerate(zip(A, H))]


def exact_metrics(probabilities, steps, budget, delta):
    """Sum iid integer score increments; average fair tie decisions exactly."""
    assert sum(probabilities) == 1 and min(probabilities) >= 0
    assert len(probabilities) == len(steps)
    lower, upper = min(steps), max(steps)
    kernel = np.zeros(upper-lower+1)
    for probability, step in zip(probabilities, steps):
        kernel[step-lower] += float(probability)
    assert abs(kernel.sum()-1) < 1e-14
    distribution = np.ones(1)
    for _ in range(budget):
        distribution = np.convolve(distribution, kernel)
    assert distribution.min() >= 0
    mass_error = abs(distribution.sum()-1)
    assert mass_error < 1e-11
    total_score = np.arange(len(distribution))+budget*lower
    adoption = float(distribution[total_score > 0].sum()+.5*distribution[total_score == 0].sum())
    # Sum loss directly rather than subtract near-unit adoption probabilities.
    incorrect = total_score < 0 if delta > 0 else total_score > 0
    ranking_error = float(distribution[incorrect].sum()+.5*distribution[total_score == 0].sum())
    regret = abs(float(delta))*ranking_error if delta else 0.0
    return dict(adoption=adoption, regret=regret, ranking_error=ranking_error,
                probability_mass_error=float(mass_error))


def main():
    config = json.loads((ROOT/"config.json").read_text())
    records, thresholds, oracles, stratum_details, cap_limits = [], [], [], [], []
    for world in focal_worlds():
        prob = joint_table(world)
        human = sum(m*h for m, h in zip(prob, H))
        advisor = sum(m*a for m, a in zip(prob, A))
        assert human == F(3, 4) and advisor == F(4, 5)
        delta = advisor-human
        for stratum, start, share in (("low", 0, world["p"]), ("high", 4, 1-world["p"])):
            stratum_details.append(dict(environment=world["environment"], stratum=stratum,
                mass=float(share), advantage=float(world["a_"+stratum]-world["h_"+stratum]),
                disagreement=float((prob[start+1]+prob[start+2])/share)))
        conditional_oracle = (world["p"]*max(world["h_low"], world["a_low"])
                              +(1-world["p"])*max(world["h_high"], world["a_high"]))
        oracles.append(dict(environment=world["environment"], global_oracle_accuracy=float(max(human, advisor)),
                            confidence_stratum_oracle_accuracy=float(conditional_oracle),
                            accuracy_increment=float(conditional_oracle-max(human, advisor))))
        for schedule in config["schedules"]:
            selected = selected_masses(prob, schedule)
            audit_yield = sum(selected)
            assert 0 < audit_yield <= 1
            conditional = [p/audit_yield for p in selected]
            opportunities = selected + [1-audit_yield]
            capped_steps = score_steps("capped", schedule)
            capped_limit = sum(p*step for p, step in zip(conditional, capped_steps))
            cap_limits.append(dict(environment=world["environment"], schedule=schedule,
                cap=2, limiting_numerator=float(capped_limit),
                degenerate_zero_mean=bool(capped_limit == 0),
                limiting_direction="advisor" if capped_limit > 0 else "self" if capped_limit < 0 else "tie"))
            for budget in config["budgets"]:
                for learner in ("absolute", "paired", "ipw", "capped"):
                    steps = score_steps(learner, schedule)
                    encountered = exact_metrics(opportunities, steps+[0], budget, delta)
                    fixed_labels = exact_metrics(conditional, steps, budget, delta)
                    records.append(dict(analysis="E1_equal_encounters", environment=world["environment"],
                        schedule=schedule, budget=budget, learner=learner, assumed_low_weight=None,
                        true_low_weight=1 if schedule == "random" else int(schedule[1:]),
                        audit_yield=float(audit_yield), expected_labels=float(budget*audit_yield),
                        no_audit_probability=float((1-audit_yield)**budget),
                        confidence_stratum_oracle_accuracy=float(conditional_oracle),
                        global_oracle_accuracy=float(max(human, advisor)),
                        fixed_label_adoption=fixed_labels["adoption"], fixed_label_regret=fixed_labels["regret"],
                        encountered_minus_fixed_label_regret=encountered["regret"]-fixed_labels["regret"],
                        **encountered))
        for schedule in ("d4", "d8"):
            k = int(schedule[1:])
            selected = selected_masses(prob, schedule)
            audit_yield = sum(selected)
            conditional = [p/audit_yield for p in selected]
            # Weighted numerator per encountered case is slope*w + intercept.
            slope = world["p"]*(world["a_low"]-world["h_low"])/k
            intercept = (1-world["p"])*(world["a_high"]-world["h_high"])
            assert slope > 0
            thresholds.append(dict(environment=world["environment"], true_schedule=schedule,
                assumed_weight_threshold=float(-intercept/slope),
                advisor_selected_above_threshold=True,
                positive_weights_always_correct=bool(intercept >= 0),
                slope_per_encounter=float(slope), intercept_per_encounter=float(intercept)))
            for assumed_weight in (1, 2, 4, 8, 16):
                steps = score_steps("ipw", schedule, assumed_weight)
                limit = sum(p*step for p, step in zip(conditional, steps))
                assert (limit > 0) == (slope*assumed_weight+intercept > 0)
                for budget in config["budgets"]:
                    risk = exact_metrics(conditional, steps, budget, delta)
                    records.append(dict(analysis="E2_weight_misspecification", environment=world["environment"],
                        schedule=schedule, budget=budget, learner="assumed_weight_paired",
                        assumed_low_weight=assumed_weight, true_low_weight=k,
                        relative_weight_ratio=assumed_weight/k,
                        audit_yield=float(audit_yield), expected_labels=budget,
                        limiting_numerator=float(limit), limiting_direction="advisor" if limit > 0 else "self" if limit < 0 else "tie",
                        **risk))
    frame = pd.DataFrame(records)
    e1 = frame[frame.analysis == "E1_equal_encounters"]
    identity_checks = []
    for environment in ("crossing", "homogeneous"):
        for budget in config["budgets"]:
            paired = e1[(e1.environment == environment) & (e1.budget == budget) & (e1.learner == "paired")].set_index("schedule")
            difference = abs(paired.loc["random", "regret"]-paired.loc["d1", "regret"])
            assert difference < 1e-14
            identity_checks.append(dict(environment=environment, budget=budget, absolute_regret_difference=float(difference)))
    summaries = []
    for environment, schedule, budget, label in (("crossing", "d4", 100, "H1_scenario"),
                                                 ("homogeneous", "d8", 20, "H2_scenario")):
        part = e1[(e1.environment == environment) & (e1.schedule == schedule) & (e1.budget == budget)].set_index("learner")
        summaries.append(dict(scenario=label, environment=environment, schedule=schedule,
            encounters=budget, expected_labels=float(part.loc["ipw", "expected_labels"]),
            equal_encounter_ipw_regret=float(part.loc["ipw", "regret"]),
            equal_encounter_paired_regret=float(part.loc["paired", "regret"]),
            equal_encounter_ipw_minus_paired=float(part.loc["ipw", "regret"]-part.loc["paired", "regret"]),
            equal_label_ipw_minus_paired=float(part.loc["ipw", "fixed_label_regret"]-part.loc["paired", "fixed_label_regret"])))
    report = dict(status="Exploratory; requested in manuscript review round 1; not preregistered",
        method="Rational probability tables and finite iid convolution of integer score increments; no Monte Carlo",
        E1="Fixed encountered opportunities; unaudited cases add zero score; no labels means a fair tie",
        E2="Fixed verified labels; assumed inverse-selection low/high weight ratios 1, 2, 4, 8, 16",
        oracle_definition="Best source conditional on confidence stratum, known to oracle, without per-case outcome knowledge",
        rows=len(records), checks_passed=True, random_d1_paired_identity_checks=identity_checks,
        focal_contrast_summaries=summaries, misspecification_thresholds=thresholds,
        conditional_oracles=oracles, stratum_details=stratum_details, capped_limits=cap_limits,
        results=records,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/"output/exploratory_checks.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    frame.to_csv(ROOT/"output/exploratory_checks.csv", index=False)
    print(json.dumps({k: report[k] for k in ("rows", "checks_passed", "focal_contrast_summaries", "misspecification_thresholds", "conditional_oracles")}, indent=2))


if __name__ == "__main__":
    main()
