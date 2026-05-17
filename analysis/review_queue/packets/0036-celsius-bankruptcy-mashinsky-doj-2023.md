# v0.3 Review Packet: `celsius-bankruptcy-mashinsky-doj-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `36` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `celsius-bankruptcy-mashinsky-doj-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_SDNY` |
| event_date | `2023-07-13` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/celsius-bankruptcy-mashinsky-doj-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Celsius Network + Alex Mashinsky + Roni Cohen-Pavon` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 5 |
| replayable trigger anchors | 5 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2023-07-13 coordinated DOJ + SEC + CFTC + FTC actions against Celsius Network and Alex Mashinsky codify a single-layer offramp_cex cascade: the centralized lending platform's withdraw-freeze (2022-06-12) and Chapter 11 collapse (2022-07-13) are legally disposed via criminal indictment + securities-fraud + commodity-pool + FTC consumer-protection parallels. Lender variant of the FTX twin; structurally narrower than the FTX exchange-plus-lender cascade." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-executive-officer-celsius-network-limited-charged-multi
- citation[1]: `primary_legal` replayable=`True` https://www.sec.gov/news/press-release/2023-127
- citation[2]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/8758-23
- citation[3]: `primary_legal` replayable=`True` https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-action-leads-record-47-billion-imposed-judgment-against-crypto-platform-celsius
- citation[4]: `primary_legal` replayable=`True` https://cases.stretto.com/celsius/

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
  "queue_id": 36,
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
  "queue_id": 36,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/celsius-bankruptcy-mashinsky-doj-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
