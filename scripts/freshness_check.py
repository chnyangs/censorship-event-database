#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check whether URLs recorded in event files are still reachable."""

from __future__ import annotations

import argparse
import sys

import validate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check link freshness in event files.")
    parser.add_argument("paths", nargs="*", help="Event YAML paths. Defaults to all events.")
    parser.add_argument("--timeout", type=float, default=10.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = validate.discover_paths(args.paths)
    failures = 0

    for path in paths:
        event = validate.load_yaml(path)
        for label, url in validate.iter_citation_like_urls(event):
            ok, detail = validate.fetch_url_status(url, args.timeout)
            if ok:
                status = "OK"
            elif detail.startswith("HTTPError"):
                status = "FAIL"
            else:
                status = "WARN"
            print(f"[{status}] {path} {label} {url} ({detail})")
            if status == "FAIL":
                failures += 1

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
