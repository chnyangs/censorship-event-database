# v0.3 Review Packet: `bitmex-cftc-doj-2020`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `23` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `bitmex-cftc-doj-2020` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_SDNY` |
| event_date | `2020-10-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitmex-cftc-doj-2020.yaml` |
| target_kind | `entity` |
| target_actor | `BitMEX (HDR Global Trading) + Hayes / Delo / Reed / Dwyer` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2020-10-01 CFTC civil complaint and DOJ SDNY criminal indictment against BitMEX (HDR Global Trading) and co-founders Arthur Hayes, Benjamin Delo, Samuel Reed, and Gregory Dwyer produced a 2-layer cascade in the dataset: an L4 user-facing notice geo-blocking US retail access and an offramp_cex restriction of US-resident derivatives rails coupled with a globally mandatory KYC programme, resolved 2021-08-10 via a $100M CFTC consent order. Structurally the BSA-AML / KYC template later extended by the Binance and KuCoin enforcement paths." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/8270-20
- citation[1]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/founders-and-executive-cryptocurrency-exchange-charged-violation-bank-secrecy-act
- citation[2]: `primary_corporate` replayable=`True` https://blog.bitmex.com/hdr-global-trading-limited-response-to-the-cftc-and-fincen/

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
  "queue_id": 23,
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
  "queue_id": 23,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitmex-cftc-doj-2020.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
