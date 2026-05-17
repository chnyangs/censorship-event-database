# v0.3 Review Packet: `fatf-virtual-currencies-key-definitions-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `84` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `fatf-virtual-currencies-key-definitions-2014` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `supranational_regulation` |
| actor | `FATF` |
| event_date | `2014-06-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-virtual-currencies-key-definitions-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Virtual currency exchangers and administrators (global FATF class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

The FATF 2014-06-26 report "Virtual Currencies — Key Definitions and Potential AML/CFT Risks" introduced a shared FATF-level taxonomy ("exchanger", "administrator", "convertible / non- convertible VC", "centralised / decentralised VC") and a preliminary risk-framing for AML/CFT exposures of virtual currency activity, establishing the foundational supranational predicate guidance for the five-year regulatory development arc culminating in the 2019-06-21 FATF R.15 INR Travel Rule extension to VASPs (fatf-r15-vasp-travel-rule-2019). The 2014 report does not itself impose binding VASP obligations; observation_kind=observed_no_change with attribution=plausible at the supranational standard-setting axis honestly represents the dispersed pre-regime predicate role. Historical-baseline tier; not used in main statistical denominators. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-currency-key-definitions-and-potential-aml-cft-risks.pdf
- citation[1]: `primary_legal` replayable=`True` https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-currency-definitions-aml-cft-risk.html

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
  "queue_id": 84,
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
  "queue_id": 84,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/fatf-virtual-currencies-key-definitions-2014.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
