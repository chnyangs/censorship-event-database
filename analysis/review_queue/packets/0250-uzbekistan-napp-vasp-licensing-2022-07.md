# v0.3 Review Packet: `uzbekistan-napp-vasp-licensing-2022-07`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `250` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `uzbekistan-napp-vasp-licensing-2022-07` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `UZ_NAPP` |
| event_date | `2022-07-14` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uzbekistan-napp-vasp-licensing-2022-07.yaml` |
| target_kind | `entity` |
| target_actor | `Republic of Uzbekistan — NAPP Order No. 32 (VASP licensing framework)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2022-07-14 the Director of the National Agency of Perspective Projects of the Republic of Uzbekistan (NAPP) signed Order No. 32 approving the Regulations on the procedure of licensing the activities of service providers in the crypto-assets turnover sphere (MoJ registration No. 3380 of 2022-08-15), establishing a mandatory domestic licensing perimeter for crypto-exchanges, crypto-depositories, crypto-stores, and mining pools restricted to Uzbek-resident legal entities. No admission-grade per-event cascade is pinned in this DRYRUN draft; coded null_event pending human audit of the offramp_cex perimeter effects." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://napp.uz/en/pages/service-providers
- citation[1]: `supporting_journalism` replayable=`True` https://manimama.eu/license-for-virtual-assets-service-providers-in-uzbekistan-prospects-for-crypto-business/
- citation[2]: `supporting_journalism` replayable=`True` https://www.lexology.com/library/detail.aspx?g=91e869a9-e800-455a-aa60-52d50e3d6c87

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
  "queue_id": 250,
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
  "queue_id": 250,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/uzbekistan-napp-vasp-licensing-2022-07.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
