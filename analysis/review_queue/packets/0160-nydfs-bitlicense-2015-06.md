# v0.3 Review Packet: `nydfs-bitlicense-2015-06`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `160` |
| status | `pending` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `nydfs-bitlicense-2015-06` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `court_civil_order` |
| actor | `US_NYDFS` |
| event_date | `2015-06-24` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/nydfs-bitlicense-2015-06.yaml` |
| target_kind | `entity` |
| target_actor | `NY virtual-currency operators (BitLicense-required class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 3 |
| observation sources | 3 |
| primary observation sources | 3 |
| replayable observation sources | 3 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2015-06-24 NYDFS BitLicense (23 NYCRR Part 200) triggered a documented L4-frontend exit by at least four named operators (ShapeShift, Kraken, Bitfinex, Poloniex) within 45 days of the effective date. The retained observations document only the frontend exit cascade; no L0/L1/L3/asset-onchain effects are claimed." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://web.archive.org/web/20150604135045/http://www.dfs.ny.gov/legal/regulations/adoptions/dfsp200t.pdf
- citation[1]: `primary_corporate` replayable=`True` https://www.dfs.ny.gov/virtual_currency_businesses

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
  "queue_id": 160,
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
  "queue_id": 160,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/nydfs-bitlicense-2015-06.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
