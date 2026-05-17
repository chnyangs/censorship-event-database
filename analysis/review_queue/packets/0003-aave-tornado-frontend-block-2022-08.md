# v0.3 Review Packet: `aave-tornado-frontend-block-2022-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `3` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `aave-tornado-frontend-block-2022-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `aave_companies_dao` |
| event_date | `2022-08-13` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/aave-tornado-frontend-block-2022-08.yaml` |
| target_kind | `entity` |
| target_actor | `Aave Companies / Aave DAO (frontend operator)` |

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

"Aave's 2022-08-13 integration of a TRM Labs compliance-screening API at the app.aave.com frontend — blocking wallets that interacted with the OFAC-designated Tornado Cash contracts from the Aave-operated UI while leaving the Aave Protocol smart contracts on-chain unaffected — documents an L4-only frontend-operator corporate-compliance action downstream of the 2022-08-08 OFAC trigger (related event tornado-cash-ofac-2022). Paper-relevant as the frontend-operator vertex of the S5_corporate cascade triangle (Circle asset, Infura/Alchemy RPC, Aave frontend) and as the comparison sibling to uniswap-frontend-delisting-2023." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://twitter.com/AaveAave/status/1558414985380536321
- citation[1]: `supporting_journalism` replayable=`True` https://blockworks.co/news/defi-web-apps-block-users-hit-by-tornado-cash-dust-attack
- citation[2]: `supporting_journalism` replayable=`True` https://cryptoslate.com/aave-confirms-trm-labs-api-blocked-dusted-ethereum-wallets-access-restored/
- citation[3]: `supporting_journalism` replayable=`True` https://decrypt.co/107890/meet-the-sleuthing-firm-helping-defi-projects-stay-compliant-with-tornado-cash-sanctions

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
  "queue_id": 3,
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
  "queue_id": 3,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/aave-tornado-frontend-block-2022-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
