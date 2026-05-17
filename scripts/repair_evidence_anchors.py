#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Batch-capture missing replayable evidence anchors.

This is a pre-human evidence repair utility. It only attaches local
body_hash/body_path anchors to existing URL-bearing trigger citations and
observation sources. It never changes event status, origin,
last_human_audit, or primary_source_verified.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from capture_http_artifact import (
    REPO_ROOT,
    build_basename,
    capture_url,
    detect_extension,
    patch_event_yaml,
)


DEFAULT_PLAN = REPO_ROOT / "analysis" / "review_queue" / "evidence_repair_plan.csv"
DEFAULT_REPORT_PREFIX = REPO_ROOT / "analysis" / "review_queue" / "evidence_anchor_repair_report"
DEFAULT_CAPTURE_ROOT = REPO_ROOT / "sources" / "http_captures"
REPORT_COLUMNS = [
    "event_id",
    "queue_id",
    "repair_class",
    "url",
    "status",
    "body_hash",
    "body_path",
    "metadata_path",
    "error",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", default=str(DEFAULT_PLAN))
    parser.add_argument("--report-prefix", default=str(DEFAULT_REPORT_PREFIX))
    parser.add_argument("--capture-root", default=str(DEFAULT_CAPTURE_ROOT))
    parser.add_argument("--priority-max", type=int, help="Only repair rows with repair_priority <= this value.")
    parser.add_argument("--limit", type=int, help="Maximum number of plan rows to process.")
    parser.add_argument("--event-id", action="append", help="Limit to one or more event IDs.")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--allow-insecure-tls", action="store_true")
    parser.add_argument("--force", action="store_true", help="Overwrite existing capture files for the same URL.")
    parser.add_argument("--dry-run", action="store_true", help="Report missing anchors without fetching or patching.")
    parser.add_argument(
        "--wayback-fallback",
        action="store_true",
        help="When current HTTP capture fails, patch the closest available Wayback snapshot if one exists.",
    )
    parser.add_argument(
        "--fail-on-capture-error",
        action="store_true",
        help="Return non-zero if any URL capture fails.",
    )
    return parser.parse_args()


def has_replayable_anchor(source: dict[str, Any]) -> bool:
    if source.get("wayback"):
        return True
    if source.get("body_hash") and source.get("body_path"):
        return True
    if source.get("query_hash"):
        return True
    measurement_ids = source.get("measurement_ids")
    if isinstance(measurement_ids, list) and any(str(item).strip() for item in measurement_ids):
        return True
    if source.get("tx_hash"):
        return True
    return False


def missing_anchor_urls(event: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    trigger = event.get("trigger") if isinstance(event.get("trigger"), dict) else {}
    for citation in trigger.get("citation") or []:
        if not isinstance(citation, dict):
            continue
        url = citation.get("url")
        if isinstance(url, str) and url and not has_replayable_anchor(citation):
            urls.append(url)

    for observation in event.get("observations") or []:
        if not isinstance(observation, dict):
            continue
        for source in observation.get("sources") or []:
            if not isinstance(source, dict):
                continue
            if source.get("type") == "primary_onchain":
                continue
            url = source.get("url")
            if isinstance(url, str) and url and not has_replayable_anchor(source):
                urls.append(url)
    return sorted(set(urls))


def load_plan(path: Path, priority_max: int | None, event_ids: set[str] | None, limit: int | None) -> list[dict[str, str]]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh))
    selected: list[dict[str, str]] = []
    for row in rows:
        if priority_max is not None and int(row["repair_priority"]) > priority_max:
            continue
        if event_ids is not None and row["event_id"] not in event_ids:
            continue
        selected.append(row)
        if limit is not None and len(selected) >= limit:
            break
    return selected


def write_capture_files(
    *,
    event_id: str,
    url: str,
    capture_root: Path,
    timeout: float,
    allow_insecure_tls: bool,
    force: bool,
) -> dict[str, str]:
    output_dir = capture_root / event_id / "v0_3_repair"
    output_dir.mkdir(parents=True, exist_ok=True)
    capture = capture_url(url, timeout=timeout, allow_insecure_tls=allow_insecure_tls)
    ext = detect_extension(str(capture["content_type"]))
    basename = build_basename(url)
    body_path = output_dir / f"{basename}{ext}"
    metadata_path = output_dir / f"{basename}.json"
    if not force and (body_path.exists() or metadata_path.exists()):
        metadata = json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
        sha = str(metadata.get("sha256") or "")
        rel_body = str(metadata.get("body_path") or body_path.relative_to(REPO_ROOT))
        rel_meta = str(metadata.get("metadata_path") or metadata_path.relative_to(REPO_ROOT))
        if not sha:
            raise RuntimeError(f"capture collision without reusable metadata: {metadata_path}")
        return {
            "body_hash": f"sha256:{sha}",
            "body_path": rel_body,
            "metadata_path": rel_meta,
            "status": "reused_existing_capture",
        }

    body = capture.pop("body")
    body_path.write_bytes(body)
    capture["body_path"] = str(body_path.relative_to(REPO_ROOT))
    capture["metadata_path"] = str(metadata_path.relative_to(REPO_ROOT))
    metadata_path.write_text(json.dumps(capture, indent=2, sort_keys=True) + "\n")
    return {
        "body_hash": f"sha256:{capture['sha256']}",
        "body_path": capture["body_path"],
        "metadata_path": capture["metadata_path"],
        "status": "captured",
    }


def closest_wayback(url: str, timeout: float) -> str | None:
    api_url = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    with urllib.request.urlopen(api_url, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    archived = payload.get("archived_snapshots", {}).get("closest", {})
    if archived.get("available") and archived.get("url"):
        return str(archived["url"])
    return None


def repair_row(
    row: dict[str, str],
    *,
    capture_root: Path,
    timeout: float,
    allow_insecure_tls: bool,
    force: bool,
    dry_run: bool,
    wayback_fallback: bool,
) -> list[dict[str, str]]:
    event_id = row["event_id"]
    event_path = REPO_ROOT / "events" / f"{event_id}.yaml"
    if not event_path.exists():
        return [
            {
                "event_id": event_id,
                "queue_id": row.get("queue_id", ""),
                "repair_class": row.get("repair_class", ""),
                "url": "",
                "status": "event_yaml_missing",
                "body_hash": "",
                "body_path": "",
                "metadata_path": "",
                "error": str(event_path),
            }
        ]

    event = yaml.safe_load(event_path.read_text()) or {}
    urls = missing_anchor_urls(event)
    if not urls:
        return [
            {
                "event_id": event_id,
                "queue_id": row.get("queue_id", ""),
                "repair_class": row.get("repair_class", ""),
                "url": "",
                "status": "no_existing_url_missing_anchor",
                "body_hash": "",
                "body_path": "",
                "metadata_path": "",
                "error": "",
            }
        ]

    report_rows: list[dict[str, str]] = []
    url_to_fields: dict[str, dict[str, str]] = {}
    for url in urls:
        base = {
            "event_id": event_id,
            "queue_id": row.get("queue_id", ""),
            "repair_class": row.get("repair_class", ""),
            "url": url,
            "body_hash": "",
            "body_path": "",
            "metadata_path": "",
            "error": "",
        }
        if dry_run:
            report_rows.append({**base, "status": "dry_run"})
            continue
        try:
            capture_fields = write_capture_files(
                event_id=event_id,
                url=url,
                capture_root=capture_root,
                timeout=timeout,
                allow_insecure_tls=allow_insecure_tls,
                force=force,
            )
            url_to_fields[url] = {
                "body_hash": capture_fields["body_hash"],
                "body_path": capture_fields["body_path"],
            }
            report_rows.append({**base, **capture_fields})
        except urllib.error.HTTPError as exc:
            error = f"HTTPError {exc.code}"
            if wayback_fallback:
                try:
                    wayback = closest_wayback(url, timeout=timeout)
                except Exception as wb_exc:  # pragma: no cover - network-dependent
                    wayback = None
                    error = f"{error}; Wayback {type(wb_exc).__name__}: {wb_exc}"
                if wayback:
                    url_to_fields[url] = {"wayback": wayback}
                    report_rows.append({**base, "status": "wayback_fallback", "metadata_path": wayback, "error": error})
                    continue
            report_rows.append({**base, "status": "capture_failed", "error": error})
        except urllib.error.URLError as exc:
            error = f"URLError {exc.reason}"
            if wayback_fallback:
                try:
                    wayback = closest_wayback(url, timeout=timeout)
                except Exception as wb_exc:  # pragma: no cover - network-dependent
                    wayback = None
                    error = f"{error}; Wayback {type(wb_exc).__name__}: {wb_exc}"
                if wayback:
                    url_to_fields[url] = {"wayback": wayback}
                    report_rows.append({**base, "status": "wayback_fallback", "metadata_path": wayback, "error": error})
                    continue
            report_rows.append({**base, "status": "capture_failed", "error": error})
        except Exception as exc:  # pragma: no cover - defensive reporting
            report_rows.append({**base, "status": "capture_failed", "error": f"{type(exc).__name__}: {exc}"})

    if url_to_fields and not dry_run:
        patch_stats = patch_event_yaml(event_path, url_to_fields)
        for report_row in report_rows:
            if report_row["url"] in url_to_fields:
                report_row["status"] = f"{report_row['status']};patched_fields={patch_stats['fields_injected']}"
    return report_rows


def write_reports(rows: list[dict[str, str]], report_prefix: Path) -> dict[str, str]:
    report_prefix.parent.mkdir(parents=True, exist_ok=True)
    csv_path = report_prefix.with_suffix(".csv")
    json_path = report_prefix.with_suffix(".json")
    md_path = report_prefix.with_suffix(".md")
    with csv_path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=REPORT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in REPORT_COLUMNS})

    status_counts: dict[str, int] = {}
    for row in rows:
        status = row.get("status", "")
        status_counts[status] = status_counts.get(status, 0) + 1
    payload = {
        "generated_at": utc_now(),
        "report_kind": "v0.3_evidence_anchor_repair_report",
        "human_audit_performed": False,
        "primary_source_verified_mutated": False,
        "row_count": len(rows),
        "status_counts": status_counts,
        "rows": rows,
    }
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    lines = [
        "# Evidence Anchor Repair Report",
        "",
        "This report records machine HTTP captures for existing URL-bearing evidence. It is not human audit.",
        "",
        "| Status | Count |",
        "| --- | ---: |",
    ]
    for status, count in sorted(status_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{status}` | {count} |")
    lines.extend(["", "## Failures / Remaining Manual Source Work", "", "| event_id | url | status | error |", "| --- | --- | --- | --- |"])
    for row in rows:
        if row.get("status", "").startswith("capture_failed") or row.get("status") in {
            "event_yaml_missing",
            "no_existing_url_missing_anchor",
        }:
            lines.append(
                f"| `{row.get('event_id', '')}` | {row.get('url', '')} | "
                f"`{row.get('status', '')}` | {str(row.get('error', '')).replace('|', '\\|')} |"
            )
    md_path.write_text("\n".join(lines) + "\n")
    return {"csv": str(csv_path), "json": str(json_path), "md": str(md_path)}


def main() -> int:
    args = parse_args()
    event_ids = set(args.event_id) if args.event_id else None
    rows = load_plan(Path(args.plan), args.priority_max, event_ids, args.limit)
    report_rows: list[dict[str, str]] = []
    for row in rows:
        report_rows.extend(
            repair_row(
                row,
                capture_root=Path(args.capture_root),
                timeout=args.timeout,
                allow_insecure_tls=args.allow_insecure_tls,
                force=args.force,
                dry_run=args.dry_run,
                wayback_fallback=args.wayback_fallback,
            )
        )
    paths = write_reports(report_rows, Path(args.report_prefix))
    print(json.dumps(paths, indent=2, sort_keys=True))
    failed = any(row.get("status", "").startswith("capture_failed") for row in report_rows)
    return 1 if failed and args.fail_on_capture_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
