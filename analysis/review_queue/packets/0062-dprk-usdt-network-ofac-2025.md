# v0.3 Review Packet: `dprk-usdt-network-ofac-2025`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `62` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `dprk-usdt-network-ofac-2025` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC` |
| event_date | `2025-11-04` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/dprk-usdt-network-ofac-2025.yaml` |
| target_kind | `address_set` |
| target_actor | `DPRK Laundering Network` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 6 |
| primary observation sources | 6 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC's 2025-11-04 DPRK laundering-network designation attached 53 USDT-TRC20 addresses to SDN, giving the first single-token / single-chain target shape in the dataset. Asset- layer cascade observation (Tether freeze response) is the natural experiment this event sets up; empirical query pending." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20251104
- citation[1]: `primary_legal` replayable=`False` https://home.treasury.gov/news/press-releases/sb0298

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
  "queue_id": 62,
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
  "queue_id": 62,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/dprk-usdt-network-ofac-2025.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
