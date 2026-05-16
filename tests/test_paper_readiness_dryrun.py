# SPDX-License-Identifier: MIT
"""Regression guards for dryrun-only human gate handling."""
from __future__ import annotations

import check_paper_readiness


def test_dryrun_human_audit_stamp_is_detected() -> None:
    event = {
        "last_human_audit": "2026-05-15",
        "analysis_notes": (
            "**LAST_HUMAN_AUDIT STAMP — DRYRUN 2026-05-15**: "
            "pipeline rehearsal only"
        ),
    }

    assert check_paper_readiness.human_audit_is_dryrun(event)


def test_strict_dryrun_audit_stamp_requires_explicit_allowance() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.handle_dryrun_audit_stamps(
        ids=["case-a"],
        gate_name="null-denominator",
        strict=True,
        allow_dryrun=False,
        errors=errors,
        warnings=warnings,
    )

    assert errors
    assert not warnings
    assert "--allow-dryrun-human-gates" in errors[0]


def test_allowed_dryrun_audit_stamp_remains_warning() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.handle_dryrun_audit_stamps(
        ids=["case-a"],
        gate_name="null-denominator",
        strict=True,
        allow_dryrun=True,
        errors=errors,
        warnings=warnings,
    )

    assert not errors
    assert warnings
    assert "DRYRUN last_human_audit" in warnings[0]


def test_strict_dryrun_irr_provenance_requires_explicit_allowance() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.handle_irr_provenance(
        mode="independent_human_dryrun_llm_simulated",
        strict_reliability=True,
        allow_dryrun=False,
        errors=errors,
        warnings=warnings,
    )

    assert errors
    assert not warnings
    assert "pipeline rehearsal" in errors[0]


def test_allowed_dryrun_irr_provenance_remains_warning() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_paper_readiness.handle_irr_provenance(
        mode="independent_human_dryrun_llm_simulated",
        strict_reliability=True,
        allow_dryrun=True,
        errors=errors,
        warnings=warnings,
    )

    assert not errors
    assert warnings
    assert "pipeline rehearsal" in warnings[0]
