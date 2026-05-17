# v0.3 Review Packet: `russia-rosfinmonitoring-binance-russia-rails-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `191` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `russia-rosfinmonitoring-binance-russia-rails-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `RU_ROSFINMONITORING` |
| event_date | `2022-01-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/russia-rosfinmonitoring-binance-russia-rails-2022.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Russia-facing RUB / P2P operations (binance.com)` |

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

"No replayable Rosfinmonitoring formal enforcement artifact against Binance's Russia-facing RUB / P2P offramp rails during the 2022 calendar window has been identified at the 2026-05-17 authoring date. The adjacent Reuters-reported April-2021 Kostarev–Rosfin data-sharing arrangement (pre-2022), Binance's voluntary April-2022 EU-sanctions-driven Russia restrictions, and the August-2023 P2P sanctioned-bank delistings do not evidence a 2022 Rosfin-initiated ruble-rail enforcement order. Coded null_event / null_case as a S4_nation_state Russia-axis denominator control, sibling to russia-cbr-crypto-payment-ban-2022 and parent to binance-russia-exit-commex-2023." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.reuters.com/investigates/special-report/finance-crypto-binance-russia/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/business/2022/04/22/binance-denies-allegations-it-shared-russian-users-data-with-law-enforcement/
- citation[2]: `primary_corporate` replayable=`True` https://www.binance.com/en/blog/leadership/binance--russia-openness-transparency-and-honesty-421499824684903741

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
  "queue_id": 191,
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
  "queue_id": 191,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/russia-rosfinmonitoring-binance-russia-rails-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
