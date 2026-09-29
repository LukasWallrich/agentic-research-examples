#!/usr/bin/env python3
"""Internal algebraic and exact-distribution checks of registered outputs."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from simulate import (ROOT, A_CORRECT, H_CORRECT, DIFFERENCE, DISAGREE,
                      environments, joint_probabilities, audit_distribution,
                      learner_scores, exact_uniform_metrics, load_config,
                      write_json, sha256)


def verify(out):
    config = load_config()
    frame = pd.read_csv(out / "summary.csv")
    cells = json.loads((out / "cells.json").read_text())
    checks = {"joint_tables": 0, "margins": 0, "sign_identities": 0,
              "weighted_limits": 0, "k1_equivalence": 0, "raw_histories": 0,
              "exact_binomial": 0, "rng_reproductions": 0}
    exact_rows = []
    assert len(frame) == 82*5*3*4
    assert len(cells) == 82*5*3
    assert len(set(c["key"] for c in cells)) == len(cells)
    for env in environments(config):
        prob = joint_probabilities(env, config)
        assert np.all(prob >= 0) and abs(prob.sum()-1) < 1e-12
        checks["joint_tables"] += 1
        for start, mass, h, a in ((0, env["p"], config["h_low"], env["a_low"]),
                                   (4, 1-env["p"], config["h_high"], env["a_high"])):
            local = prob[start:start+4] / mass
            assert abs(local[0]+local[1]-h) < 1e-12
            assert abs(local[0]+local[2]-a) < 1e-12
            checks["margins"] += 1
        h, a, d = prob @ H_CORRECT, prob @ A_CORRECT, prob @ DISAGREE
        delta = a-h
        uniform, _, _ = audit_distribution(prob, "d1")
        assert abs(uniform @ DIFFERENCE - delta/d) < 1e-12
        assert abs(uniform @ A_CORRECT - (1+delta/d)/2) < 1e-12
        checks["sign_identities"] += 1
        for schedule in config["schedules"]:
            audit, selection, audit_yield = audit_distribution(prob, schedule)
            limit = learner_scores(audit, schedule, h, config)
            target = delta if schedule == "random" else delta/d
            assert abs(float(limit["ipw"])-target) < 1e-12
            assert np.all((selection >= 0) & (selection <= 1))
            assert audit_yield > 0
            checks["weighted_limits"] += 1
        if env["focal"]:
            for n in config["budgets"]:
                for learner in ("absolute", "paired"):
                    exact = exact_uniform_metrics(env, n, learner, config)
                    row = frame[(frame.env_id == env["env_id"]) & (frame.schedule == "d1") &
                                (frame.n == n) & (frame.learner == learner)].iloc[0]
                    for metric in ("adoption", "regret"):
                        error = abs(row[metric]-exact[metric])
                        tolerance = 5*row[metric+"_mcse"]+1e-4
                        exact_rows.append(dict(env_id=env["env_id"], n=n, learner=learner,
                                               metric=metric, simulated=float(row[metric]),
                                               exact=exact[metric], error=float(error),
                                               tolerance=float(tolerance), passed=bool(error <= tolerance)))
                        assert error <= tolerance, exact_rows[-1]
                        checks["exact_binomial"] += 1
    with np.load(out / "raw_counts.npz", allow_pickle=False) as archive:
        assert len(archive.files) == len(cells)
        for cell in cells:
            counts = archive[cell["key"]]
            assert counts.dtype == np.uint16
            assert counts.shape == (config["runs"], 8)
            assert np.all(counts.sum(axis=1) == cell["n"])
            audit = np.asarray(cell["audit_probability"])
            assert np.all(counts[:, audit == 0] == 0)
            checks["raw_histories"] += len(counts)
            if cell["schedule"] in ("random", "d1"):
                probability = joint_probabilities(cell["environment"], config)
                scores = learner_scores(counts, cell["schedule"], probability @ H_CORRECT, config)
                assert np.array_equal(scores["paired"], scores["ipw"])
                assert np.array_equal(scores["paired"], scores["capped"])
                checks["k1_equivalence"] += 1
            if cell["child_index"] in (0, len(cells)//2, len(cells)-1):
                child = np.random.SeedSequence(config["seed"], spawn_key=tuple(cell["spawn_key"]))
                recreated = np.random.Generator(np.random.PCG64(child)).multinomial(cell["n"], audit, size=config["runs"])
                assert np.array_equal(counts, recreated)
                checks["rng_reproductions"] += 1
    # Confirm the primary tests exist once and match their prespecified cells.
    contrasts = pd.read_csv(out / "contrasts.csv").set_index("hypothesis")
    assert set(contrasts.index) == {"H1", "H2"} and len(contrasts) == 2
    assert contrasts.loc["H1", "schedule"] == "d4" and contrasts.loc["H1", "n"] == 100
    assert contrasts.loc["H2", "schedule"] == "d8" and contrasts.loc["H2", "n"] == 20
    assert frame.regret.between(0, frame.delta.abs()+1e-12).all()
    ties = frame.delta.abs() <= config["tie_tolerance"]
    assert (frame.loc[ties, "regret"] == 0).all()
    assert frame.loc[ties, "ranking_error"].isna().all()
    pd.DataFrame(exact_rows).to_csv(out / "exact_verification.csv", index=False)
    report = dict(passed=True, checks=checks, exact_checks=exact_rows,
                  primary_hypotheses=list(contrasts.index),
                  source_sha256=sha256(ROOT / "scripts/verify.py"))
    write_json(out / "verification.json", report)
    print(json.dumps({"passed": True, "checks": checks}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "output")
    verify(parser.parse_args().out)
