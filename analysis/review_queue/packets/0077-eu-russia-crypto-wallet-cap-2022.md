# v0.3 Review Packet: `eu-russia-crypto-wallet-cap-2022`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `77` |
| status | `needs_recheck` |
| priority | `70` |
| bucket | `legacy_admitted_primary_source_recheck` |
| next_action | `human_primary_source_recheck` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `eu-russia-crypto-wallet-cap-2022` |
| yaml_status | `admitted` |
| internal_status | `verified` |
| verification_state | `legacy_admitted_pending_v0_3_primary_source` |
| origin | `human_reviewed` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `non_us_sanctions` |
| actor | `EU_Council` |
| event_date | `2022-04-08` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-russia-crypto-wallet-cap-2022.yaml` |
| target_kind | `entity` |
| target_actor | `Russian nationals / residents above EUR 10,000 crypto threshold (EU CASP customers)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 2 |
| primary observation sources | 2 |
| replayable observation sources | 2 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"EU Council Regulation 2022/576 of 2022-04-08 (fifth sanctions package) inserted Article 5b into Regulation 833/2014, prohibiting EU operators from providing crypto-asset wallets, accounts, or custody services to Russian nationals / residents / Russian-established entities above an EUR 10,000 per-person threshold. EU-registered CASPs (Bitstamp, Kraken-EU, Coinbase-EU, Binance EU entities) implemented the cap within days. The offramp_cex layer carries the load-bearing direct-attribution observation; L4 frontend reactions are consistent with the cascade but require a Wayback-capture pass before they may anchor a separate observed_change row. The cap was superseded 2022-10-06 by the 8th- package full ban (Regulation 2022/1904)." 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0576
- citation[1]: `primary_legal` replayable=`True` https://www.consilium.europa.eu/en/press/press-releases/2022/04/08/eu-adopts-fifth-round-of-sanctions-against-russia-over-its-military-aggression-against-ukraine/

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
  "queue_id": 77,
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
  "queue_id": 77,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/eu-russia-crypto-wallet-cap-2022.yaml",
  "verification_state": "legacy_admitted_pending_v0_3_primary_source"
}
```
