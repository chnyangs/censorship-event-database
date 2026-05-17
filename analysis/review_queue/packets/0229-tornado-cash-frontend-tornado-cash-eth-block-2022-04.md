# v0.3 Review Packet: `tornado-cash-frontend-tornado-cash-eth-block-2022-04`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `229` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `tornado-cash-frontend-tornado-cash-eth-block-2022-04` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `tornado_cash_team` |
| event_date | `2022-04-15` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-frontend-tornado-cash-eth-block-2022-04.yaml` |
| target_kind | `entity` |
| target_actor | `Tornado Cash team (frontend operator)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The Tornado Cash team's 2022-04-15 integration of the Chainalysis on-chain sanctions-screening oracle contract at the tornado.cash frontend — blocking OFAC SDN addresses from depositing or withdrawing through the team-operated dapp while leaving the Tornado Cash smart contracts on Ethereum permissionless — documents the earliest L4 DeFi-frontend voluntary self-censorship action in the corpus, predating the 2022-08-08 OFAC SDN designation of Tornado Cash (tornado-cash-ofac-2022) by 116 days and seeding the 'frontend / protocol-layer split' archetype later instantiated in the 2022-08 cascade siblings (aave-tornado-frontend-block-2022-08, uniswap-balancer-tornado-frontend-block-2022-08)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://twitter.com/TornadoCash/status/1514904975037210632
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/tech/2022/04/15/tornado-cash-adds-chainalysis-tool-for-blocking-ofac-sanctioned-wallets-from-dapp
- citation[2]: `supporting_journalism` replayable=`True` https://cryptopotato.com/tornado-cash-reveals-using-chainalysis-oracle-contract/
- citation[3]: `supporting_journalism` replayable=`True` https://chainbulletin.com/tornado-cash-to-use-chainalysis-to-block-ofac-sanctioned-addresses

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
  "queue_id": 229,
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
  "queue_id": 229,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-frontend-tornado-cash-eth-block-2022-04.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
