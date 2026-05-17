# v0.3 Review Packet: `polynonce-bittrex-fincen-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `180` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `polynonce-bittrex-fincen-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `fincen_action` |
| actor | `US_FINCEN` |
| event_date | `2022-10-11` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/polynonce-bittrex-fincen-2022.yaml` |
| target_kind | `entity` |
| target_actor | `Bittrex Inc.` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"FinCEN + OFAC parallel action against Bittrex (2022-10-11) is recorded only for the Bittrex US offramp_cex post-settlement sanctioned-jurisdiction deplatforming surface; no replayable Wayback / measurement slice of the bittrex.com geoblock has been pinned at draft stage and no L0/L1/L3/L4/ asset_onchain effect is asserted." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fincen.gov/news/news-releases/fincen-announces-29-million-enforcement-action-against-virtual-asset-service
- citation[1]: `primary_legal` replayable=`True` https://www.fincen.gov/system/files/enforcement_action/2023-04-04/Bittrex_Consent_Order_10.11.2022.pdf
- citation[2]: `supporting_journalism` replayable=`True` https://www.cnbc.com/2022/10/11/crypto-company-fined-29point3-million-for-violating-multiple-us-sanctions-.html

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
  "queue_id": 180,
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
  "queue_id": 180,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/polynonce-bittrex-fincen-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
