# v0.3 Review Packet: `karpeles-arrest-tokyo-mtgox-2015`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `127` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `karpeles-arrest-tokyo-mtgox-2015` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `JP_TMPD` |
| event_date | `2015-08-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/karpeles-arrest-tokyo-mtgox-2015.yaml` |
| target_kind | `entity` |
| target_actor | `Mark Karpelès (Mt. Gox K.K. former CEO)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Tokyo MPD arrested Mark Karpelès (former Mt. Gox CEO) on 2015-08-01 on suspicion of data manipulation (and was later indicted for embezzlement and aggravated breach of trust) related to the 2014 collapse. Cascade impact is observation_kind=observed_no_change + attribution=none because Mt. Gox was already in bankruptcy from 2014-02-28 — the arrest does not produce observable change at any layer beyond the pre-existing freeze. Historical-baseline tier; not used in main statistical denominators." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.reuters.com/article/us-bitcoin-mtgox-arrest-idUSKCN0Q608B20150801
- citation[1]: `supporting_journalism` replayable=`True` https://www.cnn.com/2015/08/01/asia/bitcoin-mt-gox-karpeles-arrested/index.html
- citation[2]: `supporting_journalism` replayable=`True` https://www.nbcnews.com/news/world/head-failed-japan-based-bitcoin-exchange-mt-gox-arrested-n402391

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
  "queue_id": 127,
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
  "queue_id": 127,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/karpeles-arrest-tokyo-mtgox-2015.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
