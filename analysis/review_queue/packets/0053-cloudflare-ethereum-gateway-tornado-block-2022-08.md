# v0.3 Review Packet: `cloudflare-ethereum-gateway-tornado-block-2022-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `53` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `cloudflare-ethereum-gateway-tornado-block-2022-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `cloudflare` |
| event_date | `2022-08-12` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/cloudflare-ethereum-gateway-tornado-block-2022-08.yaml` |
| target_kind | `entity` |
| target_actor | `Cloudflare, Inc.` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 2 |
| replayable observation sources | 4 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The August 2022 Cloudflare Ethereum Gateway (cloudflare-eth.com) access restriction against the 2022-08-08 OFAC Tornado Cash SDN address set constitutes the CDN-gateway subtype of L3 censorship in the corpus — structurally distinct from the managed-RPC subtype (Infura, Alchemy, sibling event infura-alchemy-tornado-rpc-block-2022). The row does not claim ISP-level connectivity blocking, consensus-layer (PBS) effect, on-chain asset freeze, or off-ramp severance — those are sibling rows under tornado-cash-ofac-2022 / circle-usdc-tornado-2022." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://blog.cloudflare.com/cloudflare-ethereum-gateway/
- citation[1]: `primary_corporate` replayable=`True` https://www.cloudflare.com/transparency/
- citation[2]: `supporting_journalism` replayable=`True` https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored
- citation[3]: `supporting_journalism` replayable=`True` https://torrentfreak.com/cloudflare-blocks-abusive-content-on-its-ethereum-gateway-231121/

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
  "queue_id": 53,
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
  "queue_id": 53,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/cloudflare-ethereum-gateway-tornado-block-2022-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
