# v0.3 Review Packet: `uniswap-balancer-tornado-frontend-block-2022-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `245` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `uniswap-balancer-tornado-frontend-block-2022-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `uniswap_labs_and_balancer_labs` |
| event_date | `2022-08-12` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-balancer-tornado-frontend-block-2022-08.yaml` |
| target_kind | `entity` |
| target_actor | `Uniswap Labs (app.uniswap.org) and Balancer Labs (balancer.fi)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 5 |
| primary observation sources | 1 |
| replayable observation sources | 5 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2022-08-12 Uniswap Labs and Balancer Labs frontend- screening blocks of TRM-Labs-flagged wallets (seeded by the 2022-08-08 OFAC Tornado Cash SDN address set) constitute a paired L4 frontend-operator corporate-policy-change event, with two named operators (Uniswap Labs, Balancer Labs) applying the block to their hosted UIs (app.uniswap.org, balancer.fi) while the underlying smart-contract protocols remain fully functional. The row does not claim OFAC- compelled action, ISP-level connectivity blocking, consensus-layer effect, or asset-layer freeze — those are sibling-event rows under tornado-cash-ofac-2022 / infura- alchemy-tornado-rpc-block-2022 / circle-usdc-tornado-2022." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.theblock.co/post/162680
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/tech/2022/08/22/popular-uniswap-frontend-blocks-over-250-crypto-addresses-related-to-defi-crimes
- citation[2]: `supporting_journalism` replayable=`True` https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack
- citation[3]: `supporting_journalism` replayable=`True` https://thedefiant.io/news/defi/defi-bans-tornado-addresses

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
  "queue_id": 245,
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
  "queue_id": 245,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uniswap-balancer-tornado-frontend-block-2022-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
