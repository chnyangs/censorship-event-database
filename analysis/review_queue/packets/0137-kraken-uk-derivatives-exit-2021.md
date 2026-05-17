# v0.3 Review Packet: `kraken-uk-derivatives-exit-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `137` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `kraken-uk-derivatives-exit-2021` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `KRAKEN_PAYWARD` |
| event_date | `2021-01-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kraken-uk-derivatives-exit-2021.yaml` |
| target_kind | `entity` |
| target_actor | `Kraken Futures / Crypto Facilities Ltd` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Kraken Futures (Crypto Facilities Ltd) restricted UK retail customer access to crypto-derivatives products on or around 2021-01-06 in compliance with the FCA PS20/10 prohibition, retaining access only for customers categorised as Professional Clients under COBS 3. Primary observational axis is offramp_cex at the UK-retail-cohort level; attribution=plausible because the FCA prohibition is class-wide rather than Kraken-specific." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://support.kraken.com/articles/futures-trading-for-clients-in-the-united-kingdom
- citation[1]: `primary_corporate` replayable=`True` https://support.kraken.com/articles/changes-for-clients-residing-in-the-united-kingdom

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
  "queue_id": 137,
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
  "queue_id": 137,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kraken-uk-derivatives-exit-2021.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
