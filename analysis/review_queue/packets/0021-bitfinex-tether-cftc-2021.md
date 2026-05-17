# v0.3 Review Packet: `bitfinex-tether-cftc-2021`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `21` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `bitfinex-tether-cftc-2021` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `cftc_action` |
| actor | `US_CFTC` |
| event_date | `2021-10-15` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitfinex-tether-cftc-2021.yaml` |
| target_kind | `entity` |
| target_actor | `iFinex / BFXNA / BFXWW (Bitfinex) + Tether Holdings / Tether Limited / Tether Operations / Tether International (USDT issuer)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 3 |
| primary observation sources | 3 |
| replayable observation sources | 3 |
| primary replayable observation sources | 3 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"The 2021-10-15 CFTC press release 8450-21 packages two simultaneous CFTC settlements ($1.5M against iFinex / BFXNA / BFXWW for illegal off-exchange financed retail commodity transactions in digital assets, and $41M against Tether Holdings / Limited / Operations / International for false or misleading statements regarding USDT reserve backing during 2016-01 through 2018-02), each registered as a single direct-attribution observed_change row at the offramp_cex layer. The CFTC settlement extends the 2021-02-23 NYAG disclosure-regime change to the federal commodities-law axis. The row asserts neither network-layer reachability change nor any USDT addBlackList() on-chain action; the reserve-attestation regime is recorded at offramp_cex (Tether-as-issuer fiat-rails interface), not at asset_onchain." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.cftc.gov/PressRoom/PressReleases/8450-21
- citation[1]: `primary_corporate` replayable=`True` https://tether.to/en/tether-and-bitfinex-reach-settlement-with-cftc/

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
  "queue_id": 21,
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
  "queue_id": 21,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitfinex-tether-cftc-2021.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
