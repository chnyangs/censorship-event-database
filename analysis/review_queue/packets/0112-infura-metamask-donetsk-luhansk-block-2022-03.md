# v0.3 Review Packet: `infura-metamask-donetsk-luhansk-block-2022-03`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `112` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `infura-metamask-donetsk-luhansk-block-2022-03` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `consensys_infura_metamask` |
| event_date | `2022-03-03` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/infura-metamask-donetsk-luhansk-block-2022-03.yaml` |
| target_kind | `entity` |
| target_actor | `ConsenSys (Infura RPC + MetaMask wallet UI)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 5 |
| primary observation sources | 2 |
| replayable observation sources | 5 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2022-03-03 ConsenSys IP-geographic block at the Infura RPC endpoint layer and at the MetaMask wallet UI layer, applied to end-users in the Donetsk and Luhansk regions of Ukraine (plus the prior comprehensive-sanctions region set) in response to the 2022-02-21 EO 14065, constitutes the first documented S5_corporate IP-geo region-block in the corpus, with both L3 (RPC reachability) and L4 (wallet UI rendering) rows anchored on ConsenSys's own corporate statement (attribution=direct). The row does not claim ISP-level connectivity blocking, consensus-layer (PBS) effect, on-chain asset freeze, or off-ramp severance. The contemporaneous Venezuela/Iran over-block was a transient configuration error corrected within ~24h and is recorded as a recovery row on the L4 layer." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://consensys.net/blog/news/consensys-and-the-russia-ukraine-conflict/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2022/03/03/metamask-infura-block-certain-areas-amid-crypto-sanctions-fury
- citation[2]: `supporting_journalism` replayable=`True` https://www.coindesk.com/business/2022/03/04/crypto-industrys-sanctions-woes-on-full-display-in-metamasks-venezuela-hiccup
- citation[3]: `supporting_journalism` replayable=`True` https://decrypt.co/94315/ethereum-infura-cuts-off-users-separatist-areas-ukraine-accidentally-blocks-venezuela

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
  "queue_id": 112,
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
  "queue_id": 112,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/infura-metamask-donetsk-luhansk-block-2022-03.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
