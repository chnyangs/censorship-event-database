# v0.3 Review Packet: `iceland-cbi-foreign-exchange-bitcoin-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `106` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `iceland-cbi-foreign-exchange-bitcoin-2014` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `IS_CBI` |
| event_date | `2014-03-19` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/iceland-cbi-foreign-exchange-bitcoin-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Iceland-resident bitcoin purchasers` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The Central Bank of Iceland (Seðlabanki Íslands) news release of 2014-03-19, "Significant risk attached to use of virtual currency", stated the CBI's interpretation that purchases of bitcoin by Icelandic residents are prohibited under the Iceland Foreign Exchange Act and the post-2008 capital-controls regime. The cascade surface is class-level on Icelandic residents; no exchange-side Iceland-resident cutoff is documented in this authoring pass, so offramp_cex carries an observation_kind=not_observed row with attribution=plausible. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.cb.is/publications/news/news/2014/03/19/Significant-risk-attached-to-use-of-virtual-currency/
- citation[1]: `primary_legal` replayable=`True` https://www.sedlabanki.is/?PageId=eeebb4db-0460-11e5-93fa-005056bc0bdb&newsid=1fca32cd-af9c-11e3-93f5-005056bc0bdb
- citation[2]: `supporting_tracker` replayable=`True` https://www.loc.gov/item/global-legal-monitor/2014-08-12/iceland-national-digital-currency-auroracoin-launched/

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
  "queue_id": 106,
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
  "queue_id": 106,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/iceland-cbi-foreign-exchange-bitcoin-2014.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
