# v0.3 Review Packet: `sec-v-coinbase-staking-wells-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `203` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `sec-v-coinbase-staking-wells-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `sec_action` |
| actor | `US_SEC` |
| event_date | `2023-03-22` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-v-coinbase-staking-wells-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Coinbase Inc / Coinbase Global (Coinbase Earn)` |

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

"The 2023-03-22 SEC Wells notice to Coinbase explicitly named the staking service (Coinbase Earn), but Coinbase did not discontinue staking in response; the dataset records this as a null SEC-staking-enforcement comparator to Kraken 2023-02-09 (shutdown) and as a precursor to the June 2023 Coinbase suit." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.sec.gov/Archives/edgar/data/1679788/000167978823000051/coin-20230322.htm
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2023/03/22/sec-warns-coinbase-its-pursuing-enforcement-action-over-securities-violations
- citation[2]: `supporting_journalism` replayable=`True` https://decrypt.co/124262/sec-wells-notice-coinbase-enforcement-over-staking-products

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
  "queue_id": 203,
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
  "queue_id": 203,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-v-coinbase-staking-wells-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
