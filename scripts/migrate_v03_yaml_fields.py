#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Add v0.3 public verification fields to event YAML files.

This is deliberately line-oriented to preserve the existing hand-authored YAML
layout.  Internal scheduler fields such as `requires_v0_3_reextraction` are
not written to YAML.
"""

from __future__ import annotations

import argparse
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
CODEBOOK_VERSION_LINE = 'codebook_version: "1.0.0"\n'
PRIMARY_SOURCE_VERIFIED_LINE = "primary_source_verified: false\n"


def migrate_text(text: str) -> tuple[str, bool]:
    lines = text.splitlines(keepends=True)
    changed = False
    has_codebook = any(line.startswith("codebook_version:") for line in lines)
    has_primary = any(line.startswith("primary_source_verified:") for line in lines)

    if not has_codebook:
        for idx, line in enumerate(lines):
            if line.startswith("schema_version:"):
                lines.insert(idx + 1, CODEBOOK_VERSION_LINE)
                changed = True
                break

    if not has_primary:
        for idx, line in enumerate(lines):
            if line.startswith("status:"):
                lines.insert(idx + 1, PRIMARY_SOURCE_VERIFIED_LINE)
                changed = True
                break

    return "".join(lines), changed


def migrate_path(path: Path) -> bool:
    updated, changed = migrate_text(path.read_text())
    if changed:
        path.write_text(updated)
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Migrate event YAML public v0.3 fields.")
    parser.add_argument("paths", nargs="*", help="event YAML paths; defaults to events/*.yaml")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = [Path(raw) for raw in args.paths] if args.paths else sorted(EVENTS_DIR.glob("*.yaml"))
    changed = 0
    for path in paths:
        if path.name.startswith("_") or path.name == "TEMPLATE.yaml":
            continue
        if migrate_path(path):
            changed += 1
    print(f"[migrate-v03-yaml-fields] updated {changed} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
