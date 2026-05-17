# v0.3 Review Packet: `sec-v-ripple-2020`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `205` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `sec-v-ripple-2020` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `sec_action` |
| actor | `US_SEC` |
| event_date | `2020-12-22` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-v-ripple-2020.yaml` |
| target_kind | `entity` |
| target_actor | `Ripple Labs Inc / Garlinghouse / Larsen` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 5 |
| observation sources | 6 |
| primary observation sources | 6 |
| replayable observation sources | 6 |
| primary replayable observation sources | 6 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2020-12-22 SEC v. Ripple Labs Inc. civil securities-law complaint produced a two-layer cascade in the dataset: an L4 frontend corporate response on ripple.com, and an offramp_cex cascade in which four major US-facing centralized exchanges (Coinbase, Bitstamp, Binance.US, Kraken) suspended or delisted XRP for US users within ~4 weeks, with each exchange's official announcement explicitly citing the SEC complaint as the legal basis. The row asserts only these two observational axes and does not claim L0 network, L1 consensus, L3 RPC, or asset_onchain effects; downstream procedural milestones (2023 partial summary judgment, 2024 settlement, post-2023 relistings) are separate events outside the scope of this admission." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sec.gov/news/press-release/2020-338

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
  "queue_id": 205,
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
  "queue_id": 205,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-v-ripple-2020.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
