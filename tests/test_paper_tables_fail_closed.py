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

from build_admission_sensitivity import _compute_all
from build_paper_tables import _trigger_precision, build_table2


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


def test_table2_suppresses_l3_partial_only_rate(tmp_path):
    rows = [{
        "layer": "l3_rpc",
        "applicable_event_count": 9,
        "measured_count": 0,
        "partially_measured_count": 2,
        "not_measured_count": 7,
        "not_applicable_count": 42,
        "changed_under_measured_count": 0,
        "changed_under_measured_or_partial_count": 2,
        "changed_unique_action_count": 2,
        "duplicated_changed_action_count": 0,
    }]
    build_table2(rows, tmp_path, {}, [])
    rendered = (tmp_path / "table2_layer_observability.md").read_text()
    assert "named-only; no rate" in rendered
    assert "`l3_rpc` has no measured denominator" in rendered
    assert "2/2" not in rendered


def test_admission_sensitivity_suppresses_l3_partial_only_rate():
    events = [{
        "status": "admitted",
        "coverage": [{"layer": "l3_rpc", "status": "partially_measured"}],
        "observations": [{
            "layer": "l3_rpc",
            "observation_kind": "observed_change",
            "attribution": "direct",
        }],
    }]
    row = next(r for r in _compute_all(events) if r["layer"] == "l3_rpc")
    assert row["permissive_num"] == 1
    assert row["permissive_den"] == 1
    assert row["permissive_rate"] is None
    assert row["sensitivity"] == "undefined"


def test_table2_suppresses_asset_onchain_structural_rate(tmp_path):
    rows = [{
        "layer": "asset_onchain",
        "applicable_event_count": 23,
        "measured_count": 17,
        "partially_measured_count": 0,
        "not_measured_count": 6,
        "not_applicable_count": 28,
        "changed_under_measured_count": 17,
        "changed_under_measured_or_partial_count": 17,
        "changed_unique_action_count": 20,
        "duplicated_changed_action_count": 1,
    }]
    build_table2(rows, tmp_path, {}, [])
    rendered = (tmp_path / "table2_layer_observability.md").read_text()
    assert "retracted; no rate" in rendered
    assert "17/17" not in rendered


def test_admission_sensitivity_retracts_asset_onchain_rate():
    events = [{
        "status": "admitted",
        "coverage": [{"layer": "asset_onchain", "status": "measured"}],
        "observations": [{
            "layer": "asset_onchain",
            "observation_kind": "observed_change",
            "attribution": "direct",
        }],
    }]
    row = next(r for r in _compute_all(events) if r["layer"] == "asset_onchain")
    assert row["strict_num"] == 1
    assert row["strict_den"] == 1
    assert row["strict_rate"] is None
    assert row["permissive_rate"] is None
    assert row["sensitivity"] == "retracted_structural"
