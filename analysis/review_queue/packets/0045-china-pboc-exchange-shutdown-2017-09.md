# v0.3 Review Packet: `china-pboc-exchange-shutdown-2017-09`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `45` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `china-pboc-exchange-shutdown-2017-09` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `CN_PBOC` |
| event_date | `2017-09-29` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-pboc-exchange-shutdown-2017-09.yaml` |
| target_kind | `entity` |
| target_actor | `PRC domestic crypto-exchange triad (BTCC, OKCoin, Huobi)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 6 |
| primary observation sources | 2 |
| replayable observation sources | 6 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

In mid-September 2017 the PBOC and affiliated PRC regulators instructed domestic cryptocurrency exchanges to cease CNY-paired trading and wind down domestic operations; within ~2 weeks the PRC exchange triad (BTCC, OKCoin, Huobi) had announced and executed cessation of domestic CNY-paired trading, with BTCC ceasing all trading on 2017-09-30 and Huobi / OKCoin completing staged shutdown by end of October. The offramp_cex layer carries the load-bearing direct-attribution observation; L4 frontend reactions are consistent with the cascade but require a Wayback- capture pass before they may anchor a separate observed_change row. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` http://www.pbc.gov.cn/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/markets/2017/09/15/chinas-bitcoin-exchanges-receive-shutdown-orders-and-closure-timeline/
- citation[2]: `supporting_journalism` replayable=`True` https://www.coindesk.com/markets/2017/09/15/huobi-okcoin-to-stop-yuan-to-bitcoin-trading-by-octobers-end/
- citation[3]: `supporting_journalism` replayable=`True` https://qz.com/1079908/huobi-and-okcoin-chinas-two-biggest-bitcoin-exchanges-will-halt-all-trading-services-for-local-customers

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
  "queue_id": 45,
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
  "queue_id": 45,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-pboc-exchange-shutdown-2017-09.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
