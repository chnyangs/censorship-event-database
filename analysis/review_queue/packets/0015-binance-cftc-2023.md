# v0.3 Review Packet: `binance-cftc-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `15` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `binance-cftc-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `cftc_action` |
| actor | `US_CFTC` |
| event_date | `2023-03-27` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-cftc-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Holdings + Changpeng Zhao + Samuel Lim` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
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

"The 2023-03-27 CFTC civil complaint in N.D. Ill. against Binance Holdings + Changpeng Zhao + Samuel Lim (former CCO) is the first of four US federal enforcement actions that converge on the 2023-11-21 multi-agency $4.3B settlement. The CFTC complaint initiates the rails-level commodities-derivatives enforcement axis against Binance; the structural rails remediation (compliance-monitor regime, $1.35B CFTC penalty) attaches to the 2023-11-21 consolidated settlement (binance-4framework-2023), not to the 2023-03-27 filing date. One observed_change layer (offramp_cex) with direct attribution." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/8680-23

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
  "queue_id": 15,
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
  "queue_id": 15,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-cftc-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
