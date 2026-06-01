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


def test_source_commit_drift_suppressed_when_source_hash_matches() -> None:
    warnings: list[str] = []

    check_paper_readiness.maybe_warn_source_commit_drift(
        label="dataset.meta.json",
        recorded_commit="parent1",
        head="head999",
        recorded_hash="sha256:abc",
        current_hash="sha256:abc",
        warnings=warnings,
        note="source_commit is display metadata only",
    )

    assert not warnings


def test_source_commit_drift_warns_without_matching_source_hash() -> None:
    warnings: list[str] = []

    check_paper_readiness.maybe_warn_source_commit_drift(
        label="dataset.meta.json",
        recorded_commit="parent1",
        head="head999",
        recorded_hash="sha256:abc",
        current_hash="sha256:def",
        warnings=warnings,
        note="source_commit is display metadata only",
    )

    assert warnings == [
        "dataset.meta.json source_commit=parent1 but HEAD=head999; "
        "source_commit is display metadata only"
    ]


def test_table2_l3_prose_rejects_stale_no_denominator_claim() -> None:
    errors: list[str] = []

    check_paper_readiness.check_table2_layer_prose(
        [{"layer": "l3_rpc", "measured_count": "1"}],
        "`l3_rpc` has no measured denominator in this release.",
        errors,
    )

    assert errors == [
        "Table 2 prose says `l3_rpc` has no measured denominator, "
        "but derived/layer_observability.csv reports measured_count=1"
    ]


def test_table2_l3_prose_accepts_matching_measured_claim() -> None:
    errors: list[str] = []

    check_paper_readiness.check_table2_layer_prose(
        [{"layer": "l3_rpc", "measured_count": "1"}],
        "`l3_rpc` has 1 measured denominator event(s) in this snapshot.",
        errors,
    )

    assert not errors
