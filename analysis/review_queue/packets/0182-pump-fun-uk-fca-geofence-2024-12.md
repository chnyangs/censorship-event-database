# v0.3 Review Packet: `pump-fun-uk-fca-geofence-2024-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `182` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `pump-fun-uk-fca-geofence-2024-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `PUMP_FUN_OPERATORS` |
| event_date | `2024-12-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/pump-fun-uk-fca-geofence-2024-12.yaml` |
| target_kind | `entity` |
| target_actor | `Pump.fun (frontend operators)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 5 |
| replayable trigger anchors | 5 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2024-12-06 the Pump.fun frontend operators added a UK- vantage IP-detection geofence pop-up and a UK exclusion clause in the site terms of service, three calendar days after the UK FCA's 2024-12-03 unauthorised-firm warning naming Pump.fun; the underlying Pump.fun bonding-curve / memecoin launch program on Solana remained unaffected. Load-bearing axis is l4_frontend on a UK-vantage subset; attribution=direct under §1.4 (operator publicly cited FCA warning; block within ≤7-day compliance window)." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://pump.fun/
- citation[1]: `primary_legal` replayable=`True` https://www.fca.org.uk/news/warnings/pumpfun
- citation[2]: `supporting_journalism` replayable=`True` https://www.theblock.co/post/329804/uk-top-financial-regulator-says-pump-fun-doesnt-have-its-permission-to-do-business-in-the-country
- citation[3]: `supporting_journalism` replayable=`True` https://cryptoslate.com/pump-fun-updates-terms-to-block-uk-users-days-after-fca-warning/
- citation[4]: `supporting_journalism` replayable=`True` https://www.cryptotimes.io/2024/12/06/pump-fun-bans-uk-traders-in-response-to-fca-warning/

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
  "queue_id": 182,
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
  "queue_id": 182,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/pump-fun-uk-fca-geofence-2024-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
