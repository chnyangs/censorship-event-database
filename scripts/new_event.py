#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Create a new draft event file from a built-in template."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
TEMPLATE_PATH = REPO_ROOT / "templates" / "event.yaml"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new draft event YAML.")
    parser.add_argument("event_id", help="kebab-case event id, e.g. garantex-ofac-2022")
    parser.add_argument("--shape", dest="empirical_shape", default="comparison",
                        choices=["cascade", "comparison", "null_event"])
    parser.add_argument("--tier", dest="admission_tier", default="empirical_case",
                        choices=["anchor_case", "empirical_case", "null_case"])
    parser.add_argument("--trigger-type", default="corporate_policy_change")
    parser.add_argument("--actor", default="EXAMPLE_ACTOR")
    parser.add_argument("--jurisdiction", action="append", default=["US"])
    return parser.parse_args()


STRATUM_MAP = {
    "ofac_sdn_designation": "S1_ofac_sdn",
    "ofac_sdn_removal": "S2_ofac_removal",
    "doj_indictment": "S3_doj_sec_cftc_fiod",
    "doj_seizure_order": "S3_doj_sec_cftc_fiod",
    "nation_state_block": "S4_nation_state",
    "corporate_policy_change": "S5_corporate",
}


def build_template(args: argparse.Namespace) -> dict:
    if TEMPLATE_PATH.exists():
        template = yaml.safe_load(TEMPLATE_PATH.read_text())
    else:
        template = {}
    now = datetime.now(UTC)
    iso_now = now.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    today = now.date().isoformat()
    template["id"] = args.event_id
    template["schema_version"] = "0.2.0"
    template["status"] = "draft"
    template["research_stratum"] = STRATUM_MAP.get(args.trigger_type, "S5_corporate")
    template["empirical_shape"] = args.empirical_shape
    template["admission_tier"] = args.admission_tier
    # Legacy event_class field removed in schema 0.2.0
    template.pop("event_class", None)
    template["version"] = "0.1"
    template["created_at"] = iso_now
    template["last_verified"] = today
    template["trigger"]["type"] = args.trigger_type
    template["trigger"]["actor"] = args.actor
    template["trigger"]["timestamp"] = iso_now
    template["jurisdiction"] = args.jurisdiction
    return template


def main() -> int:
    args = parse_args()
    path = EVENTS_DIR / f"{args.event_id}.yaml"
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {path}")

    event = build_template(args)
    path.write_text(yaml.safe_dump(event, sort_keys=False, allow_unicode=True))
    print(f"Created {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
