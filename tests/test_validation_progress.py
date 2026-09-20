import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_validation_progress as progress


def write(root, path, data, lines=False):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("".join(json.dumps(row) + "\n" for row in data) if lines else progress.serialized(data))


def change(root, path, mutate):
    file = root / path
    data = json.loads(file.read_text())
    mutate(data)
    write(root, path, data)


@pytest.fixture
def cohort(tmp_path):
    frame = {"enumerated_action_urls": 2, "retrieved_action_pages": 2, "unretrieved_action_pages": 0,
             "body_parsed_pages": 2, "source_input_hash": "sha256:synthetic-frozen-frame"}
    write(tmp_path, progress.FRAME, frame)
    issuers = [{"symbol": "USDC", "chain_id": 1, "contract_address": "0x" + "a" * 40},
               {"symbol": "USDT", "chain_id": 1, "contract_address": "0x" + "b" * 40}]
    manifest = {"status": "machine_frozen_not_human_adjudicated", "human_gold": False, "issuers": issuers,
                "inputs": {"source_frame_input_hash": frame["source_input_hash"],
                           "source_frame_summary_sha256": progress.digest((tmp_path / progress.FRAME).read_bytes())},
                "counts": {"measurement_units": 2, "issuer_query_units": 4, "unique_action_urls": 2}}
    write(tmp_path, f"{progress.CANDIDATES}/manifest.json", manifest)
    measurements, units = [], []
    pair_values = {"usdc": [(0, 1), (1, 0)], "usdt": [(0, 0), (1, 1)]}
    for number in range(2):
        measurement = {"measurement_unit_id": f"m{number}", "normalized_address": "0x" + str(number + 1) * 40,
                       "action_url": f"https://ofac.example/action{number}", "proposed_direction": "addition",
                       "window_start_inclusive_utc": "2024-01-01T00:00:00Z", "window_end_exclusive_utc": "2024-02-01T00:00:00Z"}
        measurements.append(measurement)
        wid = f"w{number}"
        start = progress.timestamp(measurement["window_start_inclusive_utc"])
        end = progress.timestamp(measurement["window_end_exclusive_utc"])
        block_hash = lambda n: "0x" + format(n, "064x")
        write(tmp_path, f"{progress.ENDPOINTS}/windows/{wid}.json", {"window_id": wid, "action_url": measurement["action_url"],
            "start_inclusive_utc": measurement["window_start_inclusive_utc"], "end_exclusive_utc": measurement["window_end_exclusive_utc"], "status": "endpoint_collection_attempted"})
        write(tmp_path, f"{progress.ENDPOINTS}/boundaries/{wid}.json", {
            "start": {"requested_timestamp": start, "before_block": 9, "at_or_after_block": 10, "before_timestamp": start-12,
                      "at_or_after_timestamp": start, "before_hash": block_hash(9), "at_or_after_hash": block_hash(10)},
            "end": {"requested_timestamp": end, "before_block": 11, "at_or_after_block": 12, "before_timestamp": start+3600,
                    "at_or_after_timestamp": end, "before_hash": block_hash(11), "at_or_after_hash": block_hash(12)}})
        for issuer in issuers:
            name = issuer["symbol"].lower()
            unit = {**measurement, "issuer_query_id": f"m{number}_{name}", "issuer": issuer}
            units.append(unit)
            for point, label in enumerate(("window_first_block", "window_last_block")):
                snapshot = {"issuer_query_id": unit["issuer_query_id"], "measurement_unit_id": measurement["measurement_unit_id"],
                            "action_url": measurement["action_url"], "target_address": measurement["normalized_address"],
                            "issuer": name, "snapshot": label, "block_number": 10 + point,
                            "window_id": wid, "block_hash": block_hash(10 + point), "rpc_code_and_forwarding_prerequisites_pass": True,
                            "timestamp": progress.timestamp("2024-01-01T00:00:00Z") + point * 3600,
                            "state_query_status": "valid_rpc_response", "returned_blacklist_word": pair_values[name][number][point],
                            "full_window_response_classification": None}
                write(tmp_path, f"{progress.ENDPOINTS}/snapshots/{unit['issuer_query_id']}_{label}.json", snapshot)
    write(tmp_path, f"{progress.CANDIDATES}/measurement_units.jsonl", measurements, lines=True)
    write(tmp_path, f"{progress.CANDIDATES}/issuer_query_units.jsonl", units, lines=True)
    endpoint = {"recorded_snapshots": 8, "valid_endpoint_snapshots": 8, "issuer_units_with_two_valid_snapshots": 4,
                "measurement_units_with_four_valid_snapshots": 2, "planned_issuer_query_units": 4, "planned_measurement_units": 2,
                "issuer_units_incomplete_or_gap": [], "measurement_units_incomplete_or_gap": [], "endpoint_snapshot_campaign_complete": True,
                "logical_queries_reserved": 12, "http_attempts_captured": 12, "action_window_records": 2, "full_window_response_classification": None}
    write(tmp_path, f"{progress.ENDPOINTS}/summary.json", endpoint)
    interface = {"entries": [{"address": issuers[0]["contract_address"], "historical_runtime_bytes_sha256": "sha256:code",
                             "indexed_runtime_equals_observed_historical_bytes": True, "compatible_read_abi_entry_present": True,
                             "indexed_runtime_push4_selector_offsets": [10], "sourcify_runtime_match_literal": "match"}],
                 "indexed_runtime_hash_matches": 1, "compatible_abi_and_push4_selector_matches": 1,
                 "exact_source_metadata_verification_established": False, "historical_implementation_bytecode_reproduced": False}
    write(tmp_path, progress.INTERFACE, interface)
    disclosure = {"status": "machine_collected_human_adjudication_pending", "source_action_urls": 2, "candidate_target_units": 2,
                  "operator_action_windows": 2, "candidate_target_operator_units": 2,
                  "operators": [{"operator": "example", "action_windows": 2, "target_unit_outcomes": {"gap": 1, "no_disclosure_found_under_enumerated_archive": 1}}],
                  "outcome_counts": {"gap": 1, "no_disclosure_found_under_enumerated_archive": 1},
                  "negative_scope": "No exact mention in one enumerated archive; not absence of enforcement.",
                  "private_account_action_measured": False, "human_reference_complete": False}
    write(tmp_path, progress.DISCLOSURE, disclosure)
    return tmp_path


def test_recomputed_pairs_determinism_and_pending_not_zero(cohort, monkeypatch):
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "100")
    first = progress.build(cohort)
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "200")
    second = progress.build(cohort)
    assert first == second
    assert first["endpoint_contrasts"]["pair_counts"] == {
        "usdc": {"0/0": 0, "0/1": 1, "1/0": 1, "1/1": 0},
        "usdt": {"0/0": 1, "0/1": 0, "1/0": 0, "1/1": 1}}
    assert first["event_logs"]["index_stream_collection"]["metrics"] is None
    assert first["ooni"]["raw_measurements"]["status"] == "pending"
    assert first["human_reference"]["independently_adjudicated_label_count"] is None
    assert "\\ProgressLogAccepted}{pending}" in progress.tex(first)
    assert "\\ProgressUSDCZeroOne}{1}" in progress.tex(first)
    assert progress.markdown(first) == progress.markdown(second)
    assert progress.tex(first) == progress.tex(second)
    assert all("sha256" in record for record in first["inputs"].values())


@pytest.mark.parametrize("mutation", ["count", "foreign", "filename", "window", "interior_block", "prerequisite", "wrong_window"])
def test_endpoint_mismatches_are_rejected(cohort, mutation):
    path = f"{progress.ENDPOINTS}/snapshots/m0_usdc_window_first_block.json"
    if mutation == "count":
        change(cohort, f"{progress.ENDPOINTS}/summary.json", lambda r: r.update(recorded_snapshots=9))
    elif mutation == "foreign":
        change(cohort, path, lambda r: r.update(issuer_query_id="unknown"))
    elif mutation == "filename":
        (cohort / path).rename(cohort / progress.ENDPOINTS / "snapshots/stray_copy.json")
    elif mutation == "window":
        change(cohort, path, lambda r: r.update(timestamp=progress.timestamp("2024-02-01T00:00:00Z")))
    elif mutation == "interior_block":
        change(cohort, path, lambda r: r.update(block_number=11, timestamp=r["timestamp"]+3600))
    elif mutation == "prerequisite":
        change(cohort, path, lambda r: r.update(rpc_code_and_forwarding_prerequisites_pass=False))
    else:
        change(cohort, path, lambda r: r.update(window_id="w1"))
    with pytest.raises(ValueError):
        progress.build(cohort)


def test_partial_pairs_are_not_imputed_to_zero_states(cohort):
    path = f"{progress.ENDPOINTS}/snapshots/m0_usdc_window_first_block.json"
    change(cohort, path, lambda r: r.update(state_query_status="gap", returned_blacklist_word=None))
    change(cohort, f"{progress.ENDPOINTS}/summary.json", lambda r: r.update(valid_endpoint_snapshots=7,
        issuer_units_with_two_valid_snapshots=3, measurement_units_with_four_valid_snapshots=1,
        issuer_units_incomplete_or_gap=["m0_usdc"], measurement_units_incomplete_or_gap=["m0"], endpoint_snapshot_campaign_complete=False))
    result = progress.build(cohort)
    assert result["endpoint_contrasts"]["status"] == "partial_endpoint_pairs"
    assert sum(result["endpoint_contrasts"]["pair_counts"]["usdc"].values()) == 1
    assert result["endpoint_contrasts"]["pair_counts"]["usdc"]["0/1"] == 0
    assert result["endpoint_contrasts"]["issuer_units_incomplete_or_gap"] == ["m0_usdc"]


def test_source_and_crossing_integrity(cohort):
    manifest = f"{progress.CANDIDATES}/manifest.json"
    change(cohort, manifest, lambda r: r["inputs"].update(source_frame_input_hash="different"))
    with pytest.raises(ValueError, match="source frame identity"):
        progress.build(cohort)
    change(cohort, manifest, lambda r: r["inputs"].update(source_frame_input_hash="sha256:synthetic-frozen-frame"))
    path = cohort / progress.CANDIDATES / "issuer_query_units.jsonl"
    path.write_text(path.read_text() + path.read_text().splitlines()[0] + "\n")
    with pytest.raises(ValueError, match="Duplicate issuer"):
        progress.build(cohort)


def test_optional_zero_is_observed_and_retry_remains_separate(cohort):
    absent = progress.build(cohort)
    streams = {"all_four_index_ranges_complete": True, "accepted_unique_logs": 0, "pages_captured": 4,
               "independent_chain_completeness_verified": False,
               "streams": [{"stream": str(i), "index_range_complete": True, "pages_processed": 1, "accepted_logs": 0} for i in range(4)]}
    write(cohort, progress.OPTIONAL["blockscout_streams"], streams)
    write(cohort, progress.OPTIONAL["ooni_main"], {"query_count": 2, "complete_queries": 1, "failed_or_incomplete_queries": 1, "metadata_rows": 5})
    write(cohort, progress.OPTIONAL["ooni_retry"], {"retry_query_count": 1, "completed_retries": 1, "still_incomplete": 0, "metadata_rows": 2})
    present = progress.build(cohort)
    assert present["input_hash"] != absent["input_hash"]
    assert present["event_logs"]["index_stream_collection"]["metrics"]["accepted_unique_logs"] == 0
    assert present["ooni"]["main_metadata"]["metrics"]["metadata_rows"] == 5
    assert present["ooni"]["retry_metadata"]["metrics"]["metadata_rows"] == 2
    assert "combined_metadata_rows" not in present["ooni"]
    assert present["human_reference"]["status"] == "pending"
    assert "\\ProgressLogAccepted}{0}" in progress.tex(present)


def test_required_missing_and_summary_inconsistency_fail(cohort):
    change(cohort, progress.DISCLOSURE, lambda r: r.update(outcome_counts={"gap": 2}))
    with pytest.raises(ValueError, match="disclosure outcome"):
        progress.build(cohort)
    (cohort / progress.DISCLOSURE).unlink()
    with pytest.raises(ValueError, match="Required input missing"):
        progress.build(cohort)


def test_available_logs_preserve_interval_uncertainty_and_human_pending(cohort):
    report = {"issuer_units": 4, "measurement_units": 2, "issuer_units_with_indexed_events": 2,
              "measurement_units_with_indexed_events": 2, "matching_event_associations": 2, "unique_matching_event_identities": 2,
              "indexed_stream_coverage_complete": True, "zero_is_not_no_action": True, "causal_attribution_performed": False,
              "event_trigger_interval_counts": {"before_interval": 0, "within_interval": 1, "after_interval": 1},
              "within_trigger_interval_order_indeterminate": True, "exact_trigger_latency_established": False}
    write(cohort, progress.OPTIONAL["blockscout_matches"], report)
    result = progress.build(cohort)
    metrics = result["event_logs"]["candidate_event_matching"]["metrics"]
    assert metrics["event_trigger_interval_counts"]["within_interval"] == 1
    assert metrics["exact_trigger_latency_established"] is False
    assert result["human_reference"]["status"] == "pending"
    change(cohort, progress.OPTIONAL["blockscout_matches"], lambda r: r.update(exact_trigger_latency_established=True))
    with pytest.raises(ValueError, match="uncertainty"):
        progress.build(cohort)


def test_machine_summaries_cannot_supply_private_or_human_outcomes(cohort):
    change(cohort, progress.DISCLOSURE, lambda r: r.update(private_account_action_measured=True))
    with pytest.raises(ValueError, match="private account"):
        progress.build(cohort)


def write_ooni_overlay(root):
    main_dir = Path(progress.OPTIONAL["ooni_main"]).parent
    retry_dir = Path(progress.OPTIONAL["ooni_retry"]).parent
    queries = [{"query_id": "q0", "domain": "one.example", "since": "2024-01-01"},
               {"query_id": "q1", "domain": "two.example", "since": "2024-01-01"}]
    write(root, progress.OPTIONAL["ooni_main"], {"query_count": 2, "complete_queries": 1, "failed_or_incomplete_queries": 1, "metadata_rows": 5})
    write(root, progress.OPTIONAL["ooni_retry"], {"retry_query_count": 1, "completed_retries": 1, "still_incomplete": 0, "metadata_rows": 2})
    write(root, main_dir / "manifest.json", {"queries": queries, "query_count": 2})
    write(root, main_dir / "query_summaries.json", [{"query": q, "pagination_complete": index == 0} for index, q in enumerate(queries)])
    retry = {"queries": [queries[1]], "retry_query_count": 1}
    for field, name in (("source_manifest_sha256", "manifest.json"), ("source_query_summaries_sha256", "query_summaries.json"), ("source_summary_sha256", "summary.json")):
        retry[field] = progress.digest((root / main_dir / name).read_bytes())
    write(root, retry_dir / "manifest.json", retry)
    write(root, retry_dir / "query_summaries.json", [{"query": queries[1], "pagination_complete": True}])
    return main_dir, retry_dir, queries


def test_effective_ooni_queries_require_verified_retry_subset(cohort):
    main_dir, retry_dir, queries = write_ooni_overlay(cohort)
    result = progress.build(cohort)
    overlay = result["ooni"]["effective_query_coverage"]
    assert overlay["status"] == "verified_retry_overlay"
    assert overlay["metrics"]["effective_complete_queries"] == 2
    assert overlay["metrics"]["retry_is_subset_of_main_incomplete"] is True
    assert "\\ProgressOONIEffectiveCompleteQueries}{2}" in progress.tex(result)
    # Repeating an already complete main query cannot inflate coverage.
    change(cohort, retry_dir / "manifest.json", lambda r: r.update(queries=[queries[0]]))
    write(cohort, retry_dir / "query_summaries.json", [{"query": queries[0], "pagination_complete": True}])
    with pytest.raises(ValueError, match="outside the main incomplete"):
        progress.build(cohort)


def test_retry_source_hash_mismatch_cannot_create_effective_count(cohort):
    _, retry_dir, _ = write_ooni_overlay(cohort)
    change(cohort, retry_dir / "manifest.json", lambda r: r.update(source_summary_sha256="changed"))
    with pytest.raises(ValueError, match="source_summary_sha256"):
        progress.build(cohort)


def write_transport(root):
    directory = Path(progress.OPTIONAL["cross_transport"]).parent
    flags = {key: False for key in ("upstream_operator_independence_verified", "full_cohort_reconciliation", "human_reference_complete", "causal_attribution_performed")}
    queries, snapshots = [], []
    for path in sorted((root / progress.ENDPOINTS / "snapshots").glob("m0_*.json")):
        row = json.loads(path.read_text())
        qid = path.stem
        row["state_query_id"] = qid
        write(root, path.relative_to(root), row)
        snapshots.append(row)
        source = {"method": "eth_call", "params": [{"to": "0xcontract", "data": qid}, hex(row["block_number"])],
                  "result": hex(row["returned_blacklist_word"]), "status": "valid_rpc_response"}
        source_path = f"{progress.ENDPOINTS}/captures/{qid}/result.json"
        write(root, source_path, source)
        queries.append({"id": qid, "method": source["method"], "params": source["params"], "dependencies": [],
                        "is_target_state_query": True, "expected_comparison": source["result"],
                        "source_result_sha256": progress.digest((root / source_path).read_bytes())})
    write(root, f"{progress.ENDPOINTS}/collection_manifest.json", {"frozen": True})
    for name in ("collector_source.py", "transport_source.py"):
        (root / directory).mkdir(parents=True, exist_ok=True)
        (root / directory / name).write_text("# frozen synthetic source\n")
    plan = {**flags, "queries": queries, "queries_per_provider": len(queries), "max_attempts_per_provider_query": 1,
            "minimum_delay_seconds": 0.5, "maximum_total_requests": 2*len(queries), "explicit_total_request_budget": 10,
            "selected_snapshot_units": snapshots, "selected_window_ids": ["w0"],
            "providers": {"drpc_public": {"endpoint": "https://a.example"}, "one_rpc_public": {"endpoint": "https://b.example"}}}
    for field, path in (("collector_sha256", directory / "collector_source.py"), ("transport_source_sha256", directory / "transport_source.py"),
                        ("source_cohort_manifest_sha256", f"{progress.ENDPOINTS}/collection_manifest.json"),
                        ("source_cohort_summary_sha256", f"{progress.ENDPOINTS}/summary.json"),
                        ("source_cohort_units_sha256", f"{progress.CANDIDATES}/issuer_query_units.jsonl")):
        plan[field] = progress.digest((root / path).read_bytes())
    write(root, directory / "plan.json", plan)
    write(root, directory / "plan.sha256.json", {"plan_sha256": progress.digest((root / directory / "plan.json").read_bytes())})
    rows = []
    for provider, config in plan["providers"].items():
        for i, query in enumerate(queries):
            row = {key: query[key] for key in ("method", "params", "is_target_state_query")}
            row.update(query_id=query["id"], provider=provider)
            if provider == "one_rpc_public" and i > 1:
                row.update(attempted=False, status="not_attempted_provider_rate_limit_stop")
            else:
                gap = provider == "one_rpc_public" and i == 1
                result = query["expected_comparison"]
                row.update(attempted=True, status="gap" if gap else "cross_transport_match", comparison_value=None if gap else result,
                           expected_comparison=result, rpc_result={"status": "gap" if gap else "valid_rpc_response",
                           "result": None if gap else result, "attempts": [{"number": 1}]})
                capture = directory / "captures" / provider / query["id"] / "attempt_1"
                request = {"jsonrpc": "2.0", "id": 1, "method": query["method"], "params": query["params"]}
                write(root, capture / "request.json", request)
                body = b"rate limit" if gap else json.dumps({"jsonrpc": "2.0", "id": 1, "result": result}).encode()
                (root / capture / "response.body").write_bytes(body)
                write(root, capture / "capture.json", {"http_status": 429 if gap else 200, "request_url": config["endpoint"],
                    "request_sha256": progress.digest((root / capture / "request.json").read_bytes()), "response_body_sha256": progress.digest(body)})
                write(root, directory / "results" / provider / f"{query['id']}.json", row)
            rows.append(row)
    write(root, directory / "results.json", rows)
    report = {**flags, "maximum_total_requests": 8, "attempted_queries": 6, "selected_action_windows": 1, "selected_endpoint_snapshots": 4,
              "providers": [{"provider": "drpc_public", "planned_queries": 4, "attempted_queries": 4, "matched_queries": 4,
                             "matched_target_state_queries": 4, "rate_limit_stop": False},
                            {"provider": "one_rpc_public", "planned_queries": 4, "attempted_queries": 2, "matched_queries": 1,
                             "matched_target_state_queries": 1, "rate_limit_stop": True}]}
    write(root, progress.OPTIONAL["cross_transport"], report)
    return directory, plan


def test_cross_transport_verifies_captures_subset_and_stop(cohort):
    write_transport(cohort)
    result = progress.build(cohort)
    stage = result["cross_transport"]
    assert stage["status"] == "verified_frozen_subset_accounting"
    assert stage["metrics"]["attempted_queries"] == 6
    assert stage["metrics"]["providers"][1]["unissued_queries"] == 2
    assert stage["metrics"]["upstream_operator_independence_verified"] is False
    assert "\\ProgressDRPCStateMatches}{4}" in progress.tex(result)
    assert "\\ProgressOONIPostcanIdentityValidRows}{pending}" in progress.tex(result)
    assert result["ooni"]["raw_stage_counts_are_additive"] is False


@pytest.mark.parametrize("mutation", ["hash", "duplicate", "accounting", "body", "scope", "partial_window", "stop"])
def test_cross_transport_inconsistent_evidence_is_rejected(cohort, mutation):
    directory, plan = write_transport(cohort)
    if mutation == "hash":
        change(cohort, directory / "plan.sha256.json", lambda r: r.update(plan_sha256="changed"))
    elif mutation == "duplicate":
        change(cohort, directory / "results.json", lambda rows: rows.append(rows[0]))
    elif mutation == "accounting":
        change(cohort, progress.OPTIONAL["cross_transport"], lambda r: r.update(attempted_queries=5))
    elif mutation == "body":
        path = cohort / directory / "captures/drpc_public" / plan["queries"][0]["id"] / "attempt_1/response.body"
        path.write_text('{"result":"0xffff"}')
    elif mutation == "scope":
        change(cohort, progress.OPTIONAL["cross_transport"], lambda r: r.update(upstream_operator_independence_verified=True))
    elif mutation == "partial_window":
        change(cohort, directory / "plan.json", lambda r: r["selected_snapshot_units"].pop())
        write(cohort, directory / "plan.sha256.json", {"plan_sha256": progress.digest((cohort / directory / "plan.json").read_bytes())})
    else:
        change(cohort, directory / "results.json", lambda rows: rows[-1].update(status="not_attempted_dependency_gap"))
    with pytest.raises(ValueError):
        progress.build(cohort)
