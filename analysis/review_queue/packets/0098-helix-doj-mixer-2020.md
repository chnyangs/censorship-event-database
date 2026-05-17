# v0.3 Review Packet: `helix-doj-mixer-2020`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `98` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `helix-doj-mixer-2020` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_DC` |
| event_date | `2020-02-11` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/helix-doj-mixer-2020.yaml` |
| target_kind | `entity` |
| target_actor | `Helix / Coin Ninja (operated by Larry Dean Harmon)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 1 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 3 |
| replayable observation sources | 3 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2020-02-11 DOJ DDC indictment of Larry Dean Harmon for operating the Helix Bitcoin mixer (2014-2017, $300M+ laundered) produced a 2-layer comparison-shape cascade in the dataset: an l4_frontend finality on the already-self-shuttered helix .onion service and an offramp_cex mixer- operator-state transition anchored by the indictment + parallel 2020-10-19 FinCEN $60M civil money penalty. Distinct from chipmixer-doj-2023 and samourai-doj-2024 in that the mixer was already dark at indictment time and the enforcement was single-jurisdiction (US-only)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/opa/pr/ohio-resident-charged-operating-darknet-based-bitcoin-mixer-laundered-over-300-million
- citation[1]: `primary_legal` replayable=`False` https://www.fincen.gov/news/news-releases/fincen-announces-60-million-civil-money-penalty-against-larry-dean-harmon

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
  "queue_id": 98,
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
  "queue_id": 98,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/helix-doj-mixer-2020.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
