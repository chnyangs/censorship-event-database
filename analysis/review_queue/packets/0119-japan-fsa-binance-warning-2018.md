# v0.3 Review Packet: `japan-fsa-binance-warning-2018`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `119` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `japan-fsa-binance-warning-2018` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `JP_FSA` |
| event_date | `2018-03-23` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-binance-warning-2018.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Holdings Ltd.` |

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

"Japan FSA's 2018-03-23 public warning to Binance under the Payment Services Act for operating a crypto-asset exchange business targeted at Japanese residents without registration directly compelled Binance's operator-side exit from the Japanese market and relocation of its headquarters from Tokyo to Malta in March 2018. The row does not claim frontend-disable, ISP/DNS-level connectivity blocking of binance.com from Japan, on-chain asset-layer freeze, or any customer-funds freeze — only the single-entity Binance-cohort offramp_cex load-bearing axis of JP-resident-access deprecation and HQ relocation under the Payment Services Act registration regime." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsa.go.jp/news/29/sonota/

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
  "queue_id": 119,
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
  "queue_id": 119,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-binance-warning-2018.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
