# v0.3 Review Packet: `1inch-us-geofence-2021-09`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `1` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `1inch-us-geofence-2021-09` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `1INCH_FOUNDATION` |
| event_date | `2021-09-29` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/1inch-us-geofence-2021-09.yaml` |
| target_kind | `entity` |
| target_actor | `1inch Network / 1inch Foundation (frontend operator)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2021-09-29 the 1inch Network / 1inch Foundation frontend operator added a pop-up notification and an IP-based technical layer that geofenced US-vantage users from the app.1inch.io frontend, while the underlying 1inch Aggregation Protocol smart-contract layer remained unaffected. The restriction was voluntary (no specific US regulator trigger named); the operator's stated rationale was perceived US regulatory risk pending a US-targeted 1inch Pro product. Load-bearing axis is l4_frontend on a US-vantage subset." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://help.1inch.io/en/articles/5099197-which-countries-are-restricted-from-using-the-1inch-dapp
- citation[1]: `supporting_journalism` replayable=`True` https://cryptoslate.com/1inch-geofences-us-ip-addresses-says-new-product-for-the-american-market-is-in-prep/

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
  "queue_id": 1,
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
  "queue_id": 1,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/1inch-us-geofence-2021-09.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
