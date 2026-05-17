# v0.3 Review Packet: `paxos-busd-nydfs-minting-stop-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `175` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `paxos-busd-nydfs-minting-stop-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `paxos_trust` |
| event_date | `2023-02-13` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/paxos-busd-nydfs-minting-stop-2023.yaml` |
| target_kind | `asset` |
| target_actor | `Paxos Trust Company (BUSD issuer)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2023-02-13 NYDFS-directed Paxos cessation of BUSD minting realizes as an on-chain ERC-20 SupplyController shutdown on the BUSD contract (0x4Fabb145d64652a948d72533023f6E7A623C7C53): the `increaseSupply` mint function ceases to be invoked after the 2023-02-21 cutoff, and total BUSD supply decreases monotonically thereafter via redemption- driven `decreaseSupply` burns. Coded as an S5 stablecoin-issuer supply-function shutdown with NYDFS as the proximate regulator, distinct from the OFAC-driven address-set freezes of Circle USDC (2022-08-08) and Tether USDT (2023-12-09)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://paxos.com/2023/02/13/paxos-will-halt-minting-new-busd-tokens/
- citation[1]: `primary_legal` replayable=`True` https://www.dfs.ny.gov/consumers/alerts/Paxos_and_Binance

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
  "queue_id": 175,
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
  "queue_id": 175,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/paxos-busd-nydfs-minting-stop-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
