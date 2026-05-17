# v0.3 Review Packet: `mtgox-bankruptcy-tokyo-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `152` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `mtgox-bankruptcy-tokyo-2014` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `MTGOX_KK` |
| event_date | `2014-02-28` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-bankruptcy-tokyo-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Mt. Gox K.K. (MtGox Co., Ltd.)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 5 |
| primary observation sources | 3 |
| replayable observation sources | 5 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2014-02-28 Mt. Gox K.K. civil-rehabilitation filing at the Tokyo District Court permanently closed all Mt. Gox on/off-ramps (BTC, JPY, USD, EUR) and replaced the mtgox.com trading UI with a wind-down / Rehabilitation-Trustee announcement surface. Observational axes at offramp_cex and l4_frontend. Historical- baseline tier; not used in 2017+ comparable denominators." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://www.npr.org/sections/thetwo-way/2014/02/28/283863219/mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost
- citation[2]: `supporting_journalism` replayable=`True` https://www.bloomberg.com/news/articles/2014-02-28/mt-gox-exchange-files-for-bankruptcy

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
  "queue_id": 152,
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
  "queue_id": 152,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-bankruptcy-tokyo-2014.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
