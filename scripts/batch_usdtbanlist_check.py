#!/usr/bin/env python3
"""Batch-query usdtbanlist.com for each ETH/TRX address across all draft events.

For each address, capture the usdtbanlist page under sources/http_captures/<slug>/asset-layer-check/
with body_hash, then extract BLOCKED status + freeze tx/date per address.

Output: sources/asset_layer_scan/{slug}.json with per-address freeze metadata, ready for
event YAML patching.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
import urllib.request
import urllib.parse
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
EVENTS_DIR = REPO / "events"
CAPTURES_DIR = REPO / "sources" / "http_captures"
SCAN_DIR = REPO / "sources" / "asset_layer_scan"

UA = "p1-event-db-asset-scanner/0.1 (xwy411@gmail.com)"
ETH_RE = re.compile(r"^0x[0-9a-fA-F]{40}$")
TRX_RE = re.compile(r"^T[A-Za-z0-9]{33}$")


def fetch(url: str, timeout: float = 45.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def sanitize_addr(a: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", a)


def scan_event(event_yaml: Path) -> dict:
    doc = yaml.safe_load(event_yaml.read_text())
    slug = doc["id"]
    addrs = doc.get("target", {}).get("addresses", [])
    addrs = [str(a) for a in (addrs or []) if isinstance(a, (str, int))]
    eth_addrs = [a for a in addrs if ETH_RE.match(a)]
    trx_addrs = [a for a in addrs if TRX_RE.match(a)]
    if not (eth_addrs or trx_addrs):
        return {"slug": slug, "skipped": "no ETH/TRX"}

    output_dir = CAPTURES_DIR / slug / "asset-layer-check"
    output_dir.mkdir(parents=True, exist_ok=True)
    per_addr: list[dict] = []

    for addr in eth_addrs + trx_addrs:
        url = f"https://usdtbanlist.com/address/{addr}"
        clean_addr = sanitize_addr(addr)
        fname = f"usdtbanlist.com__address-{clean_addr}.html"
        out_path = output_dir / fname
        try:
            if out_path.exists() and out_path.stat().st_size > 500:
                body = out_path.read_bytes()
            else:
                body = fetch(url)
                out_path.write_bytes(body)
                time.sleep(0.8)
        except Exception as exc:
            per_addr.append({"address": addr, "error": str(exc)})
            continue
        sha = hashlib.sha256(body).hexdigest()
        text = re.sub(r"<[^>]+>", " ", body.decode("utf-8", errors="ignore"))
        text = re.sub(r"\s+", " ", text)
        blocked = "BLOCKED" in text
        # Amount regex is permissive on decimals: matches "12", "12.5", "12.56",
        # "1,234", "1,234.567". The previous `\.\d{2}` requirement silently
        # dropped freeze rows if usdtbanlist.com ever rendered 1- or 3-decimal
        # amounts. If the HTML structure changes wholesale and no bans match,
        # `_warn_if_no_matches` surfaces a warning instead of failing silently.
        amount_pat = r"[\d,]+(?:\.\d+)?"
        frozen_m = re.search(rf"Frozen:\s+({amount_pat})\s+USD[CT]", text)
        frozen_balance = frozen_m.group(1) if frozen_m else None
        # capture all Banned rows: "Banned <amt> <TOKEN> <date>  <txprefix>"
        bans = re.findall(
            rf"Banned\s+({amount_pat})\s+(USD[CT])\s+"
            r"([A-Z][a-z]+\s+\d+,\s+\d+,\s+\d+:\d+\s+[AP]M\s+UTC)\s+"
            r"([0-9a-f]{6,10})",
            text,
        )
        if blocked and not bans and len(body) > 2000:
            print(
                f"[WARN] {addr}: page contains BLOCKED marker but no Banned rows "
                f"parsed — usdtbanlist.com HTML may have changed. "
                f"Check regex against latest page format.",
                file=sys.stderr,
            )
        # Extract full tx hashes from explorer links inside the body HTML.
        # ETH: etherscan.io/tx/0x<64hex>; TRON: tronscan.org/#/transaction/<64hex>
        body_text = body.decode("utf-8", errors="ignore")
        eth_txs = re.findall(r"etherscan\.io/tx/(0x[0-9a-f]{64})", body_text)
        tron_txs = re.findall(r"tronscan\.org/#/transaction/([0-9a-f]{64})", body_text)
        full_txs = list(dict.fromkeys(eth_txs + tron_txs))

        # Merge: match ban prefix to full tx
        freeze_events = []
        for a, t, d, txprefix in bans:
            full_tx = next(
                (full for full in full_txs
                 if full.lstrip("0x").startswith(txprefix) or txprefix in full),
                None,
            )
            freeze_events.append({
                "token": t, "amount": a, "date_utc": d,
                "tx_prefix": txprefix, "tx_full": full_tx,
                "explorer_url": (
                    f"https://etherscan.io/tx/{full_tx}" if full_tx and full_tx.startswith("0x")
                    else f"https://tronscan.org/#/transaction/{full_tx}" if full_tx
                    else None
                ),
            })
        per_addr.append({
            "address": addr,
            "blocked": blocked,
            "frozen_balance": frozen_balance,
            "freeze_events": freeze_events,
            "body_sha256": sha,
            "body_path": str(out_path.relative_to(REPO)),
        })

    result = {
        "slug": slug,
        "eth_addrs_scanned": len(eth_addrs),
        "trx_addrs_scanned": len(trx_addrs),
        "per_address": per_addr,
    }
    SCAN_DIR.mkdir(parents=True, exist_ok=True)
    (SCAN_DIR / f"{slug}.json").write_text(json.dumps(result, indent=2))
    return result


def main() -> None:
    results = []
    for yml in sorted(EVENTS_DIR.glob("*.yaml")):
        r = scan_event(yml)
        results.append(r)
        blocked_count = sum(1 for a in r.get("per_address", []) if a.get("blocked"))
        total = r.get("eth_addrs_scanned", 0) + r.get("trx_addrs_scanned", 0)
        print(f"{r['slug']}: {blocked_count}/{total} blocked  {r.get('skipped', '')}")
    (SCAN_DIR / "_summary.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
