# v0.3 Review Packet: `tornado-cash-ofac-delisting-2025`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `232` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `tornado-cash-ofac-delisting-2025` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_removal` |
| actor | `US_OFAC` |
| event_date | `2025-03-21` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-ofac-delisting-2025.yaml` |
| target_kind | `address_set` |
| target_actor | `tornado_cash` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 4 |
| observation sources | 13 |
| primary observation sources | 12 |
| replayable observation sources | 12 |
| primary replayable observation sources | 11 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC delisting of Tornado Cash on 2025-03-21 (Van Loon-litigation driven) is the first reverse-cascade event in the dataset, producing observed_change on 3 layers: L1 consensus censoring-relay share dropped ≈25pp within 14 days; Circle USDC unblacklisted at least one historical address; and L4 frontend access/listing partially reemerged via maintained UI paths while canonical-domain restoration remained incomplete. Establishes structural asymmetry between cascade and reverse-cascade shapes: rollback is slower and patchier than the original cascade." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20250321
- citation[1]: `primary_legal` replayable=`False` https://home.treasury.gov/news/press-releases/sb0057

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
  "queue_id": 232,
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
  "queue_id": 232,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-ofac-delisting-2025.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
