"""Scratch: calibrate the simulation to the empirical psychometric inputs."""
import numpy as np
from scipy import optimize

N = 40000
MMAX = 25


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def logit_slope(x, y):
    def nll(p):
        z = p[0] + p[1] * x
        return np.sum(np.logaddexp(0, z) - y * z)
    return float(optimize.minimize(nll, [0, 1], method="BFGS").x[1])


def run(tau, phi, gamma, omega, sigma_a, sigma_eps, seed):
    rng = np.random.default_rng(seed)
    delta = rng.normal(0, 1, N)
    truth = np.where(delta >= 0, 1.0, -1.0)
    u = rng.normal(0, tau, N)
    a = rng.normal(0, sigma_a, (N, MMAX))
    o = rng.normal(0, 1, (N, MMAX))
    s = delta[:, None] + u[:, None] + a + rng.normal(0, sigma_eps, (N, MMAX))
    correct = (np.sign(s) == truth[:, None]).astype(float)
    v = 2 * correct - 1
    c = sigmoid(gamma * (truth[:, None] * s) + phi * o) + rng.normal(0, omega, (N, MMAX))
    c = np.clip(c, 0.001, None)
    c = (c - c.min()) / (c.max() - c.min()) + 1e-6
    beta = logit_slope(c[:, :10].ravel(), correct[:, :10].ravel())
    res = {}
    for m in (3, 9, 25):
        vm, cm = v[:, :m], c[:, :m]
        ew = vm.mean(1)
        cw = (cm * vm).sum(1) / cm.sum(1)
        res[m] = float(np.mean(cw > 0) - np.mean(ew > 0))
    # ICC quick
    item_ids = np.repeat(np.arange(N), 5)
    acc5 = correct[:, :5].ravel()
    g = np.array([acc5[i::N].mean() for i in range(N)])
    # deposition via group means
    means = acc5.reshape(N, 5).mean(1)
    grand = acc5.mean()
    ssb = 5 * np.sum((means - grand) ** 2)
    ssw = np.sum((acc5.reshape(N, 5) - means[:, None]) ** 2)
    rho = (ssb / (N - 1)) - (ssw / (N * 4))
    denom = (ssb / (N - 1)) + 4 * (ssw / (N * 4))
    res['rho'] = float(rho / denom) if denom else float('nan')
    return beta, res


print(f"{'gamma':>6}{'phi':>5}{'omega':>7}{'tau':>5} | {'beta':>7} {'rho':>7} {'d3':>8} {'d9':>8} {'d25':>8}")
for gamma in (0.3, 0.6, 1.0, 1.5):
    for phi in (0.0, 2.0):
        for omega in (0.1, 0.3):
            for tau in (0.0, 0.6):
                beta, r = run(tau, phi, gamma, omega, 0.7, 1.0, 7)
                print(f"{gamma:>6}{phi:>5}{omega:>7}{tau:>5} | {beta:>7.2f} {r['rho']:>7.3f} "
                      f"{r[3]:>8.4f} {r[9]:>8.4f} {r[25]:>8.4f}")