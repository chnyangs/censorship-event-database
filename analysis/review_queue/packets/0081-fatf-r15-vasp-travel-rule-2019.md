# v0.3 Review Packet: `fatf-r15-vasp-travel-rule-2019`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `81` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `fatf-r15-vasp-travel-rule-2019` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `FATF` |
| event_date | `2019-06-21` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-r15-vasp-travel-rule-2019.yaml` |
| target_kind | `entity` |
| target_actor | `FATF-jurisdiction VASP ecosystem` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
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

"FATF's 2019-06-21 adoption of the Interpretive Note to Recommendation 15 established the supranational legal substrate requiring Virtual Asset Service Providers in FATF member jurisdictions to apply the Travel Rule (USD/EUR 1000 originator + beneficiary metadata transmission threshold). Direct attribution at the supranational-aggregate off-ramp layer; downstream national implementations (Korea 2022-03-25, EU TFR 2023, etc.) are tracked as separate child events." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets.html
- citation[1]: `primary_legal` replayable=`False` https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Public-statement-virtual-assets.html

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
  "queue_id": 81,
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
  "queue_id": 81,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-r15-vasp-travel-rule-2019.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
