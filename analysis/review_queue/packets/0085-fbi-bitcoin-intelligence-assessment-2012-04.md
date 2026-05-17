# v0.3 Review Packet: `fbi-bitcoin-intelligence-assessment-2012-04`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `85` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `fbi-bitcoin-intelligence-assessment-2012-04` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `doj_indictment` |
| actor | `US_FBI` |
| event_date | `2012-04-24` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fbi-bitcoin-intelligence-assessment-2012-04.yaml` |
| target_kind | `entity` |
| target_actor | `Bitcoin protocol and Bitcoin-using illicit actors (US federal intelligence-assessment class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The FBI Cyber Intelligence Section / Criminal Intelligence Section assessment "Bitcoin Virtual Currency: Unique Features Present Distinct Challenges for Deterring Illicit Activity" (2012-04-24, leaked via WikiLeaks ~2013-03) is the first major US federal intelligence assessment of Bitcoin as an illicit-finance policy concern. observation_kind=coverage_gap with attribution=none because the substantive cascade is dispersed across downstream enforcement actions (Silk Road 2013, SEC v. Shavers/BTCST 2013, FinCEN FIN-2013-G001, Ripple/XRP I 2015) that inherit the intelligence-posture predicate, rather than localized to a single observable point-in-time CEX cessation. Discovery-tier only; not used in main statistical denominators. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.justsecurity.org/wp-content/uploads/2014/04/FBI.CyberIntelligenceCriminalIntelligence.2012.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://wikispooks.com/w/index.php?title=File:Bitcoin-FBI.pdf
- citation[2]: `supporting_community` replayable=`True` https://bitcointalk.org/index.php?topic=216248.0

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
  "queue_id": 85,
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
  "queue_id": 85,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fbi-bitcoin-intelligence-assessment-2012-04.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
