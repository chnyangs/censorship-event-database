# v0.3 Review Packet: `germany-bafin-binance-licence-withdrawal-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `95` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `germany-bafin-binance-licence-withdrawal-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `DE_BAFIN` |
| event_date | `2023-07-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/germany-bafin-binance-licence-withdrawal-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Binance (Germany-facing entities)` |

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

"Binance withdrew its German BaFin crypto-custody licence application on 2023-07-26 after BaFin signalled (through supervisory dialogue, not a published denial) that the application would not be approved. The withdrawal closed the path to a regulated-in-DE Binance offering under the pre-MiCA KWG crypto-custody licensing regime and produced an operator-state change at the Binance Germany-customer cohort (offramp_cex load-bearing) plus a Binance-corporate L4 frontend response (Germany-geo notices, attribution=plausible). The row does not claim ISP-level connectivity blocking, on-chain asset freeze, or class-wide German banking-rail severance." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.bafin.de/EN/Homepage/homepage_node.html
- citation[1]: `primary_corporate` replayable=`True` https://www.binance.com/en/blog

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
  "queue_id": 95,
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
  "queue_id": 95,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/germany-bafin-binance-licence-withdrawal-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
