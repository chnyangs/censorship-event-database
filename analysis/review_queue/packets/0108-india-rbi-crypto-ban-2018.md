# v0.3 Review Packet: `india-rbi-crypto-ban-2018`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `108` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `india-rbi-crypto-ban-2018` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `IN_RBI` |
| event_date | `2018-04-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/india-rbi-crypto-ban-2018.yaml` |
| target_kind | `entity` |
| target_actor | `Indian crypto exchanges (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"RBI Circular of 2018-04-06 severed INR banking channels for Indian crypto exchanges effective 2018-07-06 (3-month compliance window). Primary observational axis is offramp_cex at industry-aggregate level; multiple exchanges (Zebpay, Unocoin) shut down or relocated as a direct consequence." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NOTI15465B741A10B0E45E896C62A9C83AB938F.PDF
- citation[1]: `primary_legal` replayable=`False` https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=43574

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
  "queue_id": 108,
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
  "queue_id": 108,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/india-rbi-crypto-ban-2018.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
