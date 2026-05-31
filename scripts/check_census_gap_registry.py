#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Fail-closed checks for census-gap registry reconciliation."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = REPO_ROOT / "analysis" / "census_gap_candidates.tsv"
DEFAULT_REGISTRY = REPO_ROOT / "analysis" / "census_gap_registry.tsv"
DEFAULT_EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_NEXT_STEPS = REPO_ROOT / "analysis" / "NEXT_STEPS.md"
DEFAULT_STATE = REPO_ROOT / "analysis" / "STATE_OF_CORPUS_2026_05_31.md"

CANDIDATE_FIELDS = ("id", "date", "actor", "jurisdiction", "stratum", "layer", "one_line", "source_urls")
REGISTRY_FIELDS = (
    "id",
    "date",
    "actor",
    "jurisdiction",
    "stratum",
    "layer",
    "one_line",
    "source_url_1",
    "source_url_2",
    "confidence",
    "in_corpus",
)


@dataclass(frozen=True)
class CensusSummary:
    candidate_count: int
    registry_count: int
    covered_count: int
    not_in_corpus_count: int
    held_count: int
    missing_exact_ids: tuple[str, ...]


def _read_tsv(path: Path, required_fields: Iterable[str]) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing file: {path}")
    with path.open(newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        missing_fields = [field for field in required_fields if field not in (reader.fieldnames or [])]
        if missing_fields:
            raise ValueError(f"{path} missing required column(s): {', '.join(missing_fields)}")
        rows = list(reader)
    return rows


def _duplicates(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    dupes: set[str] = set()
    for value in values:
        if value in seen:
            dupes.add(value)
        seen.add(value)
    return sorted(dupes)


def summarize(candidates_path: Path, registry_path: Path, events_dir: Path) -> CensusSummary:
    candidate_rows = _read_tsv(candidates_path, CANDIDATE_FIELDS)
    registry_rows = _read_tsv(registry_path, REGISTRY_FIELDS)

    candidate_ids = [row["id"].strip() for row in candidate_rows]
    registry_ids = [row["id"].strip() for row in registry_rows]
    if any(not event_id for event_id in candidate_ids):
        raise ValueError(f"{candidates_path} contains blank id values")
    if any(not event_id for event_id in registry_ids):
        raise ValueError(f"{registry_path} contains blank id values")

    candidate_dupes = _duplicates(candidate_ids)
    registry_dupes = _duplicates(registry_ids)
    if candidate_dupes:
        raise ValueError(f"{candidates_path} has duplicate id(s): {', '.join(candidate_dupes)}")
    if registry_dupes:
        raise ValueError(f"{registry_path} has duplicate id(s): {', '.join(registry_dupes)}")

    invalid_booleans = sorted(
        row["id"]
        for row in registry_rows
        if row.get("in_corpus", "").strip().lower() not in {"true", "false"}
    )
    if invalid_booleans:
        raise ValueError(f"{registry_path} has non-boolean in_corpus values for: {', '.join(invalid_booleans)}")

    event_ids = {path.stem for path in events_dir.glob("*.yaml")}
    registry_id_set = set(registry_ids)
    missing_exact_ids = tuple(
        sorted(event_id for event_id in candidate_ids if event_id not in event_ids and event_id not in registry_id_set)
    )

    covered_count = sum(1 for row in registry_rows if row["in_corpus"].strip().lower() == "true")
    not_in_corpus_count = sum(1 for row in registry_rows if row["in_corpus"].strip().lower() == "false")
    held_count = sum(1 for row in registry_rows if row.get("confidence", "").strip().startswith("HELD"))

    if covered_count + not_in_corpus_count != len(registry_rows):
        raise ValueError("registry covered/not-in-corpus counts do not sum to total")

    return CensusSummary(
        candidate_count=len(candidate_rows),
        registry_count=len(registry_rows),
        covered_count=covered_count,
        not_in_corpus_count=not_in_corpus_count,
        held_count=held_count,
        missing_exact_ids=missing_exact_ids,
    )


def _extract_int(pattern: str, text: str, label: str) -> int:
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError(f"could not find {label} in documentation")
    return int(match.group(1))


def check_docs(summary: CensusSummary, next_steps_path: Path, state_path: Path) -> None:
    next_steps = next_steps_path.read_text()
    state = state_path.read_text()

    next_counts = {
        "registry_count": _extract_int(r"census_gap_registry\.tsv` has (\d+)", next_steps, "NEXT_STEPS registry count"),
        "covered_count": _extract_int(r"found (\d+) already covered", next_steps, "NEXT_STEPS covered count"),
        "not_in_corpus_count": _extract_int(r"Of the remaining\s+(\d+) `in_corpus=false`", next_steps, "NEXT_STEPS false count"),
        "held_count": _extract_int(
            r"and (\d+) (?:are explicit|is an explicit) `HELD-needs-\*`",
            next_steps,
            "NEXT_STEPS held count",
        ),
        "missing_count": _extract_int(r"Exact-id remaining queue: (\d+)", next_steps, "NEXT_STEPS exact queue count"),
    }
    state_counts = {
        "registry_count": _extract_int(r"semantic-covered slug mismatches: (\d+)", state, "STATE registry count"),
        "covered_count": _extract_int(r"registry rows, (\d+) covered", state, "STATE covered count"),
        "not_in_corpus_count": _extract_int(r"remaining (\d+) `in_corpus=false` rows", state, "STATE false count"),
        "held_count": _extract_int(
            r"and (\d+) (?:are explicit held evidence-floor rows|is an explicit held evidence-floor row)",
            state,
            "STATE held count",
        ),
        "missing_count": _extract_int(r"(\d+) exact-id candidate rows remain", state, "STATE exact queue count"),
    }
    expected = {
        "registry_count": summary.registry_count,
        "covered_count": summary.covered_count,
        "not_in_corpus_count": summary.not_in_corpus_count,
        "held_count": summary.held_count,
        "missing_count": len(summary.missing_exact_ids),
    }
    failures: list[str] = []
    for label, counts in (("NEXT_STEPS", next_counts), ("STATE", state_counts)):
        for key, actual in counts.items():
            if actual != expected[key]:
                failures.append(f"{label} {key}={actual}, expected {expected[key]}")
    if failures:
        raise ValueError("; ".join(failures))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--events-dir", type=Path, default=DEFAULT_EVENTS_DIR)
    parser.add_argument("--next-steps", type=Path, default=DEFAULT_NEXT_STEPS)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--skip-docs", action="store_true", help="Only check TSV/event reconciliation.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        summary = summarize(args.candidates, args.registry, args.events_dir)
        if not args.skip_docs:
            check_docs(summary, args.next_steps, args.state)
    except ValueError as exc:
        print(f"[census-gap-registry] FAIL: {exc}", file=sys.stderr)
        return 1

    print(
        "[census-gap-registry] OK: "
        f"{summary.candidate_count} candidates, "
        f"{summary.registry_count} registry rows, "
        f"{summary.covered_count} covered, "
        f"{summary.not_in_corpus_count} not-in-corpus, "
        f"{summary.held_count} held, "
        f"{len(summary.missing_exact_ids)} missing exact ids"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
