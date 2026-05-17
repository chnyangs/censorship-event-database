# v0.3 Review Packet: `kucoin-canada-exit-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `138` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `kucoin-canada-exit-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `KUCOIN_EXCHANGE` |
| event_date | `2023-06-28` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kucoin-canada-exit-2023.yaml` |
| target_kind | `entity` |
| target_actor | `KuCoin (Canada user cohort)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Under sustained OSC enforcement (2022-07-22 Capital Markets Tribunal order) and the 2023-02-22 CSA Staff Notice 21-332 framework, KuCoin on 2023-06-28 announced mandatory KYC effective 2023-07-15 for Canadian-resident accounts and an associated wind-down of deposit and trading services, producing a 1-layer offramp_cex cascade for the KuCoin Canada cohort. Structurally an S5 corporate-policy retreat sibling to the S4 CSA-driven Binance Canada withdrawal (canada-csa-binance-withdrawal-2023)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.kucoin.com/news/en-kucoin-announcement-regarding-canada
- citation[1]: `primary_legal` replayable=`True` https://www.osc.ca/en/news-events/news/osc-holds-global-crypto-asset-trading-platforms-accountable

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
  "queue_id": 138,
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
  "queue_id": 138,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kucoin-canada-exit-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
