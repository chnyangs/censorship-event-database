# SPDX-License-Identifier: MIT
"""Evidence-chain rendering regressions."""
from __future__ import annotations

import pytest

import render_evidence_chain


def test_related_draft_events_do_not_render_dead_links(monkeypatch):
    monkeypatch.setattr(
        render_evidence_chain,
        "_event_status_by_slug",
        lambda: {"admitted-related": "admitted", "draft-related": "draft"},
    )
    event = {
        "id": "subject",
        "status": "admitted",
        "schema_version": "0.2.0",
        "research_stratum": "S3_doj_sec_cftc_fiod",
        "empirical_shape": "null_event",
        "admission_tier": "null_case",
        "last_verified": "2026-04-22",
        "trigger": {"type": "sec_action", "actor": "US_SEC", "timestamp": "2024-04-10"},
        "target": {"kind": "entity", "chains": []},
        "coverage": [],
        "observations": [],
        "sources": [],
        "related_events": ["admitted-related", "draft-related"],
    }

    rendered = render_evidence_chain.render_event_evidence_chain(event, {})

    assert "[`admitted-related`](./admitted-related.md)" in rendered
    assert "[`draft-related`](./draft-related.md)" not in rendered
    assert "`draft-related` (draft; no rendered admitted-chain link)" in rendered


def test_prepare_output_dir_refuses_existing_unmarked_dir(tmp_path):
    out = tmp_path / "docs"
    out.mkdir()
    keep = out / "keep.md"
    keep.write_text("do not delete")

    with pytest.raises(SystemExit, match="existing unmarked"):
        render_evidence_chain.prepare_output_dir(out)

    assert keep.exists()
