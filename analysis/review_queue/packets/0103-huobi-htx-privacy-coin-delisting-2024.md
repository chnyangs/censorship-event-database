# v0.3 Review Packet: `huobi-htx-privacy-coin-delisting-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `103` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `huobi-htx-privacy-coin-delisting-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `HUOBI_HTX` |
| event_date | `2024-01-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/huobi-htx-privacy-coin-delisting-2024.yaml` |
| target_kind | `entity` |
| target_actor | `HTX (formerly Huobi; HTX Global, post-rebrand 2023-09-13)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"HTX (formerly Huobi; rebranded 2023-09-13)'s 2024 product- catalogue narrowing for privacy-asset spot-trading pairs (XMR / DASH / ZEC named in Kaiko's 2024 record-year delisting tally) narrows the centralized-exchange off-ramp surface for the affected privacy assets in the HTX corridor under continued MiCA-era + EU TFR-recast + Asia-Pacific regulatory compliance pressure. The offramp_cex layer carries the load-bearing direct-attribution observation; L0 / L1 / L3 / l4_frontend / asset_onchain are not_applicable for an exchange-listing-only action keyed to base-chain privacy assets. The row is the HTX-rebrand-era continuation of the legacy Huobi 2022-09 seven-coin privacy-asset delisting program and the fourth anchor of the 2023-2024 CEX privacy-asset delisting wave alongside binance-privacy-coin-delisting-2023, okx-privacy-token-delist-2024, and kraken-monero-eu-delisting-2024." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.htx.com/support/
- citation[1]: `supporting_tracker` replayable=`True` https://cryptoslate.com/privacy-tokens-reach-highest-delisting-rate-in-2024-kaiko/

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
  "queue_id": 103,
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
  "queue_id": 103,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/huobi-htx-privacy-coin-delisting-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
