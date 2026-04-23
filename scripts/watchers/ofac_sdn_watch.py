#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""OFAC SDN XML watcher.

Usage:
    python3 scripts/watchers/ofac_sdn_watch.py

Fetches the current SDN XML, compares it to the previous snapshot archived under
sources/ofac_sdn_diffs/, and writes a candidate_triggers stub for each newly
added or newly removed entry that matches crypto keywords or a 0x address
pattern.

Scheduled cadence: every 6 hours (see methodology.md §8 for the full watcher protocol).
"""

from __future__ import annotations

import argparse
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import urllib.request
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SDN_URL = "https://www.treasury.gov/ofac/downloads/sdn.xml"
SNAPSHOT_DIR = REPO_ROOT / "sources" / "ofac_sdn_diffs"
CANDIDATE_DIR = REPO_ROOT / "candidate_triggers"

CRYPTO_KEYWORDS = (
    "virtual currency",
    "digital currency",
    "cryptocurrency",
    "digital asset",
    "mixer",
    "blockchain",
)
ETH_ADDR_RE = re.compile(r"0x[0-9a-fA-F]{40}")
USER_AGENT = "p1-event-db-watcher/0.1 (contact: xwy411@gmail.com)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OFAC SDN XML watcher.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and diff, but do not write candidate_triggers stubs.",
    )
    return parser.parse_args()


def fetch_sdn_xml(timeout: float = 60.0) -> bytes:
    req = urllib.request.Request(SDN_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def entry_ids(xml_text: bytes) -> dict[str, str]:
    """Map SDN entry uid -> a compact textual signature containing keywords."""
    entries: dict[str, str] = {}
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return entries
    # Namespaced tags look like {ns}sdnEntry. We match by localname.
    for elem in root.iter():
        if not elem.tag.endswith("sdnEntry"):
            continue
        uid = ""
        texts: list[str] = []
        for child in elem.iter():
            if child.tag.endswith("uid") and child.text:
                uid = child.text.strip()
            if child.text and child.text.strip():
                texts.append(child.text.strip())
        if uid:
            entries[uid] = " | ".join(texts)
    return entries


def matches_crypto(signature: str) -> bool:
    lower = signature.lower()
    if any(k in lower for k in CRYPTO_KEYWORDS):
        return True
    if ETH_ADDR_RE.search(signature):
        return True
    return False


def write_candidate_stub(uid: str, signature: str, direction: str, today: str, new_xml_hash: str, dry_run: bool) -> Path | None:
    slug_piece = re.sub(r"[^A-Za-z0-9-]", "-", signature[:60]).strip("-").lower() or uid
    stub_name = f"{today}-ofac-sdn-{direction}-{uid}-{slug_piece[:40]}.yaml"
    stub_path = CANDIDATE_DIR / stub_name
    stub: dict[str, Any] = {
        "origin": "agent_draft",
        "watcher": "ofac_sdn_watch",
        "observed_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "direction": direction,  # "added" or "removed"
        "sdn_uid": uid,
        "sdn_snapshot_sha256": new_xml_hash,
        "sdn_entry_signature": signature[:500],
    }
    if dry_run:
        print(f"[dry-run] would write {stub_path}")
        return None
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    stub_path.write_text(yaml.safe_dump(stub, sort_keys=False))
    return stub_path


def main() -> int:
    args = parse_args()
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        xml_bytes = fetch_sdn_xml()
    except Exception as exc:  # pragma: no cover
        print(f"[FAIL] could not fetch SDN XML: {exc}")
        return 2
    new_hash = hashlib.sha256(xml_bytes).hexdigest()

    new_snapshot = SNAPSHOT_DIR / f"{today}.xml"
    if not new_snapshot.exists():
        new_snapshot.write_bytes(xml_bytes)
        print(f"[OK] new snapshot {new_snapshot.name} ({len(xml_bytes)} bytes, sha256={new_hash[:12]}…)")

    # Find previous snapshot for diff
    previous = sorted(p for p in SNAPSHOT_DIR.glob("*.xml") if p.name != new_snapshot.name)
    if not previous:
        print("[INFO] no previous snapshot; nothing to diff yet.")
        return 0

    prev_snapshot = previous[-1]
    old_ids = entry_ids(prev_snapshot.read_bytes())
    new_ids = entry_ids(xml_bytes)

    added = [(uid, sig) for uid, sig in new_ids.items() if uid not in old_ids]
    removed = [(uid, sig) for uid, sig in old_ids.items() if uid not in new_ids]

    relevant_added = [(u, s) for u, s in added if matches_crypto(s)]
    relevant_removed = [(u, s) for u, s in removed if matches_crypto(s)]

    print(f"[INFO] added {len(added)} entries (crypto-relevant: {len(relevant_added)})")
    print(f"[INFO] removed {len(removed)} entries (crypto-relevant: {len(relevant_removed)})")

    for uid, sig in relevant_added:
        write_candidate_stub(uid, sig, "added", today, new_hash, args.dry_run)
    for uid, sig in relevant_removed:
        write_candidate_stub(uid, sig, "removed", today, new_hash, args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
