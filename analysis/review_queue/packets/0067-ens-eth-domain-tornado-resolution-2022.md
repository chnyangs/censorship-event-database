# v0.3 Review Packet: `ens-eth-domain-tornado-resolution-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `67` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ens-eth-domain-tornado-resolution-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `ENS_LABS` |
| event_date | `2022-08-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ens-eth-domain-tornado-resolution-2022.yaml` |
| target_kind | `entity` |
| target_actor | `ENS (Ethereum Name Service) — tornadocash.eth name set` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"No ENS-protocol or ENS Labs (app.ens.domains) frontend action to block resolution, transfer, or management of the tornadocash.eth ENS name or its sub-names is documented in the public corpus following the 2022-08-08 OFAC SDN designation of Tornado Cash. The name continued to resolve via the public ENS resolver and via the eth.limo HTTPS gateway through at least end-2022. Recorded as a null_event denominator-control row that delineates the perimeter of the 2022-08-08 cascade at the ENS-name-service vertex." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.trustnodes.com/2022/08/09/torn-token-dives-as-us-bans-a-smart-contract
- citation[1]: `semi_primary_wayback` replayable=`True` https://app.ens.domains/tornadocash.eth

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
  "queue_id": 67,
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
  "queue_id": 67,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ens-eth-domain-tornado-resolution-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
