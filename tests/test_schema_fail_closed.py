# SPDX-License-Identifier: MIT
"""JSON Schema should reject validator-critical bypass shapes."""
from __future__ import annotations

import json

import jsonschema


def _schema() -> dict:
    with open("schema/event.schema.json") as f:
        return json.load(f)


def _validator(def_name: str) -> jsonschema.Draft202012Validator:
    schema = _schema()
    wrapped = {
        "$schema": schema["$schema"],
        "$defs": schema["$defs"],
        "$ref": f"#/$defs/{def_name}",
    }
    return jsonschema.Draft202012Validator(
        wrapped,
        format_checker=jsonschema.FormatChecker(),
    )


def _errors(def_name: str, value: dict) -> list[jsonschema.ValidationError]:
    return list(_validator(def_name).iter_errors(value))


def test_schema_rejects_note_only_semi_primary_source():
    source = {"type": "semi_primary_measurement", "note": "trust me"}
    assert _errors("source", source)


def test_schema_rejects_primary_onchain_without_tx_hash():
    source = {"type": "primary_onchain", "note": "missing tx"}
    assert _errors("source", source)


def test_schema_rejects_non_positive_onchain_block():
    source = {"type": "primary_onchain", "tx_hash": "0x" + "a" * 64, "block": 0}
    assert _errors("source", source)


def test_schema_rejects_whitespace_measurement_ids():
    source = {"type": "semi_primary_measurement", "measurement_ids": ["   "]}
    assert _errors("source", source)


def test_schema_rejects_invalid_source_wayback_url():
    source = {
        "type": "primary_corporate",
        "url": "https://example.com/source",
        "wayback": "not-a-url",
    }
    assert _errors("source", source)


def test_schema_rejects_hostless_source_wayback_url():
    source = {
        "type": "primary_corporate",
        "url": "https://example.com/source",
        "wayback": "https:///snapshot",
    }
    assert _errors("source", source)


def test_schema_rejects_non_http_source_url():
    source = {
        "type": "primary_corporate",
        "url": "ftp://example.com/source",
        "wayback": "https://web.archive.org/web/20240101000000/https://example.com/source",
    }
    assert _errors("source", source)


def test_schema_rejects_invalid_citation_wayback_url():
    citation = {"type": "primary_legal", "wayback": "not-a-url"}
    assert _errors("citation", citation)


def test_schema_rejects_hostless_citation_wayback_url():
    citation = {"type": "primary_legal", "wayback": "https:///snapshot"}
    assert _errors("citation", citation)


def test_schema_rejects_observed_change_with_none_attribution():
    observation = {
        "layer": "l4_frontend",
        "actor": "frontend:test",
        "event": "test_change",
        "observation_kind": "observed_change",
        "attribution": "none",
        "sources": [
            {
                "type": "primary_corporate",
                "url": "https://example.com/source",
                "wayback": "https://web.archive.org/web/20240101000000/https://example.com/source",
            }
        ],
    }
    assert _errors("observation", observation)
