# v0.3 Review Packet: `genesis-sec-gemini-earn-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `94` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `genesis-sec-gemini-earn-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `sec_action` |
| actor | `US_SEC` |
| event_date | `2023-01-12` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/genesis-sec-gemini-earn-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Genesis Global Capital, LLC + Gemini Trust Company, LLC (Gemini Earn)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2023-01-12 SEC Genesis + Gemini complaint over the Gemini Earn program is coded only as a centralized crypto lending-product restriction at the offramp_cex layer, paired with the 2023-01-19 Genesis Chapter 11 estate freeze of approximately $900M of customer crypto held for ~340K Gemini Earn investors; it does not claim a frontend, L1, L3, or on-chain censorship event." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sec.gov/news/press-release/2023-7
- citation[1]: `primary_legal` replayable=`True` https://www.sec.gov/litigation/complaints/2023/comp-pr2023-7.pdf

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
  "queue_id": 94,
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
  "queue_id": 94,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/genesis-sec-gemini-earn-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
