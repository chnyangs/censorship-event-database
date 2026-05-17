# v0.3 Review Packet: `liberty-reserve-costa-rica-license-denial-2011-03`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `143` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `liberty-reserve-costa-rica-license-denial-2011-03` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `CR_SUGEF` |
| event_date | `2011-03-07` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/liberty-reserve-costa-rica-license-denial-2011-03.yaml` |
| target_kind | `entity` |
| target_actor | `Liberty Reserve S.A. (Arthur Budovsky)` |

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

"Costa Rica's SUGEF refused on 2011-03-07 to grant Liberty Reserve S.A. authorization to operate as a regulated financial entity for lack of transparency in funding management, creating the unlicensed-operation status in Costa Rica that the May 2013 US DOJ unsealed indictment used as the 18-USC-1960 predicate. The row claims only this single-layer offramp regulatory observation with attribution=direct; no L0/L1/L3/L4/asset-onchain effects are coded. Discovery-tier only: no comparable-analysis use." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/Liberty%20Reserve%2C%20et%20al.%20Redacted%20AUSA%20Appln%20with%20exhibits.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://ticotimes.net/2013/05/27/liberty-reserve-a-cyberweb-of-intrigue
- citation[2]: `supporting_journalism` replayable=`True` https://ticotimes.net/2013/05/24/millions-of-dollars-in-limbo-after-shuttering-of-digital-currency-site-liberty-reserve
- citation[3]: `supporting_journalism` replayable=`True` https://en.wikipedia.org/wiki/Liberty_Reserve

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
  "queue_id": 143,
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
  "queue_id": 143,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/liberty-reserve-costa-rica-license-denial-2011-03.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
