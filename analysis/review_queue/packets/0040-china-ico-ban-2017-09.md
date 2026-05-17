# v0.3 Review Packet: `china-ico-ban-2017-09`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `40` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `china-ico-ban-2017-09` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `CN_PBOC` |
| event_date | `2017-09-04` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-ico-ban-2017-09.yaml` |
| target_kind | `entity` |
| target_actor | `PRC ICO + CNY-pair-exchange ecosystem (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 2 |
| replayable observation sources | 4 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The PBOC 7-Ministry Notice of 2017-09-04 (公告 [2017]) declared ICO token-issuance fundraising illegal as unauthorized public financing, halted all ICO financing activities from date of issuance, mandated refund arrangements for completed ICOs, and prohibited PRC financial institutions and non-bank payment agencies from token-related services. The asset_onchain layer carries the jurisdiction-wide issuer-rail prohibition observation; the offramp_cex layer carries the sector-wide CNY-pair delisting observation. Both rest on direct attribution from the notice text. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/3374222/index.html
- citation[1]: `supporting_tracker` replayable=`True` https://www.loc.gov/item/global-legal-monitor/2017-10-19/china-regulators-ban-companies-from-raising-money-through-virtual-currencies/
- citation[2]: `supporting_journalism` replayable=`True` https://www.cnbc.com/2017/09/04/chinese-icos-china-bans-fundraising-through-initial-coin-offerings-report-says.html

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
  "queue_id": 40,
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
  "queue_id": 40,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-ico-ban-2017-09.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
