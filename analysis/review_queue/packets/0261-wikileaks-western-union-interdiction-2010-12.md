# v0.3 Review Packet: `wikileaks-western-union-interdiction-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `261` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-western-union-interdiction-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `WESTERN_UNION_OPERATOR` |
| event_date | `2010-12-21` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-western-union-interdiction-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `WikiLeaks (donation funnel)` |

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
Machine notes: `none`

## Scoped Claim

Western Union added WikiLeaks to its money-transfer "Interdiction List" on 2010-12-21, blocking WikiLeaks from receiving donations through the Western Union rail as one of five legs of the December-2010 financial blockade. observation_kind=coverage_gap with attribution=unknown because no primary Western Union corporate disclosure was located in this authoring pass; the action is attested only via counterparty statement (WikiLeaks Banking Blockade page) and contemporaneous journalism. Discovery- ledger tier; not used in main statistical denominators. 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://wikileaks.org/Banking-Blockade.html
- citation[1]: `supporting_journalism` replayable=`True` https://www.csmonitor.com/World/Latest-News-Wires/2011/1024/Wikilieaks-says-financial-blockade-could-put-it-out-of-business

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
  "queue_id": 261,
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
  "queue_id": 261,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-western-union-interdiction-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
