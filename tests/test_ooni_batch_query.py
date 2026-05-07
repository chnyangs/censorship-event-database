# SPDX-License-Identifier: MIT
"""Regression guards for OONI query-record normalization."""
from __future__ import annotations

from ooni_batch_query import build_query_params, normalize_query_records, output_file_name, query_hash


def test_legacy_ooni_domain_mapping_expands_to_scoped_records():
    records = normalize_query_records(
        {
            "example.com": {
                "slugs": ["event-a", "event-b"],
                "since": "2024-01-01",
                "until": "2024-02-01",
            }
        }
    )

    assert [record["event_id"] for record in records] == ["event-a", "event-b"]
    assert {record["input_url"] for record in records} == {"https://example.com/"}
    assert {record["domain"] for record in records} == {"example.com"}


def test_list_ooni_query_records_expand_url_and_probe_cells():
    records = normalize_query_records(
        [
            {
                "event_id": "event-a",
                "domain": "example.org",
                "url_variants": ["https://example.org/", "http://example.org/"],
                "probe_ccs": ["US", "TR"],
                "since": "2024-01-01",
                "until": "2024-01-31",
            }
        ]
    )

    assert len(records) == 4
    hashes = {query_hash(build_query_params(record)) for record in records}
    assert len(hashes) == 4
    filename = output_file_name(records[0], next(iter(hashes)))
    assert filename.startswith("example.org__")
    assert filename.endswith("__ooni.json")
