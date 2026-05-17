# v0.3 Review Packet: `tether-doj-pig-butchering-freeze-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `222` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `tether-doj-pig-butchering-freeze-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_authored` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `tether_usdt_issuer` |
| event_date | `2023-11-20` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tether-doj-pig-butchering-freeze-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Pig-butchering / romance-scam network` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Tether's 2023-11-20 freeze of $225M USDT linked to a Southeast Asia pig-butchering syndicate — executed at DOJ/USSS request without any corresponding OFAC SDN listing — documents the DOJ-request-driven mode of stablecoin-issuer freeze action. Completes the 3-mode Tether compliance spectrum (OFAC-reactive / OFAC-preemptive / DOJ-request-only) at S5." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://tether.to/en/tether-freezes-225-million-linked-to-international-human-trafficking-syndicate/
- citation[1]: `primary_legal` replayable=`True` https://www.justice.gov/usao-edva/pr/united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto

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
  "queue_id": 222,
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
  "queue_id": 222,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tether-doj-pig-butchering-freeze-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
