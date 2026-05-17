# v0.3 Review Packet: `ukraine-virtual-assets-law-2022-03`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `244` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ukraine-virtual-assets-law-2022-03` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `UA_PRESIDENT_UA_NSSMC` |
| event_date | `2022-03-16` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ukraine-virtual-assets-law-2022-03.yaml` |
| target_kind | `entity` |
| target_actor | `Virtual Asset Service Providers servicing Ukrainian users (NSSMC-licensable class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 2 |
| replayable observation sources | 3 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2022-03-16, two and a half weeks after the start of the Russian invasion, Ukrainian President Volodymyr Zelensky signed the Law of Ukraine 'On Virtual Assets' (Bill 3637), establishing the legal status of virtual assets in Ukraine and designating the National Securities and Stock Market Commission (NSSMC) as the primary regulator of a Virtual Asset Service Provider (VASP) licensing regime. The law is dual-character — permissive in framing (legalizing the asset class amid the wartime crypto-donation surge) while simultaneously compliance-mandating at the offramp_cex layer (NSSMC licensing chokepoint for any VASP servicing UA users, including offshore centralized exchanges). The downstream UA-VASP licensing cascade is recorded as coverage_gap with attribution=unknown because it is not yet measurable at issuance date and unfolds dispersedly across 2022-2024 NSSMC secondary rulemaking and exigent wartime administrative practice." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.president.gov.ua/news/prezident-pidpisav-zakon-pro-virtualni-aktivi-73575
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto
- citation[2]: `supporting_journalism` replayable=`True` https://www.elliptic.co/blog/crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law

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
  "queue_id": 244,
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
  "queue_id": 244,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ukraine-virtual-assets-law-2022-03.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
