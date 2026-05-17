# v0.3 Review Packet: `kazakhstan-internet-shutdown-mining-2022-01`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `129` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `kazakhstan-internet-shutdown-mining-2022-01` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `KZ_PRESIDENT_TOKAYEV` |
| event_date | `2022-01-05` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kazakhstan-internet-shutdown-mining-2022-01.yaml` |
| target_kind | `entity` |
| target_actor | `Kazakhstan nationwide internet shutdown (2022-01-05 to 2022-01-10)` |

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

"On 2022-01-05 at approximately noon UTC, the government of Kazakhstan under President Tokayev ordered a nationwide internet shutdown in response to political unrest. NetBlocks recorded normalized country-level connectivity falling to ~2% (L0 layer, attribution=direct), and the bitcoin network total hashrate dropped from ~194 EH/s to ~168 EH/s within the same day as the Kazakhstan-hosted miner population (~18% global hashrate share per CBECI fall-2021) lost stratum-server connectivity (L1 consensus layer, attribution=direct, causally chained from the L0 shutdown). L0 restored on or around 2022-01-10; hashrate recovered to pre-shutdown levels within ~1 week of L0 restoration. This is the first pure L0 network-layer event in the corpus. Admission-anchor-grade promotion pending pinned archive captures (NetBlocks snapshot, IODA JSON, CBECI mining-map JSON)." 

## Trigger Citations

- citation[0]: `semi_primary_measurement` replayable=`True` https://netblocks.org/reports/internet-disrupted-in-kazakhstan-amid-energy-price-protests-oy9YQgy3
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/business/2022/01/06/kazakhstans-hashrate-drops-as-internet-blackout-persists-amid-nationwide-protests
- citation[2]: `supporting_journalism` replayable=`True` https://www.cnbc.com/2022/01/06/kazakhstan-bitcoin-mining-shuts-down-amid-fatal-protests.html
- citation[3]: `supporting_tracker` replayable=`True` https://blog.cloudflare.com/internet-shut-down-in-kazakhstan-amid-unrest/

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
  "queue_id": 129,
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
  "queue_id": 129,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/kazakhstan-internet-shutdown-mining-2022-01.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
