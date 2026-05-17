# v0.3 Review Packet: `uk-fca-binance-markets-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `241` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `uk-fca-binance-markets-2021` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `UK_FCA` |
| event_date | `2021-06-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uk-fca-binance-markets-2021.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Markets Limited (UK)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 2 |
| replayable observation sources | 4 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"FCA consumer warning of 2021-06-26 that Binance Markets Limited is not permitted to undertake regulated activity in the UK precipitated a class-wide GBP payment-rail severance from major UK retail banks (Barclays 2021-07-05, Santander 2021-07-13, others) to Binance over the following 8 weeks. Primary observational axis is offramp_cex at the UK-Binance cohort level; secondary L4-frontend response (UK-geo restriction banners on binance.com/en) attached with plausible attribution." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fca.org.uk/news/news-stories/binance-markets-limited

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
  "queue_id": 241,
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
  "queue_id": 241,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uk-fca-binance-markets-2021.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
