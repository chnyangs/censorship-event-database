# v0.3 Review Packet: `mtgox-mizuho-wire-pressure-2012`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `156` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `mtgox-mizuho-wire-pressure-2012` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `MIZUHO_BANK` |
| event_date | `2012-12-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-mizuho-wire-pressure-2012.yaml` |
| target_kind | `entity` |
| target_actor | `Mt. Gox K.K.` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"No discrete 2012-12 Mizuho Bank action against Mt. Gox K.K.'s JPY/USD wire-transfer rails is documented in the secondary sources consulted (Mt. Gox Wikipedia, Bilzin Sumberg jurisdictional retrospective on Greene v. Mizuho). The documented Mizuho correspondent-banking severance against Mt. Gox begins 2013-06-20 onward, coincident with the Mt. Gox USD withdrawal suspension. This row records observation_kind=observed_no_change + attribution=none at offramp_cex over the 2012-12 calendar month as a negative finding. null_event shape; discovery-tier; not used in main statistical denominators." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.govinfo.gov/content/pkg/USCOURTS-ilnd-1_14-cv-01437/pdf/USCOURTS-ilnd-1_14-cv-01437-0.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://en.wikipedia.org/wiki/Mt._Gox
- citation[2]: `supporting_journalism` replayable=`True` https://www.bilzin.com/we-think-big/insights/publications/2019/09/jurisdictional-lessons-from-mt-gox-cryptocurrency

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
  "queue_id": 156,
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
  "queue_id": 156,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/mtgox-mizuho-wire-pressure-2012.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
