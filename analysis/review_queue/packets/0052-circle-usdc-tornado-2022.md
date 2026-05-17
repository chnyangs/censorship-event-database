# v0.3 Review Packet: `circle-usdc-tornado-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `52` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `circle-usdc-tornado-2022` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `circle_usdc_issuer` |
| event_date | `2022-08-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/circle-usdc-tornado-2022.yaml` |
| target_kind | `address_set` |
| target_actor | `Circle (USDC)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Circle's 2022-08-08 USDC blacklist action against Tornado Cash-adjacent addresses (first on-chain tx at 19:25:35 UTC, ~5.93 hours after OFAC designation) constitutes a distinct corporate-policy-change event documenting fast stablecoin-issuer compliance with OFAC SDN. Paper- relevant asymmetry datapoint paired with Tether's 2023-12-09 retroactive sweep (~500-day-later compliance)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.circle.com/blog/ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action
- citation[1]: `primary_onchain` replayable=`False` https://etherscan.io/tx/0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9

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
  "queue_id": 52,
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
  "queue_id": 52,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/circle-usdc-tornado-2022.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
