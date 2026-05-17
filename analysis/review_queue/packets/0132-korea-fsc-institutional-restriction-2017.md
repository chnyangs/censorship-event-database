# v0.3 Review Packet: `korea-fsc-institutional-restriction-2017`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `132` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `korea-fsc-institutional-restriction-2017` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `KR_FSC` |
| event_date | `2017-12-13` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/korea-fsc-institutional-restriction-2017.yaml` |
| target_kind | `entity` |
| target_actor | `KR regulated VASP + financial-institution sector (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The KR FSC 2017-12-13 joint government emergency measure mandated real-name verified bank accounts at Korean crypto exchanges, banned anonymous virtual accounts, barred minors and foreign nationals from opening Korean exchange accounts, and prohibited regulated financial institutions from buying, holding, or investing in crypto-assets, with the banking-rail real-name mandate effective 2018-01-30 and the regulated Korean crypto-exchange sector (Upbit, Bithumb, Coinone, Korbit) complying across Q4-2017 / Q1-2018. The offramp_cex layer carries the load-bearing direct-attribution observation; L4 frontend reactions are consistent with the cascade but require a Wayback- capture pass before they may anchor a separate observed_change row. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsc.go.kr/eng/pr010101/22173
- citation[1]: `supporting_journalism` replayable=`True` https://www.welivesecurity.com/2018/01/23/south-korea-moves-ban-anonymous-cryptocurrency-trading/

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
  "queue_id": 132,
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
  "queue_id": 132,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/korea-fsc-institutional-restriction-2017.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
