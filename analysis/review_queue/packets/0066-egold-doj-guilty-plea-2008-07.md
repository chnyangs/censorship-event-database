# v0.3 Review Packet: `egold-doj-guilty-plea-2008-07`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `66` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `egold-doj-guilty-plea-2008-07` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_DOJ_DC` |
| event_date | `2008-07-21` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/egold-doj-guilty-plea-2008-07.yaml` |
| target_kind | `entity` |
| target_actor | `e-Gold Ltd. + Gold & Silver Reserve Inc. + Douglas Jackson` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2008-07-21 DOJ guilty plea by e-Gold Ltd., Gold & Silver Reserve Inc., and Douglas Jackson (in US District Court for the District of Columbia) on conspiracy to engage in money laundering (18 USC s 1956(h)) and operation of an unlicensed money transmitting business (18 USC s 1960) produced an offramp_cex cascade (e-Gold's digital-gold-account service operations ceased and did not resume). The row claims only this single-layer offramp shutdown observation with attribution=plausible; no L0/L1/L3/L4/asset-onchain effects are coded. Discovery-tier only: no comparable-analysis use." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justice.gov/archive/opa/pr/2008/July/08-crm-635.html
- citation[1]: `primary_legal` replayable=`True` https://www.secretservice.gov/press/releases/2008/07/us-secret-service-led-investigation-digital-currency-business-e-gold-pleads
- citation[2]: `primary_corporate` replayable=`False` https://legalupdate.e-gold.com/2008/07/plea-agreement-as-to-douglas-l-jackson-20080721.html

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
  "queue_id": 66,
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
  "queue_id": 66,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/egold-doj-guilty-plea-2008-07.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
