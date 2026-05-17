# v0.3 Review Packet: `bolivia-bcb-crypto-prohibition-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `29` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `bolivia-bcb-crypto-prohibition-2014` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `BO_BCB` |
| event_date | `2014-05-06` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bolivia-bcb-crypto-prohibition-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Bolivian users and intermediaries of non-state-issued currencies (class)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 2 |
| replayable trigger anchors | 2 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 1 |
| primary observation sources | 1 |
| replayable observation sources | 1 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

Banco Central de Bolivia Board Resolution No. 044/2014 (issued 2014-05-06) prohibited the use within Bolivia of any currency not issued and regulated by the Bolivian state, explicitly including bitcoin and a list of other electronic/virtual currencies, making it one of the earliest explicit nation-state-level crypto prohibitions. The prohibition is class-level and prospective; Bolivia in 2014-05 had no domestically-operated bitcoin exchange of meaningful scale and no point-in-time offramp/CEX cessation is observable. The load-bearing observation is observed_no_change at offramp_cex with a falsifiable 2014-05-06 to 2016-12-31 scope window. Historical-baseline tier; not used in main statistical denominators. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.bcb.gob.bo/webdocs/resoluciones_directorio/Resolucion_044_2014.pdf
- citation[1]: `supporting_journalism` replayable=`True` https://www.cityam.com/bitcoin-banned-bolivian-central-bank-threat-national-currency/

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
  "queue_id": 29,
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
  "queue_id": 29,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bolivia-bcb-crypto-prohibition-2014.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
