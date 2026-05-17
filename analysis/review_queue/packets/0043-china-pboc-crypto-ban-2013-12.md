# v0.3 Review Packet: `china-pboc-crypto-ban-2013-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `43` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `china-pboc-crypto-ban-2013-12` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `CN_PBOC` |
| event_date | `2013-12-05` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-pboc-crypto-ban-2013-12.yaml` |
| target_kind | `entity` |
| target_actor | `PRC financial-institution + exchange ecosystem (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

PBOC Notice 2013/289 of 2013-12-05 directed Chinese banks and payment service providers to refuse Bitcoin-related accounts and services; within ~13 days the PRC Bitcoin-exchange triad (BTC China, OKCoin, Huobi) paused CNY deposit channels in compliance. The offramp_cex layer carries the load-bearing direct-attribution observation; L4 frontend reactions are consistent with the cascade but require a Wayback-capture pass before they may anchor a separate observed_change row. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2982357/index.html
- citation[1]: `primary_legal` replayable=`False` http://www.gov.cn/gzdt/2013-12/05/content_2542584.htm
- citation[2]: `supporting_tracker` replayable=`True` https://www.loc.gov/item/global-legal-monitor/2014-01-13/china-regulators-issue-notice-on-bitcoin-risks/

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
  "queue_id": 43,
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
  "queue_id": 43,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-pboc-crypto-ban-2013-12.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
