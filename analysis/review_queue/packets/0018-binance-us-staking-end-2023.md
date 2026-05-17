# v0.3 Review Packet: `binance-us-staking-end-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `18` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `binance-us-staking-end-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `binance_us` |
| event_date | `2023-06-09` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-us-staking-end-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Binance.US / BAM Trading Services Inc.` |

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

"The 2023-06-09 Binance.US autonomous discontinuation of its staking-as- a-service product, announced four days after the SEC v. Binance complaint but executed as an autonomous corporate-policy decision rather than a regulator-ordered cessation, produced a single-layer cascade at the offramp_cex surface: the U.S.-scoped Binance.US pooled-staking product was withdrawn. The row asserts only this offramp_cex observation and does not claim L0 network, L1 consensus, L3 RPC, L4 frontend delisting/geofence, or asset_onchain issuer-freeze effects. The autonomous-vs-forced distinction relative to kraken-sec-staking-2023 (regulator-ordered twin) is the load-bearing analytical contribution." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://blog.binance.us/end-of-staking-services-on-binance-us/

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
  "queue_id": 18,
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
  "queue_id": 18,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-us-staking-end-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
