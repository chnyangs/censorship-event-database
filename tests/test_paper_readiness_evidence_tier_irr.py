# SPDX-License-Identifier: MIT
"""Regression guards for the evidence-tier IRR release gate."""
from __future__ import annotations

import json

import check_paper_readiness


ATTESTED_EVENT = {"id": "case-a", "evidence_tier": "attested_secondary"}


def _complete_report(kappa: float = 0.75) -> dict:
    variables = {}
    for variable in check_paper_readiness.EVIDENCE_TIER_IRR_VARIABLES:
        variables[variable] = {
            "kappa": kappa,
            "n_coded": 15,
            "n_total": 15,
            "n_incomplete": 0,
            "observed_agreement": 0.9,
            "expected_agreement": 0.6,
        }
    return {
        "status": "complete",
        "n_events": 15,
        "coder_provenance": {"mode": "independent_human"},
        "variables": variables,
    }


def test_missing_evidence_tier_irr_report_warns_for_working_snapshot(tmp_path) -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.check_evidence_tier_irr(
        events=[ATTESTED_EVENT],
        report_path=tmp_path / "missing.json",
        strict_reliability=False,
        errors=errors,
        warnings=warnings,
    )

    assert not errors
    assert warnings
    assert "attested_secondary" in warnings[0]


def test_missing_evidence_tier_irr_report_errors_under_strict_reliability(tmp_path) -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.check_evidence_tier_irr(
        events=[ATTESTED_EVENT],
        report_path=tmp_path / "missing.json",
        strict_reliability=True,
        errors=errors,
        warnings=warnings,
    )

    assert errors
    assert not warnings
    assert "evidence-tier IRR report is missing" in errors[0]


def test_incomplete_evidence_tier_irr_report_fails_strict(tmp_path) -> None:
    report_path = tmp_path / "evidence_tier_irr.json"
    report = _complete_report()
    report["status"] = "incomplete"
    report["coder_provenance"] = {"mode": "independent_human_pending"}
    report["variables"]["tier_ok"]["n_incomplete"] = 1
    report_path.write_text(json.dumps(report))
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.check_evidence_tier_irr(
        events=[ATTESTED_EVENT],
        report_path=report_path,
        strict_reliability=True,
        errors=errors,
        warnings=warnings,
    )

    assert any("status='incomplete'" in error for error in errors)
    assert any("independent_human_pending" in error for error in errors)
    assert any("incomplete row" in error for error in errors)


def test_complete_evidence_tier_irr_report_passes_strict(tmp_path) -> None:
    report_path = tmp_path / "evidence_tier_irr.json"
    report_path.write_text(json.dumps(_complete_report()))
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.check_evidence_tier_irr(
        events=[ATTESTED_EVENT],
        report_path=report_path,
        strict_reliability=True,
        errors=errors,
        warnings=warnings,
    )

    assert not errors
    assert not warnings


def test_low_evidence_tier_kappa_fails_strict(tmp_path) -> None:
    report_path = tmp_path / "evidence_tier_irr.json"
    report_path.write_text(json.dumps(_complete_report(kappa=0.55)))
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.check_evidence_tier_irr(
        events=[ATTESTED_EVENT],
        report_path=report_path,
        strict_reliability=True,
        errors=errors,
        warnings=warnings,
    )

    assert any("κ=0.55" in error for error in errors)
