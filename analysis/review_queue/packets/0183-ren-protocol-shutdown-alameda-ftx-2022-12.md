# v0.3 Review Packet: `ren-protocol-shutdown-alameda-ftx-2022-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `183` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ren-protocol-shutdown-alameda-ftx-2022-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `REN_PROTOCOL_TEAM` |
| event_date | `2022-12-20` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ren-protocol-shutdown-alameda-ftx-2022-12.yaml` |
| target_kind | `entity` |
| target_actor | `Ren Protocol Team (Alameda-acquired)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 1 |
| replayable observation sources | 4 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The Ren Protocol team's 2022-12-20 operator-initiated wind-down of the Ren 1.0 cross-chain bridge — burning / redemption-window close-out for renBTC and the broader ren-wrapped asset family on Ethereum, preceded by mint-cessation in the prior weeks — closed the cross-chain redemption surface of the bridge to zero at the asset_onchain layer. The asset_onchain observation carries the load-bearing plausible- attribution observation, causally linked to the upstream 2022-11-11 FTX Trading Ltd. / Alameda Research Chapter 11 collapse (Alameda was the parent / funder of the Ren team after the 2022-02 acquisition); the event is the cleanest S5 corporate-policy follow-on in the corpus to the FTX / Alameda contagion cascade affecting a cross-chain bridge primitive." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.theblock.co/post/193274/alameda-backed-ren-warns-users-of-losses-as-it-plans-to-wind-down-protocol
- citation[1]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/ren-protocol-transfers-all-assets-to-ftx-debtors-wallet-in-case-of-shutdown
- citation[2]: `supporting_journalism` replayable=`True` https://crypto.news/alameda-backed-ren-shuts-down-alerts-users-to-unwrap-tokens/

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
  "queue_id": 183,
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
  "queue_id": 183,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ren-protocol-shutdown-alameda-ftx-2022-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
