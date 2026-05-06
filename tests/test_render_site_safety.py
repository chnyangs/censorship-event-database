# SPDX-License-Identifier: MIT
"""Safety guard for destructive static-site output cleanup."""
from __future__ import annotations

import pathlib
import shutil

import pytest
import yaml

from render_site import EVENTS_DIR, REPO_ROOT, SITE_MARKER, copy_yaml_raw, prepare_site_dir


def test_prepare_site_dir_refuses_repo_root():
    with pytest.raises(SystemExit, match="refusing unsafe"):
        prepare_site_dir(REPO_ROOT)


def test_prepare_site_dir_refuses_event_corpus_dir():
    with pytest.raises(SystemExit, match="refusing unsafe"):
        prepare_site_dir(EVENTS_DIR)


def test_prepare_site_dir_refuses_git_metadata_dir():
    with pytest.raises(SystemExit, match="refusing unsafe"):
        prepare_site_dir(REPO_ROOT / ".git")


def test_prepare_site_dir_refuses_symlink_output_dir(tmp_path):
    target = tmp_path / "target"
    target.mkdir()
    link = tmp_path / "site-link"
    try:
        link.symlink_to(target, target_is_directory=True)
    except OSError as exc:  # pragma: no cover - platform permission guard
        pytest.skip(f"symlink creation unavailable: {exc}")

    with pytest.raises(SystemExit, match="symlinked"):
        prepare_site_dir(link)


def test_prepare_site_dir_allows_repo_local_output_dir():
    out = REPO_ROOT / ".render-site-safety-test-output"
    try:
        prepared = prepare_site_dir(out)

        assert prepared == out.resolve()
        assert prepared.is_dir()
    finally:
        shutil.rmtree(out, ignore_errors=True)


def test_prepare_site_dir_replaces_allowed_output_dir(tmp_path):
    out = tmp_path / "site"
    out.mkdir()
    (out / SITE_MARKER).write_text("generated")
    stale = out / "stale.txt"
    stale.write_text("old")

    prepared = prepare_site_dir(out)

    assert prepared == out.resolve()
    assert prepared.is_dir()
    assert not stale.exists()


def test_prepare_site_dir_refuses_existing_unmarked_output_dir(tmp_path):
    out = tmp_path / "important-dir"
    out.mkdir()
    (out / "keep.txt").write_text("do not delete")

    with pytest.raises(SystemExit, match="existing unmarked"):
        prepare_site_dir(out)

    assert (out / "keep.txt").exists()


def test_copy_yaml_raw_publishes_only_admitted_events(tmp_path):
    events_dir = tmp_path / "events"
    site_dir = tmp_path / "site"
    events_dir.mkdir()
    admitted = {"id": "admitted-case", "status": "admitted"}
    draft = {"id": "draft-case", "status": "draft"}
    (events_dir / "admitted-case.yaml").write_text(yaml.safe_dump(admitted))
    (events_dir / "draft-case.yaml").write_text(yaml.safe_dump(draft))

    copy_yaml_raw(events_dir, site_dir)

    assert (site_dir / "raw" / "admitted-case.yaml").exists()
    assert not (site_dir / "raw" / "draft-case.yaml").exists()
