# v0.3 Review Packet: `etherscan-tornado-cash-ui-label-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `68` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `etherscan-tornado-cash-ui-label-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `etherscan` |
| event_date | `2022-08-10` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/etherscan-tornado-cash-ui-label-2022.yaml` |
| target_kind | `entity` |
| target_actor | `Etherscan (etherscan.io)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 3 |
| replayable observation sources | 3 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Etherscan's circa-2022-08-10 application of 'OFAC Blocked' / 'OFAC SDN' public nametags on the address-page headers of the OFAC-designated Tornado Cash contracts documents a UI / discovery- layer corporate-compliance action by the dominant Ethereum block- explorer operator downstream of the 2022-08-08 OFAC trigger (related event tornado-cash-ofac-2022). Paper-relevant as a third class of L4 frontend action — discovery-layer annotation rather than access-gating — that propagates the sanctions signal to the on-chain-discovery surface used by most users." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://etherscan.io/address/0x7ff9cfad3877f21d41da833e2f775db0569ee3d9
- citation[1]: `primary_corporate` replayable=`True` https://etherscan.io/address/0xa0e1c89ef1a489c9c7de96311ed5ce5d32c20e4b
- citation[2]: `primary_corporate` replayable=`True` https://info.etherscan.com/public-name-tags-labels/

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
  "queue_id": 68,
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
  "queue_id": 68,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/etherscan-tornado-cash-ui-label-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
