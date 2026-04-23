#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Convert a `candidate_triggers/<stub>.yaml` into a draft event YAML.

Given a candidate-trigger stub produced by a watcher, this script writes a
skeleton event file under `events/<slug>.yaml` with:

- status: draft
- origin: agent_draft
- coverage[] filled for all six layers at status: not_measured
- observations: empty
- trigger and target seeded from the stub where possible

The draft is guaranteed to pass `validate.py` in `draft` status so the human
editor can inspect, enrich, and promote it.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
CANDIDATE_DIR = REPO_ROOT / "candidate_triggers"

LAYERS = (
    "l0_network",
    "l1_consensus",
    "l3_rpc",
    "l4_frontend",
    "asset_onchain",
    "offramp_cex",
)

TRIGGER_TYPE_BY_DIRECTION = {
    "added": "ofac_sdn_designation",
    "removed": "ofac_sdn_removal",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Draft an event YAML from a candidate trigger stub.")
    parser.add_argument("candidate", help="Path to the candidate_triggers YAML stub.")
    parser.add_argument(
        "--slug",
        default=None,
        help="Event slug. Defaults to a derived form of the candidate filename.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing event file with the same slug.",
    )
    return parser.parse_args()


def derive_slug(candidate_name: str) -> str:
    base = candidate_name.removesuffix(".yaml")
    base = re.sub(r"[^a-z0-9-]+", "-", base.lower()).strip("-")
    return base or "agent-draft-event"


def seed_from_stub(stub: dict[str, Any], today_iso: str) -> dict[str, Any]:
    direction = str(stub.get("direction") or "").strip()
    trigger_type = TRIGGER_TYPE_BY_DIRECTION.get(direction, "ofac_sdn_designation")
    signature = str(stub.get("sdn_entry_signature") or "").strip()[:240]
    sdn_uid = str(stub.get("sdn_uid") or "").strip()

    # Derive research_stratum from trigger_type (validator enforces this mapping)
    stratum_map = {
        "ofac_sdn_designation": "S1_ofac_sdn",
        "ofac_sdn_removal": "S2_ofac_removal",
        "doj_indictment": "S3_doj_sec_cftc_fiod",
        "doj_seizure_order": "S3_doj_sec_cftc_fiod",
        "nation_state_block": "S4_nation_state",
        "corporate_policy_change": "S5_corporate",
    }
    event: dict[str, Any] = {
        "id": "PLACEHOLDER-slug",
        "schema_version": "0.2.0",
        "status": "draft",
        "research_stratum": stratum_map.get(trigger_type, "S1_ofac_sdn"),
        "empirical_shape": "comparison",
        "admission_tier": "empirical_case",
        "origin": "agent_draft",
        "created_at": today_iso,
        "trigger": {
            "type": trigger_type,
            "actor": "US_OFAC" if trigger_type.startswith("ofac") else "UNKNOWN",
            "timestamp": stub.get("observed_at") or today_iso,
            "timestamp_precision": "hour",
            "citation": [
                {
                    "type": "primary_legal",
                    "note": (
                        f"Drafted from candidate stub: direction={direction}, "
                        f"sdn_uid={sdn_uid}, signature={signature!r}"
                    ),
                }
            ],
        },
        "target": {
            "kind": "entity",
            "enumeration": "pending",
            "entity": signature or "UNKNOWN",
        },
        "jurisdiction": ["US"] if trigger_type.startswith("ofac") else ["UNKNOWN"],
        "coverage": [
            {
                "layer": layer,
                "status": "not_measured",
                "note": "Coverage not yet evaluated by a human editor.",
            }
            for layer in LAYERS
        ],
        "observations": [],
        "analysis_notes": (
            "Agent-drafted event. Source: candidate_triggers watcher detected "
            f"{direction or 'unknown-direction'} SDN entry {sdn_uid or '(no uid)'}. "
            "Human editor must enrich target, coverage, and observations before "
            "this event can be promoted out of draft."
        ),
        "tags": ["agent_drafted"],
    }
    return event


def main() -> int:
    args = parse_args()
    candidate_path = Path(args.candidate).resolve()
    if not candidate_path.is_file():
        print(f"[FAIL] candidate file not found: {candidate_path}")
        return 2

    stub = yaml.safe_load(candidate_path.read_text()) or {}
    today_iso = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    event = seed_from_stub(stub, today_iso)

    slug = args.slug or derive_slug(candidate_path.name)
    event["id"] = slug

    EVENTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = EVENTS_DIR / f"{slug}.yaml"
    if out_path.exists() and not args.force:
        print(f"[FAIL] {out_path} already exists; pass --force to overwrite.")
        return 3

    out_path.write_text(yaml.safe_dump(event, sort_keys=False, allow_unicode=True))
    print(f"[OK] wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
