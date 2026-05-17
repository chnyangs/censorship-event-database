# v0.3 Review Packet: `fincen-virtual-currency-msb-guidance-2013`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `86` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `fincen-virtual-currency-msb-guidance-2013` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `fincen_action` |
| actor | `US_FINCEN` |
| event_date | `2013-03-18` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fincen-virtual-currency-msb-guidance-2013.yaml` |
| target_kind | `entity` |
| target_actor | `Virtual currency administrators and exchangers (US BSA money transmitters)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 1 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

FinCEN FIN-2013-G001 (2013-03-18) interpreted the Bank Secrecy Act's money-transmitter regulations to apply to virtual-currency exchangers and administrators, establishing the foundational regulatory predicate for the 2013-2016 US MSB-registration enforcement era. observation_kind=coverage_gap with attribution= none because the substantive cascade is dispersed across downstream enforcement actions (Shrem/Faiella 2014, Powell 2014, Ripple/XRP II 2015, Murgio/Coin.mx 2015) that each cite this guidance as predicate, rather than localized to a single observable point-in-time CEX cessation. Historical-baseline tier; not used in main statistical denominators. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering

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
  "queue_id": 86,
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
  "queue_id": 86,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fincen-virtual-currency-msb-guidance-2013.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
