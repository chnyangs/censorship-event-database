# v0.3 Review Packet: `binance-privacy-coin-delisting-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `16` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `binance-privacy-coin-delisting-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `binance_holdings_limited` |
| event_date | `2023-06-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-privacy-coin-delisting-2023.yaml` |
| target_kind | `asset` |
| target_actor | `Binance Holdings Limited (EU-member-state user cohort)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Binance Holdings Limited's 2023-06-26 spot-trading-pair removals on binance.com for users resident in France, Italy, Poland, and Spain — covering the privacy-asset cohort (Monero/XMR, Zcash/ZEC, Dash/DASH, MobileCoin/MOB, Beam/BEAM, Horizen/ZEN, NAV Coin/NAV, Firo/FIRO) — narrow the centralized-exchange off-ramp surface for the affected privacy assets in the Binance EU-member-state corridor. The offramp_cex layer carries the load-bearing direct-attribution observation; L0 / L1 / L3 / l4_frontend / asset_onchain are not_applicable for a geofenced exchange- listing-only action. The row is the cohort-leader anchor for the 2023-2024 privacy-coin-delisting wave on centralized exchanges (followed by okx-privacy-token-delist-2024 and the Kraken-EU 2024 follow-on, coded separately)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.binance.com/en/support

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
  "queue_id": 16,
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
  "queue_id": 16,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/binance-privacy-coin-delisting-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
