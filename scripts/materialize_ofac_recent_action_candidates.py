#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Materialize OFAC recent-action triage rows into trigger-registry stubs."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
TRIAGE_PATH = (
    REPO_ROOT
    / "sources"
    / "ofac_sdn_diffs"
    / "opensanctions"
    / "ofac-recent-actions-triage.json"
)
EVENTS_DIR = REPO_ROOT / "events"
CANDIDATE_DIR = REPO_ROOT / "candidate_triggers"
CACHE_DIR = REPO_ROOT / "sources" / "ofac_sdn_diffs" / "recent_actions_cache"

TOKEN_CHAIN_MAP = {
    "XBT": "bitcoin",
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "USDC": "ethereum",
    "TRX": "tron",
    "LTC": "litecoin",
    "ZEC": "zcash",
    "BSV": "bitcoin_sv",
    "DASH": "dash",
    "BCH": "bitcoin_cash",
    "XMR": "monero",
    "XRP": "xrp_ledger",
    "BTG": "bitcoin_gold",
    "ETC": "ethereum_classic",
}

ADDR_RE = re.compile(r"Digital Currency Address\s*-\s*([A-Z]{3,6})\s+([A-Za-z0-9]{25,110})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write candidate trigger stubs from OFAC recent-action triage output."
    )
    parser.add_argument("--triage", default=str(TRIAGE_PATH))
    parser.add_argument("--events-dir", default=str(EVENTS_DIR))
    parser.add_argument("--candidate-dir", default=str(CANDIDATE_DIR))
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Rewrite generated OFAC recent-action stubs if they already exist.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise SystemExit(f"{path}: expected YAML object")
    return raw


def date_from_yyyymmdd(value: str) -> str:
    if not re.fullmatch(r"\d{8}", value):
        raise ValueError(f"expected YYYYMMDD date, got {value!r}")
    return f"{value[:4]}-{value[4:6]}-{value[6:]}"


def event_index_by_ofac_date(events_dir: Path) -> dict[str, list[dict[str, str]]]:
    by_date: dict[str, list[dict[str, str]]] = {}
    if not events_dir.exists():
        return by_date
    for path in sorted(events_dir.glob("*.yaml")):
        event = load_yaml(path)
        trigger = event.get("trigger") or {}
        if trigger.get("actor") != "US_OFAC":
            continue
        timestamp = str(trigger.get("timestamp") or "")
        if len(timestamp) < 10:
            continue
        by_date.setdefault(timestamp[:10], []).append(
            {
                "id": str(event.get("id") or path.stem),
                "status": str(event.get("status") or ""),
                "research_stratum": str(event.get("research_stratum") or ""),
                "trigger_type": str(trigger.get("type") or ""),
            }
        )
    return by_date


def infer_trigger_type(title: str, promoted_events: list[dict[str, str]]) -> str:
    types = {event["trigger_type"] for event in promoted_events if event.get("trigger_type")}
    if len(types) == 1:
        return next(iter(types))
    lower = title.lower()
    if "removal" in lower or "removals" in lower:
        return "ofac_sdn_removal"
    return "ofac_sdn_designation"


def infer_stratum(trigger_type: str, promoted_events: list[dict[str, str]], rejected: bool) -> str | None:
    strata = {event["research_stratum"] for event in promoted_events if event.get("research_stratum")}
    if len(strata) == 1:
        return next(iter(strata))
    if rejected:
        return None
    if trigger_type == "ofac_sdn_removal":
        return "S2_ofac_removal"
    return "S1_ofac_sdn"


def infer_registry_status(row_status: str, promoted_events: list[dict[str, str]]) -> str:
    if promoted_events:
        return "promoted_to_event"
    if row_status == "addresses_present":
        return "candidate"
    return "screened_no_extractor_target"


def infer_target_kind(row_status: str) -> str | None:
    if row_status == "addresses_present":
        return "address_set"
    return None


def infer_chains(addresses_by_token: dict[str, Any]) -> list[str]:
    chains: list[str] = []
    for token in sorted(addresses_by_token):
        chain = TOKEN_CHAIN_MAP.get(token)
        if chain and chain not in chains:
            chains.append(chain)
    if "USDT" in addresses_by_token:
        for chain in ("ethereum", "tron"):
            if chain not in chains:
                chains.append(chain)
    return chains


def expected_layers(target_kind: str | None) -> list[str]:
    if target_kind == "address_set":
        return ["asset_onchain", "offramp_cex", "l4_frontend"]
    if target_kind == "entity":
        return ["offramp_cex", "l4_frontend"]
    return []


def extract_addresses(cache_path: Path) -> list[dict[str, str]]:
    if not cache_path.exists():
        return []
    html = cache_path.read_text(errors="ignore")
    clean = re.sub(r"<[^>]+>", " ", html)
    clean = re.sub(r"\s+", " ", clean)
    seen: set[tuple[str, str]] = set()
    addresses: list[dict[str, str]] = []
    for token, address in ADDR_RE.findall(clean):
        key = (token, address)
        if key in seen:
            continue
        seen.add(key)
        addresses.append({"token": token, "address": address})
    return sorted(addresses, key=lambda item: (item["token"], item["address"]))


def build_stub(
    row: dict[str, Any],
    promoted_events: list[dict[str, str]],
    cache_dir: Path = CACHE_DIR,
) -> dict[str, Any]:
    date_iso = date_from_yyyymmdd(str(row["date"]))
    row_status = str(row.get("status") or "")
    title = str(row.get("title_listing") or row.get("page_title") or "")
    registry_status = infer_registry_status(row_status, promoted_events)
    screened = registry_status == "screened_no_extractor_target"
    rejected = registry_status == "rejected_out_of_scope"
    outside_extracted_frame = rejected or screened
    trigger_type = infer_trigger_type(title, promoted_events)
    target_kind = infer_target_kind(row_status)
    addresses_by_token = row.get("addresses_by_token") or {}
    if not isinstance(addresses_by_token, dict):
        addresses_by_token = {}

    cache_path = cache_dir / f"{row['date']}.html"
    extracted_addresses = extract_addresses(cache_path)

    stub: dict[str, Any] = {
        "id": f"ofac-recent-action-{row['date']}",
        "registry_status": registry_status,
        "research_stratum": infer_stratum(trigger_type, promoted_events, outside_extracted_frame),
        "trigger": {
            "type": trigger_type,
            "actor": "US_OFAC",
            "timestamp": f"{date_iso}T00:00:00Z",
            "timestamp_precision": "day",
            "citation": [
                {
                    "type": "primary_legal",
                    "url": f"https://ofac.treasury.gov/recent-actions/{row['date']}",
                }
            ],
        },
        "jurisdiction": ["US"],
        "source_artifacts": [
            f"sources/ofac_sdn_diffs/recent_actions_cache/{row['date']}.html"
        ],
        "extraction": {
            "source": "sources/ofac_sdn_diffs/opensanctions/ofac-recent-actions-triage.json",
            "triage_status": row_status,
            "page_title": row.get("page_title") or "",
            "title_listing": title,
            "total_crypto_addresses": int(row.get("total_crypto_addresses") or 0),
            "addresses_by_token": addresses_by_token,
            "addresses": extracted_addresses,
            "entity_keyword_hits": row.get("entity_keyword_hits") or [],
            "cache_present": cache_path.exists(),
        },
    }

    if promoted_events:
        stub["promoted_event_id"] = [event["id"] for event in promoted_events]

    if target_kind:
        stub["target"] = {
            "kind": target_kind,
            "chains": infer_chains(addresses_by_token),
        }
        if extracted_addresses:
            stub["target"]["addresses"] = [
                item["address"] for item in extracted_addresses
            ]
        stub["expected_layers"] = expected_layers(target_kind)

    if outside_extracted_frame:
        stub["rejection_reason"] = (
            "OFAC recent-action sweep row did not expose a concrete crypto target "
            "under the current keyword/address extractor."
        )
        stub["triage_notes"] = (
            "Systematic OFAC backfill retained for selection transparency, but "
            "not counted as an in-frame trigger because the extractor found no "
            "concrete crypto target."
        )
    elif registry_status == "promoted_to_event":
        stub["triage_notes"] = (
            "Systematic OFAC backfill row is already represented by promoted "
            "event YAML: " + ", ".join(stub["promoted_event_id"])
        )
    else:
        stub["triage_notes"] = (
            "Systematic OFAC backfill candidate. Requires per-layer evidence "
            "collection and denominator classification before promotion."
        )

    return {key: value for key, value in stub.items() if value is not None}


def output_path(candidate_dir: Path, stub: dict[str, Any]) -> Path:
    file_name = f"{stub['id']}.yaml"
    if stub.get("registry_status") in {"rejected_out_of_scope", "screened_no_extractor_target"}:
        return candidate_dir / "rejected" / file_name
    return candidate_dir / file_name


def existing_stub_paths(candidate_dir: Path, stub_id: str) -> list[Path]:
    candidates = [
        candidate_dir / f"{stub_id}.yaml",
        candidate_dir / "rejected" / f"{stub_id}.yaml",
    ]
    return [path for path in candidates if path.exists()]


def materialize_candidates(
    triage_path: Path = TRIAGE_PATH,
    events_dir: Path = EVENTS_DIR,
    candidate_dir: Path = CANDIDATE_DIR,
    overwrite: bool = False,
) -> list[Path]:
    rows = json.loads(triage_path.read_text())
    if not isinstance(rows, list):
        raise SystemExit(f"{triage_path}: expected JSON array")

    by_date = event_index_by_ofac_date(events_dir)
    written: list[Path] = []
    for row in rows:
        if not isinstance(row, dict) or "date" not in row:
            raise SystemExit(f"{triage_path}: malformed triage row {row!r}")
        date_iso = date_from_yyyymmdd(str(row["date"]))
        stub = build_stub(row, by_date.get(date_iso, []))
        path = output_path(candidate_dir, stub)
        existing_paths = existing_stub_paths(candidate_dir, str(stub["id"]))
        if existing_paths and path not in existing_paths:
            existing = ", ".join(str(existing) for existing in existing_paths)
            raise SystemExit(
                f"{stub['id']}: existing stub is in a different registry-status "
                f"directory ({existing}); move it manually before regenerating"
            )
        if path.exists() and not overwrite:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(stub, sort_keys=False, allow_unicode=False))
        written.append(path)
    return written


def main() -> int:
    args = parse_args()
    written = materialize_candidates(
        triage_path=Path(args.triage),
        events_dir=Path(args.events_dir),
        candidate_dir=Path(args.candidate_dir),
        overwrite=args.overwrite,
    )
    print(f"[materialize_ofac_recent_action_candidates] wrote {len(written)} stubs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
