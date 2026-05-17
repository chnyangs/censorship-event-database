# v0.3 Review Packet: `metamask-snaps-region-restrictions-2023-09`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `150` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `metamask-snaps-region-restrictions-2023-09` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `CONSENSYS_METAMASK` |
| event_date | `2023-09-12` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/metamask-snaps-region-restrictions-2023-09.yaml` |
| target_kind | `entity` |
| target_actor | `MetaMask wallet end-users on stable channel (v11.0+) installing Snaps from the MetaMask Snaps directory` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 5 |
| replayable trigger anchors | 5 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 2 |
| replayable observation sources | 4 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2023-09-12 ConsenSys / MetaMask launched the Snaps platform in the MetaMask Extension stable channel (v11.0) behind an allowlist (npm package name + version + content checksum) curated through the MetaMask Snaps directory. Per-Snap regional restrictions (some Snaps unavailable in certain jurisdictions) propagate to the wallet user through the same L4 directory gate; Snap-internal RPC endpoints inherit that gating at L3 indirectly. Two observed_change layers (L4 attribution=direct; L3 attribution= plausible) → empirical_shape=comparison, admission_tier= empirical_case." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://metamask.io/news/snaps-in-metamask-stable-and-where-we-go-from-here
- citation[1]: `primary_corporate` replayable=`True` https://metamask.io/news/metamask-snaps-our-first-step-on-the-road-to-becoming-fully-permissionless
- citation[2]: `supporting_journalism` replayable=`True` https://www.cryptotimes.io/2023/09/13/metamask-launches-snaps-to-enable-in-wallet-enhancements/
- citation[3]: `supporting_journalism` replayable=`True` https://bitcoinist.com/metamask-snaps-open-beta-launches/
- citation[4]: `supporting_community` replayable=`True` https://github.com/MetaMask/snaps/discussions/1411

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
  "queue_id": 150,
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
  "queue_id": 150,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/metamask-snaps-region-restrictions-2023-09.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
