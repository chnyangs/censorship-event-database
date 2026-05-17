# v0.3 Review Packet: `consensys-metamask-infura-rpc-data-collection-2022-11`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `59` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `consensys-metamask-infura-rpc-data-collection-2022-11` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `CONSENSYS_INC` |
| event_date | `2022-11-23` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/consensys-metamask-infura-rpc-data-collection-2022-11.yaml` |
| target_kind | `entity` |
| target_actor | `MetaMask end-users using Infura as default RPC provider` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2022-11-23 ConsenSys updated the MetaMask privacy policy to publicly disclose that Infura, when used as the MetaMask default RPC provider, collects user IP addresses and Ethereum wallet addresses on every RPC request. This is a disclosure of pre- existing data-collection practice rather than a behavioral cutover at the L3 RPC layer; no new availability filter, address- set screen, or IP-geographic block is introduced. The single recorded observation is an observed_no_change row at L3 with attribution=none. The row does not claim any L0/L1/L4/asset/off- ramp cascade." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://consensys.io/privacy-policy
- citation[1]: `supporting_journalism` replayable=`True` https://www.theblock.co/post/189717/consensys-says-it-collects-ip-addresses-of-metamask-users-via-infura
- citation[2]: `supporting_journalism` replayable=`True` https://decrypt.co/115486/infura-collect-metamask-users-ip-ethereum-addresses-after-privacy-policy-update
- citation[3]: `supporting_journalism` replayable=`True` https://cryptoslate.com/consensys-updates-policy-to-collect-metamask-ip-data/

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
  "queue_id": 59,
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
  "queue_id": 59,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/consensys-metamask-infura-rpc-data-collection-2022-11.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
