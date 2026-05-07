# SPDX-License-Identifier: MIT
"""Regression guards for the L3 provider denominator census."""
from __future__ import annotations

from build_l3_provider_census import build_rows


def test_l3_provider_census_emits_provider_event_rows():
    frame = {
        "event_windows": {"event-a": {}, "event-b": {}},
        "providers": [
            {
                "provider_id": "flashbots_rpc_endpoint",
                "provider_name": "Flashbots",
                "surface_type": "public_git_filter_file",
                "public_endpoint": "https://rpc.flashbots.net",
                "public_replay_possible": "partial_git_history",
                "event_windows": {
                    "event-a": {
                        "docs_bracketed": True,
                        "git_filter_file": True,
                        "event_specific_artifact": True,
                        "artifact_ref": "analysis/operator_census/README.md",
                        "denominator_class": "named_partial_only_no_conditional_rate",
                        "rate_eligible": False,
                        "denominator_reason": "Named artifact only.",
                    }
                },
            }
        ],
    }

    rows = build_rows(frame)

    assert len(rows) == 2
    assert rows[0]["event_id"] == "event-a"
    assert rows[0]["event_specific_artifact"] is True
    assert rows[0]["rate_eligible"] is False
    assert rows[0]["denominator_class"] == "named_partial_only_no_conditional_rate"
    assert rows[1]["event_id"] == "event-b"
    assert rows[1]["denominator_class"] == "observability_gap"
