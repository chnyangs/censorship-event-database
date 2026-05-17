# v0.3 Review Packet: `ofac-hamas-irgc-virtual-currency-network-2024-01`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `167` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ofac-hamas-irgc-virtual-currency-network-2024-01` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC` |
| event_date | `2024-01-22` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-hamas-irgc-virtual-currency-network-2024-01.yaml` |
| target_kind | `entity` |
| target_actor | `Hamas / IRGC-QF joint virtual-currency procurement network` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2024-01-22 OFAC SDN designation of the joint Hamas / IRGC-QF virtual-currency procurement sub-network attached specific wallet designations with concurrent Tether USDT-TRC20 issuer freezes on the designated addresses (asset-layer cascade), with no public CEX policy-statement cascade documented in the 14-day post-designation window." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://home.treasury.gov/news/press-releases/jy2036
- citation[1]: `supporting_tracker` replayable=`True` https://www.chainalysis.com/blog/ofac-highlights-hundreds-of-millions-of-dollars-in-cryptocurrency-transactions-related-to-irgc-connected-houthi-financier-said-al-jamal/

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
  "queue_id": 167,
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
  "queue_id": 167,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-hamas-irgc-virtual-currency-network-2024-01.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
