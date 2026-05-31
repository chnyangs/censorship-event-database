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
                {
                    "type": "primary_legal",
                    "wayback": "https://web.archive.org/web/20240101000000/https://example.com/legal",
                },
                {
                    "type": "semi_primary_wayback",
                    "wayback": "https://web.archive.org/web/20240101000000/https://example.com/context",
                },
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
                "sources": [{"type": "primary_onchain", "tx_hash": "0x" + "a" * 64}],
            }
        ],
    }


def _null_event() -> dict:
    return {
        "id": "null-denominator-case",
        "status": "admitted",
        "research_stratum": "S6_supranational",
        "empirical_shape": "null_event",
        "admission_tier": "null_case",
        "trigger": {
            "citation": [
                {
                    "type": "primary_legal",
                    "wayback": "https://web.archive.org/web/20240101000000/https://example.com/legal",
                }
            ],
        },
        "target": {
            "kind": "entity",
            "entity": "supranational_policy_target",
            "enumeration": "subset",
        },
        "coverage": [
            {"layer": "offramp_cex", "status": "measured"},
            {"layer": "l0_network", "status": "not_applicable"},
        ],
        "observations": [
            {
                "layer": "offramp_cex",
                "observation_kind": "observed_no_change",
                "attribution": "none",
                "sources": [
                    {
                        "type": "primary_legal",
                        "wayback": "https://web.archive.org/web/20240101000000/https://example.com/null",
                    }
                ],
            }
        ],
    }


def _anchor_event() -> dict:
    event = deepcopy(_event())
    event["id"] = "anchor-case"
    event["status"] = "admitted"
    event["admission_tier"] = "anchor_case"
    event["coverage"] = [
        {"layer": "asset_onchain", "status": "measured"},
        {"layer": "l4_frontend", "status": "measured"},
        {"layer": "l0_network", "status": "not_applicable"},
    ]
    event["observations"] = [
        {
            "layer": "asset_onchain",
            "observation_kind": "observed_change",
            "attribution": "direct",
            "sources": [{"type": "primary_onchain", "tx_hash": "0x" + "a" * 64}],
        },
        {
            "layer": "l4_frontend",
            "observation_kind": "observed_change",
            "attribution": "direct",
            "sources": [
                {
                    "type": "primary_corporate",
                    "wayback": "https://web.archive.org/web/20240101000000/https://example.com/frontend",
                }
            ],
        },
    ]
    return event


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


def test_review_report_does_not_require_changed_layer_for_null_cases():
    case = summarize_case(_null_event())

    assert case["scores"]["attribution_reliability"] == "high"
    assert "The file does not currently retain a stable changed-layer claim." not in case["blockers"]
    assert case["overall_readiness"] == "release_ready_scoped"


def test_review_report_still_blocks_non_null_cases_without_changed_layers():
    event = _null_event()
    event["empirical_shape"] = "comparison"
    event["admission_tier"] = "empirical_case"

    case = summarize_case(event)

    assert case["scores"]["attribution_reliability"] == "low"
    assert "The file does not currently retain a stable changed-layer claim." in case["blockers"]


def test_review_report_marks_release_ready_anchor_cases_as_paper_anchors():
    case = summarize_case(_anchor_event())

    assert case["overall_readiness"] == "release_ready_complete"
    assert case["paper_use_role"] == "paper_anchor"


def test_review_report_does_not_promote_blocked_anchor_cases_to_paper_anchors():
    event = _anchor_event()
    event["observations"][1]["sources"][0]["evidence_use"] = "contextual_unarchived"

    case = summarize_case(event)

    assert case["overall_readiness"] == "admitted_scope_blocked"
    assert case["paper_use_role"] == "appendix_only"
