# SPDX-License-Identifier: MIT
"""Regression guards for legacy OONI artifact metadata backfill."""
from __future__ import annotations

import json

from backfill_l0_query_metadata import backfill_summary


def test_l0_query_metadata_backfill_writes_query_cell_fields(tmp_path):
    body = tmp_path / "sources" / "l0_datasets" / "event-a" / "example.com__ooni.json"
    body.parent.mkdir(parents=True)
    body.write_text(
        json.dumps(
            {
                "_query_url": (
                    "https://api.ooni.io/api/v1/measurements?"
                    "input=https%3A%2F%2Fexample.com%2F&since=2024-01-01"
                    "&until=2024-02-01&limit=100&test_name=web_connectivity"
                ),
                "metadata": {"count": 0, "next_url": None},
                "results": [],
            }
        )
    )
    summary = tmp_path / "sources" / "l0_datasets" / "_summary.json"
    summary.write_text(
        json.dumps(
            [
                {
                    "slug": "event-a",
                    "domain": "example.com",
                    "since": "2024-01-01",
                    "until": "2024-02-01",
                    "body_path": str(body),
                    "body_hash": "old",
                    "result_count": 0,
                    "query_url": (
                        "https://api.ooni.io/api/v1/measurements?"
                        "input=https%3A%2F%2Fexample.com%2F&since=2024-01-01"
                        "&until=2024-02-01&limit=100&test_name=web_connectivity"
                    ),
                    "error": None,
                }
            ]
        )
    )

    assert backfill_summary(summary) == 1

    raw = json.loads(body.read_text())
    rows = json.loads(summary.read_text())
    assert raw["_query_params"]["input"] == "https://example.com/"
    assert raw["_query_params"]["domain"] == "example.com"
    assert raw["_query_hash"]
    assert raw["_pagination_complete"] is True
    assert rows[0]["input_url"] == "https://example.com/"
    assert rows[0]["probe_cc"] == "*"
    assert rows[0]["query_hash"] == raw["_query_hash"]
    assert rows[0]["body_hash"] != "old"
