#!/usr/bin/env python3
"""Reviewer verification: exact focal risks without importing production code.

Builds joint tables using rational arithmetic and convolves integer score
increments. The only floating error in the benchmark is probability arithmetic;
there is no Monte Carlo approximation. All focal rows, including random audits,
are checked against this benchmark and independently scored saved histories.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def rational_probabilities(env, schedule, config):
    p, r = F(str(env['p'])), F(str(env['r']))
    masses = []
    for share, h, a in [(p, config['h_low'], env['a_low']),
                         (1-p, config['h_high'], env['a_high'])]:
        h, a = F(str(h)), F(str(a))
        joint = max(F(0), h+a-1) * (1-r) + min(h, a) * r
        masses.extend(share*x for x in [joint, h-joint, a-joint, 1-h-a+joint])
    h = p*F(str(config['h_low'])) + (1-p)*F(str(config['h_high']))
    a = p*F(str(env['a_low'])) + (1-p)*F(str(env['a_high']))
    k = 1 if schedule == 'random' else int(schedule[1:])
    selected = masses if schedule == 'random' else [
        x*(F(1,k) if j < 4 else 1) if j % 4 in (1, 2) else F(0)
        for j, x in enumerate(masses)]
    audit_yield = sum(selected)
    assert all(x >= 0 for x in masses) and sum(masses) == 1
    return np.array([float(x/audit_yield) for x in selected]), h, a-h, float(audit_yield)


def increments(learner, schedule, human):
    k = 1 if schedule == 'random' else int(schedule[1:])
    # Signs of rational scores can be evaluated exactly as integer sums.
    if learner == 'absolute':
        return np.array([human.denominator*x-human.numerator
                         for x in (1, 0, 1, 0, 1, 0, 1, 0)], dtype=int)
    low_weight = k if learner == 'ipw' else min(k, 2) if learner == 'capped' else 1
    return np.array([0, -low_weight, low_weight, 0, 0, -1, 1, 0])


def exact_risk(prob, steps, n, delta):
    lower, upper = int(steps.min()), int(steps.max())
    kernel = np.zeros(upper-lower+1)
    np.add.at(kernel, steps-lower, prob)
    distribution = np.array([1.0])
    for _ in range(n):
        distribution = np.convolve(distribution, kernel)
    scores = np.arange(len(distribution)) + n*lower
    adoption = (scores > 0).astype(float) + .5*(scores == 0)
    loss = abs(float(delta)) * (1-adoption if delta > 0 else adoption)
    assert abs(distribution.sum()-1) < 1e-11
    return float(distribution @ loss), float(distribution @ adoption)


def main():
    config = json.loads((ROOT/'config.json').read_text())
    cells = json.loads((ROOT/'output/cells.json').read_text())
    summary = pd.read_csv(ROOT/'output/summary.csv')
    contrasts = json.loads((ROOT/'output/contrasts.json').read_text())
    checks, exact = [], {}
    raw_contrasts = {}
    with np.load(ROOT/'output/raw_counts.npz', allow_pickle=False) as raw:
        for cell in cells:
            if not cell['environment']['focal']:
                continue
            env, schedule, n = cell['environment'], cell['schedule'], cell['n']
            prob, human, delta, audit_yield = rational_probabilities(env, schedule, config)
            assert np.allclose(prob, cell['audit_probability'], atol=1e-14, rtol=0)
            assert abs(audit_yield-cell['audit_yield']) < 1e-14
            counts = raw[cell['key']].astype(np.int64)
            risks = {}
            for learner in ('absolute', 'paired', 'ipw', 'capped'):
                steps = increments(learner, schedule, human)
                risk, adoption = exact_risk(prob, steps, n, delta)
                key = (env['env_id'], schedule, n, learner)
                exact[key] = risk
                numerators = counts @ steps
                adopted = (numerators > 0).astype(float) + .5*(numerators == 0)
                losses = abs(float(delta)) * (1-adopted if delta > 0 else adopted)
                risks[learner] = losses
                row = summary[(summary.env_id == env['env_id']) &
                              (summary.schedule == schedule) & (summary.n == n) &
                              (summary.learner == learner)].iloc[0]
                raw_mcse = float(losses.std(ddof=1)/np.sqrt(len(losses)))
                assert abs(losses.mean()-row.regret) < 1e-14
                assert abs(adopted.mean()-row.adoption) < 1e-14
                assert abs(raw_mcse-row.regret_mcse) < 1e-14
                tolerance = 5*raw_mcse + 1e-4
                passed = abs(risk-row.regret) <= tolerance
                assert passed, (key, risk, row.regret)
                checks.append(dict(environment=env['env_id'], schedule=schedule,
                    n=n, learner=learner, exact_regret=risk,
                    exact_adoption=adoption, simulated_regret=float(row.regret),
                    mcse=raw_mcse, error=float(row.regret-risk),
                    tolerance=tolerance, passed=bool(passed)))
            raw_diff = risks['ipw']-risks['paired']
            raw_contrasts[(env['env_id'], schedule, n)] = (
                float(raw_diff.mean()), float(raw_diff.std(ddof=1)/np.sqrt(len(raw_diff))))
    primary = []
    for contrast in contrasts:
        key = (contrast['env_id'], contrast['schedule'], contrast['n'])
        exact_diff = exact[(*key, 'ipw')]-exact[(*key, 'paired')]
        raw_mean, raw_se = raw_contrasts[key]
        assert abs(raw_mean-contrast['mean']) < 1e-14
        assert abs(raw_se-contrast['mcse']) < 1e-14
        interval_contains = contrast['ci_low'] <= exact_diff <= contrast['ci_high']
        assert abs(exact_diff-raw_mean) <= 5*raw_se+1e-4
        primary.append(dict(hypothesis=contrast['hypothesis'], exact_contrast=exact_diff,
            simulated_contrast=raw_mean, mcse=raw_se,
            difference_in_mcse=(raw_mean-exact_diff)/raw_se,
            exact_inside_registered_interval=bool(interval_contains)))
    report = dict(passed=True, method='Independent rational joint tables; n-fold discrete convolution of integer score increments; independently scored saved focal histories',
        simulation_imports=False, focal_learner_checks=len(checks), primary=primary,
        checks=checks, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/'output/independent_check.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'checks'}, indent=2))


if __name__ == '__main__':
    main()
