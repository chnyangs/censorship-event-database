# v0.3 Review Packet: `coin-mx-doj-murgio-2015`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `54` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `coin-mx-doj-murgio-2015` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_SDNY` |
| event_date | `2015-07-21` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/coin-mx-doj-murgio-2015.yaml` |
| target_kind | `entity` |
| target_actor | `Coin.mx` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The 2015-07-21 DOJ SDNY indictment of Anthony R. Murgio and Yuri Lebedev for operating Coin.mx as an unlicensed bitcoin exchange (with HOPE Federal Credit Union captured as a banking conduit and a phony "Collectors Club" front company) produced an offramp_cex cascade: Coin.mx shut down post-arrest and the USD-rails conduit through HOPE FCU was severed. The row claims only this single-layer offramp shutdown observation with attribution=direct; no L0/L1/L3/L4/asset-onchain effects are coded. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-two-florida-men-operating-underground
- citation[1]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-pleads-guilty-multimillion-dollar-money-laundering
- citation[2]: `primary_legal` replayable=`True` https://www.justice.gov/usao-sdny/pr/operator-unlawful-bitcoin-exchange-sentenced-more-5-years-prison-leading-multimillion

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
  "queue_id": 54,
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
  "queue_id": 54,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/coin-mx-doj-murgio-2015.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
