#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Emit a deterministic SOURCE_DATE_EPOCH fallback for Makefile rebuilds."""
from __future__ import annotations

import json
import subprocess
from datetime import date, datetime, time, timezone
from pathlib import Path


META_PATH = Path("dataset.meta.json")


def _parse_epoch(raw: object) -> int | None:
    if not isinstance(raw, str) or not raw.strip():
        return None

    stamp = raw.strip()
    try:
        if len(stamp) == 10:
            parsed_date = date.fromisoformat(stamp)
            dt = datetime.combine(parsed_date, time.min, tzinfo=timezone.utc)
        else:
            if stamp.endswith("Z"):
                stamp = stamp[:-1] + "+00:00"
            dt = datetime.fromisoformat(stamp)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            else:
                dt = dt.astimezone(timezone.utc)
    except ValueError:
        return None
    return int(dt.timestamp())


def _metadata_epochs(meta_path: Path) -> list[int]:
    if not meta_path.exists():
        return []
    try:
        meta = json.loads(meta_path.read_text())
    except (OSError, json.JSONDecodeError):
        return []

    epochs: list[int] = []
    for key in ("generated_at", "cutoff_date"):
        epoch = _parse_epoch(meta.get(key))
        if epoch is not None:
            epochs.append(epoch)
    return epochs


def _git_head_epoch() -> int | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ct"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (FileNotFoundError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    raw = result.stdout.strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        return None


def main() -> int:
    candidates = _metadata_epochs(META_PATH)
    git_epoch = _git_head_epoch()
    if git_epoch is not None:
        candidates.append(git_epoch)
    if not candidates:
        return 0
    print(max(candidates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
