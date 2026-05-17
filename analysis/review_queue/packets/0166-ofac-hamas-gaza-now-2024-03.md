# v0.3 Review Packet: `ofac-hamas-gaza-now-2024-03`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `166` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ofac-hamas-gaza-now-2024-03` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC` |
| event_date | `2024-03-27` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-hamas-gaza-now-2024-03.yaml` |
| target_kind | `entity` |
| target_actor | `Gaza Now (Hamas-aligned media / crypto fundraising network)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 5 |
| replayable trigger anchors | 5 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 1 |
| replayable observation sources | 2 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC's 2024-03-27 SDN designation of Gaza Now (a Gaza-based pro-Hamas news / social-media brand exploited as a crypto donation funnel) added 8 digital-currency addresses (1 BTC empty + 2 ETH + 5 USDT, ~USD 13K combined funded balance) to the SDN list as part of a joint US OFAC + UK OFSI action under EO 13224. Cascade evaluation conditional on pinned post-event usdtbanlist.com and Chainalysis slice anchors." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://home.treasury.gov/news/press-releases/jy2213
- citation[1]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20240327
- citation[2]: `supporting_journalism` replayable=`True` https://www.chainalysis.com/blog/ofac-ofsi-gaza-now-sanctions/
- citation[3]: `supporting_journalism` replayable=`True` https://www.coindesk.com/policy/2024/03/27/us-uk-issue-joint-sanctions-of-hamas-aligned-gaza-now
- citation[4]: `supporting_journalism` replayable=`True` https://www.elliptic.co/blog/crypto-regulatory-affairs-the-us-treasurys-intense-week-of-crypto-related-sanctions-actions

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
  "queue_id": 166,
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
  "queue_id": 166,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-hamas-gaza-now-2024-03.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
