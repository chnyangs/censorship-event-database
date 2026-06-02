"""Deterministic nonparametric bootstrap 95% CI for Cohen's / Fleiss' kappa.

Shared by ``compute_irr_kappa.py`` and ``compute_evidence_tier_irr_kappa.py`` so
that every published kappa carries an uncertainty interval. This matters because
the reliability subset is coded on small n (e.g. attribution n=20): a bare point
estimate of kappa=0.58 is nearly uninformative without its CI, and the project's
kappa<0.6 paper-readiness gate should be read against the interval, not the
point.

The bootstrap is seeded and therefore reproducible run-to-run, so regenerating
the kappa report does not churn the artifact.
"""
from __future__ import annotations

import random

N_BOOT = 2000
SEED = 20260602


def cohen_kappa_value(coded: list[tuple[str, str]]) -> float | None:
    """Cohen's kappa from ``(a, b)`` coded pairs; ``None`` if no coded cells."""
    if not coded:
        return None
    labels = sorted({a for a, _ in coded} | {b for _, b in coded})
    n = len(coded)
    conf = {a: {b: 0 for b in labels} for a in labels}
    for a, b in coded:
        conf[a][b] += 1
    po = sum(conf[x][x] for x in labels) / n
    marg_a = {a: sum(conf[a].values()) / n for a in labels}
    marg_b = {b: sum(conf[a][b] for a in labels) / n for b in labels}
    pe = sum(marg_a[x] * marg_b[x] for x in labels)
    return 1.0 if pe >= 1.0 else (po - pe) / (1.0 - pe)


def fleiss_kappa_value(rows: list[list[str]]) -> float | None:
    """Fleiss' kappa from rows of per-rater label lists; ``None`` if undefined."""
    coded = [r for r in rows if r and all(x and str(x).strip() for x in r)]
    if not coded:
        return None
    n_raters = len(coded[0])
    if n_raters < 2 or any(len(r) != n_raters for r in coded):
        return None
    labels = sorted({lbl for r in coded for lbl in r})
    n_rows = len(coded)
    total = n_rows * n_raters
    p_j = {lbl: 0 for lbl in labels}
    for r in coded:
        for lbl in r:
            p_j[lbl] += 1
    p_j = {lbl: c / total for lbl, c in p_j.items()}
    p_i = []
    for r in coded:
        counts: dict[str, int] = {}
        for lbl in r:
            counts[lbl] = counts.get(lbl, 0) + 1
        s = sum(v * v for v in counts.values())
        p_i.append((s - n_raters) / (n_raters * (n_raters - 1)))
    p_bar = sum(p_i) / n_rows
    pe_bar = sum(v * v for v in p_j.values())
    return 1.0 if pe_bar >= 1.0 else (p_bar - pe_bar) / (1.0 - pe_bar)


def bootstrap_ci(items: list, stat_fn, n_boot: int = N_BOOT,
                 seed: int = SEED) -> dict | None:
    """Seeded percentile bootstrap 95% CI for ``stat_fn`` over ``items``.

    Resamples ``items`` with replacement ``n_boot`` times, recomputes the
    statistic, and returns the 2.5/97.5 percentiles plus the bootstrap SE.
    Returns ``None`` when there are fewer than two items or the statistic is
    undefined on the full sample (so callers can render an honest dash).
    """
    n = len(items)
    if n < 2 or stat_fn(items) is None:
        return None
    rng = random.Random(seed)
    est: list[float] = []
    for _ in range(n_boot):
        sample = [items[rng.randrange(n)] for _ in range(n)]
        k = stat_fn(sample)
        if k is not None:
            est.append(k)
    if len(est) < 2:
        return None
    est.sort()

    def _pct(p: float) -> float:
        idx = int(round(p * (len(est) - 1)))
        return est[max(0, min(len(est) - 1, idx))]

    mean = sum(est) / len(est)
    var = sum((e - mean) ** 2 for e in est) / (len(est) - 1)
    return {
        "ci_low": round(_pct(0.025), 4),
        "ci_high": round(_pct(0.975), 4),
        "se": round(var ** 0.5, 4),
        "n_boot": len(est),
        "method": f"nonparametric percentile bootstrap, B={n_boot}, seeded",
    }
