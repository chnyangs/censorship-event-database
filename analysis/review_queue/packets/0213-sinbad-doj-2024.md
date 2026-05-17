# v0.3 Review Packet: `sinbad-doj-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `213` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `sinbad-doj-2024` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_NDGA` |
| event_date | `2025-01-10` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sinbad-doj-2024.yaml` |
| target_kind | `entity` |
| target_actor | `Sinbad (sinbad.io)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2025-01-10 DOJ Office of Public Affairs unsealing of the NDGA grand-jury indictment of Roman Vitalyevich Ostapenko, Alexander Evgenievich Oleynik, and Anton Vyachlavovich Tarasov for operating the Sinbad.io Bitcoin mixer produced a 2-layer comparison-shape cascade in the dataset: an l4_frontend finality anchored by the operator indictment (atop the prior 2023-11-27 FBI + Netherlands FIOD + Finland NBI domain seizure) and an offramp_cex mixer-operator-state transition (2 of 3 operators arrested 2024-12-01; Tarasov at large). Distinct from sinbad-ofac-2023 (OFAC SDN designation 2023-11-29) and from chipmixer-doj-2023 / samourai-doj-2024 in that the enforcement was time-split: multi-jurisdictional infrastructure seizure ~13 months before the single-jurisdictional US-only operator indictment." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering
- citation[1]: `primary_legal` replayable=`True` https://complianceconcourse.willkie.com/articles/federal-jury-indicts-blender-io-and-sinbad-io-operators-on-money-laundering-charges/

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
  "queue_id": 213,
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
  "queue_id": 213,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sinbad-doj-2024.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
