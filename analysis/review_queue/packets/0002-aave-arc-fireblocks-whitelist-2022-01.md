# v0.3 Review Packet: `aave-arc-fireblocks-whitelist-2022-01`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `2` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `aave-arc-fireblocks-whitelist-2022-01` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `AAVE_DAO_AAVE_COMPANIES` |
| event_date | `2022-01-05` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/aave-arc-fireblocks-whitelist-2022-01.yaml` |
| target_kind | `entity` |
| target_actor | `Aave Arc (Aave V2 institutional permissioned pool)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2022-01-05, Aave Arc — a permissioned-pool fork of the Aave V2 protocol — went live on Ethereum mainnet with Fireblocks as the first active whitelister and 30 KYC-vetted institutional addresses onboarded at launch. Address-binary whitelisting is enforced at the protocol-contract layer via the PermissionManager contract, making this the first major protocol-level (not frontend-level) address-binary whitelisting deployment in major DeFi. Observational axes at asset_onchain (load-bearing, attribution=direct) and l4_frontend (derived from the on-chain permission state, attribution=direct). Admission-anchor-grade promotion pending pinned archive captures." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.fireblocks.com/press/fireblocks-whitelists-30-licensed-financial-institutions-to-participate-in-permissioned-defi-with-the-launch-of-aave-arc
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/business/2022/01/05/fireblocks-whitelists-30-trading-firms-for-aaves-institutional-defi-debut
- citation[2]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/aave-launches-its-permissioned-pool-aave-arc-with-30-institutions-set-to-join

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
  "queue_id": 2,
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
  "queue_id": 2,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/aave-arc-fireblocks-whitelist-2022-01.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
