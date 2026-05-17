# v0.3 Review Packet: `wikileaks-mastercard-suspension-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `256` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-mastercard-suspension-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `MASTERCARD_OPERATOR` |
| event_date | `2010-12-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-mastercard-suspension-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `MasterCard Worldwide` |

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

"MasterCard Worldwide announced on 2010-12-06 that it was suspending acceptance of MasterCard-branded cards for WikiLeaks donations on the grounds that its rules prohibit customers from facilitating illegal action, severing the card-network donation channel routed through the DataCell ehf merchant gateway; the row is registered as a single-layer offramp_cex operator-policy-change observation in the discovery-only 2008-2012 tier and does not assert ISP-level network blocking, L1 consensus engagement, RPC-compliance filtering, asset-onchain freezing, or L4 frontend takedown by the card-network operator." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.mastercard.com/
- citation[1]: `supporting_journalism` replayable=`True` https://money.cnn.com/2010/12/08/news/companies/mastercard_wiki/index.htm
- citation[2]: `supporting_journalism` replayable=`True` https://wikileaks.org/Banking-Blockade.html

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
  "queue_id": 256,
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
  "queue_id": 256,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-mastercard-suspension-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
