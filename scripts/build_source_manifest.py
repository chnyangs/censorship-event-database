#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build a release manifest for local source artifacts."""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import pathlib
import sys
from typing import Any


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SOURCES_DIR = REPO_ROOT / "sources"
DEFAULT_OUT_PREFIX = DEFAULT_SOURCES_DIR / "source_manifest"
GENERATOR_VERSION = "0.1.0"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso, repo_relative_path, reproducible_python  # noqa: E402


CSV_COLUMNS = [
    "path",
    "artifact_family",
    "event_id",
    "extension",
    "bytes",
    "sha256",
]

EXCLUDED_EXACT = {
    "sources/.DS_Store",
    "sources/source_manifest.csv",
    "sources/source_manifest.json",
    "sources/source_manifest.md",
    "sources/source_manifest.meta.json",
    "sources/ofac_sdn_diffs/current/sdn.xml",
    "sources/ofac_sdn_diffs/opensanctions/us_ofac_sdn.ftm.json",
}

EXCLUDED_NAMES = {".DS_Store", ".gitkeep"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build source artifact manifest.")
    parser.add_argument("--sources-dir", default=str(DEFAULT_SOURCES_DIR))
    parser.add_argument("--out-prefix", default=str(DEFAULT_OUT_PREFIX))
    return parser.parse_args()


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def should_include(path: pathlib.Path, repo_root: pathlib.Path = REPO_ROOT) -> bool:
    if not path.is_file():
        return False
    rel = repo_relative_path(path, repo_root)
    if rel in EXCLUDED_EXACT:
        return False
    if path.name in EXCLUDED_NAMES:
        return False
    parts = pathlib.PurePosixPath(rel).parts
    if len(parts) >= 3 and parts[0] == "sources" and parts[1] == "operator_census":
        return parts[2] == "candidates.yaml"
    if "__pycache__" in parts or ".git" in parts:
        return False
    return True


def artifact_family(rel: str) -> str:
    parts = pathlib.PurePosixPath(rel).parts
    if len(parts) < 2 or parts[0] != "sources":
        return "other"
    return parts[1]


def event_id(rel: str) -> str:
    parts = pathlib.PurePosixPath(rel).parts
    if len(parts) < 3 or parts[0] != "sources":
        return ""
    family = parts[1]
    if family in {"http_captures", "archived_htmls", "l0_datasets", "l1_datasets"}:
        return "" if parts[2].startswith("_") else parts[2]
    if family == "asset_layer_scan":
        return "" if parts[2].startswith("_") else pathlib.PurePosixPath(parts[2]).stem
    return ""


def build_rows(
    sources_dir: pathlib.Path = DEFAULT_SOURCES_DIR,
    repo_root: pathlib.Path = REPO_ROOT,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(sources_dir.rglob("*")):
        if not should_include(path, repo_root):
            continue
        rel = repo_relative_path(path, repo_root)
        rows.append(
            {
                "path": rel,
                "artifact_family": artifact_family(rel),
                "event_id": event_id(rel),
                "extension": path.suffix.lower().lstrip(".") or "none",
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    rows.sort(key=lambda row: row["path"])
    return rows


def write_csv(rows: list[dict[str, Any]], path: pathlib.Path) -> None:
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_meta(rows: list[dict[str, Any]]) -> dict[str, Any]:
    dataset_meta = load_meta()
    return {
        "dataset_version": dataset_meta.get("dataset_version"),
        "cutoff_date": dataset_meta.get("cutoff_date"),
        "source_commit": dataset_meta.get("source_commit"),
        "generated_at": now_utc_iso(),
        "generator": pathlib.Path(__file__).name,
        "generator_version": GENERATOR_VERSION,
        "python": reproducible_python(),
        "row_count": len(rows),
        "total_bytes": sum(int(row["bytes"]) for row in rows),
        "excluded_policy": {
            "operator_census_clones": "re-fetchable from sources/operator_census/candidates.yaml; compact receipts live in analysis/operator_census/commits.json",
            "large_upstream_dumps": "excluded per .gitignore and regenerated/fetched separately",
            "retrieval_receipts": "sources/external_retrieval_receipts.yaml documents excluded upstream inputs",
            "self_outputs": "source_manifest.* files excluded to avoid recursive hashes",
        },
    }


def write_json(rows: list[dict[str, Any]], meta: dict[str, Any], path: pathlib.Path) -> None:
    path.write_text(json.dumps({"meta": meta, "rows": rows}, indent=2, sort_keys=True) + "\n")


def build_markdown(rows: list[dict[str, Any]], meta: dict[str, Any]) -> str:
    family_counts = collections.Counter(str(row["artifact_family"]) for row in rows)
    extension_counts = collections.Counter(str(row["extension"]) for row in rows)
    lines = [
        "# Source Artifact Manifest",
        "",
        f"Dataset snapshot: v{meta.get('dataset_version') or '?'} · "
        f"cutoff `{meta.get('cutoff_date') or 'n/a'}` · "
        f"commit `{meta.get('source_commit') or 'n/a'}` · "
        f"generated `{meta.get('generated_at')}`",
        "",
        "This manifest lists local source artifacts included in the release "
        "reproduction surface and records their SHA-256 hashes. Re-fetchable "
        "operator-census repository clones and large upstream dumps excluded "
        "by `.gitignore` are intentionally not listed; their retrieval policy "
        "is recorded in `sources/external_retrieval_receipts.yaml`.",
        "",
        f"- Files: {meta['row_count']}",
        f"- Total bytes: {meta['total_bytes']}",
        "",
        "## By Artifact Family",
        "",
        "| family | files |",
        "| --- | ---: |",
    ]
    for family, count in sorted(family_counts.items()):
        lines.append(f"| `{family}` | {count} |")
    lines.extend(
        [
            "",
            "## By Extension",
            "",
            "| extension | files |",
            "| --- | ---: |",
        ]
    )
    for ext, count in sorted(extension_counts.items()):
        lines.append(f"| `{ext}` | {count} |")
    lines.extend(
        [
            "",
            "## Exclusions",
            "",
            "- `sources/operator_census/*/` clones are re-fetchable from "
            "`sources/operator_census/candidates.yaml` and are not release inputs. "
            "`analysis/operator_census/commits.json` is the compact tracked receipt.",
            "- `sources/ofac_sdn_diffs/current/sdn.xml` and "
            "`sources/ofac_sdn_diffs/opensanctions/us_ofac_sdn.ftm.json` are "
            "large upstream dumps excluded by `.gitignore`.",
            "- `sources/external_retrieval_receipts.yaml` records the retrieval "
            "contract for excluded upstream inputs.",
            "- `source_manifest.*` outputs are excluded from their own input set.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    sources_dir = pathlib.Path(args.sources_dir)
    out_prefix = pathlib.Path(args.out_prefix)
    out_prefix.parent.mkdir(parents=True, exist_ok=True)
    rows = build_rows(sources_dir=sources_dir)
    meta = build_meta(rows)
    write_csv(rows, out_prefix.with_suffix(".csv"))
    write_json(rows, meta, out_prefix.with_suffix(".json"))
    out_prefix.with_suffix(".meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    out_prefix.with_suffix(".md").write_text(build_markdown(rows, meta))
    print(f"[source-manifest] wrote {len(rows)} rows to {repo_relative_path(out_prefix)}.*")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
