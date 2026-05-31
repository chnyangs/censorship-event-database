# SPDX-License-Identifier: MIT
"""Regression guards for review-report readiness scoring."""
from __future__ import annotations

from copy import deepcopy

from review_report import summarize_case


def _event() -> dict:
    return {
        "id": "mixed-trigger-case",
        "status": "draft",
        "research_stratum": "S3_doj_sec_cftc_fiod",
        "empirical_shape": "comparison",
        "admission_tier": "empirical_case",
        "trigger": {
            "citation": [
                {"type": "primary_legal"},
                {"type": "semi_primary_wayback"},
            ],
        },
        "target": {
            "kind": "address_set",
            "enumeration": "complete",
            "addresses": ["0x0000000000000000000000000000000000000001"],
        },
        "coverage": [
            {"layer": "asset_onchain", "status": "measured"},
            {"layer": "l0_network", "status": "not_applicable"},
        ],
        "observations": [
            {
                "layer": "asset_onchain",
                "observation_kind": "observed_change",
                "attribution": "direct",
                "sources": [{"type": "primary_onchain"}],
            }
        ],
    }


def test_review_report_treats_mixed_primary_trigger_citations_as_reliable():
    case = summarize_case(_event())

    assert case["scores"]["trigger_reliability"] == "high"
    assert "Tighten target enumeration or target scope before treating the trigger as settled." not in case["blockers"]
    assert "candidate_for_admission" == case["overall_readiness"]


def test_review_report_separates_missing_primary_trigger_from_target_scope():
    event = deepcopy(_event())
    event["trigger"]["citation"] = [{"type": "semi_primary_wayback"}]

    case = summarize_case(event)

    assert case["scores"]["trigger_reliability"] == "medium"
    assert "Add a primary trigger source before treating the trigger as settled." in case["blockers"]
    assert "Tighten target enumeration or target scope before treating the trigger as settled." not in case["blockers"]
