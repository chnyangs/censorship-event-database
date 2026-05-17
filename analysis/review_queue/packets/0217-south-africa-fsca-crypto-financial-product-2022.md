# v0.3 Review Packet: `south-africa-fsca-crypto-financial-product-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `217` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `south-africa-fsca-crypto-financial-product-2022` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `ZA_FSCA` |
| event_date | `2022-10-19` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/south-africa-fsca-crypto-financial-product-2022.yaml` |
| target_kind | `entity` |
| target_actor | `South-Africa-operating Crypto Asset Service Providers and FAIS advisers (FSCA-FAIS-regulated)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"FSCA Declaration 2022-10-19 (Government Notice 1350, Government Gazette 47334) declares crypto assets a financial product under the South African FAIS Act, bringing persons providing FAIS-defined advice and intermediary services in respect of crypto assets into the FSP licensing perimeter, with a transitional exemption pending licence-application disposition (window 2023-06-01 to 2023-11-30). As of the 2026-05-17 authoring date no class-level offramp_cex behavioral change at the ZA CASP cohort attributable specifically to the Declaration has been observed — coded null_event / null_case as a S4_nation_state denominator control on the African-continent axis, sibling to MiCA (eu-mica-2023) and a downstream national- implementation companion to FATF R.15 (fatf-r15-vasp-travel-rule- 2019)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsca.co.za/News%20Documents/FSCA%20Press%20Release_Declaration%20of%20Crypto%20Assets%20As%20A%20Financial%20Product_20%20October%202022.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://www.cliffedekkerhofmeyr.com/en/news/publications/2022/Practice/Finance/finance-and-banking-alert-20-october-2022-fsca-declares-crypto-assets-as-a-financial-product-.html

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
  "queue_id": 217,
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
  "queue_id": 217,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/south-africa-fsca-crypto-financial-product-2022.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
