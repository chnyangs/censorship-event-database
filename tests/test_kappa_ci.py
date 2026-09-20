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


def test_constant_agreement_is_not_defined_kappa() -> None:
    coded = [("yes", "yes")] * 20
    assert cohen_kappa_value(coded) is None
    assert fleiss_kappa_value([["yes", "yes", "yes"]] * 20) is None
    assert bootstrap_ci(coded, cohen_kappa_value) is None


def test_bootstrap_reports_undefined_resamples() -> None:
    ci = bootstrap_ci([("a", "a"), ("b", "b")], cohen_kappa_value, n_boot=100)
    assert ci is not None
    assert ci["n_boot_undefined"] > 0
    assert ci["n_boot"] + ci["n_boot_undefined"] == 100
    assert ci["conditional_on_defined_resamples"] is True


def test_event_bootstrap_preserves_all_cells_together() -> None:
    items = [("a", 0)] * 2 + [("b", 1)] * 3
    seen = []

    def stat(sample):
        seen.append(sample)
        return sum(value for _, value in sample) / len(sample)

    ci = bootstrap_ci(items, stat, n_boot=30, cluster_ids=[event for event, _ in items])
    assert ci["resampling_unit"] == "event"
    assert ci["n_units"] == 2
    for sample in seen:
        assert sum(event == "a" for event, _ in sample) % 2 == 0
        assert sum(event == "b" for event, _ in sample) % 3 == 0
    assert bootstrap_ci(items, stat, cluster_ids=["one-event"] * 5) is None


def test_nonfinite_statistics_do_not_produce_a_ci() -> None:
    assert bootstrap_ci([1, 2], lambda _: float("nan")) is None


def test_irr_summary_uses_event_clusters_and_undefined_kappa() -> None:
    from compute_irr_kappa import _cohens_kappa, _fleiss_kappa

    constant = _cohens_kappa([("event-a", "L1", "yes", "yes")] * 5)
    assert constant["observed_agreement"] == 1
    assert constant["kappa"] is None
    assert "undefined" in constant["reason"]
    varied = _cohens_kappa([("event-a", "L1", "yes", "yes"),
                            ("event-a", "L2", "yes", "yes"),
                            ("event-b", "L1", "no", "no")])
    assert varied["n_events"] == 2
    assert varied["kappa_ci"]["resampling_unit"] == "event"
    assert _fleiss_kappa([["yes", "yes"]] * 3)["fleiss_kappa"] is None
    assert _fleiss_kappa([["yes"], ["no"]])["fleiss_kappa"] is None
