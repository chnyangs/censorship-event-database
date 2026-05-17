# v0.3 Review Packet: `indonesia-bappebti-illegal-exchange-block-2023`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `109` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `indonesia-bappebti-illegal-exchange-block-2023` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `nation_state_block` |
| actor | `ID_BAPPEBTI` |
| event_date | `2023-07-25` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/indonesia-bappebti-illegal-exchange-block-2023.yaml` |
| target_kind | `entity` |
| target_actor | `Foreign unlicensed crypto exchanges (ID cohort)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 3 |
| replayable trigger anchors | 3 |
| coverage rows | 6 |
| observations | 2 |
| observation sources | 4 |
| primary observation sources | 2 |
| replayable observation sources | 4 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"BAPPEBTI's 2023-07-25 enforcement order, routed via Kominfo ISP-level domain blocking, directly compelled Indonesian-geo unreachability of unlicensed offshore crypto-exchange frontends (binance.com, bybit.com, okx.com, kucoin.com, mexc.com) under BAPPEBTI Regulation No. 8/2021 Article 5 (CPFAK licensing requirement), producing an L4 frontend observed_change (attribution=direct) with cascading IDR on/off-ramp severance at the named offshore-CEX cohort (offramp_cex attribution=plausible because the rail severance is downstream of the frontend block rather than a direct banking-prohibition directive). The row does not claim L0 network-level connectivity measurement (no OONI / Censored Planet slice captured this session; per Kazakhstan honesty rule l0_network is `not_measured`), nor on-chain asset freeze, nor banking-rail prohibition on Indonesian banks." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://bappebti.go.id/
- citation[1]: `supporting_journalism` replayable=`True` https://inet.detik.com/law-and-policy/d-6685046/ratusan-exchanger-kripto-nakal-diblokir-kominfo
- citation[2]: `supporting_journalism` replayable=`True` https://kumparan.com/kumparanbisnis/bappebti-gandeng-kominfo-blokir-platform-kripto-luar-negeri-239TA5gFYDn

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
  "queue_id": 109,
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
  "queue_id": 109,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/indonesia-bappebti-illegal-exchange-block-2023.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
