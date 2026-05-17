# v0.3 Review Packet: `canada-csa-binance-withdrawal-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `35` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `canada-csa-binance-withdrawal-2023` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `CA_CSA` |
| event_date | `2023-02-22` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/canada-csa-binance-withdrawal-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Binance (Canada user cohort)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2023-02-22 CSA Staff Notice 21-332 enhanced pre-registration-undertaking framework — restricting Canadian crypto-trading-platform stablecoin offerings and investor-position limits — produced a 2-layer cascade for the Binance Canada cohort: a customer-facing market-exit announcement on binance.com (2023-05-12) and a corresponding offramp_cex shutdown of CAD rails and Canadian-resident accounts. Structurally an entity-self-withdrawal response to a class-wide securities-registration framework rather than a banking-rail cascade." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.securities-administrators.ca/news/
- citation[1]: `primary_corporate` replayable=`True` https://www.binance.com/en/blog/ecosystem/an-update-on-binance-in-canada-3550161948550610227

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
  "queue_id": 35,
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
  "queue_id": 35,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/canada-csa-binance-withdrawal-2023.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
