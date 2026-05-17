# v0.3 Review Packet: `tornado-cash-github-takedown-2022-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `230` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `tornado-cash-github-takedown-2022-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `github_microsoft` |
| event_date | `2022-08-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-github-takedown-2022-08.yaml` |
| target_kind | `entity` |
| target_actor | `GitHub (Microsoft) — tornadocash organisation and developer accounts` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 5 |
| primary observation sources | 2 |
| replayable observation sources | 5 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Microsoft / GitHub's 2022-08-08 takedown of the tornadocash GitHub organisation (tornado-core, tornado-cli, classic contracts, relayer, ui) and suspension of co-founder Roman Semenov's developer account — effective the same day as the OFAC SDN designation of Tornado Cash (related event tornado-cash-ofac-2022) — documents the source-code-distribution sub-layer of the L4 frontend vertex in the S5_corporate cascade. Paper-relevant as the earliest and most foundational source-code-platform compliance action in the corpus and as the comparison sibling to the application-UI L4 rows (Aave, Uniswap/Balancer, Cloudflare Ethereum Gateway)." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.theregister.com/AMP/2022/08/24/github_eff_tornado_cash
- citation[1]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/github-unbans-tornado-cash-repositories-following-ofac-guidance
- citation[2]: `supporting_journalism` replayable=`True` https://www.eff.org/deeplinks/2023/04/update-tornado-cash
- citation[3]: `supporting_journalism` replayable=`True` https://www.virtualcurrencyreport.com/2022/08/ofac-takes-action-against-virtual-currency-tornado-cashin-novel-application-of-sanctions-authorities/

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
  "queue_id": 230,
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
  "queue_id": 230,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-github-takedown-2022-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
