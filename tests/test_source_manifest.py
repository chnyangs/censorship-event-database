# SPDX-License-Identifier: MIT
"""Regression guards for source artifact manifest generation."""
from __future__ import annotations

import hashlib
import csv
import json

import check_paper_readiness
from build_source_manifest import build_rows, should_include


def test_source_manifest_excludes_recursive_outputs_and_refetchable_clones(tmp_path):
    root = tmp_path
    sources = root / "sources"
    (sources / "operator_census" / "flashbots__rpc-endpoint").mkdir(parents=True)
    (sources / "operator_census").mkdir(exist_ok=True)
    clone_file = sources / "operator_census" / "flashbots__rpc-endpoint" / "README.md"
    clone_file.write_text("clone")
    candidates = sources / "operator_census" / "candidates.yaml"
    candidates.write_text("repos: []\n")
    manifest = sources / "source_manifest.csv"
    manifest.write_text("old")

    rows = build_rows(sources, root)

    assert should_include(candidates, root)
    assert not should_include(clone_file, root)
    assert not should_include(manifest, root)
    assert [row["path"] for row in rows] == ["sources/operator_census/candidates.yaml"]


def test_source_manifest_hashes_and_classifies_event_artifacts(tmp_path):
    root = tmp_path
    body = root / "sources" / "http_captures" / "event-a" / "primary" / "example.html"
    body.parent.mkdir(parents=True)
    body.write_text("hello")

    rows = build_rows(root / "sources", root)

    assert len(rows) == 1
    row = rows[0]
    assert row["path"] == "sources/http_captures/event-a/primary/example.html"
    assert row["artifact_family"] == "http_captures"
    assert row["event_id"] == "event-a"
    assert row["extension"] == "html"
    assert row["bytes"] == 5
    assert row["sha256"] == hashlib.sha256(b"hello").hexdigest()


def test_paper_readiness_source_manifest_rehashes_current_files(monkeypatch, tmp_path):
    root = tmp_path
    body = root / "sources" / "http_captures" / "event-a" / "primary" / "example.html"
    body.parent.mkdir(parents=True)
    body.write_text("hello")
    sources = root / "sources"
    manifest_prefix = sources / "source_manifest"
    row = {
        "path": "sources/http_captures/event-a/primary/example.html",
        "artifact_family": "http_captures",
        "event_id": "event-a",
        "extension": "html",
        "bytes": "5",
        "sha256": hashlib.sha256(b"stale").hexdigest(),
    }
    meta = {"row_count": 1, "total_bytes": 5}

    with manifest_prefix.with_suffix(".csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(row), lineterminator="\n")
        writer.writeheader()
        writer.writerow(row)
    manifest_prefix.with_suffix(".json").write_text(
        json.dumps({"meta": meta, "rows": [row]}) + "\n"
    )
    manifest_prefix.with_suffix(".meta.json").write_text(json.dumps(meta) + "\n")

    monkeypatch.setattr(check_paper_readiness, "REPO_ROOT", root)
    monkeypatch.setattr(check_paper_readiness, "SOURCE_MANIFEST_PREFIX", manifest_prefix)
    errors: list[str] = []

    check_paper_readiness.check_source_manifest(errors)

    assert any("manifest sha256" in error for error in errors)
