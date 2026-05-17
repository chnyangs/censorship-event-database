# v0.3 Review Packet: `kingdom-trust-fincen-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `130` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `kingdom-trust-fincen-2021` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `fincen_action` |
| actor | `US_FINCEN` |
| event_date | `2023-04-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kingdom-trust-fincen-2021.yaml` |
| target_kind | `entity` |
| target_actor | `The Kingdom Trust Company` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

FinCEN's 2023-04-26 $1.5 million civil money penalty against The Kingdom Trust Company is a BSA / AML enforcement action targeting the entity's non-conventional trust-services line (Latin-American international wire and payment processing) and does not, on the public record captured in this authoring pass, engage KTC's crypto-IRA custody business or produce a strong-attribution crypto-censorship cascade observation. Coded as null_event / null_case pending primary-source pinning and any captured downstream crypto-offramp effect. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fincen.gov/news/news-releases/fincen-assesses-15-million-civil-money-penalty-against-kingdom-trust-company
- citation[1]: `primary_legal` replayable=`True` https://www.fincen.gov/sites/default/files/enforcement_action/2023-04-27/FinCEN_KTC_ConsentOrder_FINAL_042523.pdf

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
  "queue_id": 130,
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
  "queue_id": 130,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kingdom-trust-fincen-2021.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
