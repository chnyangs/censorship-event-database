# v0.3 Review Packet: `switzerland-finma-tezos-zg-2018`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `220` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `switzerland-finma-tezos-zg-2018` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `CH_FINMA` |
| event_date | `2018-02-16` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/switzerland-finma-tezos-zg-2018.yaml` |
| target_kind | `entity` |
| target_actor | `Swiss-nexus ICO sponsors (2017 cohort; Tezos Foundation, Zug, CH, as load-bearing illustrative target)` |

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

FINMA's 2018-02-16 "Guidelines for enquiries regarding the regulatory framework for initial coin offerings (ICOs)" established the Swiss-jurisdiction tripartite payment / utility / asset token taxonomy that classifies token issuances under Swiss financial market law (GwG / Code of Obligations / FinSA-precursor frame) and that Swiss-nexus 2017-cohort ICO sponsors — most prominently the Tezos Foundation (Zug, CH) — must apply retroactively. The guidelines are framework predicate guidance, not a per-entity enforcement order; observation_kind=observed_no_change with attribution=none at the token-classification axis honestly represents the dispersed framework predicate role. The concurrent Tezos Foundation governance dispute (Gevers vs Breitman) is documented in analysis_notes as contextual background but is not coded as a censorship-layer observation. Comparable-analysis tier; null_case admission candidate pending human audit and archival pinning. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.finma.ch/en/news/2018/02/20180216-mm-ico-wegleitung/
- citation[1]: `supporting_journalism` replayable=`True` https://www.reuters.com/article/us-swiss-finma-ico-idUSKCN1G01YE

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
  "queue_id": 220,
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
  "queue_id": 220,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/switzerland-finma-tezos-zg-2018.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
