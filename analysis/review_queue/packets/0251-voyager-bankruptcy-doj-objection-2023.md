# v0.3 Review Packet: `voyager-bankruptcy-doj-objection-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `251` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `voyager-bankruptcy-doj-objection-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `court_civil_order` |
| actor | `US_TRUSTEE_SDNY` |
| event_date | `2023-03-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/voyager-bankruptcy-doj-objection-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Voyager Digital + Binance.US (BAM Trading)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 1 |
| replayable observation sources | 4 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2023-03-08 DOJ (U.S. Trustee) objection and appeal of Voyager Digital's Chapter 11 plan-confirmation order, citing AML / sanctions-enforcement grounds against the plan's third-party releases and the Binance.US acquisition route, codifies a single-layer offramp_cex observation: it blocked the planned Binance.US acquisition (formally abandoned 2023-04-25) and forced Voyager into self-liquidation distributions. M&A-cancellation variant of the lender-bankruptcy twin; distinct from the criminal Voyager / Alameda executive investigations." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2023/03/10/us-doj-appeals-new-york-judges-decision-to-approve-voyagers-sale-to-binanceus
- citation[1]: `primary_legal` replayable=`True` https://cases.stretto.com/Voyager/court-docket
- citation[2]: `supporting_journalism` replayable=`True` https://cointelegraph.com/news/us-officials-appeal-protections-for-voyager-execs-in-binance-us-sale

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
  "queue_id": 251,
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
  "queue_id": 251,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/voyager-bankruptcy-doj-objection-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
