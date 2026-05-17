# v0.3 Review Packet: `japan-fsa-zaif-orders-2018-09`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `126` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `japan-fsa-zaif-orders-2018-09` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `JP_FSA` |
| event_date | `2018-09-25` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-zaif-orders-2018-09.yaml` |
| target_kind | `entity` |
| target_actor | `Tech Bureau, Inc. (Zaif)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Japan FSA's 2018-09-25 business-improvement order against Tech Bureau, Inc. (the third 2018 FSA supervisory order against the Zaif operator, following the 2018-09-14 hack of approximately ¥7 billion / USD 60-67M in BTC, BCH, and MONA) directly compelled the Zaif operator-state change of customer-withdrawal-rail freeze and the forced asset-and-business transfer to Fisco Cryptocurrency Exchange completed in late 2018. The row does not claim frontend-disable, ISP/DNS-level connectivity blocking, on-chain asset-layer freeze, or class-wide Japanese VASP-cohort suspension — only the single-entity Tech Bureau/Zaif-cohort offramp_cex load-bearing axis under the Payment Services Act supervisory regime." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsa.go.jp/news/30/sonota/

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
  "queue_id": 126,
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
  "queue_id": 126,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-zaif-orders-2018-09.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
