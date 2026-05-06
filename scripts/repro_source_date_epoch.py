#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Emit a deterministic SOURCE_DATE_EPOCH fallback from committed metadata."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


META_PATH = Path("dataset.meta.json")


def main() -> int:
    if not META_PATH.exists():
        return 0

    raw = json.loads(META_PATH.read_text()).get("generated_at")
    if not isinstance(raw, str) or not raw.strip():
        return 0

    stamp = raw.strip()
    if stamp.endswith("Z"):
        stamp = stamp[:-1] + "+00:00"
    print(int(datetime.fromisoformat(stamp).timestamp()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
