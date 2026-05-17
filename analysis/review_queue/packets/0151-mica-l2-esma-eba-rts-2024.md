# v0.3 Review Packet: `mica-l2-esma-eba-rts-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `151` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `mica-l2-esma-eba-rts-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `EU_ESMA_EBA` |
| event_date | `2024-03-25` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mica-l2-esma-eba-rts-2024.yaml` |
| target_kind | `entity` |
| target_actor | `EU CASP + ART/EMT issuer ecosystem (MiCA Level-2 RTS-regulated)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 3 |
| replayable observation sources | 4 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"ESMA + EBA finalized the MiCA Level-2 Regulatory Technical Standards through 2024 (canonical L2 milestone 2024-03-25 with ESMA's CP3 final consultation, EBA parallel reserve-composition RTS, and the 2024-12-17 STOR Final Report). Recorded as a null event because the Level-2 RTS impose forward-looking authorization, reserve-management, and market-abuse-detection obligations rather than producing retroactive per-address or per-CASP observable cross-layer behavior at trigger date; downstream CASP-level follow-on actions are tracked as separate events." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica

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
  "queue_id": 151,
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
  "queue_id": 151,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mica-l2-esma-eba-rts-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
