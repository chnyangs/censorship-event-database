# SPDX-License-Identifier: MIT
from __future__ import annotations

import pytest

from check_census_gap_registry import check_docs, summarize


def _write(path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def _candidate_tsv() -> str:
    return (
        "id\tdate\tactor\tjurisdiction\tstratum\tlayer\tone_line\tsource_urls\n"
        "in-event\t2024-01-01\ta\tUS\tS5_corporate\tl4_frontend\trow\thttps://example.com/a\n"
        "covered-row\t2024-01-02\tb\tUS\tS5_corporate\tl4_frontend\trow\thttps://example.com/b\n"
        "held-row\t2024-01-03\tc\tUS\tS5_corporate\tasset_onchain\trow\thttps://example.com/c\n"
    )


def _registry_tsv() -> str:
    return (
        "id\tdate\tactor\tjurisdiction\tstratum\tlayer\tone_line\tsource_url_1\tsource_url_2\tconfidence\tin_corpus\n"
        "covered-row\t2024-01-02\tb\tUS\tS5_corporate\tl4_frontend\trow\thttps://example.com/b\t-\tREVIEWED-covered\ttrue\n"
        "held-row\t2024-01-03\tc\tUS\tS5_corporate\tasset_onchain\trow\thttps://example.com/c\t-\tHELD-needs-asset-onchain-txhash\tfalse\n"
    )


def test_census_registry_summary_counts_and_missing_queue(tmp_path):
    _write(tmp_path / "analysis/census_gap_candidates.tsv", _candidate_tsv())
    _write(tmp_path / "analysis/census_gap_registry.tsv", _registry_tsv())
    _write(tmp_path / "events/in-event.yaml", "id: in-event\n")

    summary = summarize(
        tmp_path / "analysis/census_gap_candidates.tsv",
        tmp_path / "analysis/census_gap_registry.tsv",
        tmp_path / "events",
    )

    assert summary.candidate_count == 3
    assert summary.registry_count == 2
    assert summary.covered_count == 1
    assert summary.not_in_corpus_count == 1
    assert summary.held_count == 1
    assert summary.missing_exact_ids == ()


def test_census_registry_fails_on_unreconciled_candidate(tmp_path):
    _write(tmp_path / "analysis/census_gap_candidates.tsv", _candidate_tsv())
    _write(tmp_path / "analysis/census_gap_registry.tsv", _registry_tsv())

    summary = summarize(
        tmp_path / "analysis/census_gap_candidates.tsv",
        tmp_path / "analysis/census_gap_registry.tsv",
        tmp_path / "events",
    )

    assert summary.missing_exact_ids == ("in-event",)


def test_census_registry_rejects_stale_doc_counts(tmp_path):
    _write(tmp_path / "analysis/census_gap_candidates.tsv", _candidate_tsv())
    _write(tmp_path / "analysis/census_gap_registry.tsv", _registry_tsv())
    _write(tmp_path / "events/in-event.yaml", "id: in-event\n")
    summary = summarize(
        tmp_path / "analysis/census_gap_candidates.tsv",
        tmp_path / "analysis/census_gap_registry.tsv",
        tmp_path / "events",
    )
    next_steps = tmp_path / "analysis/NEXT_STEPS.md"
    state = tmp_path / "analysis/STATE_OF_CORPUS_2026_05_31.md"
    _write(
        next_steps,
        (
            "`census_gap_registry.tsv` has 99 verified+scope-tagged rows. "
            "Registry reconciliation on 2026-05-31 found 1 already covered. "
            "Of the remaining 1 `in_corpus=false` rows, 0 are reviewed and 1 are explicit `HELD-needs-*`. "
            "Exact-id remaining queue: 0 candidate rows not yet in events or registry."
        ),
    )
    _write(
        state,
        (
            "semantic-covered slug mismatches: 2 verified+scope-tagged registry rows, 1 covered "
            "by corpus. Of the remaining 1 `in_corpus=false` rows, 0 are reviewed and "
            "1 are explicit held evidence-floor rows; 0 exact-id candidate rows remain."
        ),
    )

    with pytest.raises(ValueError, match="NEXT_STEPS registry_count=99"):
        check_docs(summary, next_steps, state)


def test_census_registry_accepts_current_doc_counts(tmp_path):
    _write(tmp_path / "analysis/census_gap_candidates.tsv", _candidate_tsv())
    _write(tmp_path / "analysis/census_gap_registry.tsv", _registry_tsv())
    _write(tmp_path / "events/in-event.yaml", "id: in-event\n")
    summary = summarize(
        tmp_path / "analysis/census_gap_candidates.tsv",
        tmp_path / "analysis/census_gap_registry.tsv",
        tmp_path / "events",
    )
    next_steps = tmp_path / "analysis/NEXT_STEPS.md"
    state = tmp_path / "analysis/STATE_OF_CORPUS_2026_05_31.md"
    _write(
        next_steps,
        (
            "`census_gap_registry.tsv` has 2 verified+scope-tagged rows. "
            "Registry reconciliation on 2026-05-31 found 1 already covered. "
            "Of the remaining 1 `in_corpus=false` rows, 0 are reviewed and 1 are explicit `HELD-needs-*`. "
            "Exact-id remaining queue: 0 candidate rows not yet in events or registry."
        ),
    )
    _write(
        state,
        (
            "semantic-covered slug mismatches: 2 verified+scope-tagged registry rows, 1 covered "
            "by corpus. Of the remaining 1 `in_corpus=false` rows, 0 are reviewed and "
            "1 are explicit held evidence-floor rows; 0 exact-id candidate rows remain."
        ),
    )

    check_docs(summary, next_steps, state)
