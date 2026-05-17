# v0.3 Review Packet: `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `161` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `court_civil_order` |
| actor | `US_NYDFS` |
| event_date | `2015-08-10` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015.yaml` |
| target_kind | `entity` |
| target_actor | `BitLicense-non-compliant crypto exchanges (cluster)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2015-08-10 BitLicense grace-period expiration triggered a cluster of crypto exchange exits from the New York market: Bitfinex, Kraken, ShapeShift, Poloniex, BitFlyer USA, OkCoin, and GoCoin all withdrew from serving NY-resident users via L4-frontend NY-state geofencing and offramp_cex account closures. Observational axes at l4_frontend and offramp_cex. Historical-baseline tier; not used in main statistical denominators." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.dfs.ny.gov/virtual_currency_businesses

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
  "queue_id": 161,
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
  "queue_id": 161,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/nydfs-bitlicense-bitfinex-kraken-shapeshift-exit-2015.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
