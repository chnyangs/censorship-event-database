# v0.3 Review Packet: `cryptex-ofac-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `60` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `cryptex-ofac-2024` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC` |
| event_date | `2024-09-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/cryptex-ofac-2024.yaml` |
| target_kind | `address_set` |
| target_actor | `Cryptex` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 5 |
| observation sources | 9 |
| primary observation sources | 7 |
| replayable observation sources | 6 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC designation of the Cryptex Russian exchange on 2024-09-26 co-occurred (same-day) with a US Secret Service judicial seizure of the canonical cryptex.net domain (L4 observed_change, direct attribution), while producing no measurable step change in Ethereum aggregate OFAC-compliant relay share (L1 null at day granularity)." Other layers remain scoped for follow-up. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20240926
- citation[1]: `primary_legal` replayable=`False` https://home.treasury.gov/news/press-releases/jy2595

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
  "queue_id": 60,
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
  "queue_id": 60,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/cryptex-ofac-2024.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
