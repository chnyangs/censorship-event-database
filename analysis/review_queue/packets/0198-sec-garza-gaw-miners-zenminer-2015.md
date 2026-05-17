# v0.3 Review Packet: `sec-garza-gaw-miners-zenminer-2015`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `198` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `sec-garza-gaw-miners-zenminer-2015` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `sec_action` |
| actor | `US_SEC` |
| event_date | `2015-12-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-garza-gaw-miners-zenminer-2015.yaml` |
| target_kind | `entity` |
| target_actor | `GAW Miners / ZenMiner / Garza` |

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

The 2015-12-01 SEC civil action against Homero Joshua Garza, GAW Miners, LLC, and ZenMiner, LLC for the unregistered sale of Hashlet "securities" pointing to nonexistent or oversold cloud- mining capacity precipitated the cessation of the gawminers.com and zenminer.com cloud-mining-service frontends in the months following filing. The row claims only this single-layer L4 frontend cessation observation with attribution=direct; no L0/L1/L3/asset-onchain/offramp_cex effects are coded because the Hashlet product was a service contract rather than an on-chain freezable token and the operator was a cloud-mining service rather than a fiat off-ramp / exchange. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.sec.gov/litigation/litreleases/2015/lr23415.htm
- citation[1]: `primary_legal` replayable=`True` https://www.sec.gov/files/litigation/complaints/2015/comp23415.pdf
- citation[2]: `primary_legal` replayable=`True` https://www.sec.gov/news/pressrelease/2015-271.html

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
  "queue_id": 198,
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
  "queue_id": 198,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/sec-garza-gaw-miners-zenminer-2015.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
