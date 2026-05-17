# v0.3 Review Packet: `apple-india-crypto-exchange-removal-2024-01`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `6` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `apple-india-crypto-exchange-removal-2024-01` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `APPLE` |
| event_date | `2024-01-10` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/apple-india-crypto-exchange-removal-2024-01.yaml` |
| target_kind | `entity` |
| target_actor | `Offshore VDA exchanges (Apple App Store IN regional storefront, FIU-IND cascade)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2024-01-10, Apple removed offshore Virtual Digital Asset exchange apps (Binance, OKX, Kraken, KuCoin, MEXC Global, Bitfinex, Bittrex, Bitstamp) from the Apple App Store India regional storefront as a corporate compliance response to the FIU-IND 2023-12-28 show-cause notices and the MEITY section 69A URL blocking order. Observational axis at l4_frontend (Apple App Store IN regional removal). Admission-anchor-grade promotion pending pinned App Store IN availability snapshots." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://techcrunch.com/2024/01/09/apple-crypto-apps-binance-india/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2024/01/10/binance-kucoin-other-exchanges-served-notice-by-indian-government-removed-from-apples-app-store
- citation[2]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/apple-india-binance-kraken-crypto-exchanges-delist-fiu-notice

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
  "queue_id": 6,
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
  "queue_id": 6,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/apple-india-crypto-exchange-removal-2024-01.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
