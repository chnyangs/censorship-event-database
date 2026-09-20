# SPDX-License-Identifier: MIT
from pathlib import Path

import pytest

from build_validation_frame import classify_header, history_dates, parse_action, parse_listing


def test_listing_keeps_multiple_actions_same_day_and_noncrypto_categories():
    raw = b'''Displaying 1 - 2 of 2 results.
      <a href="/recent-actions/20221230">General guidance</a>
      <a href="/recent-actions/20221230_33">Settlement agreement</a>
      <a href="/recent-actions/enforcement-actions">Category</a>'''
    parsed = parse_listing(raw, 2022)
    assert parsed["total"] == 2
    assert {r["action_slug"] for r in parsed["actions"]} == {"20221230", "20221230_33"}


def test_listing_without_result_count_is_not_accepted():
    with pytest.raises(ValueError, match="marker missing"):
        parse_listing(b"<p>Access denied</p>", 2022)


def test_official_nonstandard_listing_routes_are_retained():
    raw = b'''Displaying 1 - 1 of 1 results.
      <div class="views-row"><div><a href="/node/970956">Changes to January 01, 2022 guidance</a></div>
      <div>April 03, 2023 - <a href="/recent-actions/miscellaneous">Miscellaneous</a></div></div>'''
    parsed = parse_listing(raw, 2023)
    assert parsed["actions"][0]["action_slug"] == "node-970956"
    assert parsed["actions"][0]["date_candidate"] == "2023-04-03"


def test_explicit_markers_preserve_addition_and_removal_of_same_address():
    address = "0x" + "a" * 40
    raw = f'''<meta charset="utf8"/><div>Release Date 11/08/2022</div>
    <div class="field--name-field-body"><p>The following entities have been added to OFAC's SDN List:</p>
    <p>TARGET A; Digital Currency Address - ETH {address};<br />Other line</p>
    <p>The following entities have been removed from OFAC's SDN List:</p>
    <p>TARGET A; Digital Currency Address - ETH {address};</p></div>'''.encode()
    parsed = parse_action(raw)
    assert parsed["release_date"] == "2022-11-08"
    assert [r["proposed_action_type"] for r in parsed["entries"]] == ["addition", "removal"]
    assert all(r["target_entry_prefix_candidate"] == "TARGET A" for r in parsed["entries"])
    assert all("pending_independent_adjudication" in r["status"] for r in parsed["entries"])
    assert all(r["proposed_list_scope"] == "sdn" for r in parsed["entries"])


def test_non_sdn_marker_does_not_become_sdn_proposal():
    address = "0x" + "a" * 40
    raw = f'''<div class="field--name-field-body"><p>The following entries have been added to the Non-SDN List:</p>
    <p>NAME; Digital Currency Address - ETH {address};</p></div>'''.encode()
    assert parse_action(raw)["entries"][0]["proposed_list_scope"] == "non_sdn"


def test_mixed_marker_and_unmarked_hex_are_not_assigned_known_action():
    assert classify_header("The following names have been added or removed from the SDN List:") == "unclassified_mixed_marker"
    assert classify_header("The following deletions have been made to OFAC's SDN List:") == "removal"
    address = "0x" + "b" * 40
    parsed = parse_action(f'<div class="field--name-field-body">Other chain {address}</div>'.encode())
    assert parsed["entries"] == []
    assert parsed["unclassified_hex_strings"] == [address]


def test_history_dates_only_dated_headings_of_requested_year():
    text = "• 01/03/25\ntext DOB 01/04/25\n 01/05/25:\n01/05/25\n12/31/24\n"
    assert history_dates(text, 2025) == ["2025-01-03", "2025-01-05"]
