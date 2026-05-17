# v0.3 Review Packet: `philippines-sec-binance-block-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `178` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `philippines-sec-binance-block-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `PH_NTC` |
| event_date | `2024-03-25` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/philippines-sec-binance-block-2024.yaml` |
| target_kind | `domain` |
| target_actor | `Binance (PH-vantage access)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 3 |
| replayable observation sources | 4 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2024-03-25 Philippines NTC blocking order, following the 2023-11 SEC Notice of Warning Against Binance, severed PH-vantage network access to binance.com / binance.org and closed Binance PHP peso on/off-ramps to Philippine users. Observational axes at l0_network (PH-ISP blocking) and offramp_cex (PHP rail closure). L0 admission-anchor-grade promotion pending OONI Probe PH / Censored Planet follow-up batch query." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sec.gov.ph/notice-of-warning/notice-of-warning-against-binance/
- citation[1]: `supporting_journalism` replayable=`True` https://www.gmanetwork.com/news/money/companies/901661/sec-formally-requests-ntc-to-block-binance-in-ph/story/

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
  "queue_id": 178,
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
  "queue_id": 178,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/philippines-sec-binance-block-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
