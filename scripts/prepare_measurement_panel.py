#!/usr/bin/env python3
"""Capture primary panel sources and emit a machine-prepared verification sidecar.

This does not freeze the protected cohort manifest or certify historical
implementation/availability. Successful content assertions are narrow, replayable
source checks, not independent human adjudication.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from measurement_pilot import CONTRACTS, ROOT, digest, dump, http_once, save_attempt, utc_now

SOURCES = [
    ("circle_addresses", "https://developers.circle.com/stablecoins/usdc-contract-addresses", [CONTRACTS["usdc"]["address"]]),
    ("circle_blacklist_source", "https://raw.githubusercontent.com/circlefin/stablecoin-evm/master/contracts/v1/Blacklistable.sol", ["event Blacklisted(address indexed", "event UnBlacklisted(address indexed", "function isBlacklisted"]),
    ("circle_proxy_source", "https://raw.githubusercontent.com/circlefin/stablecoin-evm/master/contracts/upgradeability/UpgradeabilityProxy.sol", ["org.zeppelinos.proxy.implementation", "IMPLEMENTATION_SLOT"]),
    ("tether_addresses", "https://tether.to/en/supported-protocols/", [CONTRACTS["usdt"]["address"]]),
    ("tether_verified_contract", "https://etherscan.io/address/0xdAC17F958D2ee523a2206206994597C13D831ec7#code", ["event AddedBlackList(address", "event RemovedBlackList(address", "isBlackListed", "deprecated", "upgradedAddress"]),
    ("ethereum_json_rpc", "https://ethereum.org/en/developers/docs/apis/json-rpc/", ["eth_getLogs", "eth_getStorageAt"]),
    ("flashbots_docs", "https://docs.flashbots.net/flashbots-protect/quick-start", ["rpc.flashbots.net"]),
    ("flashbots_public_repo", "https://raw.githubusercontent.com/flashbots/rpc-endpoint/main/README.md", ["rpc.flashbots.net"]),
    ("infura_docs", "https://docs.metamask.io/services/get-started/", ["API key"]),
    ("alchemy_endpoints", "https://www.alchemy.com/rpc/ethereum", ["https://eth-mainnet.g.alchemy.com/public"]),
    ("quicknode_endpoints", "https://www.quicknode.com/docs/ethereum/endpoints", ["quiknode.pro", "auth-token"]),
    ("coinbase_sanctions_disclosure", "https://www.coinbase.com/blog/using-crypto-tech-to-promote-sanctions-compliance", ["sanctions"]),
    ("coinbase_index", "https://www.coinbase.com/blog", ["Coinbase"]),
    ("kraken_sanctions_disclosure", "https://blog.kraken.com/news/strengthening-sanctions-compliance", ["sanctions"]),
    ("kraken_index", "https://blog.kraken.com/", ["Kraken"]),
    ("binance_announcement_index", "https://www.binance.com/en/support/announcement", ["announcement"]),
]


def capture_source(spec, root: Path, transport=http_once) -> dict:
    key, url, assertions = spec
    attempts = []
    for number in (1, 2):
        record = save_attempt(root / key / f"attempt_{number}", transport(url), None, url)
        text = html.unescape(record["body"].decode("utf-8", errors="replace"))
        # Collapse whitespace for declarations split across HTML/source lines.
        normalized = " ".join(text.split()).lower()
        matches = {assertion: assertion.lower() in normalized for assertion in assertions}
        attempts.append({"number": number, "http_status": record["http_status"], "transport_error": record["transport_error"], "body_sha256": record["response_body_sha256"], "content_assertions": matches})
        if record["http_status"] == 200 and not record["transport_error"] and all(matches.values()):
            capture_path = root / key / f"attempt_{number}"
            try:
                capture_path = capture_path.relative_to(ROOT)
            except ValueError:
                pass
            return {"source_id": key, "url": url, "status": "captured_content_assertions_pass", "capture_path": str(capture_path), "attempts": attempts}
        if number == 1:
            time.sleep(0.2)
    return {"source_id": key, "url": url, "status": "unavailable_or_content_unverified", "attempts": attempts}


def prepare(root: Path, transport=http_once) -> dict:
    if (root / "verified_panel.json").exists():
        raise ValueError("Refusing to overwrite a panel sidecar; use a new --out-dir")
    root.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        sources = list(pool.map(lambda spec: capture_source(spec, root, transport), SOURCES))
    source_map = {row["source_id"]: row for row in sources}
    def passed(*keys):
        return all(source_map[key]["status"] == "captured_content_assertions_pass" for key in keys)
    panel = {
        "prepared_at_utc": utc_now(), "status": "machine_prepared_current_source_checks_historical_verification_pending",
        "independent_human_validation": False, "main_cohort_execution_manifest_frozen": False,
        "protected_proposed_manifest_unchanged": "analysis/validation_cohort/panel_manifest.json",
        "sources": sources,
        "contracts": {name: {**contract,
            "canonical_address_source": "circle_addresses" if name == "usdc" else "tether_addresses",
            "interface_source": "circle_blacklist_source" if name == "usdc" else "tether_verified_contract",
            "address_source_match": passed("circle_addresses" if name == "usdc" else "tether_addresses"),
            "interface_source_match": passed("circle_blacklist_source" if name == "usdc" else "tether_verified_contract"),
            "historical_implementation_verified": False,
            "historical_caveat": "Proxy implementation must be resolved at each historical block and its deployed ABI verified; current master source is not historical bytecode proof." if name == "usdc" else "Legacy contract has deprecated/upgradedAddress forwarding; verify these historical values. Etherscan source for issuer-linked canonical address is a secondary verification service, not independent bytecode reproduction.",
        } for name, contract in CONTRACTS.items()},
        "signature_hash_method": "Ethereum Keccak-256 of canonical signatures; selectors use first 4 bytes. Not NIST SHA3-256. Constants reproducible with Crypto.Hash.keccak; collector needs no crypto dependency.",
        "rpc_panel": [
            {"name": "Flashbots Protect", "source_ids": ["flashbots_docs", "flashbots_public_repo"], "endpoint": "https://rpc.flashbots.net", "credentials": "none documented for this public endpoint", "current_documentation_match": passed("flashbots_docs"), "historical_existence_interval": "pending", "caveat": "Current endpoint and repository describe current interfaces; read calls do not test historical transaction filtering or production policy."},
            {"name": "Infura", "source_ids": ["infura_docs"], "endpoint_template": "https://mainnet.infura.io/v3/{API_KEY}", "credentials": "API key; unavailable in this no-key pilot", "current_documentation_match": passed("infura_docs"), "historical_existence_interval": "pending", "pilot_status": "not_queried_credentials_required"},
            {"name": "Alchemy", "source_ids": ["alchemy_endpoints"], "endpoint": "https://eth-mainnet.g.alchemy.com/public", "credentials": "none for documented public endpoint", "current_documentation_match": passed("alchemy_endpoints"), "historical_existence_interval": "pending", "caveat": "Public access tier is distinct from keyed archive access; historical method availability must be tested, not assumed."},
            {"name": "QuickNode", "source_ids": ["quicknode_endpoints"], "endpoint_template": "https://{endpoint}.quiknode.pro/{auth-token}/", "credentials": "per-account endpoint/token; unavailable in this no-key pilot", "current_documentation_match": passed("quicknode_endpoints"), "historical_existence_interval": "pending", "pilot_status": "not_queried_credentials_required"},
        ],
        "disclosure_panel": [
            {"name": "Coinbase", "source_ids": ["coinbase_index", "coinbase_sanctions_disclosure"], "index_url": "https://www.coinbase.com/blog", "current_source_match": passed("coinbase_index"), "historical_archive_completeness": "unverified"},
            {"name": "Kraken", "source_ids": ["kraken_index", "kraken_sanctions_disclosure"], "index_url": "https://blog.kraken.com/", "current_source_match": passed("kraken_index"), "historical_archive_completeness": "unverified"},
            {"name": "Binance", "source_ids": ["binance_announcement_index"], "index_url": "https://www.binance.com/en/support/announcement", "current_source_match": passed("binance_announcement_index"), "historical_archive_completeness": "unverified"},
        ],
        "disclosure_limit": "Captured current index/policy pages establish public source availability only. No historical archive sweep, target-specific negative, private account outcome, or historical service-access outcome is established.",
        "pilot_contract_prerequisites_met": passed("circle_addresses", "circle_blacklist_source", "circle_proxy_source", "tether_addresses", "tether_verified_contract"),
        "still_required_for_T4": ["T3 frame reconciliation and independently checked eligibility", "historical implementation/ABI and provider existence intervals", "historical archive completeness", "independent source and action-stage adjudication", "frozen main-cohort execution manifest"],
    }
    dump(root / "verified_panel.json", panel)
    return panel


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "sources/measurement_panel")
    args = parser.parse_args()
    panel = prepare(args.out_dir)
    print(json.dumps({"pilot_contract_prerequisites_met": panel["pilot_contract_prerequisites_met"], "sources": [{"id": row["source_id"], "status": row["status"]} for row in panel["sources"]]}, indent=2))


if __name__ == "__main__":
    main()
