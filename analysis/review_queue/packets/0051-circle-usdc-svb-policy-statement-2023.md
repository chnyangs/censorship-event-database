# v0.3 Review Packet: `circle-usdc-svb-policy-statement-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `51` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `circle-usdc-svb-policy-statement-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `CIRCLE_USDC_ISSUER` |
| event_date | `2023-03-11` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/circle-usdc-svb-policy-statement-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Circle Internet Financial (USDC issuer)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Circle Internet Financial's 2023-03-11 corporate-transparency statement disclosing ~$3.3B of USDC cash reserves held at Silicon Valley Bank at the time of FDIC receivership — paired with Circle's commitment to full 1:1 USDC backing using corporate funds and the pre-announcement of redemption / minting resumption Monday 2023-03-13 — documents an S5 stablecoin-issuer policy posture under acute banking-rail stress. No address-level freeze, holder restriction, or off-ramp action is taken; the row carries no observed_change and functions as denominator control for the S5 corporate-policy-change stratum, scoping the 'transparency over restriction' baseline against which S5 OFAC-cascade and discretionary-freeze rows can be compared." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes
- citation[1]: `primary_corporate` replayable=`True` https://www.circle.com/blog/an-update-on-usdc-and-silicon-valley-bank

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
  "queue_id": 51,
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
  "queue_id": 51,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/circle-usdc-svb-policy-statement-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
