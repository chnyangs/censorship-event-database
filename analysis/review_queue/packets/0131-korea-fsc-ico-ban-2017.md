# v0.3 Review Packet: `korea-fsc-ico-ban-2017`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `131` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `korea-fsc-ico-ban-2017` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `KR_FSC` |
| event_date | `2017-09-29` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/korea-fsc-ico-ban-2017.yaml` |
| target_kind | `entity` |
| target_actor | `KR ICO + crypto-margin sector (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The KR FSC 2017-09-29 joint statement imposed a full ban on all forms of ICOs and prohibited margin/lending crypto products at regulated Korean financial institutions, with the regulated Korean crypto-exchange sector (Upbit, Bithumb, Coinone, Korbit) complying across Q4-2017 / Q1-2018. The offramp_cex layer carries the load-bearing direct-attribution observation; L4 frontend reactions are consistent with the cascade but require a Wayback-capture pass before they may anchor a separate observed_change row. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsc.go.kr/eng/new_press

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
  "queue_id": 131,
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
  "queue_id": 131,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/korea-fsc-ico-ban-2017.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
