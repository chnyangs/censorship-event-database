# v0.3 Review Packet: `ebullion-doj-fbi-seizure-2008-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `65` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ebullion-doj-fbi-seizure-2008-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_seizure_order` |
| actor | `US_DOJ_CDCA` |
| event_date | `2008-08-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ebullion-doj-fbi-seizure-2008-08.yaml` |
| target_kind | `entity` |
| target_actor | `e-Bullion / Goldfinger Coin & Bullion / James Fayed` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2008-08 DOJ CDCA / FBI LA federal arrest of James Fayed and asset seizure against Goldfinger Coin & Bullion / e-Bullion under 18 USC s 1960 (unlicensed money transmitting) produced an offramp_cex cascade (e-Bullion's digital-gold-currency service ceased; e-bullion.com pulled 2008-08-05; platform did not resume). The row claims only this single-layer offramp shutdown observation with attribution=direct; no L0/L1/L3/L4/asset-onchain effects are coded. Discovery-tier only: no comparable-analysis use." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-cdca/pr/united-states-returns-98-million-recovered-e-bullion-illegal-money-transmitting
- citation[1]: `primary_legal` replayable=`True` https://www.fbi.gov/contact-us/field-offices/losangeles/news/press-releases/united-states-returns-nearly-12-million-to-victims-of-illegal-money-transmitting-business-called-e-bullion
- citation[2]: `supporting_journalism` replayable=`True` https://en.wikipedia.org/wiki/E-Bullion

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
  "queue_id": 65,
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
  "queue_id": 65,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ebullion-doj-fbi-seizure-2008-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
