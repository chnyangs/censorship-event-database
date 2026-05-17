# v0.3 Review Packet: `eu-tfr-recast-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `79` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `eu-tfr-recast-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `EU_Council` |
| event_date | `2023-05-31` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-tfr-recast-2023.yaml` |
| target_kind | `entity` |
| target_actor | `EU-operating Crypto-Asset Service Providers (TFR-Recast-regulated)` |

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

"EU Regulation 2023/1113 (TFR Recast), adopted 2023-05-31 alongside MiCA, establishes a zero-de-minimis Travel Rule for all CASP-to-CASP crypto-asset transfers in the EU-27 — the supranational implementation of FATF Recommendation 15 (2019) and a metadata-layer companion to MiCA's licensing framework. Effective 2024-12-30. Represents a supranational regulatory-framework trigger at the offramp_cex layer distinct from sanction-style enforcement; downstream CASP-specific compliance actions are expected as follow-on events." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113
- citation[1]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113

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
  "queue_id": 79,
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
  "queue_id": 79,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-tfr-recast-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
