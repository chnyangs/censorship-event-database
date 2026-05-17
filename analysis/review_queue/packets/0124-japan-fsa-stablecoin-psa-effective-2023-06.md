# v0.3 Review Packet: `japan-fsa-stablecoin-psa-effective-2023-06`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `124` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `japan-fsa-stablecoin-psa-effective-2023-06` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `JP_FSA` |
| event_date | `2023-06-01` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-stablecoin-psa-effective-2023-06.yaml` |
| target_kind | `entity` |
| target_actor | `JP-jurisdiction stablecoin issuer + EPIESP intermediary ecosystem (FSA-licensed)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"Japan's 2023-06-01 commencement of the Payment Services Act Amendment Act established the Electronic Payment Instrument (EPI / 電子決済手段) regulatory regime for fiat-referenced stablecoins, restricting EPI issuance to JP-licensed banks, fund transfer service providers, and trust companies/banks, and requiring Electronic Payment Instrument Exchange Service Provider (EPIESP) registration for stablecoin intermediation. As the first major industrial-democracy stablecoin issuer regime to take legal effect, it predates EU MiCA stablecoin provisions (2024-06-30) and the HK HKMA Stablecoins Ordinance (2025-08-01). The row does not claim any specific 2023-06-01 issuer-side launch, JP-VASP stablecoin delisting cascade, on-chain asset-layer freeze, or frontend takedown; it documents the regulatory-framework trigger as a null_event pending downstream EPIESP-registration and EPI-issuer- licence events authored as separate rows." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fsa.go.jp/en/newsletter/weekly2023/540.html
- citation[1]: `supporting_journalism` replayable=`True` https://cryptoforinnovation.org/policy-brief-summary-of-japanese-fsa-crypto-asset-and-stablecoins-framework/
- citation[2]: `supporting_journalism` replayable=`True` https://news.bitcoin.com/japan-stablecoin-regulation-explained-psa-rules-jpy-coins-and-bank-issuers/

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
  "queue_id": 124,
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
  "queue_id": 124,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/japan-fsa-stablecoin-psa-effective-2023-06.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
