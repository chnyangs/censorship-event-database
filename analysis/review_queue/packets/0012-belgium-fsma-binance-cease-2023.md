# v0.3 Review Packet: `belgium-fsma-binance-cease-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `12` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `belgium-fsma-binance-cease-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `BE_FSMA` |
| event_date | `2023-06-23` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/belgium-fsma-binance-cease-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Binance (Belgium-facing entities)` |

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

"FSMA order of 2023-06-23 directly compelled Binance to cease offering virtual-currency exchange and custody-wallet services to Belgian residents and to repatriate customer holdings from non-EEA-incorporated Binance entities, producing a regulator-mandated operator-state change at the Binance Belgian-customer cohort (offramp_cex load-bearing) and a Binance-corporate L4 frontend response (Belgium-geo restriction notices, attribution=plausible). The row does not claim ISP-level connectivity blocking, on-chain asset freeze, or class-wide Belgian banking-rail severance." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsma.be/en/news

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
  "queue_id": 12,
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
  "queue_id": 12,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/belgium-fsma-binance-cease-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
