# v0.3 Review Packet: `china-weibo-crypto-exchange-purge-2021-03`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `48` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `china-weibo-crypto-exchange-purge-2021-03` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `CN_WEIBO_CAC` |
| event_date | `2021-03-11` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-weibo-crypto-exchange-purge-2021-03.yaml` |
| target_kind | `entity` |
| target_actor | `Sina Weibo official accounts of Binance / Huobi / OKEx` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 3 |
| observation sources | 6 |
| primary observation sources | 0 |
| replayable observation sources | 6 |
| primary replayable observation sources | 0 |

Machine blockers: `no_observation_primary_source_detected`
Machine notes: `none`

## Scoped Claim

On 2021-03-11 morning (Beijing time), the official Chinese- language Sina Weibo accounts of Binance, Huobi (HTX) and OKEx (OKX) were rendered inaccessible with the standard PRC content- takedown formula, eliminating the search/social discovery path to those exchanges' Chinese-language official content. The takedowns are coded attribution=plausible (CAC-coordinated inference) per codebook §1.4 because no public per-account CAC directive was archived; the cascade surface is L4 frontend at the discovery layer only. 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge
- citation[1]: `supporting_journalism` replayable=`True` https://www.globaltimes.cn/page/202103/1218100.shtml
- citation[2]: `supporting_journalism` replayable=`True` https://forkast.news/weibo-takedown-huobi-binance-okex-crypto-china/

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
  "queue_id": 48,
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
  "queue_id": 48,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-weibo-crypto-exchange-purge-2021-03.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
