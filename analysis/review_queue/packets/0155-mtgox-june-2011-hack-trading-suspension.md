# v0.3 Review Packet: `mtgox-june-2011-hack-trading-suspension`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `155` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `mtgox-june-2011-hack-trading-suspension` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `MTGOX_OPERATOR` |
| event_date | `2011-06-19` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-june-2011-hack-trading-suspension.yaml` |
| target_kind | `entity` |
| target_actor | `Mt. Gox` |

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

"Mt. Gox suspended all trading globally from 2011-06-20 to 2011-06-26 after a 2011-06-19 user-database compromise was used to flood the order book with sell orders and crash the nominal BTC price to ~$0.01. The row claims only this single-layer offramp_cex operator-suspension observation, coded as attribution=plausible because the suspension is an operator-policy choice in response to a hack rather than externally compelled censorship. Discovery-only tier; not used in main statistical denominators." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://mtgox.com/press_release_20110630.html
- citation[1]: `supporting_journalism` replayable=`True` https://en.wikipedia.org/wiki/Mt._Gox
- citation[2]: `supporting_journalism` replayable=`True` https://blockonomi.com/mt-gox-hack/

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
  "queue_id": 155,
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
  "queue_id": 155,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-june-2011-hack-trading-suspension.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
