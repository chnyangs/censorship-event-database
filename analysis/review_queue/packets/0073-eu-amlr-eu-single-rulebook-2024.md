# v0.3 Review Packet: `eu-amlr-eu-single-rulebook-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `73` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `eu-amlr-eu-single-rulebook-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `EU_Council` |
| event_date | `2024-05-30` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-amlr-eu-single-rulebook-2024.yaml` |
| target_kind | `entity` |
| target_actor | `EU-operating Crypto-Asset Service Providers (AMLR-regulated)` |

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

"EU Regulation 2024/1624 (AMLR — Anti-Money Laundering Regulation / single rulebook), adopted 2024-05-30 alongside AMLA Regulation 2024/1620, replaces the patchwork of national AMLD transpositions with a directly-applicable EU regulation and brings CASPs into the EU AML obliged-entities perimeter at the regulation level. Crypto-specific provisions: EUR 1,000 occasional-/non-customer-transaction CDD threshold (Art. 19) and ban on anonymous CASP-hosted accounts and anonymity- enhancing instruments (Art. 79). General application 2027-07-10. null_event in this corpus: the regulatory trigger is registered but the application date is future-effective, so no downstream CASP behavioral change at the offramp_cex layer is yet observable." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng
- citation[1]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng

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
  "queue_id": 73,
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
  "queue_id": 73,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-amlr-eu-single-rulebook-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
