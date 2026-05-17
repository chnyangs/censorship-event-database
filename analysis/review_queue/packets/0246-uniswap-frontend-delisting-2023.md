# v0.3 Review Packet: `uniswap-frontend-delisting-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `246` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `uniswap-frontend-delisting-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `uniswap_labs` |
| event_date | `2023-07-21` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-frontend-delisting-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Uniswap Labs (frontend operator)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Uniswap Labs' 2023-07-21 restriction of more than 100 ERC-20 tokens from the app.uniswap.org frontend UI — without corresponding action at the Uniswap Protocol (smart-contract) layer — documents a standalone L4-only frontend-operator compliance action. Paper-relevant as the clearest example of frontend/protocol decoupling in the dataset." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://blog.uniswap.org/

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
  "queue_id": 246,
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
  "queue_id": 246,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-frontend-delisting-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
