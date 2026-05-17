# v0.3 Review Packet: `malaysia-sc-binance-disable-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `147` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `malaysia-sc-binance-disable-2021` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `MY_SC` |
| event_date | `2021-07-30` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/malaysia-sc-binance-disable-2021.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Holdings Ltd. (MY cohort)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Malaysia SC enforcement order of 2021-07-30 directly compelled Binance to disable its website (binance.com) and mobile applications (iOS / Android) for Malaysian users within a 14-business-day compliance window, producing a regulator-mandated operator-state change at the Binance Malaysian-customer cohort (L4 frontend load-bearing) with cascading severance of the Binance-MY MYR on/off-ramp rail (offramp_cex, attribution=plausible because the rail severance is downstream of the frontend disable rather than a direct banking-prohibition directive). The row does not claim ISP / DNS-level connectivity blocking, on-chain asset freeze, or class-wide Malaysian banking-rail severance." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sc.com.my/resources/media/media-release

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
  "queue_id": 147,
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
  "queue_id": 147,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/malaysia-sc-binance-disable-2021.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
