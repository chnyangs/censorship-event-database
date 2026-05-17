# v0.3 Review Packet: `indonesia-bi-bitcoin-warning-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `110` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `indonesia-bi-bitcoin-warning-2014` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `ID_BI` |
| event_date | `2014-02-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/indonesia-bi-bitcoin-warning-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Indonesia-resident bitcoin/VC users` |

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

Bank Indonesia's 2014-02-06 Siaran Pers No. 16/6/Dkom stated the class-level administrative position that Bitcoin and other virtual currencies are not legal tender in Indonesia under Law No. 7 of 2011 on Currency, are not regulated by Bank Indonesia, and are used at the user's own risk. The advisory did not direct ISP-level blocking, banking-rail prohibition, or exchange-side action; the cascade surface is class-level on Indonesian residents/businesses, and no exchange-side Indonesia-resident cutoff is documented in the public record within the 90-day post-release window, so the event admits as a historical-baseline null_event / null_case with an observed_no_change row at offramp_cex. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_160614.aspx
- citation[1]: `supporting_journalism` replayable=`True` https://en.antaranews.com/news/168747/bitcoin-is-not-lawfully-accepted-payment-instrument-in-indonesia-bi

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
  "queue_id": 110,
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
  "queue_id": 110,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/indonesia-bi-bitcoin-warning-2014.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
