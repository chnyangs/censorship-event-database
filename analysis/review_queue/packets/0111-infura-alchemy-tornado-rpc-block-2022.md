# v0.3 Review Packet: `infura-alchemy-tornado-rpc-block-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `111` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `infura-alchemy-tornado-rpc-block-2022` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `consensys_infura` |
| event_date | `2022-08-09` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/infura-alchemy-tornado-rpc-block-2022.yaml` |
| target_kind | `address_set` |
| target_actor | `Infura (ConsenSys) and Alchemy Insights` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 3 |
| observation sources | 5 |
| primary observation sources | 3 |
| replayable observation sources | 5 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2022-08-09 Infura and Alchemy RPC-provider blocks of requests touching the 2022-08-08 OFAC Tornado Cash SDN address set constitute the first documented L3 RPC-provider sanctions block in the corpus, with two named providers' own corporate-policy statements (attribution=direct) and a downstream L4 wallet/aggregator UI cascade (attribution=plausible, via Infura's MetaMask-default-RPC position). The row does not claim ISP-level connectivity blocking, consensus-layer (PBS) effect, on-chain asset freeze, or off-ramp severance — those are sibling-event rows under tornado-cash-ofac-2022 / circle-usdc-tornado-2022." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://infura.io/terms
- citation[1]: `primary_corporate` replayable=`True` https://docs.alchemy.com/reference/compliance-program
- citation[2]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets
- citation[3]: `supporting_journalism` replayable=`True` https://www.theblock.co/post/162680

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
  "queue_id": 111,
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
  "queue_id": 111,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/infura-alchemy-tornado-rpc-block-2022.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
