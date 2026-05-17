# v0.3 Review Packet: `iran-government-mining-electricity-restriction-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `114` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `iran-government-mining-electricity-restriction-2021` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `IR_TAVANIR` |
| event_date | `2021-05-22` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/iran-government-mining-electricity-restriction-2021.yaml` |
| target_kind | `entity` |
| target_actor | `Iranian Tavanir-licensed bitcoin mining farms (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

_No scoped claim in YAML payload._

## Trigger Citations

- citation[0]: `primary_government` replayable=`True` https://www.mehrnews.com/news/5217539/%D9%85%D8%B1%D8%A7%DA%A9%D8%B2-%D9%85%D8%AC%D8%A7%D8%B2-%D8%A7%D8%B3%D8%AA%D8%AE%D8%B1%D8%A7%D8%AC-%D8%B1%D9%85%D8%B2-%D8%A7%D8%B1%D8%B2-%D8%A7%D8%B2-%D8%A7%D9%85%D8%B1%D9%88%D8%B2-%D8%AE%D8%A7%D9%85%D9%88%D8%B4-%D9%85%DB%8C-%D8%B4%D9%88%D9%86%D8%AF
- citation[1]: `supporting_journalism` replayable=`True` https://www.cnbc.com/2021/05/26/iran-bans-bitcoin-mining-as-its-cities-suffer-blackouts.html
- citation[2]: `supporting_journalism` replayable=`True` https://www.aljazeera.com/economy/2021/5/26/iran-bans-all-crypto-mining-after-summer-power-cuts-strike
- citation[3]: `supporting_journalism` replayable=`True` https://fortune.com/2021/05/27/iran-ban-crypto-mining-bitcoin-blackout-energy-use/

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
  "queue_id": 114,
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
  "queue_id": 114,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/iran-government-mining-electricity-restriction-2021.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
