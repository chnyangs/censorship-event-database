#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build an independent-human IRR packet with blank worksheets.

The packet deliberately excludes key files, existing recode values, kappa
reports, LLM rationale, and rendered event pages. It is a distribution bundle
for a blinded human coder, not a computed reliability result.
"""
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import sys
from typing import Any

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import load_meta, now_utc_iso, repo_relative_path, reproducible_python  # noqa: E402


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER_RATER_DIR = REPO_ROOT / "analysis" / "inter_rater"
DEFAULT_OUT_DIR = REPO_ROOT / "site" / "h1_irr_packet"
VOCAB_PATH = REPO_ROOT / "schema" / "controlled_vocab.yaml"

WORKSHEETS = [
    "coverage_status_blind.csv",
    "observation_kind_blind.csv",
    "attribution_blind.csv",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build blank independent-human IRR packet.")
    parser.add_argument("--input-dir", default=str(INTER_RATER_DIR))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    return parser.parse_args()


def load_yaml(path: pathlib.Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text()) or {}


def blank_worksheet(src: pathlib.Path, dest: pathlib.Path) -> int:
    with src.open(newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])
    for row in rows:
        if "recode_value" in row:
            row["recode_value"] = ""
        if "recoder_comment" in row:
            row["recoder_comment"] = ""
    with dest.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def write_rubric(vocab: dict[str, Any], dest: pathlib.Path) -> None:
    coverage = ", ".join(f"`{v}`" for v in vocab.get("coverage_statuses", []))
    kinds = ", ".join(f"`{v}`" for v in vocab.get("observation_kinds", []))
    attribution = ", ".join(f"`{v}`" for v in vocab.get("attribution_levels", []))
    dest.write_text(
        "\n".join(
            [
                "# Independent-Human IRR Rubric",
                "",
                "Fill only `recode_value` and optional `recoder_comment`.",
                "Do not consult `*_key.csv`, kappa reports, rendered event pages, LLM audit notes, or prior recoder comments.",
                "",
                "## Variables",
                "",
                f"- `coverage_status`: one of {coverage}.",
                f"- `observation_kind`: one of {kinds}.",
                f"- `attribution`: one of {attribution}.",
                "",
                "## Coding Rules",
                "",
                "- `coverage_status` answers whether the row's layer had a measurement denominator in the stated scope.",
                "- `observation_kind` codes the factual row type: changed state, no observed change under a scoped denominator, or coverage gap.",
                "- `attribution` codes trigger linkage, not merely temporal order.",
                "- Use `unknown` for an observed transition whose linkage to the named trigger is unresolved.",
                "- Leave `recode_value` blank only when the packet lacks enough information to code the row; explain that in `recoder_comment`.",
                "",
                "After completion, return the filled CSVs to the maintainer, who may run `make irr-kappa` only after placing them in the expected analysis path.",
                "",
            ]
        )
    )


def write_readme(row_counts: dict[str, int], dest: pathlib.Path) -> None:
    lines = [
        "# H1 Independent-Human IRR Packet",
        "",
        f"Generated: `{now_utc_iso()}`",
        "",
        "This packet is for an independent, blinded human recode of paper-critical variables. It intentionally contains blank worksheets and coding instructions only.",
        "",
        "## Contents",
        "",
        "| file | rows |",
        "| --- | ---: |",
    ]
    for name, count in sorted(row_counts.items()):
        lines.append(f"| `{name}` | {count} |")
    lines.extend(
        [
            "| `sample_manifest.csv` | sample metadata |",
            "| `meta.yaml` | sampler metadata |",
            "| `rubric.md` | coding rubric |",
            "",
            "## Excluded On Purpose",
            "",
            "- `*_key.csv` gold labels",
            "- `kappa_report.*`",
            "- existing filled recode values",
            "- rendered site pages and LLM audit notes",
            "",
        ]
    )
    dest.write_text("\n".join(lines))


def main() -> int:
    args = parse_args()
    input_dir = pathlib.Path(args.input_dir)
    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    row_counts: dict[str, int] = {}
    for filename in WORKSHEETS:
        src = input_dir / filename
        if not src.exists():
            print(f"error: missing worksheet {repo_relative_path(src)}", file=sys.stderr)
            return 1
        row_counts[filename] = blank_worksheet(src, out_dir / filename)

    for filename in ("sample_manifest.csv", "meta.yaml"):
        src = input_dir / filename
        if src.exists():
            (out_dir / filename).write_text(src.read_text())

    vocab = load_yaml(VOCAB_PATH)
    write_rubric(vocab, out_dir / "rubric.md")
    write_readme(row_counts, out_dir / "README.md")

    meta = {
        "generated_at": now_utc_iso(),
        "generator": "scripts/build_irr_packet.py",
        "python": reproducible_python(),
        "dataset_meta": load_meta(),
        "input_dir": repo_relative_path(input_dir),
        "output_dir": repo_relative_path(out_dir),
        "excluded_files": [
            "*_key.csv",
            "kappa_report.*",
            "rendered site/event pages",
            "LLM audit notes",
        ],
        "worksheets": row_counts,
    }
    (out_dir / "packet_meta.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(f"[irr-packet] wrote blank packet to {repo_relative_path(out_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
