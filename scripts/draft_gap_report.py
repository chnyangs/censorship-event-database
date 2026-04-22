#!/usr/bin/env python3
"""Summarize unresolved evidence gaps across draft events."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _gap_markers import AUTHOR_DRAFT as GAP_MARKERS  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a draft-gap report.")
    parser.add_argument(
        "paths",
        nargs="*",
        help="Event YAML paths. Defaults to all draft events under events/.",
    )
    return parser.parse_args()


def discover_paths(raw_paths: list[str]) -> list[Path]:
    if raw_paths:
        return [Path(path).resolve() for path in raw_paths]
    return sorted(EVENTS_DIR.glob("*.yaml"))


def load_event(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text())


def walk_for_gaps(node: Any, path: str, gaps: list[tuple[str, str]]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            walk_for_gaps(value, f"{path}.{key}", gaps)
        return
    if isinstance(node, list):
        for idx, value in enumerate(node):
            walk_for_gaps(value, f"{path}[{idx}]", gaps)
        return
    if not isinstance(node, str):
        return

    lowered = node.lower()
    for marker in GAP_MARKERS:
        if marker in lowered:
            gaps.append((path, node.strip()))
            break


def main() -> int:
    args = parse_args()
    paths = discover_paths(args.paths)
    grouped: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for path in paths:
        if path.name == "TEMPLATE.yaml":
            continue
        event = load_event(path)
        if event.get("status") != "draft":
            continue
        gaps: list[tuple[str, str]] = []
        walk_for_gaps(event, "event", gaps)
        grouped[event.get("id", path.stem)].extend(gaps)

    for event_id in sorted(grouped):
        print(f"{event_id}:")
        for field_path, message in grouped[event_id]:
            print(f"  - {field_path}: {message}")
        if not grouped[event_id]:
            print("  - no gap markers found")

    if not grouped:
        print("No draft events with gap markers found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
