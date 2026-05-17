# v0.3 Review Packet: `unsc-resolution-2371-dprk-crypto-2017`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `249` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `unsc-resolution-2371-dprk-crypto-2017` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `non_us_sanctions` |
| actor | `UN_SECURITY_COUNCIL` |
| event_date | `2017-08-05` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/unsc-resolution-2371-dprk-crypto-2017.yaml` |
| target_kind | `entity` |
| target_actor | `Democratic People's Republic of Korea (DPRK)` |

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

"UN Security Council Resolution 2371, adopted unanimously on 2017-08-05, is the foundational 2017 DPRK-sanctions instrument whose expanded financial-institution reach (Foreign Trade Bank asset freeze; financial-services-as-financial-institution clarification) supplies the legal scaffolding subsequently used by the 1718 Sanctions Committee and US OFAC to frame DPRK crypto-laundering as sanctions evasion. Coded as null_event / null_case at the corpus's resolution: 2371 does not itself enumerate cryptocurrency addresses or virtual-asset service providers, and no per-event observed_change cascade is directly attributable to the 2017-08-05 adoption date; downstream Lazarus / DPRK-USDT enforcement actions are tracked as separate child events." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://main.un.org/securitycouncil/en/s/res/2371-(2017)
- citation[1]: `primary_legal` replayable=`True` https://www.un.org/press/en/2017/sc12945.doc.htm
- citation[2]: `supporting_tracker` replayable=`True` https://www.armscontrol.org/factsheets/un-security-council-resolutions-north-korea

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
  "queue_id": 249,
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
  "queue_id": 249,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/unsc-resolution-2371-dprk-crypto-2017.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
