#!/usr/bin/env python3
"""Offline byte/ABI comparison of frozen historical inventory and captured metadata.

Preserves Sourcify's reported match level. No compilation or network access.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from collect_issuer_cohort_snapshots import immutable, read_json
from measurement_pilot import ROOT, digest
from prepare_historical_interface_inventory import push4_offsets


def compare(entry, data):
    runtime = data.get("runtimeBytecode", {})
    onchain = bytes.fromhex(runtime.get("onchainBytecode", "0x")[2:])
    compiled = bytes.fromhex(runtime.get("recompiledBytecode", "0x")[2:])
    identity = str(data.get("chainId")) == "1" and str(data.get("address", "")).lower() == entry["address"]
    result = {"address": entry["address"], "issuer": entry["issuer"], "source_identity_matches_inventory": identity,
              "historical_runtime_bytes_sha256": entry["runtime_bytes_sha256"],
              "sourcify_indexed_onchain_runtime_sha256": digest(onchain),
              "sourcify_reported_recompiled_runtime_sha256": digest(compiled),
              "indexed_runtime_equals_observed_historical_bytes": bool(identity and onchain and digest(onchain) == entry["runtime_bytes_sha256"]),
              "reported_recompiled_full_runtime_equals_indexed_runtime": bool(onchain and onchain == compiled),
              "sourcify_runtime_match_literal": data.get("runtimeMatch"),
              "sourcify_creation_match_literal": data.get("creationMatch"),
              "sourcify_verified_at": data.get("verifiedAt"),
              "sourcify_compilation": data.get("compilation"),
              "historical_implementation_bytecode_reproduced": False,
              "exact_source_metadata_verification_established": False,
              "human_reference_complete": False}
    aux = runtime.get("cborAuxdata", {})
    transformations = runtime.get("transformations", [])
    values = runtime.get("transformationValues", {}).get("cborAuxdata", {})
    comparison = {"comparison_available": False}
    if len(aux) == 1 and len(transformations) == 1:
        key, field = next(iter(aux.items()))
        transformation = transformations[0]
        offset = field["offset"]
        declared_compiled_suffix = bytes.fromhex(field["value"][2:])
        declared_onchain_suffix = bytes.fromhex(values.get(key, "0x")[2:])
        suffixes_match_declarations = (compiled[offset:] == declared_compiled_suffix and onchain[offset:] == declared_onchain_suffix)
        declared_suffix_lengths_valid = all(len(value) >= 2 and int.from_bytes(value[-2:], "big") + 2 == len(value)
                                            for value in (declared_compiled_suffix, declared_onchain_suffix))
        declaration_valid = (transformation.get("type") == "replace" and transformation.get("reason") == "cborAuxdata"
                             and transformation.get("offset") == offset and 0 < offset <= min(len(onchain), len(compiled))
                             and suffixes_match_declarations and declared_suffix_lengths_valid)
        comparison = {"comparison_available": True, "prefix_start_byte_inclusive": 0, "prefix_end_byte_exclusive": offset,
                      "onchain_runtime_bytes": len(onchain), "reported_recompiled_runtime_bytes": len(compiled),
                      "onchain_prefix_sha256": digest(onchain[:offset]), "reported_recompiled_prefix_sha256": digest(compiled[:offset]),
                      "onchain_suffix_start_byte_inclusive": offset, "onchain_suffix_end_byte_exclusive": len(onchain),
                      "reported_recompiled_suffix_end_byte_exclusive": len(compiled),
                      "onchain_suffix_sha256": digest(onchain[offset:]), "reported_recompiled_suffix_sha256": digest(compiled[offset:]),
                      "declaration_and_length_checks_pass": declaration_valid,
                      "prefix_bytes_identical": onchain[:offset] == compiled[:offset],
                      "difference_confined_to_declared_cbor_suffix": bool(declaration_valid and onchain[:offset] == compiled[:offset])}
    result["byte_comparison"] = comparison
    function_name = entry["expected_read_signature"].split("(")[0]
    functions = [f for f in data.get("abi", []) if f.get("type") == "function" and f.get("name") == function_name
                 and [p["type"] for p in f.get("inputs", [])] == ["address"] and [p["type"] for p in f.get("outputs", [])] == ["bool"]
                 and (f.get("stateMutability") in ("view", "pure") or f.get("constant") is True)]
    result["expected_read_signature"] = entry["expected_read_signature"]
    result["expected_selector"] = entry["expected_selector"]
    result["compatible_read_abi_entries"] = functions
    result["compatible_read_abi_entry_present"] = len(functions) == 1
    result["indexed_runtime_push4_selector_offsets"] = push4_offsets(runtime.get("onchainBytecode", "0x"), entry["expected_selector"])
    result["observation_count"] = len(entry["observations"])
    result["observed_block_range_inclusive"] = [min(o["block_number"] for o in entry["observations"]), max(o["block_number"] for o in entry["observations"])]
    return result


def analyze(directory):
    inventory = read_json(directory / "inventory.json")
    entries = []
    for entry in inventory["entries"]:
        capture = directory / "captures" / f"{entry['address']}_verification" / "attempt_1"
        metadata = read_json(capture / "capture.json")
        body = (capture / "response.body").read_bytes()
        if metadata["response_body_sha256"] != digest(body):
            raise ValueError("Metadata capture hash mismatch")
        report = compare(entry, read_json(capture / "response.body"))
        report.update(capture_path=str(capture.relative_to(directory)), response_body_sha256=digest(body),
                      source_url=metadata["requested_url"])
        entries.append(report)
    report = {"status": "offline_historical_runtime_and_abi_association_comparison",
              "inventory_sha256": digest((directory / "inventory.json").read_bytes()),
              "lookup_summary_sha256": digest((directory / "lookup_summary.json").read_bytes()),
              "analysis_script_sha256": digest(Path(__file__).read_bytes()), "entries": entries,
              "indexed_runtime_hash_matches": sum(e["indexed_runtime_equals_observed_historical_bytes"] for e in entries),
              "compatible_abi_and_push4_selector_matches": sum(e["compatible_read_abi_entry_present"] and bool(e["indexed_runtime_push4_selector_offsets"]) for e in entries),
              "exact_source_metadata_verification_established": False,
              "historical_implementation_bytecode_reproduced": False,
              "full_snapshot_independent_chain_reconciliation_complete": False,
              "interpretation": "Reports Sourcify's literal match level and separately compares captured indexed bytecode with earlier historical RPC bytes. Agreement before a declared CBOR suffix supports only executable-prefix agreement and ABI compatibility. No exact/full source reproduction, compiler execution, behavioral proof, or full independent chain reconciliation is claimed."}
    immutable(directory / "association_report.json", report)
    immutable(directory / "analysis_source.py", Path(__file__).read_bytes(), raw=True)
    return report


def main():
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=ROOT / "analysis/historical_interface_verification/v1")
    args = parser.parse_args()
    print(json.dumps(analyze(args.directory), indent=2))


if __name__ == "__main__":
    main()
