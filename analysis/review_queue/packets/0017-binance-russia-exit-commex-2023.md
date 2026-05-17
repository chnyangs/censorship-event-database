# v0.3 Review Packet: `binance-russia-exit-commex-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `17` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `binance-russia-exit-commex-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `binance_holdings_limited` |
| event_date | `2023-09-27` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-russia-exit-commex-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Binance Holdings Limited (Russia market) / CommEX` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2023-09-27 Binance Holdings Limited divestiture of its Russia-market business to the newly-created CommEX exchange, executed under US Treasury OFAC pressure and contemporaneous EU sanctions-enforcement concerns about ruble-denominated crypto trading, produced a two-layer cascade in the dataset: an L4 frontend transition notice on binance.com (Russian-locale) plus a destination landing on commex.com, and an offramp_cex restructuring in which Binance RUB on/off-ramp rails were wound down and the Russian user book was administratively migrated to CommEX over an announced one-year window. The row asserts only these two observational axes and does not claim L0 network, L1 consensus, L3 RPC, or asset_onchain effects; the downstream 2024-09 CommEX shutdown is a separate event row outside the scope of this admission." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.binance.com/en/blog/ecosystem/binance-fully-exits-russia-with-sale-to-commex-3550293696068383963
- citation[1]: `primary_corporate` replayable=`True` https://www.prnewswire.com/news-releases/binance-fully-exits-russia-with-sale-to-commex-301940042.html
- citation[2]: `primary_corporate` replayable=`True` https://commex.com/en/blog/post-detail/commex-announcement

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
  "queue_id": 17,
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
  "queue_id": 17,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-russia-exit-commex-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
