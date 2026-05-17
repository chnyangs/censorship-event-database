# v0.3 Review Packet: `japan-fsa-binance-sakura-acquisition-2022-11`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `118` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `japan-fsa-binance-sakura-acquisition-2022-11` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `JP_FSA` |
| event_date | `2022-11-30` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-binance-sakura-acquisition-2022-11.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Holdings + Sakura Exchange BitCoin (SEBC)` |

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

"Japan FSA's registered-VASP regime under the Payment Services Act permitted Binance's 2022-11-30 acquisition of 100% of Sakura Exchange BitCoin (SEBC), a JFSA-registered Crypto-Asset Exchange Service Provider, enabling Binance's re-entry into the Japanese market via licensed-VASP change-of-control. As of the 2026-05-17 authoring date no enforcement-driven JP-resident-access restriction attributable specifically to the 2022-11-30 trigger has been observed. Coded null_event / null_case as the permissive counter- example to JP_FSA enforcement actions against Binance (japan-fsa-binance-warning-2018) and to non-US national regulator Binance-market-access denials (france-amf-binance-psan-2022, germany-bafin-binance-licence-withdrawal-2023), and as a S4_nation_state permissive denominator control." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.binance.com/en/blog/markets/binance-acquires-sakura-exchange-bitcoin-marking-its-official-entry-into-japan-3556095942303204167
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/business/2022/11/30/binance-enters-japan-with-acquisition-of-regulated-crypto-exchange-sakura
- citation[2]: `supporting_journalism` replayable=`True` https://decrypt.co/116013/binance-acquires-japanese-crypto-exchange-sakura

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
  "queue_id": 118,
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
  "queue_id": 118,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-binance-sakura-acquisition-2022-11.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
