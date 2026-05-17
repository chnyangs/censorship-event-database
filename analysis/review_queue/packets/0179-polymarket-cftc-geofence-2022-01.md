# v0.3 Review Packet: `polymarket-cftc-geofence-2022-01`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `179` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `polymarket-cftc-geofence-2022-01` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `cftc_action` |
| actor | `US_CFTC` |
| event_date | `2022-01-03` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/polymarket-cftc-geofence-2022-01.yaml` |
| target_kind | `entity` |
| target_actor | `Polymarket (Blockratize, Inc.)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The 2022-01-03 CFTC settlement against Blockratize Inc. d/b/a Polymarket ($1.4M penalty + cease-and-desist) produced a single-layer L4 cascade -- a US-vantage geofence at polymarket.com -- with the on-chain Polygon protocol contracts remaining functional. Longitudinal validation via the 2026-04 DOJ SDNY indictment of Master Sergeant Gannon Ken Van Dyke (for using classified Maduro-operation intel to win ~$409K on Polymarket) confirms the US-vantage geofence remained in place through 2026 and that VPN-bypass is well-documented. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/8478-22

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
  "queue_id": 179,
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
  "queue_id": 179,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/polymarket-cftc-geofence-2022-01.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
