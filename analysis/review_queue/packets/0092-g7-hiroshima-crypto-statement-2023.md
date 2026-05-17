# v0.3 Review Packet: `g7-hiroshima-crypto-statement-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `92` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `g7-hiroshima-crypto-statement-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `G7` |
| event_date | `2023-05-20` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/g7-hiroshima-crypto-statement-2023.yaml` |
| target_kind | `entity` |
| target_actor | `G7-jurisdiction crypto-asset ecosystem` |

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

"The G7 Hiroshima Leaders' Communiqué, issued at the Hiroshima Summit on 2023-05-20, is a class-level G7 coordination instrument endorsing accelerated global implementation of FATF Standards on virtual assets (including the Travel Rule) and the OECD Crypto- Asset Reporting Framework (CARF) for tax transparency. Coded as null_event / null_case at the corpus's resolution: no per-event observed_change cascade is directly attributable to the 2023-05-20 communiqué date; downstream FATF, OECD CARF, and G20 endorsement cascades are tracked as separate child events." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.mofa.go.jp/policy/economy/summit/hiroshima23/documents/pdf/Leaders_Communique_01_en.pdf
- citation[1]: `primary_legal` replayable=`True` https://www.consilium.europa.eu/media/64497/g7-2023-hiroshima-leaders-communique.pdf

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
  "queue_id": 92,
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
  "queue_id": 92,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/g7-hiroshima-crypto-statement-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
