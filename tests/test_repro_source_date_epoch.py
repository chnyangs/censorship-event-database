# SPDX-License-Identifier: MIT
"""Regression guard for non-git reproducibility epoch fallback."""
from __future__ import annotations

from datetime import datetime

import repro_source_date_epoch


def test_repro_source_date_epoch_reads_dataset_metadata(tmp_path, monkeypatch, capsys):
    meta = tmp_path / "dataset.meta.json"
    meta.write_text('{"generated_at": "2026-04-27T11:03:02Z"}')
    monkeypatch.setattr(repro_source_date_epoch, "META_PATH", meta)

    assert repro_source_date_epoch.main() == 0

    expected = int(datetime.fromisoformat("2026-04-27T11:03:02+00:00").timestamp())
    assert capsys.readouterr().out.strip() == str(expected)
