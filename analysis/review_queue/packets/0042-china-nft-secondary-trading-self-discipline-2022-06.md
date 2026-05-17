# v0.3 Review Packet: `china-nft-secondary-trading-self-discipline-2022-06`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `42` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `china-nft-secondary-trading-self-discipline-2022-06` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `CN_BANKING_ASSOC + CN_INTERNET_SOC + CN_SAC` |
| event_date | `2022-06-30` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-nft-secondary-trading-self-discipline-2022-06.yaml` |
| target_kind | `entity` |
| target_actor | `PRC digital-collectibles platforms (Tencent Huanhe, Alibaba Phoenix, JD Lingxi, Baidu, etc.)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 0 |
| replayable observation sources | 4 |
| primary replayable observation sources | 0 |

Machine blockers: `no_observation_primary_source_detected`
Machine notes: `none`

## Scoped Claim

On 2022-06-30, three PRC industry self-regulatory bodies (China Banking Association, Internet Society of China, Securities Association of China) issued a 14-article self-discipline initiative co-signed by approximately 30 platform signatories (including Tencent Huanhe and Alibaba/Ant Group Phoenix) that banned secondary trading of NFTs ("digital collectibles") and restricted primary sales to RMB-denominated, real-name-authenticated flows on permissioned consortium chains. Observational axes at l4_frontend (secondary-trading UI removal) and asset_onchain (issuance restricted to primary-only). Admission-anchor-grade promotion pending pinned platform / consortium-chain artifacts. 

## Trigger Citations

- citation[0]: `supporting_journalism` replayable=`True` https://www.scmp.com/tech/big-tech/article/3184021/china-nfts-tencent-and-ant-group-join-industry-pledge-ban
- citation[1]: `supporting_journalism` replayable=`True` https://www.euronews.com/next/2022/06/30/china-tech-nfts
- citation[2]: `supporting_journalism` replayable=`True` https://www.asiafinancial.com/chinas-big-tech-groups-pledge-to-help-ban-nft-trading

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
  "queue_id": 42,
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
  "queue_id": 42,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/china-nft-secondary-trading-self-discipline-2022-06.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
