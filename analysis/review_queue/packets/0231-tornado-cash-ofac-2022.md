# v0.3 Review Packet: `tornado-cash-ofac-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `231` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `tornado-cash-ofac-2022` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC` |
| event_date | `2022-08-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-ofac-2022.yaml` |
| target_kind | `address_set` |
| target_actor | `tornado_cash` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 5 |
| observation sources | 14 |
| primary observation sources | 13 |
| replayable observation sources | 13 |
| primary replayable observation sources | 12 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC designation of Tornado Cash on 2022-08-08 produced the defining 3-layer cascade in the dataset: L4 frontend (tornado.cash taken offline ≈22h), asset_onchain (Circle USDC batch-blacklisted 19/38 addresses within 6h; dYdX closed accounts within 34h), and L1 consensus (censoring- relay share rose from 10.80% day-1 of PBS era to 41.10% 18 days later). The paper-defining original-cascade event, paired with the 2025-03-21 delisting reverse-cascade." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20220808
- citation[1]: `primary_legal` replayable=`False` https://ofac.treasury.gov/specially-designated-nationals-list-sdn-list/archive-of-changes-to-the-sdn-list

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
  "queue_id": 231,
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
  "queue_id": 231,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-ofac-2022.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
