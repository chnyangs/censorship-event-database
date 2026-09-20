#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Prepare an unadjudicated E2 inventory from local OFAC page caches only.

No network, outcome measurement, inferred designation/removal, or frame-completeness
claim. Missing cached days are unassessed, not days with zero legal actions.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import pathlib
import re
from datetime import date, timedelta
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = "1.0.0"
ADDRESS = re.compile(r"(?<![A-Za-z0-9])0x[0-9a-fA-F]{40}(?![A-Za-z0-9])")
QUERY_FIELDS = ["query_id", "legal_action_id", "target_id", "address", "panel_member_id",
                "surface", "window_start_utc", "window_end_utc", "query_specification",
                "endpoint_or_archive", "request_artifact", "response_artifact", "response_hash",
                "attempted_at_utc", "executed_by", "pagination_complete", "execution_status",
                "coverage_limitations", "outcome", "supporting_locator", "manual_minutes", "notes"]
ADJUDICATION_FIELDS = ["reviewer_id", "reviewed_at_utc", "canonical_action_id", "action_type",
                       "target_id", "target_name", "chain", "eligible_for_frame", "evidence_locator",
                       "adjudication_notes"]


def csv_text(rows, fields):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.title_parts, self.canonical = [], [], ""
        self.hidden_depth, self.in_title = 0, False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in ("script", "style"):
            self.hidden_depth += 1
        if tag == "title":
            self.in_title = True
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical = attributes.get("href", "")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden_depth = max(0, self.hidden_depth - 1)
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if not self.hidden_depth:
            self.parts.append(data)
            if self.in_title:
                self.title_parts.append(data)


def extract_page(raw: bytes) -> dict:
    parser = VisibleText()
    parser.feed(raw.decode("utf-8", errors="replace"))
    visible = " ".join(" ".join(parser.parts).split())
    match = re.search(r"Release Date\s+(\d{2})/(\d{2})/(\d{4})", visible)
    release_date = ""
    if match:
        try:
            release_date = date(int(match[3]), int(match[1]), int(match[2])).isoformat()
        except ValueError:
            pass
    addresses = {}
    for match in ADDRESS.finditer(visible):
        addresses.setdefault(match.group().lower(), {
            "address_string": match.group(),
            "text_context": visible[max(0, match.start() - 100):match.end() + 100],
        })
    return {"title": " ".join(parser.title_parts).strip(), "canonical_url": parser.canonical,
            "page_release_date": release_date, "addresses": addresses}


def panel_manifest(start: date, end: date) -> dict:
    panels = []
    for surface, names in (("asset_onchain", ("USDC_Ethereum", "USDT_Ethereum")),
                           ("rpc", ("Flashbots_Protect", "Infura", "Alchemy", "QuickNode")),
                           ("offramp_public_disclosure", ("Coinbase", "Kraken", "Binance"))):
        for name in names:
            panels.append({"panel_member_id": name.lower(), "name": name.replace("_", " "),
                           "surface": surface, "identity_verification_status": "pending",
                           "contract_or_endpoint": None, "operator_existence_interval": None,
                           "outcome_collection_status": "not_started"})
    return {"status": "proposed_design_not_execution_manifest", "protocol": "docs/two-arm-validation-protocol.md",
            "trigger_frame_start": start.isoformat(), "trigger_frame_end": end.isoformat(),
            "proposed_trigger_frame": "OFAC additions/removals explicitly enumerating Ethereum addresses; human action/target/chain adjudication required",
            "panels": panels, "pretrigger_days": 7, "posttrigger_days": 30,
            "endpoints_days": [1, 7, 14, 30], "manual_followup_minutes_per_action_operator": 30,
            "failed_endpoint_max_attempts": 2,
            "missingness_rule": "Unassessed or unavailable is not no reaction; retain outcome-independent eligibility.",
            "exclusions": "L0, L1 and frontend have no complete validation panel in this phase."}


def prepare(cache_dir: pathlib.Path, start: date, end: date) -> dict[str, str]:
    if start > end:
        raise ValueError("Start date must not follow end date")
    inventory, candidates, adjudication = [], [], []
    digest = hashlib.sha256()
    cached_dates = set()
    outside_window = 0
    for path in sorted(cache_dir.glob("*.html")):
        if not re.fullmatch(r"\d{8}", path.stem):
            continue
        filename_date = date.fromisoformat(f"{path.stem[:4]}-{path.stem[4:6]}-{path.stem[6:]}")
        if not start <= filename_date <= end:
            outside_window += 1
            continue
        raw = path.read_bytes()
        digest.update(path.name.encode() + b"\0" + str(len(raw)).encode() + b"\0" + raw)
        parsed = extract_page(raw)
        try:
            source_path = str(path.resolve().relative_to(ROOT))
        except ValueError:
            source_path = str(path.resolve())
        row = {"page_id": f"ofac-recent-action-{path.stem}",
               "filename_action_date_candidate": filename_date.isoformat(),
               "page_release_date": parsed["page_release_date"], "title": parsed["title"],
               "canonical_url": parsed["canonical_url"], "source_path": source_path,
               "body_hash": "sha256:" + hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
               "candidate_address_strings": len(parsed["addresses"]),
               "date_check": ("agrees" if parsed["page_release_date"] == filename_date.isoformat()
                              else "needs_date_review"),
               "status": "cached_page_pending_adjudication"}
        inventory.append(row)
        cached_dates.add(filename_date)
        for normalized, address in sorted(parsed["addresses"].items()):
            item_id = hashlib.sha256((row["page_id"] + "\0" + normalized).encode()).hexdigest()[:20]
            candidate = {"candidate_id": item_id, "page_id": row["page_id"],
                         "filename_action_date_candidate": row["filename_action_date_candidate"],
                         "page_release_date": row["page_release_date"],
                         "ethereum_address_candidate": address["address_string"],
                         "normalized_hex_string": normalized, "source_path": source_path,
                         "body_hash": row["body_hash"], "text_context": address["text_context"],
                         "status": "pending_action_target_adjudication"}
            candidates.append(candidate)
            adjudication.append({**candidate, **{key: "" for key in ADJUDICATION_FIELDS}})
    days, months = [], collections.defaultdict(lambda: {"calendar_days": 0, "cached_page_days": 0})
    current = start
    while current <= end:
        cached = current in cached_dates
        days.append({"date": current.isoformat(),
                     "local_inventory_status": "cached_page_unadjudicated" if cached else "unassessed_no_local_page",
                     "frame_reconciliation_status": "unassessed",
                     "in_frame_action_count": ""})
        month = current.strftime("%Y-%m")
        months[month]["calendar_days"] += 1
        months[month]["cached_page_days"] += int(cached)
        current += timedelta(days=1)
    monthly = [{"month": month, **counts,
                "unassessed_no_cache_days": counts["calendar_days"] - counts["cached_page_days"],
                "frame_reconciliation_status": "unassessed", "in_frame_action_count": ""}
               for month, counts in sorted(months.items())]
    summary = {"procedure_version": VERSION, "source_input_hash": "sha256:" + digest.hexdigest(),
               "window_start": start.isoformat(), "window_end": end.isoformat(),
               "status": "local_preflight_only_outcome_study_not_executed", "network_requests": 0,
               "cached_pages_in_window": len(inventory), "cached_pages_outside_window": outside_window,
               "pages_with_candidate_hex_strings": sum(bool(r["candidate_address_strings"]) for r in inventory),
               "candidate_page_address_pairs": len(candidates),
               "distinct_candidate_hex_strings": len({r["normalized_hex_string"] for r in candidates}),
               "date_review_required_pages": sum(r["date_check"] != "agrees" for r in inventory),
               "calendar_days": len(days), "unassessed_no_cache_days": len(days) - len(cached_dates),
               "frame_completeness": "not_assessed", "adjudicated_actions": 0,
               "outcome_queries_executed": 0, "human_gold_available": False,
               "extraction_limit": "Visible-text 0x plus 40 hex characters only; chain, target, action type, eligibility and completeness require adjudication. Empty extraction is not an exclusion decision."}
    inventory_fields = ["page_id", "filename_action_date_candidate", "page_release_date", "title", "canonical_url",
                        "source_path", "body_hash", "bytes", "candidate_address_strings", "date_check", "status"]
    candidate_fields = ["candidate_id", "page_id", "filename_action_date_candidate", "page_release_date",
                        "ethereum_address_candidate", "normalized_hex_string", "source_path", "body_hash", "text_context", "status"]
    readme = f"""# Bounded validation cohort: local preflight

**Outcome study NOT EXECUTED.** This is an inventory of available local caches,
not the executed cohort, independent human gold, or a complete OFAC action frame.

Window: {start} through {end}. The inventory contains {len(inventory)} cached
pages, {len(candidates)} candidate page/address pairs, and
{summary['distinct_candidate_hex_strings']} distinct hexadecimal strings.
There are {summary['unassessed_no_cache_days']} days without a local cached page;
their status is **unassessed**, never zero actions. Every month still requires
source-frame reconciliation, including months with cached pages.

`cached_page_inventory.csv` preserves raw hashes and paths. `candidate_addresses.csv`
extracts visible-text address-shaped strings only. Even a zero-address page remains
in the inventory; it is not adjudicated out of scope. Regex does not identify
chain, legal additions/removals, named targets or frame eligibility.
`action_target_adjudication_blank.csv` leaves those decisions and reviewer fields
blank. `panel_manifest.json` instantiates the proposed named panel; endpoint,
contract and existence-interval verification remain pending.
`query_log_template.csv` is a header-only blank log, with no outcomes or executions.

Run `python scripts/prepare_validation_cohort.py` from the repository root.
No network requests are made. Changed adjudication worksheets, query logs, frame
reconciliation ledgers, and panel identity manifests are never overwritten;
use a new `--out-dir` for a new snapshot. See
`docs/two-arm-validation-protocol.md` for frame reconciliation, measurement stages,
uniform effort and the distinction between domain and measurement research arms.

Next: reconcile every source period, independently adjudicate action/target/chain,
verify the panel identities, freeze the execution manifest, then execute queries
with complete logs and independent source-entailment review. Outcomes and any
completeness claims require that additional work.
"""
    return {"summary.json": json.dumps(summary, indent=2, sort_keys=True) + "\n",
            "cached_page_inventory.csv": csv_text(inventory, inventory_fields),
            "candidate_addresses.csv": csv_text(candidates, candidate_fields),
            "action_target_adjudication_blank.csv": csv_text(adjudication, candidate_fields + ADJUDICATION_FIELDS),
            "frame_daily_ledger.csv": csv_text(days, list(days[0])),
            "frame_monthly_ledger.csv": csv_text(monthly, list(monthly[0])),
            "panel_manifest.json": json.dumps(panel_manifest(start, end), indent=2, sort_keys=True) + "\n",
            "query_log_template.csv": csv_text([], QUERY_FIELDS), "README.md": readme}


def write_outputs(outputs: dict[str, str], out_dir: pathlib.Path) -> None:
    # These files all receive human decisions during later protocol stages.
    # Check every one before any write, including before refreshing summary.json.
    protected = {
        "action_target_adjudication_blank.csv", "query_log_template.csv",
        "frame_daily_ledger.csv", "frame_monthly_ledger.csv", "panel_manifest.json",
    }
    for name in protected:
        path = out_dir / name
        if path.exists() and path.read_text() != outputs[name]:
            raise ValueError(f"Refusing to overwrite changed human worksheet/log: {path}; use a new --out-dir")
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, contents in outputs.items():
        (out_dir / name).write_text(contents)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=pathlib.Path, default=ROOT / "sources/ofac_sdn_diffs/recent_actions_cache")
    parser.add_argument("--out-dir", type=pathlib.Path, default=ROOT / "analysis/validation_cohort")
    parser.add_argument("--start", type=date.fromisoformat, default=date(2022, 1, 1))
    parser.add_argument("--end", type=date.fromisoformat, default=date(2025, 12, 31))
    args = parser.parse_args()
    if not args.cache_dir.is_dir():
        raise ValueError(f"Cache directory does not exist: {args.cache_dir}")
    outputs = prepare(args.cache_dir, args.start, args.end)
    write_outputs(outputs, args.out_dir)
    print(outputs["summary.json"], end="")


if __name__ == "__main__":
    main()
