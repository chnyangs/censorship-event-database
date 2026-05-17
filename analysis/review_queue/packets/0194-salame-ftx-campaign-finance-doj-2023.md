# v0.3 Review Packet: `salame-ftx-campaign-finance-doj-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `194` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `salame-ftx-campaign-finance-doj-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_SDNY` |
| event_date | `2023-09-07` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/salame-ftx-campaign-finance-doj-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Ryan Salame` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2023-09-07 DOJ SDNY guilty plea by Ryan Salame (former co-CEO, FTX Digital Markets) to campaign-finance and unlicensed money-transmitting conspiracies — a downstream individual-defendant accountability action in the FTX-collapse enforcement cascade — produces zero observed_change layers in the cross-layer censorship-substrate frame. The row is retained as a null_case denominator control in the S3 us-federal-enforcement cluster; the load-bearing offramp_cex shutdown is coded on the parent ftx-bankman-fried-doj-2022 row at the 2022-11-11 Chapter 11 + 2022-12-13 federal-enforcement trigger, ~9 months prior." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/statement-us-attorney-damian-williams-guilty-plea-ryan-salame-former-ceo-ftx
- citation[1]: `primary_legal` replayable=`True` https://content.govdelivery.com/attachments/USDOJUSAO/2023/09/07/file_attachments/2607934/U.S.%20v.%20Salame%20Information.pdf

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
  "queue_id": 194,
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
  "queue_id": 194,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/salame-ftx-campaign-finance-doj-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
