# v0.3 Review Packet: `kucoin-doj-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `139` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `kucoin-doj-2024` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_SDNY_CFTC` |
| event_date | `2024-03-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kucoin-doj-2024.yaml` |
| target_kind | `entity` |
| target_actor | `KuCoin (Peken Global / Mek Global) + Chun Gan + Ke Tang` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
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

"The 2024-03-26 DOJ SDNY indictment + CFTC consent order against KuCoin and its founders produced a 2-layer cascade in the dataset: an L4 customer-facing US-off-boarding announcement on kucoin.com and an offramp_cex shutdown of US-resident services tied to a $300M CFTC penalty and full US market exit. Structurally narrower than the 4-framework Binance settlement and broader than the Kraken staking-only service shutdown." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/founders-and-executives-global-cryptocurrency-exchange-charged-bank-secrecy-act-and
- citation[1]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/8866-24
- citation[2]: `primary_legal` replayable=`False` https://www.fincen.gov/news/news-releases

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
  "queue_id": 139,
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
  "queue_id": 139,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kucoin-doj-2024.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
