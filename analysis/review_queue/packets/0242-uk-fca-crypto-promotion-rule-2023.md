# v0.3 Review Packet: `uk-fca-crypto-promotion-rule-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `242` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `uk-fca-crypto-promotion-rule-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `UK_FCA` |
| event_date | `2023-10-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uk-fca-crypto-promotion-rule-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Cryptoasset firms marketing to UK consumers (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 3 |
| observation sources | 5 |
| primary observation sources | 3 |
| replayable observation sources | 5 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The UK FCA's Financial Promotions Regime for cryptoassets (Policy Statement PS23/6 + Finalised Guidance FG23/3), effective 2023-10-08, required all cryptoasset firms (UK-domiciled and overseas) marketing to UK consumers to communicate financial promotions via one of four legal routes under FSMA section 21. Within the compliance window, Bybit and KuCoin announced UK retail-customer restrictions / exits explicitly citing the regime; load-bearing observational axis is offramp_cex (Bybit and KuCoin UK retail restrictions, attribution=direct), with secondary l4_frontend UK-geo banners (attribution=plausible)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.fca.org.uk/publications/policy-statements/ps23-6-financial-promotion-rules-cryptoassets
- citation[1]: `primary_legal` replayable=`True` https://www.fca.org.uk/firms/cryptoassets/marketing-uk-consumers
- citation[2]: `primary_legal` replayable=`True` https://www.fca.org.uk/publications/finalised-guidance/fg23-3-cryptoasset-financial-promotions
- citation[3]: `primary_legal` replayable=`True` https://www.fca.org.uk/news/press-releases/fca-sets-expectations-ahead-incoming-crypto-marketing-rules

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
  "queue_id": 242,
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
  "queue_id": 242,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uk-fca-crypto-promotion-rule-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
