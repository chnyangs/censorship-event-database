# v0.3 Review Packet: `eu-14th-russia-sanctions-spfs-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `70` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `eu-14th-russia-sanctions-spfs-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `non_us_sanctions` |
| actor | `EU_COUNCIL` |
| event_date | `2024-06-24` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-14th-russia-sanctions-spfs-2024.yaml` |
| target_kind | `entity` |
| target_actor | `SPFS financial-messaging network + non-EU CASPs facilitating Russian defence procurement (Annex XLV class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Council Regulation (EU) 2024/1745, adopted on 2024-06-24 as the EU's 14th Russia-sanctions package, introduced the first explicit EU prohibition on connecting to Russia's SPFS financial-messaging network and extended the crypto- asset provisions framework via new Article 5ad (Annex XLV class for non-EU CASPs facilitating Russian defence- industrial procurement). Coded as null_event / null_case at the corpus's resolution: the regulation is framework- level with Annex XLV listings populated by subsequent implementing decisions; no per-event observed_change cascade is directly attributable to the 2024-06-24 adoption date." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/eli/reg/2024/1745/oj
- citation[1]: `primary_legal` replayable=`True` https://www.consilium.europa.eu/en/press/press-releases/2024/06/24/russia-s-war-of-aggression-against-ukraine-comprehensive-eu-s-14th-package-of-sanctions-cracks-down-on-circumvention-and-adopts-energy-measures/
- citation[2]: `supporting_journalism` replayable=`True` https://enlargement.ec.europa.eu/news/eu-adopts-14th-package-sanctions-against-russia-its-continued-illegal-war-against-ukraine-2024-06-24_en

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
  "queue_id": 70,
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
  "queue_id": 70,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-14th-russia-sanctions-spfs-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
