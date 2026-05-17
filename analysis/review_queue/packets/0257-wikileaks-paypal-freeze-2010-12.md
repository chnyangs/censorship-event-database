# v0.3 Review Packet: `wikileaks-paypal-freeze-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `257` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-paypal-freeze-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `PAYPAL_OPERATOR` |
| event_date | `2010-12-04` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-paypal-freeze-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `WikiLeaks (donation pass-through via Wau-Holland-Stiftung)` |

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

"On 2010-12-04, PayPal permanently restricted the WikiLeaks donation merchant account (registered to the Wau-Holland-Stiftung pass-through), citing its Acceptable Use Policy prohibition on facilitating activities determined illegal. PayPal VP Osama Bedier subsequently (2010-12-08, Le Web Paris) acknowledged that a US State Department determination that WikiLeaks' activities were illegal under US law informed the decision. The freeze is the pre-Bitcoin conceptual analog of an offramp_cex / payment-rail closure (the only observed cascade axis in 2010 in the absence of any blockchain-asset substrate for WikiLeaks donations). Observational axis at offramp_cex (load-bearing, attribution=direct via PayPal's own corporate statement). Admission-anchor-grade promotion pending pinned archive captures." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.thepaypalblog.com/2010/12/why-paypal-restricted-wikileaks-account/
- citation[1]: `supporting_journalism` replayable=`True` https://www.cnn.com/2010/US/12/04/wikileaks.pay.pal/index.html
- citation[2]: `supporting_journalism` replayable=`True` https://www.bloomberg.com/news/articles/2010-12-04/paypal-restricts-wikileaks-account-as-website-comes-under-global-scrutity
- citation[3]: `supporting_journalism` replayable=`True` https://techcrunch.com/2010/12/08/paypal-wikileaks/

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
  "queue_id": 257,
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
  "queue_id": 257,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-paypal-freeze-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
