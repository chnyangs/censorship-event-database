# v0.3 Review Packet: `kazakhstan-digital-assets-law-2023-02`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `128` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `kazakhstan-digital-assets-law-2023-02` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `KZ_PRESIDENT` |
| event_date | `2023-02-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kazakhstan-digital-assets-law-2023-02.yaml` |
| target_kind | `entity` |
| target_actor | `Republic of Kazakhstan — Law No. 193-VII On Digital Assets` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 2 |
| replayable observation sources | 4 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2023-02-06 the President of the Republic of Kazakhstan signed Law No. 193-VII On Digital Assets, in force 2023-04-01, which introduced (i) a mandatory state cryptomining-licence and pool-accreditation regime and (ii) an AIFC-confined commercial digital-asset exchange registration regime. Both effects are attribution=direct from the legal text: unlicensed cryptomining on Kazakh territory and off-AIFC commercial exchange activity for Kazakh-vantage users become unlicensed from the in-force date. Load-bearing axes are l1_consensus (Kazakh mining substrate) and offramp_cex (Kazakh-vantage commercial exchange perimeter)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://adilet.zan.kz/eng/docs/Z2300000193
- citation[1]: `supporting_journalism` replayable=`True` https://www.loc.gov/item/global-legal-monitor/2023-04-30/kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptomining/
- citation[2]: `supporting_journalism` replayable=`True` https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets

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
  "queue_id": 128,
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
  "queue_id": 128,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kazakhstan-digital-assets-law-2023-02.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
