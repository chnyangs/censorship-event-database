# v0.3 Review Packet: `augur-v2-us-uk-geofence-2020-07`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `9` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `augur-v2-us-uk-geofence-2020-07` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `FORECAST_FOUNDATION` |
| event_date | `2020-07-28` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/augur-v2-us-uk-geofence-2020-07.yaml` |
| target_kind | `entity` |
| target_actor | `Forecast Foundation / PM Research Augur v2 client surface` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `null_event_no_repair_needed`

## Scoped Claim

As of this repair pass, primary Augur launch-window artifacts confirm generic jurisdictional-compliance disclaimer language but do not confirm the previously drafted US/UK Augur v2 frontend geofence; the candidate remains a draft coverage_gap pending primary evidence. 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://augur.net/disclaimer/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/tech/2020/07/28/5-years-after-launch-predictions-market-platform-augur-releases-version-2

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
  "queue_id": 9,
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
  "queue_id": 9,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/augur-v2-us-uk-geofence-2020-07.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
