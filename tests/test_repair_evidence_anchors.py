# SPDX-License-Identifier: MIT
"""Regression tests for pre-human evidence-anchor repair helpers."""
from __future__ import annotations

from repair_evidence_anchors import has_replayable_anchor, missing_anchor_urls


def test_missing_anchor_urls_collects_trigger_and_observation_urls_without_anchors():
    event = {
        "trigger": {
            "citation": [
                {"url": "https://example.test/needs-trigger"},
                {
                    "url": "https://example.test/has-trigger",
                    "body_hash": "sha256:" + "a" * 64,
                    "body_path": "sources/http_captures/event/source.html",
                },
            ]
        },
        "observations": [
            {
                "sources": [
                    {"type": "primary_legal", "url": "https://example.test/needs-source"},
                    {"type": "primary_onchain", "url": "https://example.test/onchain"},
                    {
                        "type": "primary_corporate",
                        "url": "https://example.test/has-source",
                        "wayback": "https://web.archive.org/web/20240101000000/https://example.test/has-source",
                    },
                ]
            }
        ],
    }

    assert missing_anchor_urls(event) == [
        "https://example.test/needs-source",
        "https://example.test/needs-trigger",
    ]


def test_replayable_anchor_accepts_local_body_wayback_query_measurement_or_tx():
    assert has_replayable_anchor({"body_hash": "sha256:" + "a" * 64, "body_path": "sources/a.html"})
    assert has_replayable_anchor({"wayback": "https://web.archive.org/web/1/https://example.test"})
    assert has_replayable_anchor({"query_hash": "sha256:" + "b" * 64})
    assert has_replayable_anchor({"measurement_ids": ["m1"]})
    assert has_replayable_anchor({"tx_hash": "0xabc"})
    assert not has_replayable_anchor({"url": "https://example.test"})
