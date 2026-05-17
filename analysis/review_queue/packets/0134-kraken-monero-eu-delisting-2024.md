# v0.3 Review Packet: `kraken-monero-eu-delisting-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `134` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `kraken-monero-eu-delisting-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `KRAKEN_PAYWARD` |
| event_date | `2024-10-31` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kraken-monero-eu-delisting-2024.yaml` |
| target_kind | `entity` |
| target_actor | `Kraken (Payward, Inc.) — EEA user cohort` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Kraken (Payward, Inc.)'s 2024-10-31 15:00 UTC termination of Monero (XMR) spot trading and deposits for clients resident in the European Economic Area — closing the XMR/USD, XMR/EUR, XMR/BTC, and XMR/USDT pairs and force-converting remaining XMR balances to BTC by 2025-01-06 — narrows the centralized-exchange off-ramp surface for Monero in the Kraken EEA corridor under MiCA-era compliance pressure. The offramp_cex layer carries the load-bearing direct-attribution observation; L0 / L1 / L3 / l4_frontend / asset_onchain are not_applicable for a geofenced exchange-listing-only action keyed to a single base-chain privacy asset. The row is the largest 2024 EU-jurisdictional privacy-coin delisting anchor in the 2023-2024 CEX privacy-asset delisting wave (alongside binance-privacy-coin-delisting-2023 and okx-privacy-token-delist-2024)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://support.kraken.com/articles/support-for-monero-xmr-in-europe

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
  "queue_id": 134,
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
  "queue_id": 134,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kraken-monero-eu-delisting-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
