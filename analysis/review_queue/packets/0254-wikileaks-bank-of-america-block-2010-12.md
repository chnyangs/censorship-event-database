# v0.3 Review Packet: `wikileaks-bank-of-america-block-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `254` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-bank-of-america-block-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `BANK_OF_AMERICA_OPERATOR` |
| event_date | `2010-12-18` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-bank-of-america-block-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `WikiLeaks` |

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

Bank of America's public statement of 2010-12-18 announcing that the bank "will not process any transactions of any type that we have reason to believe are intended for WikiLeaks", citing internal-payment-policy interpretation regarding WikiLeaks activities deemed "inconsistent with our internal policies for processing payments", constitutes a discovery-ledger corporate- policy-change event documenting US-bank-rail off-ramp closure against WikiLeaks. Fifth and final constituent action of the December 2010 "banking blockade" cluster. 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://newsroom.bankofamerica.com/
- citation[1]: `supporting_journalism` replayable=`True` https://www.reuters.com/article/idUSTRE6BH0NQ/
- citation[2]: `supporting_journalism` replayable=`True` https://www.nbcnews.com/id/wbna40728284
- citation[3]: `supporting_journalism` replayable=`True` https://www.aljazeera.com/economy/2010/12/18/bank-of-america-cuts-off-wikileaks
- citation[4]: `supporting_journalism` replayable=`True` https://www.cbsnews.com/news/bank-of-america-to-block-donations-to-wikileaks/
- citation[5]: `supporting_community` replayable=`True` https://wikileaks.org/Banking-Blockade.html

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
  "queue_id": 254,
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
  "queue_id": 254,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-bank-of-america-block-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
