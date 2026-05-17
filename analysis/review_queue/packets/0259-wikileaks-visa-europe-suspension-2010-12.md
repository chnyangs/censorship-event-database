# v0.3 Review Packet: `wikileaks-visa-europe-suspension-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `259` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-visa-europe-suspension-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `VISA_EUROPE_OPERATOR` |
| event_date | `2010-12-07` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-visa-europe-suspension-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `DataCell ehf (Iceland-based card-donation processor for WikiLeaks)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 1 |
| replayable observation sources | 4 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

On 2010-12-07 Visa Europe publicly suspended acceptance of WikiLeaks-related card donations pending an investigation of whether the WikiLeaks website contravened Visa operating rules, and Visa-licensed acquirer Teller A/S (Danish, with agent Korta in Iceland) terminated the DataCell ehf merchant agreement that had carried WikiLeaks donations under a services agreement dated 2010-10-18. The cascade surface is the card-network acquirer rail (offramp_cex layer analogue for the 2010 fiat payments stack); attribution is direct via Visa Europe's own corporate statement and corroborating Reuters / BBC / Guardian contemporaneous journalism. 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.visaeurope.com/media/pdf/wikileaks_statement.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://www.reuters.com/article/idUSTRE6B65T420101207
- citation[2]: `supporting_journalism` replayable=`True` https://www.bbc.co.uk/news/world-us-canada-11935539
- citation[3]: `supporting_journalism` replayable=`True` https://www.theguardian.com/media/2010/dec/07/visa-mastercard-wikileaks-back

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
  "queue_id": 259,
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
  "queue_id": 259,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-visa-europe-suspension-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
