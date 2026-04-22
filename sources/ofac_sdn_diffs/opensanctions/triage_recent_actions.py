#!/usr/bin/env python3
"""Triage OFAC Recent Actions crypto-keyword candidates.

For each date in ofac-recent-actions-crypto-candidates.json:
  1. GET ofac.treasury.gov/recent-actions/YYYYMMDD
  2. Cache the HTML under sources/ofac_sdn_diffs/recent_actions_cache/YYYYMMDD.html
  3. Extract Digital Currency Address counts per token + entity keyword hits
  4. Write ofac-recent-actions-triage.json with classification + counts.
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "sources" / "ofac_sdn_diffs" / "opensanctions" / "ofac-recent-actions-crypto-candidates.json"
CACHE_DIR = ROOT / "sources" / "ofac_sdn_diffs" / "recent_actions_cache"
OUT = ROOT / "sources" / "ofac_sdn_diffs" / "opensanctions" / "ofac-recent-actions-triage.json"

HEADERS = {"User-Agent": "p1-event-db-watcher/0.1 (xwy411@gmail.com)"}

ADDR_RE = re.compile(r"Digital Currency Address\s*-\s*([A-Z]{3,6})\s+([A-Za-z0-9]{25,110})")
ENTITY_KEYWORDS = [
    "tornado cash", "bitzlato", "garantex", "hydra market", "hydra (",
    "blender.io", "blender ", "chatex", "suex", "sinbad.io", "sinbad ",
    "cryptex", "lazarus", "samourai", "chipmixer", "pm2btc",
    "predatorpay", "ransomware", "darknet", "mixer", "kucoin",
    "huobi", "binance", "rusdex",
]


def fetch(date: str) -> str:
    cache = CACHE_DIR / f"{date}.html"
    if cache.exists() and cache.stat().st_size > 0:
        return cache.read_text(errors="ignore")
    url = f"https://ofac.treasury.gov/recent-actions/{date}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8", errors="ignore")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache.write_text(body)
    time.sleep(1.1)
    return body


def analyze(html: str) -> dict:
    clean = re.sub(r"<[^>]+>", " ", html)
    clean = re.sub(r"\s+", " ", clean)
    matches = ADDR_RE.findall(clean)
    by_token_unique: dict[str, set[str]] = {}
    for tok, addr in matches:
        by_token_unique.setdefault(tok, set()).add(addr)
    token_counts = {t: len(a) for t, a in by_token_unique.items()}
    total_addrs = sum(token_counts.values())
    lower = clean.lower()
    entity_hits = [k for k in ENTITY_KEYWORDS if k in lower]
    # page title from <title>...</title>
    title_m = re.search(r"<title>([^<]+)</title>", html)
    title = title_m.group(1).strip() if title_m else ""
    return {
        "page_title": title,
        "total_crypto_addresses": total_addrs,
        "addresses_by_token": token_counts,
        "entity_keyword_hits": entity_hits,
    }


def main() -> None:
    candidates = json.loads(SRC.read_text())
    results = []
    for i, c in enumerate(candidates, 1):
        date = c["date"]
        try:
            html = fetch(date)
        except Exception as exc:
            print(f"[{i}/{len(candidates)}] {date} FAIL {exc}")
            results.append({**c, "error": str(exc)})
            continue
        info = analyze(html)
        status = "addresses_present" if info["total_crypto_addresses"] > 0 else (
            "entity_mentions_no_addrs" if info["entity_keyword_hits"] else "no_crypto_content"
        )
        row = {
            "date": date,
            "title_listing": c.get("title", ""),
            "status": status,
            **info,
        }
        results.append(row)
        print(f"[{i}/{len(candidates)}] {date} {status} addrs={info['total_crypto_addresses']} ents={len(info['entity_keyword_hits'])}")

    results.sort(key=lambda r: r["date"])
    OUT.write_text(json.dumps(results, indent=2, ensure_ascii=False, default=str))
    # summary
    by_status = Counter(r.get("status", "error") for r in results)
    print("\nStatus distribution:")
    for k, v in by_status.most_common():
        print(f"  {k}: {v}")
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
