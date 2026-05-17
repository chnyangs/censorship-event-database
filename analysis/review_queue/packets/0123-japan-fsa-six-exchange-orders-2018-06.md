# v0.3 Review Packet: `japan-fsa-six-exchange-orders-2018-06`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `123` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `japan-fsa-six-exchange-orders-2018-06` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `JP_FSA` |
| event_date | `2018-06-22` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-six-exchange-orders-2018-06.yaml` |
| target_kind | `entity` |
| target_actor | `JP FSA 2018-06-22 six-exchange business-improvement-order cohort` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 5 |
| primary observation sources | 1 |
| replayable observation sources | 5 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2018-06-22, the Japan FSA simultaneously issued business- improvement orders under the Payment Services Act to six registered crypto-asset exchanges — bitFlyer, Quoine, BTC Box, Bit Bank, BitPoint, and Tech Bureau (Zaif) — citing inadequate AML/CFT and KYC frameworks, compelling each operator to file a remediation plan by 2018-07-23 and to report monthly thereafter. bitFlyer additionally voluntarily suspended new-customer registrations the same day pending re-verification of existing customers' KYC data. The row does not claim frontend-disable, ISP/DNS-level connectivity blocking, on-chain asset-layer freeze, or any full withdrawal-rail suspension — only the single-day six-way offramp_cex supervisory- order load-bearing axis and bitFlyer's same-day onboarding pause." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsa.go.jp/news/30/sonota/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/markets/2018/06/22/japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges/
- citation[2]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/japan-hits-6-more-crypto-exchanges-with-business-improvement-orders

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
  "queue_id": 123,
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
  "queue_id": 123,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-six-exchange-orders-2018-06.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
