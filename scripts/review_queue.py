#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""CLI for the v0.3 ingestion review queue."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from ingestion_v03 import DEFAULT_DB_PATH, next_review_item, resolve_review_item


def _load_decision(raw: str) -> dict[str, Any]:
    maybe_path = Path(raw)
    if maybe_path.exists():
        return json.loads(maybe_path.read_text())
    return json.loads(raw)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="v0.3 review queue CLI")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--next", action="store_true", help="print the next pending item as JSON")
    group.add_argument(
        "--decision",
        help=(
            "JSON object or path. Required keys: queue_id, decision, actor, reason. "
            "Optional: new_event_status, metadata."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    db_path = Path(args.db)
    if args.next:
        item = next_review_item(db_path)
        if item is None:
            print("{}")
            return 0
        print(json.dumps(item, indent=2, sort_keys=True))
        return 0

    decision = _load_decision(args.decision)
    required = {"queue_id", "decision", "actor", "reason"}
    missing = sorted(required - set(decision))
    if missing:
        print(f"decision JSON missing required key(s): {', '.join(missing)}", file=sys.stderr)
        return 2
    result = resolve_review_item(
        db_path=db_path,
        queue_id=int(decision["queue_id"]),
        decision=str(decision["decision"]),
        actor=str(decision["actor"]),
        reason=str(decision["reason"]),
        new_event_status=decision.get("new_event_status"),
        metadata=decision.get("metadata") or {},
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
