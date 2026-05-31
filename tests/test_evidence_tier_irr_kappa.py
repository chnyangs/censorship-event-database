# SPDX-License-Identifier: MIT
"""Regression guards for the evidence-tier IRR scoring helper."""
from __future__ import annotations

import pytest

import compute_evidence_tier_irr_kappa as evidence_irr


def _row(event_id: str, a: str = "", b: str = "") -> dict[str, str]:
    row = {column: "" for column in evidence_irr.REQUIRED_COLUMNS}
    row.update(
        {
            "id": event_id,
            "stratum": "S4",
            "jurisdiction": "CN",
            "trigger_type": "nation_state_block",
            "sample_reason": "test",
            "coder_a_tier_ok": a,
            "coder_b_tier_ok": b,
            "coder_a_section9_clear": a,
            "coder_b_section9_clear": b,
            "coder_a_single_source_ok": a,
            "coder_b_single_source_ok": b,
        }
    )
    return row


def test_cohens_kappa_scores_complete_two_label_sample() -> None:
    stats = evidence_irr.cohens_kappa([("yes", "yes"), ("yes", "no"), ("no", "no")])

    assert stats["n_coded"] == 3
    assert stats["observed_agreement"] == 0.6667
    assert stats["expected_agreement"] == 0.4444
    assert stats["kappa"] == 0.4


def test_incomplete_packet_fails_by_default() -> None:
    rows = [_row("case-a", "yes", "yes"), _row("case-b")]

    with pytest.raises(evidence_irr.PacketError, match="packet is incomplete"):
        evidence_irr.build_report(rows)


def test_incomplete_packet_can_be_summarized_without_completion_claim() -> None:
    rows = [_row("case-a", "yes", "yes"), _row("case-b")]

    report = evidence_irr.build_report(rows, allow_incomplete=True)

    assert report["status"] == "incomplete"
    assert report["coder_provenance"]["mode"] == "independent_human_pending"
    assert report["variables"]["tier_ok"]["n_coded"] == 1
    assert report["variables"]["tier_ok"]["n_incomplete"] == 1


def test_invalid_label_fails_closed() -> None:
    rows = [_row("case-a", "maybe", "yes")]

    with pytest.raises(evidence_irr.PacketError, match="expected one of"):
        evidence_irr.build_report(rows, allow_incomplete=True)
