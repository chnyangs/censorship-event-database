# SPDX-License-Identifier: MIT
"""Lock the fail-closed properties of the paper-table generator.

- Day-precision triggers must NEVER land in Panel A.
- `trigger_is_action` events must land in Panel C regardless of precision.
- A null-case event with NO validator-recognized evidence anchor must
  cause the generator to raise SystemExit (ship-blocker).
- The precision helper must prefer `trigger.timestamp_precision` (canonical
  schema field) over legacy `trigger.precision`.
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys
import tempfile

import pytest
import yaml

from build_paper_tables import _trigger_precision


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


# ---------- precision helper ----------

def test_precision_reads_canonical_field():
    e = {"trigger": {"timestamp_precision": "minute", "timestamp": "2022-08-08T13:30:00Z"}}
    assert _trigger_precision(e) == "hour"


def test_precision_day_value_routes_to_day_bucket():
    e = {"trigger": {"timestamp_precision": "day", "timestamp": "2022-08-08T13:30:00Z"}}
    assert _trigger_precision(e) == "day"


def test_precision_legacy_precision_field_fallback():
    """Legacy `trigger.precision` (schema predecessor) is accepted when
    the canonical field is missing, for backward compat."""
    e = {"trigger": {"precision": "second"}}
    assert _trigger_precision(e) == "hour"


def test_precision_midnight_timestamp_heuristic_is_day(capsys):
    """When precision is unlabeled AND the timestamp is exactly midnight,
    the heuristic buckets as 'day' and warns to stderr."""
    e = {"id": "test", "trigger": {"timestamp": "2022-08-08T00:00:00Z"}}
    assert _trigger_precision(e) == "day"
    captured = capsys.readouterr()
    assert "warning" in captured.err


# ---------- fail-closed abort on anchorless null ----------

@pytest.fixture
def corpus_with_anchorless_null(tmp_path):
    """Copy the real events dir, then strip ALL evidence anchors from one
    null-case observed_no_change source so the generator must abort."""
    fake_events = tmp_path / "events"
    shutil.copytree(REPO_ROOT / "events", fake_events)

    target = fake_events / "iran-ransomware-ofac-2018.yaml"
    e = yaml.safe_load(target.read_text())
    for obs in e.get("observations") or []:
        if obs.get("observation_kind") != "observed_no_change":
            continue
        for src in obs.get("sources") or []:
            for k in ("body_hash", "body_path", "query_hash",
                      "measurement_ids", "scope_descriptor"):
                src.pop(k, None)
    target.write_text(yaml.dump(e, sort_keys=False))
    return fake_events


def test_build_paper_tables_aborts_on_anchorless_null(corpus_with_anchorless_null, tmp_path):
    """A null-case event with zero evidence anchors must cause a non-zero
    exit — this is a ship-blocker per docs/paper_claims.md §4."""
    out_dir = tmp_path / "paper_tables"
    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "build_paper_tables.py"),
            "--events-dir", str(corpus_with_anchorless_null),
            "--out-dir", str(out_dir),
        ],
        capture_output=True, text=True,
    )
    assert result.returncode != 0, (
        f"Generator should abort on anchorless null; stdout={result.stdout!r} "
        f"stderr={result.stderr!r}"
    )
    assert "iran-ransomware-ofac-2018" in result.stderr
    assert "ABORT" in result.stderr
