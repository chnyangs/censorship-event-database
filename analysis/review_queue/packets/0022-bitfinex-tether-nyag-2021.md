# v0.3 Review Packet: `bitfinex-tether-nyag-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `22` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `bitfinex-tether-nyag-2021` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `US_NY_OAG` |
| event_date | `2021-02-23` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitfinex-tether-nyag-2021.yaml` |
| target_kind | `entity` |
| target_actor | `iFinex / BFXNA / BFXWW (Bitfinex) + Tether Holdings / Tether Operations / Tether Limited / Tether International (USDT issuer)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 4 |
| replayable observation sources | 4 |
| primary replayable observation sources | 4 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2021-02-23 NY OAG settlement against iFinex / BFXNA / BFXWW and the Tether issuer entities imposes a $18.5M monetary penalty, a prospective prohibition on trading activity with New York persons or entities, and a two-year quarterly USDT reserve- composition reporting obligation. The row registers two direct-attribution observed_change observations at the offramp_cex layer (the NY-resident trading prohibition and the Tether reserve-attestation regime change). The row asserts neither network-layer reachability change nor any USDT addBlackList() on-chain action; the reserve-attestation regime is an off-chain disclosure obligation registered at offramp_cex on the Tether-as-issuer fiat-rails interface." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf
- citation[1]: `primary_corporate` replayable=`True` https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/

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
  "queue_id": 22,
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
  "queue_id": 22,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitfinex-tether-nyag-2021.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
