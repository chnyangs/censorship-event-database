# SPDX-License-Identifier: MIT
"""v0.3 public YAML surface checks."""
from __future__ import annotations

import yaml

from validate import EventValidator


LAYERS = [
    "l0_network",
    "l1_consensus",
    "l3_rpc",
    "l4_frontend",
    "asset_onchain",
    "offramp_cex",
]


def _vocab() -> dict:
    return yaml.safe_load(open("schema/controlled_vocab.yaml"))


def _draft_event(**overrides):
    event = {
        "id": "test-event",
        "schema_version": "0.2.0",
        "codebook_version": "1.0.0",
        "status": "draft",
        "primary_source_verified": False,
        "research_stratum": "S1_ofac_sdn",
        "temporal_tier": "comparable_main_2017_present",
        "analysis_use": "comparable_analysis",
        "empirical_shape": "null_event",
        "admission_tier": "null_case",
        "origin": "agent_draft",
        "trigger": {
            "type": "ofac_sdn_designation",
            "actor": "US_OFAC",
            "timestamp": "2024-01-01T00:00:00Z",
            "timestamp_precision": "day",
            "citation": [
                {
                    "type": "primary_legal",
                    "url": "https://example.test/source",
                    "wayback": "https://web.archive.org/web/20240101000000/https://example.test/source",
                }
            ],
        },
        "target": {"kind": "entity", "enumeration": "pending"},
        "jurisdiction": ["US"],
        "coverage": [{"layer": layer, "status": "not_measured"} for layer in LAYERS],
        "observations": [],
    }
    event.update(overrides)
    return event


def test_validator_rejects_internal_reextraction_flag_in_yaml(tmp_path):
    validator = EventValidator(_vocab())
    event = _draft_event(requires_v0_3_reextraction=True)

    result = validator.validate_event(tmp_path / "event.yaml", event)

    assert any("requires_v0_3_reextraction is an internal" in error for error in result.errors)


def test_validator_rejects_agent_draft_primary_source_verified_true(tmp_path):
    validator = EventValidator(_vocab())
    event = _draft_event(primary_source_verified=True)

    result = validator.validate_event(tmp_path / "event.yaml", event)

    assert any("origin=agent_draft cannot declare primary_source_verified=true" in error for error in result.errors)
