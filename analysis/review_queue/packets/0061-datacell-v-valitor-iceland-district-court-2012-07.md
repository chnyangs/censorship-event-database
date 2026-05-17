# v0.3 Review Packet: `datacell-v-valitor-iceland-district-court-2012-07`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `61` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `datacell-v-valitor-iceland-district-court-2012-07` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `court_civil_order` |
| actor | `IS_REYKJAVIK_DISTRICT_COURT` |
| event_date | `2012-07-12` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/datacell-v-valitor-iceland-district-court-2012-07.yaml` |
| target_kind | `entity` |
| target_actor | `Valitor hf. / DataCell ehf.` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 6 |
| replayable trigger anchors | 6 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 1 |
| replayable observation sources | 4 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2012-07-12, the Reykjavik District Court (Iceland) ordered Valitor hf. (the Iceland Visa/Mastercard sub-processor) to restore the DataCell ehf. merchant gateway used to collect WikiLeaks donations over Visa/Mastercard card rails within 14 days, on pain of daily fines of ISK 800,000 for each day of non-compliance. The ruling is the first judicial finding worldwide that a card-network WikiLeaks payment blockade was unlawful at the merchant-services contract layer, and constitutes a court-ordered counter-censorship (recovery / restoration) event at the offramp_cex cascade axis. The cascade surface moves in the restoration direction, away from the 2010-12 WikiLeaks payment-rail blockade. Observational axis at offramp_cex (load-bearing, attribution=direct via the court order self- attesting the restoration mandate). Admission-anchor-grade promotion pending pinned archive captures." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fink.org/FILES/translated-judgment-valitor.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://www.bloomberg.com/news/articles/2012-07-12/iceland-court-orders-valitor-to-process-wikileaks-donations-1-
- citation[2]: `supporting_journalism` replayable=`True` https://grapevine.is/news/2012/07/13/datacell-wins-case-against-valitor/
- citation[3]: `supporting_journalism` replayable=`True` https://rsf.org/en/court-orders-visa-subcontractor-lift-block-payments-wikileaks
- citation[4]: `supporting_journalism` replayable=`True` https://www.computerworld.com/article/1417186/wikileaks-donations-via-visa-and-mastercard-may-resume-icelandic-court-rules.html
- citation[5]: `supporting_community` replayable=`True` https://wikileaks.org/Wikileaks-has-launched-a-case.html

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
  "queue_id": 61,
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
  "queue_id": 61,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/datacell-v-valitor-iceland-district-court-2012-07.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
