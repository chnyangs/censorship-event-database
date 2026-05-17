# v0.3 Review Packet: `makerdao-emergency-shutdown-contingency-2022-08`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `146` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `makerdao-emergency-shutdown-contingency-2022-08` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `MAKERDAO_GOVERNANCE` |
| event_date | `2022-08-18` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/makerdao-emergency-shutdown-contingency-2022-08.yaml` |
| target_kind | `entity` |
| target_actor | `MakerDAO governance community (MKR voters + Maker Foundation contributors)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 6 |
| replayable trigger anchors | 6 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 4 |
| primary observation sources | 2 |
| replayable observation sources | 4 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Between 2022-08-08 (OFAC Tornado Cash SDN designation) and 2022-08-31, the MakerDAO governance community publicly debated three discretionary protocol-level censorship-response postures — Emergency Shutdown of the Maker Protocol, migration of ~33% of DAI collateral away from USDC/USDP toward ETH, and abandonment of the DAI USD peg — none of which was enacted in the debate window. The row carries no observed_change and functions as a counterfactual-contingency denominator control for the S5 DAO-governance-response-to-sanctions stratum, scoping the 'debated but not enacted' baseline against which contemporaneous S5 enacted-response rows (Circle USDC Tornado freeze, Aave Tornado frontend block, dYdX Tornado account block) can be compared. Foundational DAO-governance-response-to- sanctions case." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://forum.makerdao.com/search/query.json?term=USDC%20Tornado%20Cash
- citation[1]: `primary_corporate` replayable=`True` https://forum.makerdao.com/t/circle-started-freezing-usdc-which-went-through-tornado-cash/17101.json
- citation[2]: `supporting_journalism` replayable=`True` https://thedefiant.io/news/defi/tornado-impact-makerdao-dai
- citation[3]: `supporting_journalism` replayable=`True` https://decrypt.co/107273/makerdao-founder-dai-drop-dollar-peg-tornado-cash-usdc
- citation[4]: `supporting_journalism` replayable=`True` https://www.coindesk.com/business/2022/08/18/makerdao-prepares-emergency-shutdown-contingency-in-case-of-usdc-sanctions
- citation[5]: `supporting_journalism` replayable=`True` https://cryptoslate.com/makerdao-plans-against-sanctions-from-usdc-exposure/

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
  "queue_id": 146,
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
  "queue_id": 146,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/makerdao-emergency-shutdown-contingency-2022-08.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
