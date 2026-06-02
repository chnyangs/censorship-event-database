"""Tests for the shared bootstrap-CI helper used by both IRR kappa scripts."""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from _kappa_ci import bootstrap_ci, cohen_kappa_value, fleiss_kappa_value  # noqa: E402


def test_cohen_kappa_value_matches_known() -> None:
    # Same 3-row sample asserted in test_evidence_tier_irr_kappa.py.
    coded = [("yes", "yes"), ("yes", "no"), ("no", "no")]
    assert round(cohen_kappa_value(coded), 4) == 0.4


def test_cohen_kappa_value_none_when_empty() -> None:
    assert cohen_kappa_value([]) is None


def test_bootstrap_ci_is_deterministic() -> None:
    coded = ([("direct", "direct")] * 14
             + [("direct", "plausible")] * 3
             + [("plausible", "plausible")] * 3)
    first = bootstrap_ci(coded, cohen_kappa_value)
    second = bootstrap_ci(coded, cohen_kappa_value)
    assert first == second
    assert first is not None
    assert first["ci_low"] <= first["ci_high"]


def test_bootstrap_ci_none_for_singleton() -> None:
    assert bootstrap_ci([("yes", "yes")], cohen_kappa_value) is None


def test_bootstrap_ci_degenerate_when_perfect_agreement() -> None:
    coded = [("a", "a")] * 10 + [("b", "b")] * 10
    ci = bootstrap_ci(coded, cohen_kappa_value)
    assert ci is not None
    assert ci["ci_low"] == 1.0 and ci["ci_high"] == 1.0


def test_fleiss_kappa_value_perfect() -> None:
    rows = [["x", "x", "x"], ["y", "y", "y"]]
    assert fleiss_kappa_value(rows) == 1.0


def test_fleiss_kappa_value_none_single_rater() -> None:
    assert fleiss_kappa_value([["x"], ["y"]]) is None
