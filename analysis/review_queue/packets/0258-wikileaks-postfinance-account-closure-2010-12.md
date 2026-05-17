# v0.3 Review Packet: `wikileaks-postfinance-account-closure-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `258` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-postfinance-account-closure-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `SWISSPOST_POSTFINANCE_OPERATOR` |
| event_date | `2010-12-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-postfinance-account-closure-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `PostFinance customer account "Assange Julian Paul, Geneve" (Julian Assange / WikiLeaks Defence Fund)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 5 |
| replayable trigger anchors | 5 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2010-12-06, PostFinance (Swiss Post's retail-banking arm) terminated the customer account registered as 'Assange Julian Paul, Geneve' — the account WikiLeaks had publicly advertised as the destination for the 'Julian Assange and other WikiLeaks Staff Defence Fund' — citing residency-verification failure under customer-relationship criteria. One observed_change at offramp_cex (load-bearing, attribution=direct, anchored on the PostFinance same-day media statement plus same-day Bloomberg / Al Jazeera / France 24 / swissinfo coverage). Discovery-ledger-only per temporal_tier=discovery_only_2008_2012." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://www.postfinance.ch/en/about-us/media/news-archive/2010/wikileaks.html
- citation[1]: `supporting_journalism` replayable=`True` https://www.bloomberg.com/news/articles/2010-12-06/wikileaks-founder-assange-s-swisspost-account-closed-on-residency-question
- citation[2]: `supporting_journalism` replayable=`True` https://www.aljazeera.com/news/2010/12/6/swiss-bank-closes-wikileaks-account
- citation[3]: `supporting_journalism` replayable=`True` https://www.france24.com/en/20101206-swiss-bank-closes-assange-account-accuses-lying-wikileaks-paypal-post
- citation[4]: `supporting_journalism` replayable=`True` https://www.swissinfo.ch/eng/wikileaks-supporters-attack-postfinance-site/28971816

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
  "queue_id": 258,
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
  "queue_id": 258,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-postfinance-account-closure-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
