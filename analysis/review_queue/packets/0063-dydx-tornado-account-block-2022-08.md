# v0.3 Review Packet: `dydx-tornado-account-block-2022-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `63` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `dydx-tornado-account-block-2022-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `dydx_trading_inc` |
| event_date | `2022-08-11` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/dydx-tornado-account-block-2022-08.yaml` |
| target_kind | `entity` |
| target_actor | `dYdX Trading Inc.` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 6 |
| primary observation sources | 2 |
| replayable observation sources | 6 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"dYdX's 2022-08-11 block of accounts whose wallets had any historical interaction with the OFAC-designated Tornado Cash contracts — implemented via a third-party compliance vendor flag at the dYdX-operated trading UI, with funds remaining withdrawable from flagged accounts — documents an L4-frontend + offramp_cex dual-layer corporate-compliance action and the first major operator-acknowledged history-based 'guilt by association' block downstream of the 2022-08-08 OFAC trigger (related event tornado-cash-ofac-2022). Paper-relevant as the hybrid-CEX vertex of the S5_corporate cascade (alongside aave-tornado-frontend-block-2022-08 at L4 and uniswap-balancer-tornado-frontend-block-2022-08 at L4)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://dydx.exchange/blog/tornado-cash-update
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash
- citation[2]: `supporting_journalism` replayable=`True` https://www.theblock.co/post/162928/dydx-confirms-blocking-user-accounts-tied-to-tornado-cash
- citation[3]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/dydx-confirms-blocking-and-unblocking-some-accounts-linked-to-tornado-cash

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
  "queue_id": 63,
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
  "queue_id": 63,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/dydx-tornado-account-block-2022-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
