#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Jurisdictional distribution of the admitted corpus.

Addresses the reviewer finding that the admitted corpus is
US/EU-dominant and English-indexable; the paper's honest rebrand
requires exposing this distribution in a table rather than
soft-pedaling it in prose.

Emits:
  derived/jurisdiction_distribution.csv
  derived/jurisdiction_distribution.md
  analysis/paper_tables/table7_jurisdiction_distribution.md
"""
from __future__ import annotations

import argparse
import collections
import csv
import pathlib
import sys
from typing import Iterable

import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO_ROOT / "events"
DEFAULT_DERIVED_DIR = REPO_ROOT / "derived"
PAPER_TABLES_DIR = REPO_ROOT / "analysis" / "paper_tables"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _dataset_meta import now_utc_iso  # noqa: E402

# Region buckets for honest landscape framing. A country in multiple
# buckets (e.g. UK is "Europe" but not "EU_bloc") is not a data
# problem — the paper's claim is that the US / Europe / Rest split
# is ~75/15/10, not exact.
REGION_BUCKETS = {
    "US": ["US"],
    "Europe (EU+UK+CH+non-bloc)": ["UK", "EU", "DE", "NL", "PL", "PT", "CH", "IS"],
    "Rest of World": ["RU", "CN", "IN", "KR", "NG", "TR", "AU", "CA"],
    "Corporate (no jurisdiction)": ["corporate_global"],
}


def _load_events() -> list[dict]:
    events = []
    for p in sorted(EVENTS_DIR.glob("*.yaml")):
        if p.name == "TEMPLATE.yaml" or p.name.startswith("_"):
            continue
        e = yaml.safe_load(p.read_text())
        if isinstance(e, dict) and e.get("status") == "admitted":
            events.append(e)
    return events


def _regions_for(jurisdiction_list: list[str]) -> set[str]:
    """All matching regions, not just the first.

    Earlier this returned the first matching region, which made
    multi-jurisdiction events (e.g. ['UK', 'US']) count only against
    the first bucket and made the 'Europe (EU+UK+CH+non-bloc)' row
    much smaller than expected. The downstream prose then said
    'Europe-second-heaviest' even though the table showed Europe
    third — an internal contradiction. The fix here is to count an
    event in every region whose member country appears in its
    jurisdiction list, with the explicit caveat (in Table 7's prose)
    that region shares can sum to > 100 % because of multi-region
    events.
    """
    if not jurisdiction_list:
        return {"Unspecified"}
    matched: set[str] = set()
    for region, codes in REGION_BUCKETS.items():
        if any(c in codes for c in jurisdiction_list):
            matched.add(region)
    if not matched:
        matched.add("Other")
    return matched


def _classify(events: list[dict]) -> tuple[
        collections.Counter, collections.Counter, collections.Counter,
        collections.Counter]:
    by_country: collections.Counter = collections.Counter()
    by_region: collections.Counter = collections.Counter()
    by_actor: collections.Counter = collections.Counter()
    by_us_vs_nonus: collections.Counter = collections.Counter()
    for e in events:
        jlist = e.get("jurisdiction") or []
        if isinstance(jlist, str):
            jlist = [jlist]
        for code in (jlist or ["Unspecified"]):
            by_country[code] += 1
        for region in _regions_for(jlist):
            by_region[region] += 1
        by_us_vs_nonus[
            "US" if "US" in jlist else "non-US" if jlist else "Unspecified"
        ] += 1
        actor = (e.get("trigger") or {}).get("actor", "Unspecified")
        by_actor[actor] += 1
    return by_country, by_region, by_actor, by_us_vs_nonus


def _render_region(by_region: collections.Counter,
                   total: int) -> list[str]:
    """Render the region table.

    Region tallies are inclusive: an event with jurisdictions
    ['UK', 'US'] counts in BOTH 'US' and 'Europe', so the column
    sum can exceed `total` and the share column shows what
    fraction of admitted events touched that region (not what
    fraction belong exclusively to it). The caption disclaims
    this so readers do not over-interpret the share column as a
    partition.
    """
    lines = ["| region | events touching | share of corpus |",
             "| --- | ---: | ---: |"]
    region_sum = 0
    for region in list(REGION_BUCKETS.keys()) + ["Other", "Unspecified"]:
        n = by_region.get(region, 0)
        if n == 0:
            continue
        region_sum += n
        pct = (n / total * 100) if total else 0.0
        lines.append(f"| {region} | {n} | {pct:.1f}% |")
    lines.append(f"| **CORPUS TOTAL** | **{total}** | — |")
    lines.append(
        f"_Region rows are inclusive — an event with jurisdictions "
        f"`[UK, US]` counts in both US and Europe, so column sum "
        f"({region_sum}) ≥ corpus total ({total}). Share column "
        f"shows what fraction of admitted events touched the region, "
        f"not the region's exclusive share._"
    )
    return lines


def _render_country(by_country: collections.Counter) -> list[str]:
    lines = ["| jurisdiction code | events |",
             "| --- | ---: |"]
    for c, n in by_country.most_common():
        lines.append(f"| `{c}` | {n} |")
    return lines


def _write_derived(by_country, by_region, by_actor, by_us,
                   out_dir: pathlib.Path, total: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "jurisdiction_distribution.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dimension", "value", "count"])
        for c, n in by_country.most_common():
            w.writerow(["country", c, n])
        for r, n in by_region.most_common():
            w.writerow(["region", r, n])
        for a, n in by_actor.most_common():
            w.writerow(["actor", a, n])
        for u, n in by_us.most_common():
            w.writerow(["us_vs_nonus", u, n])
    md = [
        "# Jurisdictional distribution (derived)",
        "",
        f"Generated: `{now_utc_iso()}`. Corpus: n = {total} events.",
        "",
        "## By region",
        "",
        *_render_region(by_region, total),
        "",
        "## By country / bloc",
        "",
        *_render_country(by_country),
        "",
        "## By trigger actor (top 15)",
        "",
        "| actor | events |",
        "| --- | ---: |",
    ]
    for a, n in by_actor.most_common(15):
        md.append(f"| `{a}` | {n} |")
    (out_dir / "jurisdiction_distribution.md").write_text("\n".join(md) + "\n")


def _write_paper_table(by_country, by_region, by_us, total: int,
                       paper_tables_dir: pathlib.Path = PAPER_TABLES_DIR) -> None:
    paper_tables_dir.mkdir(parents=True, exist_ok=True)
    us = by_us.get("US", 0)
    non_us = by_us.get("non-US", 0)
    unspec = by_us.get("Unspecified", 0)

    # Rank regions to derive the "second-heaviest" label honestly
    # rather than hard-coding "Europe".
    region_rank = sorted(
        ((r, by_region.get(r, 0))
         for r in list(REGION_BUCKETS.keys()) + ["Other", "Unspecified"]
         if by_region.get(r, 0) > 0),
        key=lambda kv: -kv[1],
    )
    second_label = (
        f"second-most-touched region (under inclusive multi-jurisdiction "
        f"counting): **{region_rank[1][0]}** ({region_rank[1][1]} events)"
        if len(region_rank) >= 2 else "no second region"
    )
    rest_pct = sum(by_country.get(c, 0)
                   for c in ['RU', 'CN', 'IN', 'KR', 'NG', 'TR']) * 100 / total

    md = [
        "# Table 7 · Jurisdictional composition of the admitted corpus",
        "",
        f"Generated: `{now_utc_iso()}`.",
        "",
        f"**US-trigger share** (events with `US` in `jurisdiction`): "
        f"{us}/{total} ({us/total*100:.1f}%) · "
        f"**non-US-trigger share**: {non_us}/{total} "
        f"({non_us/total*100:.1f}%)"
        + (f" · Unspecified: {unspec}" if unspec else "") + ".",
        "",
        f"The v0.1 corpus is US-trigger-dominant ({us/total*100:.1f}% "
        f"of admitted events have `US` in their jurisdiction list); "
        f"{second_label}. Non-Western state-actor jurisdictions "
        f"(RU / CN / IN / KR / NG / TR) account for "
        f"~{rest_pct:.1f}% of country-level mentions. **Region row "
        f"counts use inclusive multi-jurisdiction membership** — an "
        f"event with `[UK, US]` is counted in both the US and "
        f"Europe rows; do not read region shares as a partition. "
        f"This concentration is a property of the sampling frame, "
        f"not of the underlying phenomenon, and is driven by the "
        f"frame's public-English-language-archival requirement "
        f"combined with the high absolute volume of OFAC / DOJ / "
        f"SEC activity in 2022-2025. The paper's landscape claims "
        f"must be bounded accordingly; see `docs/paper_claims.md "
        f"§0 Sampling frame` and `docs/datasheet.md §3` for the "
        f"honest statement.",
        "",
        "## Distribution by region (inclusive)",
        "",
        *_render_region(by_region, total),
        "",
        "## Distribution by country / bloc (all codes)",
        "",
        *_render_country(by_country),
        "",
        "## What this table says (phrasing-lock)",
        "",
        "- PREFER: \"the v0.1 corpus is US-trigger-dominant and "
        "English-indexable\", \"~75% of admitted events have `US` in "
        "their jurisdiction list\", \"events outside the US/Europe "
        "block are thinner in the v0.1 frame\".",
        "- FORBID: \"censorship is concentrated in the US\", "
        "\"non-Western jurisdictions do not censor crypto\", \"US is "
        "the primary site of crypto censorship\". All three inversions "
        "confuse the sampling frame for the phenomenon.",
        "- FORBID treating region shares as a partition that sums to "
        "100% — they sum higher because of multi-jurisdiction events.",
        "",
    ]
    (paper_tables_dir / "table7_jurisdiction_distribution.md").write_text(
        "\n".join(md))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(DEFAULT_DERIVED_DIR),
                        help="Where derived/jurisdiction_distribution.{csv,md} go.")
    parser.add_argument("--paper-tables-dir", default=str(PAPER_TABLES_DIR),
                        help="Where Table 7 goes (default: analysis/paper_tables).")
    args = parser.parse_args()

    events = _load_events()
    by_country, by_region, by_actor, by_us = _classify(events)
    out_dir = pathlib.Path(args.out_dir)
    paper_tables_dir = pathlib.Path(args.paper_tables_dir)
    _write_derived(by_country, by_region, by_actor, by_us,
                   out_dir, len(events))
    _write_paper_table(by_country, by_region, by_us, len(events),
                       paper_tables_dir=paper_tables_dir)
    print(f"[jurisdiction] wrote {out_dir}/jurisdiction_distribution.{{csv,md}} "
          f"and {paper_tables_dir}/table7_jurisdiction_distribution.md",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
