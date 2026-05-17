# v0.3 Review Packet: `thailand-sec-binance-bybit-c-and-d-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `228` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `thailand-sec-binance-bybit-c-and-d-2021` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `TH_SEC` |
| event_date | `2021-07-02` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/thailand-sec-binance-bybit-c-and-d-2021.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Holdings Ltd. (TH cohort) + Bybit Fintech Limited (TH cohort)` |

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

"Thailand SEC criminal complaint filed 2021-07-02 against Binance with the Royal Thai Police Economic Crime Suppression Division (and the contemporaneous TH SEC unlicensed-operator enforcement posture extending to Bybit) under the Emergency Decree on Digital Asset Businesses Act B.E. 2561 produced a plausible-attribution constraint on the Thai THB on/off-ramp rails accessible via binance.com and bybit.com (offramp_cex load-bearing), without an accompanying regulator-directed L4-frontend disable order, L0 network block, or on-chain asset freeze. The row does not claim a direct Thai-banking-rail severance directive from TH SEC." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9017

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
  "queue_id": 228,
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
  "queue_id": 228,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/thailand-sec-binance-bybit-c-and-d-2021.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
