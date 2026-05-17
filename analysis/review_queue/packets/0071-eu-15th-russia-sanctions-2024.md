# v0.3 Review Packet: `eu-15th-russia-sanctions-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `71` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `eu-15th-russia-sanctions-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `non_us_sanctions` |
| actor | `EU_Council` |
| event_date | `2024-12-16` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-15th-russia-sanctions-2024.yaml` |
| target_kind | `entity` |
| target_actor | `15th-package designees (persons / entities / vessels / companies)` |

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

"EU Council Regulation 2024/3192 (15th Russia-sanctions package), adopted 2024-12-16, is a mostly-technical entity-listing / shadow-fleet package: 84 new individual / entity designations, 52 new third-country vessel listings, and 32 new military-industrial support company listings. It introduces NO new horizontal CASP-level or on-chain provisions beyond the 12th-package Article 5aa user-class prohibition and the 14th-package SPFS / crypto-services tightenings. null_event in this corpus: the crypto-relevant footprint is the absorption of 84 designees into standing CASP screening, which is not separately replayable as observed_change at this snapshot." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202403192
- citation[1]: `primary_legal` replayable=`True` https://www.consilium.europa.eu/en/press/press-releases/2024/12/16/russia-s-war-of-aggression-against-ukraine-eu-adopts-15th-package-of-restrictive-measures/

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
  "queue_id": 71,
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
  "queue_id": 71,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-15th-russia-sanctions-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
