#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build a denominator-aware summary for archived OONI L0 query artifacts."""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import pathlib
import sys
from typing import Any
import urllib.parse

import yaml


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SUMMARY = REPO_ROOT / "sources" / "l0_datasets" / "_summary.json"
DEFAULT_OUT_DIR = REPO_ROOT / "derived"
EVENTS_DIR = REPO_ROOT / "events"
GENERATOR_VERSION = "0.1.0"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso, repo_relative_path, reproducible_python  # noqa: E402


CSV_COLUMNS = [
    "event_id",
    "domain",
    "input_url",
    "probe_cc",
    "since",
    "until",
    "query_hash",
    "query_url",
    "body_path",
    "body_hash",
    "query_error",
    "result_count",
    "metadata_count",
    "country_count",
    "probe_countries",
    "measurement_ids",
    "anomaly_count",
    "confirmed_count",
    "failure_count",
    "denominator_class",
    "rate_reportable",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build L0 OONI coverage summary artifacts.")
    parser.add_argument("--summary", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text())


def csv_join(values: list[str]) -> str:
    return ",".join(sorted(value for value in values if value))


def body_path(row: dict[str, Any], repo_root: pathlib.Path = REPO_ROOT) -> pathlib.Path | None:
    raw = row.get("body_path")
    if not raw:
        return None
    path = pathlib.Path(str(raw))
    return path if path.is_absolute() else repo_root / path


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value in {None, "", "false", "False", 0, "0"}:
        return False
    return True


def result_measurement_id(result: dict[str, Any]) -> str:
    for key in ("measurement_uid", "measurement_id", "report_id"):
        value = result.get(key)
        if value:
            return str(value)
    return ""


def result_country(result: dict[str, Any]) -> str:
    for key in ("probe_cc", "country_code", "probe_country"):
        value = result.get(key)
        if value:
            return str(value)
    return ""


def query_hash(params: dict[str, Any]) -> str:
    payload = json.dumps(params, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def strip_sha256_prefix(value: Any) -> str:
    text = str(value or "").strip()
    return text.split(":", 1)[1] if text.startswith("sha256:") else text


def domain_from_input_url(input_url: str) -> str:
    host = urllib.parse.urlparse(input_url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def query_params_from_url(url: str) -> dict[str, str]:
    parsed = urllib.parse.urlparse(url)
    raw_params = urllib.parse.parse_qs(parsed.query)
    return {
        key: values[0]
        for key, values in raw_params.items()
        if values
    }


def summarize_row(row: dict[str, Any], repo_root: pathlib.Path = REPO_ROOT) -> dict[str, Any]:
    path = body_path(row, repo_root)
    data: dict[str, Any] = {}
    body_error = ""
    if path and path.exists():
        try:
            loaded = load_json(path)
            if isinstance(loaded, dict):
                data = loaded
        except Exception as exc:  # pragma: no cover - defensive corrupt-artifact path
            body_error = f"could not parse body_path: {exc}"
    elif path:
        body_error = "body_path missing"

    results = data.get("results") if isinstance(data.get("results"), list) else []
    metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    query_error = str(row.get("error") or data.get("_error") or body_error or "")
    result_count = len(results) if results else int(row.get("result_count") or 0)
    metadata_count = int(metadata.get("count") or result_count or 0)

    countries = sorted({result_country(result) for result in results if isinstance(result, dict)})
    measurement_ids = sorted(
        {
            result_measurement_id(result)
            for result in results
            if isinstance(result, dict) and result_measurement_id(result)
        }
    )
    anomaly_count = sum(1 for result in results if isinstance(result, dict) and truthy(result.get("anomaly")))
    confirmed_count = sum(1 for result in results if isinstance(result, dict) and truthy(result.get("confirmed")))
    failure_count = sum(1 for result in results if isinstance(result, dict) and truthy(result.get("failure")))

    if query_error:
        denominator_class = "query_error"
    elif result_count > 0:
        denominator_class = "measurement_denominator"
    else:
        denominator_class = "no_ooni_measurements"

    return {
        "event_id": row.get("slug") or row.get("event_id") or "",
        "domain": row.get("domain") or "",
        "input_url": row.get("input_url") or "",
        "probe_cc": row.get("probe_cc") or (data.get("_query_params") or {}).get("probe_cc") or "*",
        "since": row.get("since") or "",
        "until": row.get("until") or "",
        "query_hash": row.get("query_hash") or data.get("_query_hash") or "",
        "query_url": row.get("query_url") or data.get("_query_url") or "",
        "body_path": row.get("body_path") or "",
        "body_hash": row.get("body_hash") or "",
        "query_error": query_error,
        "result_count": result_count,
        "metadata_count": metadata_count,
        "country_count": len([country for country in countries if country]),
        "probe_countries": csv_join(countries),
        "measurement_ids": csv_join(measurement_ids),
        "anomaly_count": anomaly_count,
        "confirmed_count": confirmed_count,
        "failure_count": failure_count,
        "denominator_class": denominator_class,
        "rate_reportable": "yes" if denominator_class == "measurement_denominator" else "no",
    }


def event_l0_denominator_rows(
    events_dir: pathlib.Path = EVENTS_DIR,
    repo_root: pathlib.Path = REPO_ROOT,
) -> list[dict[str, Any]]:
    """Return L0 measurement rows declared directly in event YAML.

    v0.3 repair passes may attach a replayable OONI denominator artifact to an
    event's `coverage[].denominator_artifact` before that query is folded into
    the legacy `sources/l0_datasets/_summary.json` registry.  Paper readiness
    needs those event-scoped denominators to be visible in the L0 summary.
    """
    rows: list[dict[str, Any]] = []
    if not events_dir.exists():
        return rows
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = yaml.safe_load(path.read_text())
        if not isinstance(event, dict):
            continue
        event_id = str(event.get("id") or path.stem)
        for coverage in event.get("coverage") or []:
            if not isinstance(coverage, dict):
                continue
            if coverage.get("layer") != "l0_network":
                continue
            if coverage.get("status") not in {"measured", "partially_measured"}:
                continue
            artifact = coverage.get("denominator_artifact")
            if not isinstance(artifact, dict):
                continue
            if artifact.get("type") != "semi_primary_measurement":
                continue
            if not artifact.get("measurement_ids"):
                continue
            query_url = str(artifact.get("query_url") or artifact.get("url") or "").strip()
            if not query_url:
                continue
            params = query_params_from_url(query_url)
            input_url = params.get("input") or str(artifact.get("input_url") or "")
            domain = str(artifact.get("domain") or domain_from_input_url(input_url) or "")
            normalized_params: dict[str, Any] = {
                "input": input_url,
                "since": params.get("since") or artifact.get("since") or "",
                "until": params.get("until") or artifact.get("until") or "",
                "limit": int(params.get("limit") or artifact.get("limit") or 100),
                "test_name": params.get("test_name") or "web_connectivity",
                "domain": domain,
            }
            if params.get("probe_cc") or artifact.get("probe_cc"):
                normalized_params["probe_cc"] = params.get("probe_cc") or artifact.get("probe_cc")
            raw_row = {
                "event_id": event_id,
                "domain": domain,
                "input_url": input_url,
                "probe_cc": normalized_params.get("probe_cc") or "*",
                "since": normalized_params["since"],
                "until": normalized_params["until"],
                "query_hash": artifact.get("query_hash") or query_hash(normalized_params),
                "query_url": query_url,
                "body_path": artifact.get("body_path") or "",
                "body_hash": strip_sha256_prefix(artifact.get("body_hash")),
                "error": artifact.get("error") or "",
            }
            rows.append(summarize_row(raw_row, repo_root))
    return rows


def build_rows(
    summary_path: pathlib.Path,
    repo_root: pathlib.Path = REPO_ROOT,
    events_dir: pathlib.Path = EVENTS_DIR,
) -> list[dict[str, Any]]:
    raw_rows = load_json(summary_path)
    if not isinstance(raw_rows, list):
        raise SystemExit(f"{summary_path}: expected JSON array")
    rows = [summarize_row(row, repo_root) for row in raw_rows if isinstance(row, dict)]
    rows.extend(event_l0_denominator_rows(events_dir, repo_root))
    deduped: dict[tuple[str, str, str, str, str, str], dict[str, Any]] = {}
    for row in rows:
        key = (
            row["event_id"],
            row["domain"],
            row["input_url"],
            row["since"],
            row["until"],
            row["body_path"],
        )
        deduped[key] = row
    rows = list(deduped.values())
    rows.sort(key=lambda row: (row["event_id"], row["domain"], row["since"], row["until"]))
    return rows


def l0_applicable_events(events_dir: pathlib.Path = EVENTS_DIR) -> list[str]:
    event_ids: list[str] = []
    if not events_dir.exists():
        return event_ids
    for path in sorted(events_dir.glob("*.yaml")):
        if path.name == "TEMPLATE.yaml" or path.name.startswith("_"):
            continue
        event = yaml.safe_load(path.read_text())
        if not isinstance(event, dict):
            continue
        for coverage in event.get("coverage") or []:
            if (
                isinstance(coverage, dict)
                and coverage.get("layer") == "l0_network"
                and coverage.get("status") != "not_applicable"
            ):
                event_ids.append(str(event.get("id") or path.stem))
                break
    return sorted(event_ids)


def build_markdown(rows: list[dict[str, Any]], applicable_events: list[str] | None = None) -> str:
    meta = load_meta()
    class_counts = collections.Counter(row["denominator_class"] for row in rows)
    event_counts = collections.Counter(row["event_id"] for row in rows)
    applicable_events = applicable_events if applicable_events is not None else l0_applicable_events()
    queried_events = set(event_counts)
    not_queried = sorted(set(applicable_events) - queried_events)
    lines = [
        "# L0 OONI coverage summary",
        "",
        f"Dataset snapshot: v{meta.get('dataset_version') or '?'} · "
        f"cutoff `{meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{meta.get('source_commit') or 'n/a'}` · "
        f"generated `{now_utc_iso()}`",
        "",
        "This artifact summarizes archived OONI web-connectivity query outputs "
        "for candidate L0 network-layer evidence. It is denominator-aware: "
        "`no_ooni_measurements` means the public OONI query returned no "
        "measurements for that domain/window, not that blocking was absent.",
        "",
        "## Denominator classes",
        "",
        "| denominator_class | rows |",
        "| --- | ---: |",
    ]
    for key, count in sorted(class_counts.items()):
        lines.append(f"| `{key}` | {count} |")

    lines.extend(
        [
            "",
            "## Event coverage",
            "",
            "| event_id | domain rows | measurement-denominator rows | no-measurement rows | query-error rows |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for event_id in sorted(event_counts):
        event_rows = [row for row in rows if row["event_id"] == event_id]
        counts = collections.Counter(row["denominator_class"] for row in event_rows)
        lines.append(
            f"| `{event_id}` | {len(event_rows)} | "
            f"{counts.get('measurement_denominator', 0)} | "
            f"{counts.get('no_ooni_measurements', 0)} | "
            f"{counts.get('query_error', 0)} |"
        )

    lines.extend(
        [
            "",
            "## Applicable-event coverage",
            "",
            "| class | events |",
            "| --- | ---: |",
            f"| `queried_no_ooni_measurements` | {len([event_id for event_id in applicable_events if event_id in queried_events])} |",
            f"| `not_queried_yet` | {len(not_queried)} |",
            f"| `cp_not_ingested_v0_1` | {len(applicable_events)} |",
            "",
        ]
    )
    if not_queried:
        lines.append(
            "`not_queried_yet` events: "
            + ", ".join(f"`{event_id}`" for event_id in not_queried)
            + "."
        )
        lines.append("")

    lines.extend(
        [
            "",
            "## Phrasing lock",
            "",
            "- A zero-result OONI query is an observability gap, not evidence of no L0 censorship.",
            "- Any L0 rate must be scoped to returned measurements, countries, domains, and time windows.",
            "- Event YAML `coverage.status` remains authoritative; this artifact only summarizes attached raw query surfaces.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(rows: list[dict[str, Any]], out_dir: pathlib.Path, summary_path: pathlib.Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "l0_coverage_summary.csv"
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    payload = {
        "meta": {
            "generated_at": now_utc_iso(),
            "generator": {
                "script": "scripts/build_l0_coverage_summary.py",
                "version": GENERATOR_VERSION,
                "python": reproducible_python(),
            },
            "dataset_snapshot": load_meta(),
            "source_summary": repo_relative_path(summary_path),
        },
        "rows": rows,
    }
    (out_dir / "l0_coverage_summary.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (out_dir / "l0_coverage_summary.md").write_text(build_markdown(rows))


def main() -> int:
    args = parse_args()
    summary_path = pathlib.Path(args.summary)
    rows = build_rows(summary_path)
    write_outputs(rows, pathlib.Path(args.out_dir), summary_path)
    print(f"[build_l0_coverage_summary] wrote {len(rows)} rows to {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
