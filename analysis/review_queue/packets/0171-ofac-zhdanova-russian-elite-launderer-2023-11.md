# v0.3 Review Packet: `ofac-zhdanova-russian-elite-launderer-2023-11`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `171` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ofac-zhdanova-russian-elite-launderer-2023-11` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC` |
| event_date | `2023-11-03` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-zhdanova-russian-elite-launderer-2023-11.yaml` |
| target_kind | `entity` |
| target_actor | `Ekaterina Zhdanova` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 5 |
| primary observation sources | 1 |
| replayable observation sources | 5 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC designation of Ekaterina Zhdanova on 2023-11-03 — the first OFAC action targeting a virtual-currency-specialized concierge-laundering operator (rather than an exchange or anonymizer) — produced plausible-attribution cascade at the asset_onchain (chain-analytics tagging) and offramp_cex (KYT flagging at counterparty mainstream CEXes and at Garantex) layers; L0/L1/L3/L4 layers are structurally not_applicable for an individual-level designation with no canonical service frontend." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20231103
- citation[1]: `primary_legal` replayable=`True` https://home.treasury.gov/news/press-releases/jy2735
- citation[2]: `supporting_journalism` replayable=`True` https://www.chainalysis.com/blog/ofac-russia-crypto-money-laundering-sanctions-2023/
- citation[3]: `supporting_journalism` replayable=`True` https://www.elliptic.co/blog/ofac-sanctions-russian-national-for-facilitating-sanctions-evasion

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
  "queue_id": 171,
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
  "queue_id": 171,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-zhdanova-russian-elite-launderer-2023-11.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
