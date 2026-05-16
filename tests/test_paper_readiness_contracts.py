# SPDX-License-Identifier: MIT
"""Regression guards for release-surface readiness contracts."""
from __future__ import annotations

import check_paper_readiness


def test_unclassified_unarchived_trigger_citation_fails_strict_repro() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    events = [
        {
            "id": "event-a",
            "trigger": {
                "citation": [
                    {"type": "primary_legal", "wayback": "https://web.archive.org/web/1/https://example.com"},
                    {"type": "primary_legal", "url": "https://example.com/live"},
                ]
            },
        }
    ]

    check_paper_readiness.check_trigger_citation_archiving(
        events,
        errors,
        warnings,
        strict_repro=True,
    )

    assert errors
    assert "trigger.citation[1]" in errors[0]
    assert not warnings


def test_contextual_unarchived_trigger_citation_passes_with_archived_sibling() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    events = [
        {
            "id": "event-a",
            "trigger": {
                "citation": [
                    {"type": "primary_legal", "wayback": "https://web.archive.org/web/1/https://example.com"},
                    {
                        "type": "primary_legal",
                        "url": "https://example.com/live",
                        "evidence_use": "contextual_unarchived",
                    },
                ]
            },
        }
    ]

    check_paper_readiness.check_trigger_citation_archiving(
        events,
        errors,
        warnings,
        strict_repro=True,
    )

    assert not errors
    assert not warnings


def test_dataset_surface_contract_rejects_bad_paper_corpus_count() -> None:
    errors: list[str] = []
    meta = {
        "event_count": 2,
        "registry_event_count": 2,
        "paper_corpus_statuses": ["admitted"],
        "paper_corpus_event_count": 2,
        "release_surface_scope": "all_event_yaml_records",
        "counts_by_status": {"admitted": 1, "rejected": 1},
    }
    rows = [
        {"id": "admitted-a", "status": "admitted", "paper_corpus_included": "true"},
        {"id": "rejected-a", "status": "rejected", "paper_corpus_included": "false"},
    ]

    check_paper_readiness.check_dataset_surface_contract(meta, rows, [{}, {}], errors)

    assert any("paper_corpus_event_count" in error for error in errors)


def test_dataset_surface_contract_rejects_bad_csv_inclusion_flag() -> None:
    errors: list[str] = []
    meta = {
        "event_count": 2,
        "registry_event_count": 2,
        "paper_corpus_statuses": ["admitted"],
        "paper_corpus_event_count": 1,
        "release_surface_scope": "all_event_yaml_records",
        "counts_by_status": {"admitted": 1, "rejected": 1},
    }
    rows = [
        {"id": "admitted-a", "status": "admitted", "paper_corpus_included": "false"},
        {"id": "rejected-a", "status": "rejected", "paper_corpus_included": "false"},
    ]

    check_paper_readiness.check_dataset_surface_contract(meta, rows, [{}, {}], errors)

    assert any("paper_corpus_included" in error for error in errors)
