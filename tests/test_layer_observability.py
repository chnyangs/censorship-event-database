# SPDX-License-Identifier: MIT
"""Lock the coverage-matched numerator rule (post-2026-04-23 P1 fix).

`changed_given_measured` must be computed as
`changed_under_measured_count / measured_count`, NOT
`changed_count / measured_count`. The old formula inflated the ratio by
counting partially_measured rows in the numerator while the denominator
excluded them. These tests are the regression guard.
"""
from __future__ import annotations

from build_layer_observability import compute_row


def _event(slug: str, cov_status: str, kinds: list[str]) -> dict:
    """Fabricate a minimal event with one layer's coverage + observations."""
    layer = "l4_frontend"
    return {
        "id": slug,
        "coverage": [{"layer": layer, "status": cov_status}],
        "observations": [
            {"layer": layer, "observation_kind": k, "attribution": "direct"}
            for k in kinds
        ],
    }


def _event_with_action(slug: str, cov_status: str, action_id: str) -> dict:
    layer = "asset_onchain"
    return {
        "id": slug,
        "coverage": [{"layer": layer, "status": cov_status}],
        "observations": [
            {
                "layer": layer,
                "observation_kind": "observed_change",
                "attribution": "direct",
                "action_id": action_id,
            }
        ],
    }


def test_measured_changed_contributes_to_both_numerators():
    events = [_event("a", "measured", ["observed_change"])]
    row = compute_row("l4_frontend", events)
    assert row["changed_under_measured_count"] == 1
    assert row["changed_under_measured_or_partial_count"] == 1
    assert row["measured_count"] == 1
    assert row["changed_given_measured"] == 1.0
    assert row["changed_given_measured_or_partial"] == 1.0


def test_partial_changed_counts_for_partial_numerator_only():
    """P1 regression guard: partial-coverage changed row MUST NOT inflate
    `changed_given_measured` — it belongs only in the `_or_partial` numerator."""
    events = [
        _event("a", "measured", ["observed_change"]),
        _event("b", "partially_measured", ["observed_change"]),
    ]
    row = compute_row("l4_frontend", events)
    assert row["changed_under_measured_count"] == 1            # only a
    assert row["changed_under_measured_or_partial_count"] == 2  # a + b
    assert row["measured_count"] == 1
    assert row["partially_measured_count"] == 1
    # measured-only rate: 1/1 = 1.0 (NOT 2/1 = 2.0, which would be the bug)
    assert row["changed_given_measured"] == 1.0
    # combined rate: 2 / 2 = 1.0
    assert row["changed_given_measured_or_partial"] == 1.0


def test_numerator_must_match_denominator_subset():
    """Locks the exact v0.1.0 l1_consensus pattern: 1 measured-changed, 1
    partial-changed, 6 measured total, 1 partial total. Must NOT collapse."""
    events = (
        [_event(f"m{i}", "measured", [])            for i in range(5)]
        + [_event("m5",    "measured", ["observed_change"])]
        + [_event("p0",    "partially_measured", ["observed_change"])]
    )
    row = compute_row("l4_frontend", events)
    assert row["measured_count"] == 6
    assert row["partially_measured_count"] == 1
    assert row["changed_under_measured_count"] == 1
    assert row["changed_under_measured_or_partial_count"] == 2
    assert row["changed_given_measured"] == pytest_approx(1 / 6)
    assert row["changed_given_measured_or_partial"] == pytest_approx(2 / 7)


def test_zero_denominator_renders_as_none():
    """L0-pattern: no measured, no partial, denominator=0 — rate must be None
    so the table renders `—`, NOT 0."""
    events = [
        _event("nm1", "not_measured", []),
        _event("nm2", "not_measured", []),
    ]
    row = compute_row("l4_frontend", events)
    assert row["measured_count"] == 0
    assert row["partially_measured_count"] == 0
    assert row["changed_given_measured"] is None
    assert row["changed_given_measured_or_partial"] is None


def test_not_applicable_excluded_from_applicable_count():
    events = [
        _event("a",  "measured", ["observed_change"]),
        _event("na", "not_applicable", []),
    ]
    row = compute_row("l4_frontend", events)
    assert row["not_applicable_count"] == 1
    assert row["applicable_event_count"] == 1      # excludes not_applicable


def test_duplicate_action_ids_are_deduped_separately_from_event_counts():
    events = [
        _event_with_action("ofac-event", "measured", "shared-tx"),
        _event_with_action("issuer-event", "measured", "shared-tx"),
    ]
    row = compute_row("asset_onchain", events)
    assert row["changed_under_measured_count"] == 2
    assert row["changed_unique_action_count"] == 1
    assert row["duplicated_changed_action_count"] == 1


# Simple tolerant equality to avoid a full pytest-approx import dance.
class _Approx:
    def __init__(self, v, tol=1e-9):
        self.v, self.tol = v, tol
    def __eq__(self, other):
        return abs(other - self.v) < self.tol
    def __repr__(self):
        return f"~{self.v}"


def pytest_approx(v, tol=1e-9):
    return _Approx(v, tol)
