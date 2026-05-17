# v0.3 Review Packet: `bangladesh-bb-bitcoin-warning-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `11` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `bangladesh-bb-bitcoin-warning-2014` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `BD_BB` |
| event_date | `2014-09-15` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bangladesh-bb-bitcoin-warning-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Bangladesh-resident bitcoin transacting parties` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 0 |
| replayable observation sources | 2 |
| primary replayable observation sources | 0 |

Machine blockers: `none_detected`
Machine notes: `null_event_no_repair_needed`

## Scoped Claim

Bangladesh Bank's 2014-09-15 warning stated that bitcoin transactions could constitute unauthorised acts under the Foreign Exchange Regulation Act 1947 and the AML/CFT statutes (Money Laundering Prevention Act 2012, Anti-Terrorism Act 2009), carrying up to 12 years' imprisonment. The cascade surface is class-level on Bangladeshi residents; no exchange- side Bangladesh-resident cutoff or falsifiable null-observation query is documented in this authoring pass, so offramp_cex carries a draft-only observation_kind=coverage_gap row with attribution=none. 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.coindesk.com/markets/2014/09/16/bangladesh-central-bank-cryptocurrency-use-is-a-punishable-offense
- citation[1]: `supporting_tracker` replayable=`True` https://www.thedailystar.net/law-our-rights/law-analysis/bitcoin-legality-in-bangladesh-bank-1602583
- citation[2]: `supporting_journalism` replayable=`True` https://futrlaw.org/bangladesh-bank-issues-cautionary-notice-bitcoin/

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
  "queue_id": 11,
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
  "queue_id": 11,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bangladesh-bb-bitcoin-warning-2014.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
