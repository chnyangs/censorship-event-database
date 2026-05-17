# v0.3 Review Packet: `mtgox-coinlab-civil-2013`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `153` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `mtgox-coinlab-civil-2013` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `court_civil_order` |
| actor | `US_WDWA_COURT` |
| event_date | `2013-05-02` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-coinlab-civil-2013.yaml` |
| target_kind | `entity` |
| target_actor | `Mt. Gox K.K.` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"CoinLab v. Mt. Gox civil complaint (filed 2013-05-02 in US District Court, Western District of Washington, Case 2:13-cv-00777-RSL) sought $75M damages for Mt. Gox's breach of the November 2012 North American operations agreement. The row records observation_kind=observed_no_change + attribution=none at offramp_cex over the 11-day window 2013-05-02 to 2013-05-13 (closing one day before the federal Dwolla seizure mtgox-dhs-dwolla-wells-fargo-seizure-2013), because the civil filing itself produced no observable USD on/off-ramp change. null_event shape; historical-baseline tier; not used in main statistical denominators." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.coindesk.com/markets/2013/05/03/coinlab-sues-mt-gox-in-us-court
- citation[1]: `supporting_journalism` replayable=`True` https://www.geekwire.com/2013/bitcoin-seattles-coinlab-files-75m-suit-mt-gox-exchange-alleges-breach-contract/
- citation[2]: `supporting_journalism` replayable=`True` https://dockets.justia.com/docket/washington/wawdce/2:2013cv00777/192566
- citation[3]: `primary_legal` replayable=`True` https://www.courtlistener.com/docket/4537232/coinlab-inc-v-mt-gox-kk/

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
  "queue_id": 153,
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
  "queue_id": 153,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-coinlab-civil-2013.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
