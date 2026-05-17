# v0.3 Review Packet: `ftx-bankman-fried-doj-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `89` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ftx-bankman-fried-doj-2022` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_SDNY` |
| event_date | `2022-12-13` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ftx-bankman-fried-doj-2022.yaml` |
| target_kind | `entity` |
| target_actor | `Samuel Bankman-Fried / FTX Trading Ltd. / Alameda Research LLC` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 3 |
| replayable observation sources | 3 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2022-12-13 coordinated US DOJ SDNY + SEC + CFTC enforcement action against Samuel Bankman-Fried, FTX Trading Ltd., and Alameda Research LLC, cascading on top of the 2022-11-11 FTX Chapter 11 bankruptcy filing, produced a one-layer admitted observation in the dataset: an offramp_cex global withdraw-pause and Chapter 11 customer-asset freeze affecting FTX.com international, FTX.US, and Alameda Research assets. Attribution is plausible (not direct) to the 2022-12-13 federal trigger because the off-ramp shutdown was proximately effected by the prior corporate Chapter 11 filing. The row does not claim L0 network, L1 consensus, L3 RPC, asset_onchain, or admission-grade L4 frontend effects; the FTX.com US-user geofencing well predates the trigger and is not coded as an attributable observation." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/united-states-attorney-announces-charges-against-ftx-founder-samuel-bankman-fried
- citation[1]: `primary_legal` replayable=`True` https://www.sec.gov/news/press-release/2022-219
- citation[2]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/8638-22
- citation[3]: `primary_corporate` replayable=`True` https://www.ftx.com/en/press-releases/ftx-trading-ltd-voluntary-chapter-11-cases

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
  "queue_id": 89,
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
  "queue_id": 89,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ftx-bankman-fried-doj-2022.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
