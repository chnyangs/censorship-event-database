# v0.3 Review Packet: `uniswap-tokenized-stocks-delisting-2021-07`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `248` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `uniswap-tokenized-stocks-delisting-2021-07` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `uniswap_labs` |
| event_date | `2021-07-23` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-tokenized-stocks-delisting-2021-07.yaml` |
| target_kind | `entity` |
| target_actor | `Uniswap Labs (frontend operator, app.uniswap.org)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Uniswap Labs' 2021-07-23 restriction of approximately 100 tokenized-equity / option / synthetic-equity tokens from the app.uniswap.org frontend UI — taken preemptively, with no SEC enforcement instrument issued at that date and without corresponding action at the Uniswap Protocol smart-contract layer — documents the 2021 antecedent of the 2023 sibling uniswap-frontend-delisting-2023 and the cleanest 2021 example in the dataset of an L4-only frontend-operator compliance action taken in anticipation of (not in reaction to) US securities-enforcement pressure." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://app.uniswap.org

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
  "queue_id": 248,
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
  "queue_id": 248,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-tokenized-stocks-delisting-2021-07.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
