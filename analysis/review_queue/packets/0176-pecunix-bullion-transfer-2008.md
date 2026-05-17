# v0.3 Review Packet: `pecunix-bullion-transfer-2008`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `176` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `pecunix-bullion-transfer-2008` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `PECUNIX_OPERATOR` |
| event_date | `2008-06-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/pecunix-bullion-transfer-2008.yaml` |
| target_kind | `entity` |
| target_actor | `Pecunix` |

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

"In 2008, the Pecunix directors transferred the platform's gold bullion reserves from Mat Securitas Express AG (Zurich, Switzerland) to an undisclosed location — a single custody-layer offramp_cex operational-policy change at a digital-gold-currency administrator, plausibly responsive to the broader 2008 US DOJ digital-gold enforcement cycle (e-Gold guilty plea, e-Bullion seizure) though not directly triggered by any sanction or order naming Pecunix. The row claims only this single-layer custody policy change with attribution=plausible; no L0/L1/L3/L4/asset-onchain effects are coded. Discovery-tier only: no comparable-analysis use." 

## Trigger Citations

- citation[0]: `supporting_community` replayable=`True` https://en.wikipedia.org/wiki/Digital_gold_currency
- citation[1]: `supporting_community` replayable=`True` https://en-academic.com/dic.nsf/enwiki/1580701
- citation[2]: `supporting_journalism` replayable=`True` https://themonetaryfuture.blogspot.com/2010/07/overview-of-pecunix.html

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
  "queue_id": 176,
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
  "queue_id": 176,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/pecunix-bullion-transfer-2008.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
