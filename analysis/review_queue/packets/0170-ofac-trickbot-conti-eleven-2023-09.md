# v0.3 Review Packet: `ofac-trickbot-conti-eleven-2023-09`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `170` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `ofac-trickbot-conti-eleven-2023-09` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `ofac_sdn_designation` |
| actor | `US_OFAC + UK_NCA + US_DOJ` |
| event_date | `2023-09-07` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-trickbot-conti-eleven-2023-09.yaml` |
| target_kind | `entity` |
| target_actor | `Trickbot/Conti gang — 11 Russian nationals (Andrey Zhuykov, Maksim Galochkin, Maksim Rudenskiy, Mikhail Tsarev, Dmitry Putilin, Maksim Khaliullin, Sergey Loguntsov, Alexander Mozhaev, Vadym Valiakhmetov, Artem Kurov, Mikhail Chernov)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 3 |
| replayable observation sources | 4 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"OFAC press release jy1714 of 2023-09-07, jointly with UK NCA designations and DOJ indictment unsealings, designated 11 Russian nationals connected to the Trickbot/Conti cybercrime gang — the first major US-UK joint cyber-financial sanctions package — producing a comparison-shape cascade with observed_change at offramp_cex (sanctioned-person ramp blocking) and asset_onchain (per-individual SDN wallet attachments)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://home.treasury.gov/news/press-releases/jy1714
- citation[1]: `primary_legal` replayable=`True` https://www.nationalcrimeagency.gov.uk/news/russian-ransomware-group-hit-with-new-sanctions
- citation[2]: `primary_legal` replayable=`True` https://www.justice.gov/opa/pr/us-and-uk-disrupt-trickbot-malware
- citation[3]: `supporting_journalism` replayable=`True` https://www.bleepingcomputer.com/news/security/us-and-uk-sanction-11-trickbot-and-conti-cybercrime-gang-members/

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
  "queue_id": 170,
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
  "queue_id": 170,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/ofac-trickbot-conti-eleven-2023-09.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
