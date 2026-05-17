# v0.3 Review Packet: `fatf-targeted-update-va-vasp-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `83` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `fatf-targeted-update-va-vasp-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `FATF` |
| event_date | `2023-06-27` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-targeted-update-va-vasp-2023.yaml` |
| target_kind | `entity` |
| target_actor | `FATF-jurisdiction VASP / DeFi / stablecoin ecosystem` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"FATF's 2023-06-27 'Virtual Assets: Targeted Update on Implementation of the FATF Standards on VAs and VASPs' is the third major FATF update post-R.15 (2019) and post-2021 Targeted Update, documenting that 75% of evaluated jurisdictions are only partially or not compliant with R.15/INR.15 and that >50% of 151 surveyed jurisdictions had taken no Travel Rule implementation steps. Coded as null_event / null_case at the corpus's resolution: no per-event observed_change cascade is directly attributable to the 2023-06-27 publication date; downstream member-state implementations (EU TFR 2023, national VASP rule updates) are tracked as separate child events." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-update-virtual-assets-vasps-2023.html
- citation[1]: `primary_legal` replayable=`True` https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/June2023-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf

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
  "queue_id": 83,
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
  "queue_id": 83,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-targeted-update-va-vasp-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
