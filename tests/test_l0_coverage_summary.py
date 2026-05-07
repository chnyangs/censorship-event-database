# SPDX-License-Identifier: MIT
"""Regression guards for denominator-aware L0 OONI summary artifacts."""
from __future__ import annotations

import json

from build_l0_coverage_summary import build_markdown, build_rows


def test_l0_summary_treats_zero_ooni_results_as_observability_gap(tmp_path):
    body = tmp_path / "sources" / "l0_datasets" / "event-a" / "example.com__ooni.json"
    body.parent.mkdir(parents=True)
    body.write_text(json.dumps({"_query_url": "https://api.ooni.io/q", "metadata": {"count": 0}, "results": []}))
    summary = tmp_path / "sources" / "l0_datasets" / "_summary.json"
    summary.write_text(
        json.dumps(
            [
                {
                    "slug": "event-a",
                    "domain": "example.com",
                    "since": "2024-01-01",
                    "until": "2024-02-01",
                    "body_path": "sources/l0_datasets/event-a/example.com__ooni.json",
                    "body_hash": "abc",
                    "result_count": 0,
                    "query_url": "https://api.ooni.io/q",
                    "error": None,
                }
            ]
        )
    )

    rows = build_rows(summary, tmp_path)

    assert rows[0]["denominator_class"] == "no_ooni_measurements"
    assert rows[0]["rate_reportable"] == "no"
    assert rows[0]["result_count"] == 0


def test_l0_summary_counts_measurement_denominator_fields(tmp_path):
    body = tmp_path / "sources" / "l0_datasets" / "event-b" / "example.org__ooni.json"
    body.parent.mkdir(parents=True)
    body.write_text(
        json.dumps(
            {
                "_query_url": "https://api.ooni.io/q2",
                "metadata": {"count": 2},
                "results": [
                    {
                        "measurement_uid": "m1",
                        "probe_cc": "US",
                        "anomaly": True,
                        "confirmed": False,
                        "failure": None,
                    },
                    {
                        "measurement_uid": "m2",
                        "probe_cc": "TR",
                        "anomaly": False,
                        "confirmed": True,
                        "failure": "dns_nxdomain_error",
                    },
                ],
            }
        )
    )
    summary = tmp_path / "sources" / "l0_datasets" / "_summary.json"
    summary.write_text(
        json.dumps(
            [
                {
                    "slug": "event-b",
                    "domain": "example.org",
                    "since": "2024-01-01",
                    "until": "2024-02-01",
                    "body_path": "sources/l0_datasets/event-b/example.org__ooni.json",
                    "body_hash": "def",
                    "result_count": 2,
                    "query_url": "https://api.ooni.io/q2",
                    "error": None,
                }
            ]
        )
    )

    rows = build_rows(summary, tmp_path)

    assert rows[0]["denominator_class"] == "measurement_denominator"
    assert rows[0]["rate_reportable"] == "yes"
    assert rows[0]["country_count"] == 2
    assert rows[0]["probe_countries"] == "TR,US"
    assert rows[0]["measurement_ids"] == "m1,m2"
    assert rows[0]["anomaly_count"] == 1
    assert rows[0]["confirmed_count"] == 1
    assert rows[0]["failure_count"] == 1


def test_l0_markdown_reports_not_queried_applicable_events():
    rows = [
        {
            "event_id": "event-a",
            "domain": "example.com",
            "denominator_class": "no_ooni_measurements",
        }
    ]

    markdown = build_markdown(rows, applicable_events=["event-a", "event-b"])

    assert "| `queried_no_ooni_measurements` | 1 |" in markdown
    assert "| `not_queried_yet` | 1 |" in markdown
    assert "`event-b`" in markdown
