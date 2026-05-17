# v0.3 Review Packet: `eba-virtual-currencies-opinion-eba-op-2014-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `64` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `eba-virtual-currencies-opinion-eba-op-2014-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `EU_EBA` |
| event_date | `2014-07-04` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eba-virtual-currencies-opinion-eba-op-2014-08.yaml` |
| target_kind | `entity` |
| target_actor | `EU credit/payment/e-money institutions handling virtual currencies` |

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

"EBA Opinion EBA/Op/2014/08 of 4 July 2014 ('Opinion on virtual currencies') is the first major EU-level supervisory instrument on virtual currencies; it advises national supervisory authorities to discourage EU credit institutions, payment institutions, and e-money institutions from buying, holding, or selling virtual currencies pending a longer-term regulatory regime. The load-bearing axis is offramp_cex at the dispersed-cascade institutional-aggregate layer; downstream banking-rail / payment- rail severance against EU crypto businesses across 2014-2018 is consistent with the cascade hypothesis but not enumerated in this draft." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.eba.europa.eu/sites/default/files/documents/10180/657547/81409b94-4222-45d7-ba3b-7deb5863ab57/EBA-Op-2014-08%20Opinion%20on%20Virtual%20Currencies.pdf
- citation[1]: `primary_legal` replayable=`True` https://eba.europa.eu/eba-proposes-potential-regulatory-regime-for-virtual-currencies-but-also-advises-that-financial-institutions-should-not-buy-hold-or-sell-them-whilst-n

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
  "queue_id": 64,
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
  "queue_id": 64,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eba-virtual-currencies-opinion-eba-op-2014-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
