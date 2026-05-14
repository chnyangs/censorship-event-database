# SPDX-License-Identifier: MIT
from __future__ import annotations

from build_action_registry import build_rows


def test_action_registry_groups_duplicate_physical_actions():
    events = [
        {
            "id": "ofac-event",
            "status": "admitted",
            "observations": [
                {
                    "layer": "asset_onchain",
                    "actor": "circle",
                    "event": "blacklist",
                    "observation_kind": "observed_change",
                    "action_id": "circle:tornado:blacklist-tx",
                }
            ],
        },
        {
            "id": "issuer-event",
            "status": "admitted",
            "observations": [
                {
                    "layer": "asset_onchain",
                    "actor": "circle",
                    "event": "blacklist",
                    "observation_kind": "observed_change",
                    "action_id": "circle:tornado:blacklist-tx:issuer-view",
                    "duplicate_of_action_id": "circle:tornado:blacklist-tx",
                }
            ],
        },
    ]

    rows = build_rows(events)

    assert len(rows) == 1
    assert rows[0]["canonical_action_id"] == "circle:tornado:blacklist-tx"
    assert rows[0]["row_count"] == 2
    assert rows[0]["duplicate_row_count"] == 1
    assert rows[0]["event_ids"] == "issuer-event;ofac-event"
