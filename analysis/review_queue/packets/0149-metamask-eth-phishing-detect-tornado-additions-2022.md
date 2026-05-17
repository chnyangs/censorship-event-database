# v0.3 Review Packet: `metamask-eth-phishing-detect-tornado-additions-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `149` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `metamask-eth-phishing-detect-tornado-additions-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `CONSENSYS_METAMASK` |
| event_date | `2022-08-12` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/metamask-eth-phishing-detect-tornado-additions-2022.yaml` |
| target_kind | `entity` |
| target_actor | `ConsenSys / MetaMask (eth-phishing-detect blocklist maintainer)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"ConsenSys / MetaMask's 2022-08-12 (DRYRUN-estimated) extension of the public eth-phishing-detect blocklist (consumed by the MetaMask wallet UI to surface phishing / risk warnings) with Tornado Cash interaction entries — following the 2022-08-08 OFAC SDN designation of Tornado Cash (related event tornado-cash-ofac-2022) — documents an L4 wallet-UI warning-layer corporate-compliance action distinct from the L3 Infura RPC block (related event infura-alchemy-tornado-rpc-block-2022). Paper-relevant as the wallet-UI warning-layer vertex of the ConsenSys-operated compliance stack (Infura RPC + MetaMask wallet UI) downstream of the 2022-08-08 OFAC trigger." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://github.com/MetaMask/eth-phishing-detect
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/tech/2022/08/17/tornado-cash-fallout-can-ethereum-be-censored
- citation[2]: `supporting_journalism` replayable=`True` https://davidgerard.co.uk/blockchain/2022/08/09/us-sanctions-tornado-cash-and-crypto-shrieks-in-horror/

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
  "queue_id": 149,
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
  "queue_id": 149,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/metamask-eth-phishing-detect-tornado-additions-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
