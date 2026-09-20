import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from analyze_historical_interface_matches import compare
from collect_issuer_cohort_snapshots import read_json


def fixture():
    directory = ROOT / "analysis/historical_interface_verification/v1"
    entry = read_json(directory / "inventory.json")["entries"][0]
    data = read_json(directory / "captures" / f"{entry['address']}_verification/attempt_1/response.body")
    return entry, data


def test_metadata_difference_is_not_promoted_to_exact_reproduction():
    entry, data = fixture()
    result = compare(entry, data)
    assert result["indexed_runtime_equals_observed_historical_bytes"]
    assert result["sourcify_runtime_match_literal"] == "match"
    assert result["byte_comparison"]["difference_confined_to_declared_cbor_suffix"]
    assert not result["reported_recompiled_full_runtime_equals_indexed_runtime"]
    assert not result["exact_source_metadata_verification_established"]
    assert not result["historical_implementation_bytecode_reproduced"]
    assert result["compatible_read_abi_entry_present"]


def test_wrong_address_or_executable_byte_is_not_accepted():
    entry, data = fixture()
    bad = copy.deepcopy(data)
    bad["address"] = "0x" + "0" * 40
    assert not compare(entry, bad)["indexed_runtime_equals_observed_historical_bytes"]
    bad = copy.deepcopy(data)
    raw = bad["runtimeBytecode"]["recompiledBytecode"]
    bad["runtimeBytecode"]["recompiledBytecode"] = "0x00" + raw[4:]
    assert not compare(entry, bad)["byte_comparison"]["difference_confined_to_declared_cbor_suffix"]
