# SPDX-License-Identifier: MIT
"""Lock the 6-class archetype rule and the trigger_is_action coincidence rule.

These tests fail-closed when somebody reintroduces a prior review-flagged bug:

- the rule-based classifier must remain deterministic (6 classes, priority-
  ordered, no clustering),
- `trigger_is_action` must require BOTH `trigger.type = corporate_policy_change`
  AND `|time_to_first_change_hours| <= 1h`, so that corporate retreats with
  real measured latency (e.g. Coinbase India exit at 72h) do NOT get silenced
  in Panel C.
"""
from __future__ import annotations

from datetime import datetime, timezone

import pytest

from assign_archetypes import (
    TRIGGER_IS_ACTION_MAX_DELTA_H,
    classify,
    derive_event,
    latency_regime,
)


# ---------- classify: priority-ordered archetype rules ----------

def test_classify_null_event():
    assert classify(set()) == "null_event"


def test_classify_multi_layer_two():
    assert classify({"asset_onchain", "l4_frontend"}) == "multi_layer"


def test_classify_multi_layer_five():
    assert classify({
        "asset_onchain", "l1_consensus", "l3_rpc", "l4_frontend", "offramp_cex"
    }) == "multi_layer"


def test_classify_asset_only():
    assert classify({"asset_onchain"}) == "asset_only"


def test_classify_frontend_only():
    assert classify({"l4_frontend"}) == "frontend_only"


def test_classify_cex_only():
    assert classify({"offramp_cex"}) == "cex_only"


@pytest.mark.parametrize("layer", ["l0_network", "l1_consensus", "l3_rpc"])
def test_classify_other_single_layer_safety_class(layer):
    """L0 / L1 / L3 singletons land in the safety class."""
    assert classify({layer}) == "other_single_layer"


# ---------- latency bands ----------

def test_latency_none():
    assert latency_regime(None) == "none"


@pytest.mark.parametrize("h,expected", [
    (0.0, "synchronous"),
    (1.0, "synchronous"),   # inclusive right on 1h
    (1.0001, "acute"),
    (30.0, "acute"),         # inclusive right on 30h
    (30.01, "delayed"),
    (720.0, "delayed"),       # inclusive right on 30d
    (720.01, "lagged"),
    (99999.0, "lagged"),
])
def test_latency_bands_are_inclusive_right(h, expected):
    assert latency_regime(h) == expected


# ---------- trigger_is_action coincidence rule ----------

def _event(trigger_type: str, obs_delta_h: float | None) -> dict:
    """Fabricate a minimal event YAML dict with one observed_change obs."""
    trigger_ts = datetime(2022, 8, 8, 14, 30, tzinfo=timezone.utc)
    ev = {
        "id": "test-synth",
        "trigger": {
            "type": trigger_type,
            "timestamp": trigger_ts.isoformat(),
        },
        "observations": [],
    }
    if obs_delta_h is not None:
        ev["observations"].append({
            "layer": "asset_onchain",
            "observation_kind": "observed_change",
            "attribution": "direct",
            "delta_hours": obs_delta_h,
        })
    return ev


def test_trigger_is_action_fires_on_coincident_policy_change():
    """Circle / Tether / Uniswap pattern: corporate_policy_change with t≈0."""
    row = derive_event(_event("corporate_policy_change", 0.0))
    assert row["trigger_is_action"] is True


def test_trigger_is_action_fires_when_delta_exactly_at_tolerance():
    """Boundary: |delta| == TRIGGER_IS_ACTION_MAX_DELTA_H is still true."""
    row = derive_event(_event("corporate_policy_change", TRIGGER_IS_ACTION_MAX_DELTA_H))
    assert row["trigger_is_action"] is True


def test_trigger_is_action_suppressed_when_delta_exceeds_tolerance():
    """Coinbase-India pattern: corporate_policy_change with 72h measured delta.

    MUST be classified as a real latency observation (trigger_is_action=false)
    so it enters Panel B of Table 4, not Panel C. This regression guard locks
    the 2026-04-24 fix to the classifier.
    """
    row = derive_event(_event("corporate_policy_change", 72.0))
    assert row["trigger_is_action"] is False


def test_trigger_is_action_suppressed_for_non_policy_trigger():
    """Non-`corporate_policy_change` triggers never fire the flag, even at t=0."""
    row = derive_event(_event("ofac_sdn_designation", 0.0))
    assert row["trigger_is_action"] is False


def test_trigger_is_action_false_when_no_observed_change():
    """A null event (no observed_change rows) cannot be trigger_is_action."""
    row = derive_event(_event("corporate_policy_change", None))
    assert row["trigger_is_action"] is False
