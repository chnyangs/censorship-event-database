# v0.3 Review Packet: `eu-dac8-crypto-asset-reporting-directive-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `75` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `eu-dac8-crypto-asset-reporting-directive-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `EU_Council` |
| event_date | `2023-10-17` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-dac8-crypto-asset-reporting-directive-2023.yaml` |
| target_kind | `entity` |
| target_actor | `EU-operating Reporting Crypto-Asset Service Providers (DAC8-regulated)` |

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

"EU Council Directive (EU) 2023/2226 (DAC8), adopted 2023-10-17, transposes the OECD Crypto-Asset Reporting Framework (CARF, 2022) into EU law, imposing CARF-aligned tax due diligence and transaction-level reporting obligations on EU-operating Reporting Crypto-Asset Service Providers (RCASPs). Member-State transposition due 2025-12-31; application 2026-01-01; first reporting 2027. As of the 2026-05-17 authoring date no observed RCASP-level change has materialized — coded null_event / null_case as the EU-level metadata-layer companion to MiCA (eu-mica-2023) and TFR Recast (eu-tfr-recast-2023), and the EU implementation child of CARF (oecd-carf-2022)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2226
- citation[1]: `primary_legal` replayable=`True` https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en

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
  "queue_id": 75,
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
  "queue_id": 75,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-dac8-crypto-asset-reporting-directive-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
