# SPDX-License-Identifier: MIT
"""Regression guards for source admissibility checks."""
from __future__ import annotations

import yaml

from validate import EventValidator, ValidationResult, VOCAB_PATH


def _validator() -> EventValidator:
    return EventValidator(yaml.safe_load(VOCAB_PATH.read_text()))


def _result() -> ValidationResult:
    return ValidationResult(path=VOCAB_PATH)


def test_primary_onchain_rejects_truncated_tx_hash():
    result = _result()
    _validator()._validate_sources(
        0,
        "asset_onchain",
        [{"type": "primary_onchain", "tx_hash": "075d10048c048e755d1d"}],
        result,
        "admitted",
    )

    assert any("tx_hash" in error for error in result.errors)


def test_primary_onchain_rejects_zero_block_anchor():
    result = _result()
    _validator()._validate_sources(
        0,
        "asset_onchain",
        [{"type": "primary_onchain", "tx_hash": "0x" + "a" * 64, "block": 0}],
        result,
        "admitted",
    )

    assert any("block must be a positive integer" in error for error in result.errors)


def test_note_only_semi_primary_does_not_satisfy_admission():
    result = _result()
    _validator()._validate_sources(
        0,
        "l4_frontend",
        [
            {"type": "semi_primary_wayback", "note": "Wayback showed this."},
            {"type": "semi_primary_wayback", "note": "Another note."},
        ],
        result,
        "admitted",
    )

    assert any("Free-form notes alone" in error for error in result.errors)


def test_observed_change_rejects_none_attribution():
    result = _result()
    event = {
        "status": "admitted",
        "empirical_shape": "comparison",
        "trigger": {"timestamp": "2024-01-01T00:00:00Z"},
        "coverage": [{"layer": layer, "status": "not_applicable"} for layer in _validator().layers],
        "observations": [
            {
                "layer": "l4_frontend",
                "actor": "frontend:test",
                "event": "state_changed",
                "observation_kind": "observed_change",
                "attribution": "none",
                "timestamp": "2024-01-01T00:00:00Z",
                "precision": "day",
                "sources": [
                    {
                        "type": "primary_corporate",
                        "url": "https://example.com",
                        "body_hash": "sha256:" + "a" * 64,
                        "body_path": "sources/http_captures/example.html",
                    }
                ],
            }
        ],
    }
    for entry in event["coverage"]:
        if entry["layer"] == "l4_frontend":
            entry["status"] = "measured"

    _validator()._validate_observations(event, result)

    assert any("observed_change should use attribution" in error for error in result.errors)


def test_coverage_rejects_unknown_provider_scope():
    result = _result()
    _validator()._validate_coverage(
        [
            {"layer": "l0_network", "status": "not_applicable"},
            {"layer": "l1_consensus", "status": "not_applicable"},
            {"layer": "l3_rpc", "status": "partially_measured", "provider_scope": "private_guess"},
            {"layer": "l4_frontend", "status": "not_applicable"},
            {"layer": "asset_onchain", "status": "not_applicable"},
            {"layer": "offramp_cex", "status": "not_applicable"},
        ],
        result,
    )

    assert any("provider_scope" in error for error in result.errors)


def test_trigger_archive_anchor_rejects_invalid_wayback_url():
    result = _result()
    _validator()._validate_trigger(
        {
            "type": "sec_action",
            "actor": "US_SEC",
            "timestamp": "2024-01-01T00:00:00Z",
            "timestamp_precision": "day",
            "citation": [{"type": "primary_legal", "wayback": "not-a-url"}],
        },
        result,
    )

    assert any("wayback must be a valid URL" in error for error in result.errors)


def test_observation_source_rejects_invalid_wayback_url():
    result = _result()
    _validator()._validate_sources(
        0,
        "l4_frontend",
        [
            {
                "type": "primary_corporate",
                "url": "https://example.com/source",
                "wayback": "not-a-url",
            }
        ],
        result,
        "admitted",
    )

    assert any("sources[0].wayback must be a valid URL" in error for error in result.errors)


def test_blank_measurement_ids_do_not_satisfy_semi_primary_admission():
    result = _result()
    _validator()._validate_sources(
        0,
        "l4_frontend",
        [
            {"type": "semi_primary_measurement", "measurement_ids": [""]},
            {"type": "semi_primary_measurement", "measurement_ids": ["   "]},
        ],
        result,
        "admitted",
    )

    assert any("measurement_ids" in error for error in result.errors)


def test_blank_measurement_ids_do_not_anchor_observed_no_change():
    result = _result()
    event = {
        "status": "admitted",
        "empirical_shape": "null_event",
        "trigger": {"timestamp": "2024-01-01T00:00:00Z"},
        "coverage": [{"layer": layer, "status": "not_applicable"} for layer in _validator().layers],
        "observations": [
            {
                "layer": "l4_frontend",
                "actor": "frontend:test",
                "event": "state_stayed_up",
                "observation_kind": "observed_no_change",
                "attribution": "none",
                "window": [
                    "2024-01-01T00:00:00Z",
                    "2024-01-02T00:00:00Z",
                ],
                "sources": [
                    {"type": "semi_primary_measurement", "measurement_ids": [""]},
                    {"type": "semi_primary_measurement", "measurement_ids": ["also-valid"]},
                ],
            }
        ],
    }
    for entry in event["coverage"]:
        if entry["layer"] == "l4_frontend":
            entry["status"] = "measured"

    _validator()._validate_observations(event, result)

    assert any("measurement_ids" in error for error in result.errors)
