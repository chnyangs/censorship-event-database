# v0.3 Review Packet: `tether-retroactive-sweep-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `225` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `tether-retroactive-sweep-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `tether_usdt_issuer` |
| event_date | `2023-12-09` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tether-retroactive-sweep-2023.yaml` |
| target_kind | `address_set` |
| target_actor | `Historical OFAC SDN ETH cluster` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 3 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Tether executed a retroactive batch freeze of historical OFAC-SDN ETH addresses on 2023-12-09 04:34-05:36 UTC, affecting addresses across ≥4 prior SDN events (SUEX 2021, Chatex 2021, Russia-election 2020, Russian-cyber-theft 2020). The minute-level timestamp clustering across distinct SDN events rules out coincidental action and establishes the batch as a single Tether policy operation." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://usdtbanlist.com/address/0x19aa5fe80d33a56d56c78e82ea5e50e5d80b4dff
- citation[1]: `supporting_community` replayable=`True` https://usdtbanlist.com/address/0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45

## Required Human Decisions

- Confirm this row is one concrete trigger/target unit under the codebook.
- Confirm the trigger has at least one replayable primary or admission-grade source anchor.
- Confirm layer observations still support the YAML status and scoped claim.
- Resolve only after primary-source re-extraction is complete.

## Decision JSON Templates

Promotion after real human verification:

```json
{
  "actor": "human:<name>",
  "decision": "resolved",
  "metadata": {
    "human_review_required": true,
    "packet_generated_at": "2026-05-17T11:01:29Z",
    "review_type": "v0.3_primary_source_reextraction"
  },
  "new_event_status": "verified",
  "queue_id": 225,
  "reason": "Primary-source re-extraction completed; event evidence supports primary_source_verified=true."
}
```

Needs recheck / cannot verify yet:

```json
{
  "actor": "human:<name>",
  "decision": "needs_recheck",
  "metadata": {
    "human_review_required": true,
    "review_type": "v0.3_primary_source_reextraction"
  },
  "queue_id": 225,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tether-retroactive-sweep-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
