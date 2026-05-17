# v0.3 Review Packet: `hongkong-hkma-stablecoins-ordinance-2025`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `99` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `hongkong-hkma-stablecoins-ordinance-2025` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `HK_HKMA` |
| event_date | `2025-08-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/hongkong-hkma-stablecoins-ordinance-2025.yaml` |
| target_kind | `entity` |
| target_actor | `HK-operating + HKD-referenced stablecoin issuer ecosystem (HKMA-licensed)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 3 |
| replayable observation sources | 3 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The Hong Kong Stablecoins Ordinance (Cap. 656) commenced operation on 2025-08-01, establishing the first HKMA-administered licensing regime for fiat-referenced stablecoin (FRS) issuers, including extraterritorial application to any HKD-referenced stablecoin issuer worldwide. Unlicensed issuance carries criminal penalties up to HK$5 million fine and 7 years imprisonment. Observational axes at asset_onchain (issuance- licensing gate) and offramp_cex (downstream HK-stablecoin fiat-rail severance for unlicensed issuers). Admission-anchor promotion pending pinned body_hash anchors for HKMA, HKSAR Government, and HKMA implementation-notice URLs plus published HKMA licensing-register snapshot." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/
- citation[1]: `primary_legal` replayable=`True` https://www.info.gov.hk/gia/general/202506/06/P2025060600275.htm
- citation[2]: `primary_legal` replayable=`True` https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/07/20250729-4/

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
  "queue_id": 99,
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
  "queue_id": 99,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/hongkong-hkma-stablecoins-ordinance-2025.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
