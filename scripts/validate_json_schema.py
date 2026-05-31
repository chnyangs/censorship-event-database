#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate event YAML files against schema/event.schema.json."""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Any

import jsonschema
import yaml

from _yaml_strict import load_yaml_unique_keys


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schema" / "event.schema.json"


def _clean_nulls(node: Any) -> Any:
    """Match release JSON semantics: absent optional values are omitted."""
    if isinstance(node, dict):
        return {k: _clean_nulls(v) for k, v in node.items() if v is not None}
    if isinstance(node, list):
        return [_clean_nulls(v) for v in node]
    return node


def _load_event(path: pathlib.Path) -> dict[str, Any]:
    data = load_yaml_unique_keys(path)
    if not isinstance(data, dict):
        raise ValueError("top-level YAML document must be a mapping")
    return json.loads(json.dumps(_clean_nulls(data), default=str))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("events", nargs="+", help="event YAML files to validate")
    args = parser.parse_args()

    schema = json.loads(SCHEMA_PATH.read_text())
    failures: list[str] = []
    for raw in args.events:
        path = pathlib.Path(raw)
        try:
            jsonschema.validate(
                _load_event(path),
                schema,
                format_checker=jsonschema.FormatChecker(),
            )
        except (OSError, ValueError, yaml.YAMLError, jsonschema.ValidationError) as exc:
            if isinstance(exc, jsonschema.ValidationError):
                pointer = "/" + "/".join(str(part) for part in exc.absolute_path)
                failures.append(f"{path.name} at {pointer}: {exc.message}")
            else:
                failures.append(f"{path.name}: {exc}")

    if failures:
        print("[schema] JSON-Schema validation failed:", file=sys.stderr)
        for failure in failures:
            print(f" - {failure}", file=sys.stderr)
        return 1

    print(f"[schema] OK: validated {len(args.events)} event file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
