# v0.3 Review Packet: `teraexchange-cftc-bitcoin-swap-2015`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `221` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `teraexchange-cftc-bitcoin-swap-2015` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `cftc_action` |
| actor | `US_CFTC` |
| event_date | `2015-09-24` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/teraexchange-cftc-bitcoin-swap-2015.yaml` |
| target_kind | `entity` |
| target_actor | `TeraExchange LLC` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"CFTC In re TeraExchange LLC (Order issued 2015-09-24, Docket 15-33) is the first CFTC enforcement action against a CFTC-registered Swap Execution Facility offering a Bitcoin-referenced derivative product. The captured Order imposed a cease-and-desist plus binding undertakings on the SEF; the retained observation anchors only the regulator-side regime-change action at the offramp_cex layer. No civil monetary penalty was imposed in the 2015-09-24 Order, and no L0/L1/L3/L4-frontend/asset-onchain effects are claimed." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/7240-15
- citation[1]: `primary_legal` replayable=`True` https://www.cftc.gov/idc/groups/public/@lrenforcementactions/documents/legalpleading/enfteraexchangeorder92415.pdf

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
  "queue_id": 221,
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
  "queue_id": 221,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/teraexchange-cftc-bitcoin-swap-2015.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
