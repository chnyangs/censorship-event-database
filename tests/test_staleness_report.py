# SPDX-License-Identifier: MIT
"""Regression guards for deterministic staleness artifacts."""
from __future__ import annotations

from _dataset_meta import today_utc_date
from staleness_report import build_report


def test_staleness_report_honors_source_date_epoch(monkeypatch):
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "0")

    report = build_report(today_utc_date())

    assert report["generated_at"] == "1970-01-01T00:00:00Z"
