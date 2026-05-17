# v0.3 Review Packet: `singapore-mas-retail-crypto-restriction-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `216` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `singapore-mas-retail-crypto-restriction-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `SG_MAS` |
| event_date | `2022-01-17` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/singapore-mas-retail-crypto-restriction-2022.yaml` |
| target_kind | `entity` |
| target_actor | `SG DPT service providers (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"MAS issued guidelines on 2022-01-17 prohibiting Digital Payment Token (DPT) service providers from marketing DPT services to the Singapore general public (public-area advertising, social media, broadcast / print media, third-party influencers, physical DPT ATMs), and followed with a 2022-07-06 consultation paper proposing retail-investor suitability assessment, leverage / credit restrictions, and enhanced KYC + risk-disclosure obligations. Load-bearing observational axes are L4 frontend (cohort-wide DPT public-marketing takedown, direct attribution) and offramp_cex (SG retail DPT onboarding friction, plausible attribution)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.mas.gov.sg/news/media-releases/2022/mas-issues-guidelines-to-discourage-cryptocurrency-trading-by-general-public

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
  "queue_id": 216,
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
  "queue_id": 216,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/singapore-mas-retail-crypto-restriction-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
