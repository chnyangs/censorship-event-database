# v0.3 Review Packet: `china-inner-mongolia-mining-ban-2021-05`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `41` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `china-inner-mongolia-mining-ban-2021-05` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `CN_INNER_MONGOLIA_NDRC` |
| event_date | `2021-05-25` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-inner-mongolia-mining-ban-2021-05.yaml` |
| target_kind | `entity` |
| target_actor | `Inner Mongolia Autonomous Region Development and Reform Commission (内蒙古自治区发展和改革委员会)` |

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

"On 2021-05-25, the Inner Mongolia Autonomous Region Development and Reform Commission published a draft enforcement notice ('Eight Measures on Resolutely Investigating, Punishing and Rectifying Virtual Currency Mining Behavior') enumerating four classes of mining-related targets, announcing a public reporting hotline + email channel for citizens, and specifying penalties (power-trading bans, business-license revocations, enterprise shutdowns). The notice operationalizes the 2021-02-25 Inner Mongolia NDRC mandate that all bitcoin mining cease by end of April 2021 and is the first concrete province-level enforcement framework in the 2021 CN mining-ban cascade. Observational axis at l1_consensus (attribution=direct on the policy-instrument anchor; downstream physical-effect observations such as mining-rig confiscations and hashrate migration are documented in contemporaneous reporting but not load-bearing in this scoped claim). Admission-anchor-grade promotion pending pinned archive captures." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://fgw.nmg.gov.cn/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2021/05/25/inner-mongolia-outlines-how-it-may-ban-crypto-mining/
- citation[2]: `supporting_journalism` replayable=`True` https://www.scmp.com/economy/china-economy/article/3134058/chinas-cryptocurrency-crackdown-sees-inner-mongolia-call
- citation[3]: `supporting_journalism` replayable=`True` https://www.cnbc.com/2021/05/26/major-china-bitcoin-mining-hub-lays-out-harsher-crackdown-measures.html

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
  "queue_id": 41,
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
  "queue_id": 41,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-inner-mongolia-mining-ban-2021-05.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
