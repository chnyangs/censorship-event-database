# v0.3 Review Packet: `ripple-fincen-xrp-2015`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `184` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ripple-fincen-xrp-2015` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `fincen_action` |
| actor | `US_FINCEN` |
| event_date | `2015-05-05` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ripple-fincen-xrp-2015.yaml` |
| target_kind | `entity` |
| target_actor | `Ripple Labs Inc. + XRP II, LLC` |

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

FinCEN's 2015-05-05 settlement with Ripple Labs Inc. and XRP II, LLC ($700,000 civil monetary penalty + non-prosecution agreement with US Attorney's Office N.D. Cal.) was the FIRST civil enforcement action by FinCEN against a virtual-currency exchanger and imposed by consent a structural overhaul of XRP II's BSA / AML compliance program (MSB registration, SAR retroactive review, customer-identification program, independent reviewer). The offramp_cex layer carries the load-bearing direct-attribution observation; other layers are not_applicable on construct-out-of-scope or construct-did-not-exist grounds. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fincen.gov/news/news-releases/fincen-fines-ripple-labs-inc-first-civil-enforcement-action-against-virtual
- citation[1]: `primary_legal` replayable=`True` https://www.justice.gov/usao-ndca/pr/ripple-labs-inc-resolves-criminal-investigation

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
  "queue_id": 184,
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
  "queue_id": 184,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ripple-fincen-xrp-2015.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
