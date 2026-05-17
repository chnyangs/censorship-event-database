# v0.3 Review Packet: `thailand-bot-bitcoin-prohibition-2013`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `227` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `thailand-bot-bitcoin-prohibition-2013` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `TH_BOT` |
| event_date | `2013-07-29` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/thailand-bot-bitcoin-prohibition-2013.yaml` |
| target_kind | `entity` |
| target_actor | `Bitcoin Co. Ltd (Thailand)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

On 2013-07-29 the Bank of Thailand Foreign Exchange Administration and Policy Department issued a verbal administrative advisement to Bitcoin Co. Ltd that bitcoin trading was illegal under Thai law given the Exchange Control Act B.E. 2485 framework; Bitcoin Co. Ltd suspended operations the same day and resumed approximately 6.5 months later (2014-02-15) following a BOT clarification letter. The offramp_cex layer carries the single direct-attribution observed_change row; L0/L1/L3/asset_onchain are not_applicable on construct or scope grounds and L4 frontend is not_measured pending Wayback capture. 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://bitcoin.co.th/trading-suspended-due-to-bank-of-thailand-advisement/
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/markets/2013/07/29/bank-of-thailand-allegedly-declares-bitcoin-illegal-thai-exchange-suspends-trading
- citation[2]: `supporting_journalism` replayable=`True` https://www.bangkokpost.com/business/362222/bitcoin-declared-illegal-in-thailand
- citation[3]: `supporting_journalism` replayable=`True` https://reason.com/2013/07/31/thailands-central-bank-outlaws-bitcoin-t/

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
  "queue_id": 227,
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
  "queue_id": 227,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/thailand-bot-bitcoin-prohibition-2013.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
