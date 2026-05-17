# v0.3 Review Packet: `tornado-cash-tornadocash-org-seizure-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `236` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `tornado-cash-tornadocash-org-seizure-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `tornado_cash_team` |
| event_date | `2022-08-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-tornadocash-org-seizure-2022.yaml` |
| target_kind | `entity` |
| target_actor | `Tornado Cash — tornadocash.org canonical domain` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 1 |
| replayable observation sources | 4 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The operator-initiated cessation of the canonical tornadocash.org web-domain entrypoint on 2022-08-08 — the same day as the OFAC SDN designation of Tornado Cash (related event tornado-cash-ofac-2022) — documents the canonical-web-domain sub-layer of the L4 frontend vertex in the S5_corporate cascade. Distinct from the third-party GitHub source-code-host takedown (tornado-cash-github-takedown-2022-08), this row captures the project's own DNS / web-entrypoint cessation as an operator-self-imposed compliance reaction. Paper-relevant as the canonical-domain analogue to the source-code-platform and application-UI L4 rows in the 2022-08-08 cascade." 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://alexbobes.medium.com/crypto-mixers-and-tornado-cash-shutdown-98a6e743b596
- citation[1]: `supporting_journalism` replayable=`True` https://www.eff.org/deeplinks/2023/04/update-tornado-cash
- citation[2]: `supporting_journalism` replayable=`True` https://federal-lawyer.com/ofac-and-tornado-cash-a-timeline-of-the-events-leading-to-and-following-ofacs-sanctions/
- citation[3]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2022/08/08/crypto-mixing-service-tornado-cash-blacklisted-by-us-treasury

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
  "queue_id": 236,
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
  "queue_id": 236,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/tornado-cash-tornadocash-org-seizure-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
