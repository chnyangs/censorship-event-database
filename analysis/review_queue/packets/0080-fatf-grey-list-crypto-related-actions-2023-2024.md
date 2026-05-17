# v0.3 Review Packet: `fatf-grey-list-crypto-related-actions-2023-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `80` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `fatf-grey-list-crypto-related-actions-2023-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `FATF` |
| event_date | `2023-10-27` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-grey-list-crypto-related-actions-2023-2024.yaml` |
| target_kind | `entity` |
| target_actor | `FATF grey-list member states (UAE, Türkiye in-scope subset)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Across the 2023-2024 FATF plenary cycle, two grey-list adjustments foregrounded explicit crypto / VASP compliance findings: the United Arab Emirates (action-plan progress recognised at the October 2023 plenary, formal removal 2024-02-23) and Türkiye (removed 2024-06-28 following passage of the 2024-06-26 SPK crypto-asset licensing law). Coded as null_event / null_case at the corpus's resolution: no per-event observed_change cascade is directly attributable to the grey-list adjustments themselves; downstream member-state VASP enforcement actions are tracked as separate child events." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fatf-gafi.org/en/the-fatf/news.html
- citation[1]: `primary_legal` replayable=`True` https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf
- citation[2]: `supporting_journalism` replayable=`True` https://complyadvantage.com/insights/fatf-plenary-june-2024/
- citation[3]: `supporting_journalism` replayable=`True` https://www.nortonrosefulbright.com/en/knowledge/publications/eb06aa7c/uae-removed-from-the-fatf-grey-list

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
  "queue_id": 80,
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
  "queue_id": 80,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-grey-list-crypto-related-actions-2023-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
