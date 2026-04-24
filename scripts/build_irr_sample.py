#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Inter-rater reliability sampler.

Build a stratified sample of events for a blind second-coder audit.
Output is two files per variable:

1. `<out>/<var>_blind.csv`: the blind worksheet — event_id, layer,
   any relevant evidence context — with the original code STRIPPED.
   A second coder fills in `recode_value`.
2. `<out>/<var>_key.csv`: the original code (gold copy), written
   simultaneously. The key file is closed until the blind worksheet
   is filled in and committed.

Variables audited by default:
- `coverage_status`: `measured` / `partially_measured` / `not_measured` / `not_applicable`
- `observation_kind`: `observed_change` / `observed_no_change` / `coverage_gap`
- `attribution`: `direct` / `plausible` / `none`

Usage:
    python3 scripts/build_irr_sample.py --out analysis/inter_rater
    python3 scripts/build_irr_sample.py --n-events 15 --seed 42
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import random
import sys
from collections import defaultdict
from typing import Iterable

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import now_utc_iso  # noqa: E402

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"


def _load_events() -> list[dict]:
    events = []
    for p in sorted(EVENTS_DIR.glob("*.yaml")):
        e = yaml.safe_load(p.read_text())
        if not isinstance(e, dict):
            continue
        e["_path"] = str(p.relative_to(REPO_ROOT))
        events.append(e)
    return events


def _stratify_sample(events: list[dict], n: int, rng: random.Random) -> list[dict]:
    """Stratify by admission_tier; return ~n events balanced across
    anchor_case / empirical_case / null_case."""
    by_tier: dict[str, list[dict]] = defaultdict(list)
    for e in events:
        tier = e.get("admission_tier", "empirical_case")
        by_tier[tier].append(e)
    out: list[dict] = []
    # Fixed targets (tuned for the v0.1 corpus: ≈5 anchors, ≈35 empirical, ≈13 nulls)
    want = {"anchor_case": max(3, n // 3),
            "empirical_case": max(n // 2, 6),
            "null_case": max(n // 4, 3)}
    for tier, k in want.items():
        pool = by_tier.get(tier, [])
        k = min(k, len(pool))
        out.extend(rng.sample(pool, k))
    # Pad or trim to exactly n.
    if len(out) < n:
        remaining = [e for e in events if e not in out]
        pad = min(n - len(out), len(remaining))
        out.extend(rng.sample(remaining, pad))
    return out[:n]


def _write_coverage_status(sample: list[dict], out_dir: pathlib.Path) -> int:
    blind_rows = []
    key_rows = []
    rid = 0
    for e in sample:
        eid = e["id"]
        notes_hint = (e.get("analysis_notes") or "")[:180].replace("\n", " ")
        for cov in e.get("coverage") or []:
            layer = cov.get("layer")
            orig = cov.get("status")
            note = (cov.get("note") or "")[:180].replace("\n", " ")
            blind_rows.append({
                "row_id": rid,
                "event_id": eid, "layer": layer,
                "coverage_note": note,
                "event_notes": notes_hint,
                "recode_value": "",
                "recoder_comment": "",
            })
            key_rows.append({"row_id": rid, "event_id": eid, "layer": layer,
                             "original_value": orig})
            rid += 1
    _write_csv(out_dir / "coverage_status_blind.csv", blind_rows)
    _write_csv(out_dir / "coverage_status_key.csv", key_rows)
    return len(blind_rows)


def _write_observation_kind(sample: list[dict], out_dir: pathlib.Path) -> int:
    blind_rows = []
    key_rows = []
    rid = 0
    for e in sample:
        eid = e["id"]
        for obs in e.get("observations") or []:
            layer = obs.get("layer")
            orig = obs.get("observation_kind")
            sources = obs.get("sources") or []
            src_hint = "; ".join(
                f"{s.get('type','?')}: {(s.get('url') or s.get('body_path') or '')[:80]}"
                for s in sources[:3]
            )
            note = (obs.get("note") or "")[:180].replace("\n", " ")
            blind_rows.append({
                "row_id": rid,
                "event_id": eid, "layer": layer,
                "observation_note": note,
                "source_hint": src_hint,
                "recode_value": "",
                "recoder_comment": "",
            })
            key_rows.append({"row_id": rid, "event_id": eid, "layer": layer,
                             "original_value": orig})
            rid += 1
    _write_csv(out_dir / "observation_kind_blind.csv", blind_rows)
    _write_csv(out_dir / "observation_kind_key.csv", key_rows)
    return len(blind_rows)


def _write_attribution(sample: list[dict], out_dir: pathlib.Path) -> int:
    blind_rows = []
    key_rows = []
    rid = 0
    for e in sample:
        eid = e["id"]
        for obs in e.get("observations") or []:
            if obs.get("observation_kind") != "observed_change":
                continue
            layer = obs.get("layer")
            orig = obs.get("attribution")
            note = (obs.get("note") or "")[:180].replace("\n", " ")
            blind_rows.append({
                "row_id": rid,
                "event_id": eid, "layer": layer,
                "observation_note": note,
                "recode_value": "",
                "recoder_comment": "",
            })
            key_rows.append({"row_id": rid, "event_id": eid, "layer": layer,
                             "original_value": orig})
            rid += 1
    _write_csv(out_dir / "attribution_blind.csv", blind_rows)
    _write_csv(out_dir / "attribution_key.csv", key_rows)
    return len(blind_rows)


def _write_csv(path: pathlib.Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="analysis/inter_rater")
    parser.add_argument("--n-events", type=int, default=15)
    parser.add_argument("--seed", type=int, default=20260424)
    args = parser.parse_args()

    out_dir = REPO_ROOT / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    events = _load_events()
    rng = random.Random(args.seed)
    sample = _stratify_sample(events, args.n_events, rng)

    manifest_rows = [
        {"event_id": e["id"],
         "admission_tier": e.get("admission_tier", "—"),
         "trigger_type": (e.get("trigger") or {}).get("type", "—"),
         "path": e.get("_path", "")}
        for e in sample
    ]
    _write_csv(out_dir / "sample_manifest.csv", manifest_rows)

    cov_n = _write_coverage_status(sample, out_dir)
    obs_n = _write_observation_kind(sample, out_dir)
    attr_n = _write_attribution(sample, out_dir)

    meta = {
        "generated_at": now_utc_iso(),
        "seed": args.seed,
        "n_events": len(sample),
        "n_coverage_rows": cov_n,
        "n_observation_rows": obs_n,
        "n_attribution_rows": attr_n,
    }
    (out_dir / "meta.yaml").write_text(yaml.dump(meta, sort_keys=False))
    print(f"[irr] wrote {out_dir}/ — {len(sample)} events, "
          f"{cov_n} coverage rows, {obs_n} observation rows, "
          f"{attr_n} attribution rows", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
