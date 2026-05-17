# v0.3 Review Packet: `australia-asic-binance-derivatives-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `10` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `australia-asic-binance-derivatives-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `AU_ASIC` |
| event_date | `2023-04-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/australia-asic-binance-derivatives-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Oztures Trading Pty Ltd (Binance Australia Derivatives)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"ASIC media release 23-079MR of 2023-04-06 cancelled the AFSL of Oztures Trading Pty Ltd (trading as Binance Australia Derivatives) after a targeted review found ~500 retail clients had been wrongly classified as wholesale clients, directly compelling the shutdown of Binance's Australian derivatives operations (effective 2023-04-14 with transitional close-out through 2023-04-21). Primary observational axis is offramp_cex at the Binance-Australia-derivatives cohort level; secondary L4-frontend response (AU-geo derivatives- shutdown banners on binance.com) attached with plausible attribution. The row does not claim ISP-level connectivity blocking, on-chain asset freeze, or cancellation of Binance Australia's separate spot- exchange AUSTRAC registration." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-079mr-asic-cancels-binance-australia-afs-licence/

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
  "queue_id": 10,
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
  "queue_id": 10,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/australia-asic-binance-derivatives-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
