# SPDX-License-Identifier: MIT
"""Regression guard for non-git reproducibility epoch fallback."""
from __future__ import annotations

from datetime import datetime

import repro_source_date_epoch
import build_dataset
from _dataset_meta import repo_relative_path, reproducible_python


def test_repro_source_date_epoch_reads_dataset_metadata(tmp_path, monkeypatch, capsys):
    meta = tmp_path / "dataset.meta.json"
    meta.write_text('{"generated_at": "2026-04-27T11:03:02Z"}')
    monkeypatch.setattr(repro_source_date_epoch, "META_PATH", meta)
    monkeypatch.setattr(repro_source_date_epoch, "_git_head_epoch", lambda: None)

    assert repro_source_date_epoch.main() == 0

    expected = int(datetime.fromisoformat("2026-04-27T11:03:02+00:00").timestamp())
    assert capsys.readouterr().out.strip() == str(expected)


def test_repro_source_date_epoch_uses_cutoff_when_head_commit_predates_it(tmp_path, monkeypatch, capsys):
    meta = tmp_path / "dataset.meta.json"
    meta.write_text('{"generated_at": "2026-05-31T16:38:43Z", "cutoff_date": "2026-06-01"}')
    monkeypatch.setattr(repro_source_date_epoch, "META_PATH", meta)
    monkeypatch.setattr(
        repro_source_date_epoch,
        "_git_head_epoch",
        lambda: int(datetime.fromisoformat("2026-05-31T16:40:00+00:00").timestamp()),
    )

    assert repro_source_date_epoch.main() == 0

    expected = int(datetime.fromisoformat("2026-06-01T00:00:00+00:00").timestamp())
    assert capsys.readouterr().out.strip() == str(expected)


def test_repro_source_date_epoch_keeps_later_head_commit(tmp_path, monkeypatch, capsys):
    meta = tmp_path / "dataset.meta.json"
    meta.write_text('{"generated_at": "2026-06-01T00:00:00Z", "cutoff_date": "2026-06-01"}')
    head_epoch = int(datetime.fromisoformat("2026-06-02T03:04:05+00:00").timestamp())
    monkeypatch.setattr(repro_source_date_epoch, "META_PATH", meta)
    monkeypatch.setattr(repro_source_date_epoch, "_git_head_epoch", lambda: head_epoch)

    assert repro_source_date_epoch.main() == 0

    assert capsys.readouterr().out.strip() == str(head_epoch)


def test_repo_relative_path_removes_checkout_prefix(tmp_path):
    root = tmp_path / "repo"
    path = root / "sources" / "l0_datasets" / "_summary.json"
    path.parent.mkdir(parents=True)
    path.write_text("[]")

    assert repo_relative_path(path, root) == "sources/l0_datasets/_summary.json"


def test_reproducible_python_uses_declared_abi(monkeypatch):
    monkeypatch.delenv("REPRODUCIBLE_PYTHON_ABI", raising=False)
    assert reproducible_python() == "3.12"
    monkeypatch.setenv("REPRODUCIBLE_PYTHON_ABI", "3.12-test")
    assert reproducible_python() == "3.12-test"


def test_source_input_hash_uses_repo_relative_paths(tmp_path, monkeypatch):
    repo = tmp_path / "repo"
    events = repo / "events"
    events.mkdir(parents=True)
    (events / "a.yaml").write_text("id: a\n")
    (repo / "CITATION.cff").write_text('version: "0.1.0"\n')
    monkeypatch.setattr(build_dataset, "REPO_ROOT", repo)
    monkeypatch.setattr(build_dataset, "SOURCE_INPUT_GLOBS", ["CITATION.cff", "events/*.yaml"])

    digest, count = build_dataset.source_input_hash()

    assert digest.startswith("sha256:")
    assert count == 2
