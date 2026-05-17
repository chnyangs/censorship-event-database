# v0.3 Review Packet: `sec-v-uniswap-wells-notice-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `207` |
| status | `pending` |
| priority | `90` |
| bucket | `legacy_rejected_reference_review` |
| next_action | `confirm_rejected_reference_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `sec-v-uniswap-wells-notice-2024` |
| yaml_status | `rejected` |
| internal_status | `retracted` |
| verification_state | `legacy_rejected_reference` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `sec_action` |
| actor | `US_SEC` |
| event_date | `2024-04-10` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-v-uniswap-wells-notice-2024.yaml` |
| target_kind | `entity` |
| target_actor | `Uniswap Labs` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"SEC Wells notice against Uniswap Labs (disclosed 2024-04-10, dropped 2025-02-25) was the lowest-enforcement-intensity SEC crypto event in the dataset, producing no L4 cascade. Demonstrates that SEC pre-enforcement signals alone — without formal complaint filing — do NOT produce measurable censorship effects at the frontend or off-ramp layers." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://blog.uniswap.org/fighting-for-defi
- citation[1]: `primary_legal` replayable=`True` https://www.sec.gov/newsroom/press-releases

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
  "queue_id": 207,
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
  "queue_id": 207,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-v-uniswap-wells-notice-2024.yaml",
  "verification_state": "legacy_rejected_reference"
}
```
