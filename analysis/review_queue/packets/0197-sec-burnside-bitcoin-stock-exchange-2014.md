# v0.3 Review Packet: `sec-burnside-bitcoin-stock-exchange-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `197` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `sec-burnside-bitcoin-stock-exchange-2014` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `sec_action` |
| actor | `US_SEC` |
| event_date | `2014-12-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-burnside-bitcoin-stock-exchange-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Ethan Burnside / BTC Trading Corp` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2014-12-08 SEC cease-and-desist settlement against Ethan Burnside and BTC Trading Corp finalized the shutdown of two unregistered Bitcoin/Litecoin-denominated securities-exchange venues (BTCT and LTC-Global) at the L4 frontend and offramp_cex layers; the row claims only this two-layer cessation observation and not network blocking, on-chain asset action, or PBS-era L1/L3 effects." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sec.gov/news/press-release/2014-273
- citation[1]: `primary_legal` replayable=`True` https://www.sec.gov/litigation/admin/2014/33-9684.pdf

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
  "queue_id": 197,
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
  "queue_id": 197,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-burnside-bitcoin-stock-exchange-2014.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
