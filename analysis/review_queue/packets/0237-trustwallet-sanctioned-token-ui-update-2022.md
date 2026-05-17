# v0.3 Review Packet: `trustwallet-sanctioned-token-ui-update-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `237` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `trustwallet-sanctioned-token-ui-update-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `TRUSTWALLET_BINANCE` |
| event_date | `2022-08-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/trustwallet-sanctioned-token-ui-update-2022.yaml` |
| target_kind | `entity` |
| target_actor | `Trust Wallet (Binance affiliate)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The candidate event "Trust Wallet (Binance-affiliated) UI update to display warnings on OFAC-sanctioned tokens following the 2022-08-08 OFAC SDN cascade (related event tornado-cash-ofac-2022)" could not be verified against any pinned Trust-Wallet-operated corporate channel in this authoring pass. The row is coded as a low-confidence null_event with one observed_no_change row at l4_frontend (attribution=none) and l4_frontend coverage.status= not_measured pending human audit of Trust Wallet release notes, GitHub history, and community discussion. 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://trustwallet.com/blog/cryptocurrency/tornado-cash-explained

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
  "queue_id": 237,
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
  "queue_id": 237,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/trustwallet-sanctioned-token-ui-update-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
