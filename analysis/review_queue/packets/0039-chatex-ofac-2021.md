# v0.3 Review Packet: `chatex-ofac-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `39` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `chatex-ofac-2021` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC` |
| event_date | `2021-11-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/chatex-ofac-2021.yaml` |
| target_kind | `address_set` |
| target_actor | `Chatex` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 5 |
| primary observation sources | 5 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC designation of Chatex on 2021-11-08 produced a direct L4 frontend change within 9 days in the form of an operator-posted compliance notice freezing customer withdrawals, mechanistically distinct from the same-quarter SUEX case (no frontend reaction) despite both being foreign exchange entities sanctioned under the same policy push." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20211108
- citation[1]: `primary_legal` replayable=`False` https://home.treasury.gov/news/press-releases/jy0471

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
  "queue_id": 39,
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
  "queue_id": 39,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/chatex-ofac-2021.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
