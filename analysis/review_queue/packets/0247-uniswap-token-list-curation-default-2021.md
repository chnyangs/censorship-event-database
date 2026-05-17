# v0.3 Review Packet: `uniswap-token-list-curation-default-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `247` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `uniswap-token-list-curation-default-2021` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `uniswap_labs` |
| event_date | `2021-07-23` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-token-list-curation-default-2021.yaml` |
| target_kind | `entity` |
| target_actor | `Uniswap Labs (frontend operator, app.uniswap.org)` |

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

"Uniswap Labs' default token list curation policy — formalized 2021-07-23 alongside the synthetic-stocks delisting batch and after the 2021-04 Wells-notice-era regulatory-pressure cycle — establishes that the US-based frontend operator (Uniswap Labs) holds discretionary curation power over which ERC-20 tokens are surfaced on app.uniswap.org, separate from the autonomous on-chain Uniswap Protocol smart contracts. This framework row carries no row-local observed_change (the per-token cascade observations are coded on the sibling events uniswap-tokenized-stocks-delisting-2021-07 and uniswap-frontend-delisting-2023); it functions as a policy-scoping anchor for the Uniswap-Labs frontend-curation arc and as denominator control in S5 corporate-frontend analyses." 

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
  "queue_id": 247,
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
  "queue_id": 247,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-token-list-curation-default-2021.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
