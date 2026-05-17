# v0.3 Review Packet: `brazil-bacen-stablecoin-restriction-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `30` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `brazil-bacen-stablecoin-restriction-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `BR_BACEN` |
| event_date | `2023-06-13` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/brazil-bacen-stablecoin-restriction-2023.yaml` |
| target_kind | `entity` |
| target_actor | `BACEN-supervised virtual-asset service providers (BRL-pegged stablecoin issuers and offshore stablecoin trading venues)` |

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

_No scoped claim in YAML payload._

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11563.htm
- citation[1]: `primary_legal` replayable=`True` https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/L14478.htm
- citation[2]: `supporting_journalism` replayable=`True` https://www.loc.gov/item/global-legal-monitor/2023-01-31/brazil-new-law-regulates-cryptocurrency/

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
  "queue_id": 30,
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
  "queue_id": 30,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/brazil-bacen-stablecoin-restriction-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
