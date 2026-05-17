# v0.3 Review Packet: `hongkong-sfc-vatp-licensing-2023-06`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `102` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `hongkong-sfc-vatp-licensing-2023-06` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `HK_SFC` |
| event_date | `2023-06-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/hongkong-sfc-vatp-licensing-2023-06.yaml` |
| target_kind | `entity` |
| target_actor | `Hong Kong SFC VATP licensing regime` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 1 |
| replayable observation sources | 4 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

_No scoped claim in YAML payload._

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sfc.hk/-/media/EN/files/ER/PDF/23CP2_Consultation-Conclusions-on-VATP_eng.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://www.davispolk.com/insights/client-update/hong-kong-licensing-regime-virtual-asset-trading-platforms-comes-force

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
  "queue_id": 102,
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
  "queue_id": 102,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/hongkong-sfc-vatp-licensing-2023-06.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
