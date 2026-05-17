# v0.3 Review Packet: `japan-fsa-ftx-japan-suspension-2022-11`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `122` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `japan-fsa-ftx-japan-suspension-2022-11` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `JP_FSA_KANTO_LFB` |
| event_date | `2022-11-10` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-ftx-japan-suspension-2022-11.yaml` |
| target_kind | `entity` |
| target_actor | `FTX Japan KK` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Japan's 2022-11-10 Kanto Local Finance Bureau business-suspension order, business-improvement order, and order to retain assets domestically against FTX Japan KK (issued one day before the US parent's 2022-11-11 Chapter 11 filing) directly compelled the FTX Japan operator-state change of customer-withdrawal-rail freeze (both crypto-asset and JPY fiat withdrawals) and Japan-domestic retention of customer-segregated assets across the 2022-11-09 to 2023-02-20 window, with recovery via the 2023-02-21 customer-asset refund channel through the Liquid Japan web platform. The row does not claim frontend-disable, ISP/DNS-level connectivity blocking, on-chain asset-layer freeze, or class-wide Japanese VASP-cohort suspension — only the single-entity FTX-Japan-cohort offramp_cex load-bearing axis under the Payment Services Act and Financial Instruments and Exchange Act supervisory regime." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsa.go.jp/news/r4/sonota/20221110/20221110.html
- citation[1]: `primary_legal` replayable=`True` https://www.fsa.go.jp/en/news/2022/20221111/20221110.html

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
  "queue_id": 122,
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
  "queue_id": 122,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-ftx-japan-suspension-2022-11.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
