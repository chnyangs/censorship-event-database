# v0.3 Review Packet: `storm-semenov-doj-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `218` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `storm-semenov-doj-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_SDNY` |
| event_date | `2023-08-23` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/storm-semenov-doj-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Roman Storm + Roman Semenov` |

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

"DOJ SDNY indictment of Roman Storm and Roman Semenov on 2023-08-23 — co-occurring with the same-day OFAC individual designation of Semenov — documented US criminal-law enforcement of crypto privacy-tool developers, paired with the 2022-08-10 NL FIOD Pertsev arrest as the second major cross-jurisdictional Tornado Cash developer-enforcement event." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations

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
  "queue_id": 218,
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
  "queue_id": 218,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/storm-semenov-doj-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
