#!/usr/bin/env python3
"""Citation-only wrapper around validate.py."""

from __future__ import annotations

import argparse
from pathlib import Path

import validate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check citation URL reachability.")
    parser.add_argument("paths", nargs="*", help="Event YAML paths. Defaults to all events.")
    parser.add_argument("--timeout", type=float, default=10.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vocab = validate.load_yaml(validate.VOCAB_PATH)
    validator = validate.EventValidator(vocab)
    paths = validate.discover_paths(args.paths)
    all_ok = True

    for path in paths:
        event = validate.load_yaml(path)
        result = validator.validate_event(
            path=Path(path),
            event=event,
            check_citations=True,
            timeout=args.timeout,
        )
        status = "OK" if not result.errors else "FAIL"
        print(f"[{status}] {path}")
        for warning in result.warnings:
            print(f"  WARN: {warning}")
        for error in result.errors:
            print(f"  ERROR: {error}")
        all_ok = all_ok and not result.errors

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
