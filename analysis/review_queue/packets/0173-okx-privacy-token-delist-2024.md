# v0.3 Review Packet: `okx-privacy-token-delist-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `173` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `okx-privacy-token-delist-2024` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `okx_exchange` |
| event_date | `2023-12-29` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/okx-privacy-token-delist-2024.yaml` |
| target_kind | `asset` |
| target_actor | `OKX (centralized-exchange operator)` |

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

"OKX's 2023-12-29 spot-trading-pair removals at www.okx.com — covering privacy-asset pairs (Monero/XMR, Zcash/ZEC, Dash/DASH, Horizen/ZEN) and bundled non-privacy pairs in the same delisting operation — narrow the centralized-exchange off-ramp surface for the affected privacy assets in the OKX corridor. The offramp_cex layer carries the load-bearing direct-attribution observation; L0 / L1 / L3 / l4_frontend / asset_onchain are not_applicable for an exchange-listing-only action." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.okx.com/en-us/help/okx-to-delist-several-spot-trading-pairs-12-29

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
  "queue_id": 173,
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
  "queue_id": 173,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/okx-privacy-token-delist-2024.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
