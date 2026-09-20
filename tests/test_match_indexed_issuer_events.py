import pytest

from match_blockscout_issuer_logs import interval_timing, match_units


def inputs(initial=0, final=0):
    unit = {"issuer_query_id": "q", "measurement_unit_id": "m", "issuer": {"symbol": "USDC"},
            "normalized_address": "0x" + "a" * 40, "action_url": "https://source.test/action",
            "proposed_direction": "addition", "window_start_inclusive_utc": "2022-01-01T00:00:00Z",
            "trigger_earliest_utc": "2022-01-15T00:00:00Z", "trigger_latest_exclusive_utc": "2022-01-16T00:00:00Z",
            "window_end_exclusive_utc": "2022-02-01T00:00:00Z"}
    snapshots = [{"issuer_query_id": "q", "snapshot": label, "issuer": "usdc",
                  "target_address": unit["normalized_address"], "block_number": block,
                  "state_query_status": "valid_rpc_response", "returned_blacklist_word": word,
                  "rpc_code_and_forwarding_prerequisites_pass": True}
                 for label, block, word in (("window_first_block", 10, initial), ("window_last_block", 20, final))]
    return [unit], snapshots


def event(block, direction, index=0):
    return {"issuer": "usdc", "affected_address": "0x" + "a" * 40,
            "block_number": block, "log_index": index, "direction": direction,
            "block_timestamp": f"2022-01-{min(block,28):02}T12:00:00Z",
            "transaction_hash": f"tx{block}-{index}", "block_hash": f"block{block}"}


def test_zero_match_kept_and_never_becomes_no_action():
    units, snapshots = inputs()
    rows, summary = match_units(units, snapshots, [], {"usdc": True, "usdt": True})
    assert len(rows) == 1 and rows[0]["matching_indexed_event_count"] == 0
    assert rows[0]["response_classification"] is None
    assert summary["zero_is_not_no_action"] is True
    assert summary["causal_attribution_performed"] is False


def test_inclusive_matching_but_replay_excludes_first_post_block_boundary():
    units, snapshots = inputs(initial=1, final=0)
    events = [event(9, "add"), event(10, "add"), event(15, "remove"), event(20, "remove"), event(21, "add")]
    rows, summary = match_units(units, snapshots, events, {"usdc": True, "usdt": True})
    row = rows[0]
    assert [e["block_number"] for e in row["matching_indexed_events"]] == [10, 15, 20]
    assert row["events_at_first_post_block_snapshot"] == 1
    assert row["endpoint_word_consistency_given_indexed_sequence"] == "consistent_given_indexed_sequence"
    assert summary["unique_matching_event_identities"] == 3


def test_add_remove_order_within_one_block_is_retained():
    units, snapshots = inputs()
    rows, _ = match_units(units, snapshots, [event(15, "remove", 2), event(15, "add", 1)], {"usdc": True})
    assert [e["direction"] for e in rows[0]["matching_indexed_events"]] == ["add", "remove"]
    assert rows[0]["endpoint_word_consistency_given_indexed_sequence"] == "consistent_given_indexed_sequence"


def test_incomplete_index_does_not_assess_consistency():
    units, snapshots = inputs(initial=0, final=1)
    rows, _ = match_units(units, snapshots, [], {"usdc": False})
    assert rows[0]["endpoint_word_consistency_given_indexed_sequence"] == "not_assessed_incomplete_index_range"
    assert rows[0]["replayed_last_word_from_strictly_after_first_block"] is None


def test_duplicate_identity_is_deduplicated_but_conflict_is_error():
    units, snapshots = inputs(final=1)
    added = event(15, "add")
    rows, summary = match_units(units, snapshots, [added, added], {"usdc": True})
    assert rows[0]["add_count"] == 1 and summary["duplicate_input_event_rows_removed"] == 1
    with pytest.raises(ValueError, match="Conflicting"):
        match_units(units, snapshots, [added, {**added, "direction": "remove"}], {"usdc": True})


def test_nonmatching_issuer_or_address_is_not_associated():
    units, snapshots = inputs()
    events = [{**event(15, "add"), "issuer": "usdt"}, {**event(16, "add"), "affected_address": "0x" + "d" * 40}]
    rows, summary = match_units(units, snapshots, events, {"usdc": True})
    assert rows[0]["matching_indexed_event_count"] == 0
    assert summary["issuer_units"] == 1 and summary["measurement_units"] == 1


@pytest.mark.parametrize("stamp,position,lower,upper", [
    ("2022-01-14T23:59:59Z", "before_interval", -86401, -1),
    ("2022-01-15T12:00:00Z", "within_interval", -43200, 43200),
    ("2022-01-16T00:00:00Z", "after_interval", 0, 86400),
])
def test_half_open_trigger_interval_gives_bounds_not_exact_latency(stamp, position, lower, upper):
    value = interval_timing(stamp, "2022-01-15T00:00:00Z", "2022-01-16T00:00:00Z")
    assert value["trigger_interval_position"] == position
    assert value["delay_lower_bound_seconds"] == lower and value["delay_upper_bound_seconds"] == upper
    assert value["delay_lower_bound_exclusive"] is True and value["delay_upper_bound_inclusive"] is True
    assert value["exact_trigger_latency_established"] is False
    if position == "within_interval":
        assert value["ordering_within_interval"] == "indeterminate"
