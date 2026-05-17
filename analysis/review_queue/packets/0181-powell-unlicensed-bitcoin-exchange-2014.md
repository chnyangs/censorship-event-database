# v0.3 Review Packet: `powell-unlicensed-bitcoin-exchange-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `181` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `powell-unlicensed-bitcoin-exchange-2014` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_CDIL` |
| event_date | `2014-12-04` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/powell-unlicensed-bitcoin-exchange-2014.yaml` |
| target_kind | `entity` |
| target_actor | `John D. Powell (Normal, IL — individual MSB / cash-for-bitcoin exchanger)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2014-12-04 USDC CDIL sentencing of John D. Powell (48 months for two counts of 18 U.S.C. § 1960 operating an unlicensed money service business) terminated Powell's individual cash-for-bitcoin MSB off-ramp activity, recorded here as a single observed_change at offramp_cex with attribution=direct. The row claims only this single-layer individual-operator shutdown observation; no L0/L1/L3/L4/asset-onchain effects are coded because Powell operated without a named corporate vehicle, clearnet domain, or platform footprint identifiable from the DOJ trigger artifact." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-cdil/pr/mclean-county-man-serve-four-years-prisonfor-operating-unlicensed-internet-bitcoin

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
  "queue_id": 181,
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
  "queue_id": 181,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/powell-unlicensed-bitcoin-exchange-2014.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
