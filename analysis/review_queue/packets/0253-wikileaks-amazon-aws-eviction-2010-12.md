# v0.3 Review Packet: `wikileaks-amazon-aws-eviction-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `253` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-amazon-aws-eviction-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `AMAZON_AWS_OPERATOR` |
| event_date | `2010-12-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-amazon-aws-eviction-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `WikiLeaks (Sunshine Press)` |

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

"On 2010-12-01, Amazon Web Services terminated WikiLeaks' EC2 / S3 cloud-hosting account approximately 2 days after WikiLeaks had migrated to AWS to escape DDoS against its self-hosted infrastructure, following same-morning public pressure from Senator Joe Lieberman's office. AWS publicly grounded the termination in TOS violation and denied that the Lieberman contact prompted the decision. Observational axis at l4_frontend (cloud-hosting eviction). Discovery-only precedent for the corporate-intermediary censorship pattern; not eligible for the 2017+ comparable denominator." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://aws.amazon.com/message/65348/
- citation[1]: `supporting_journalism` replayable=`True` https://www.cnn.com/2010/US/12/01/wikileaks.amazon/index.html
- citation[2]: `supporting_journalism` replayable=`True` https://www.theregister.com/2010/12/01/wikileaks_disappers_from_amazon_us/

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
  "queue_id": 253,
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
  "queue_id": 253,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-amazon-aws-eviction-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
