# v0.3 Review Packet: `circle-usdc-cryptex-freeze-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `50` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `circle-usdc-cryptex-freeze-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `CIRCLE_USDC_ISSUER` |
| event_date | `2024-09-26` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/circle-usdc-cryptex-freeze-2024.yaml` |
| target_kind | `entity` |
| target_actor | `Cryptex` |

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

Circle's 2024-09-27 03:00 UTC USDC blacklist of the OFAC-named Cryptex ETH address 0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7 (~27h after the 2024-09-26 SDN) constitutes a distinct corporate-policy-change event documenting Circle's compliance response to a single-address OFAC SDN, sibling to the cryptex-ofac-2024 cascade. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ofac.treasury.gov/recent-actions/20240926
- citation[1]: `primary_onchain` replayable=`True` https://etherscan.io/tx/0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da

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
  "queue_id": 50,
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
  "queue_id": 50,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/circle-usdc-cryptex-freeze-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
