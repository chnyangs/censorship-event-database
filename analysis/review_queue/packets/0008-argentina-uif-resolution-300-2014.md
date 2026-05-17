# v0.3 Review Packet: `argentina-uif-resolution-300-2014`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `8` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `argentina-uif-resolution-300-2014` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `AR_UIF` |
| event_date | `2014-07-04` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/argentina-uif-resolution-300-2014.yaml` |
| target_kind | `entity` |
| target_actor | `Argentine Article-20 obliged entities (sujetos obligados)` |

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

Resolución UIF N° 300/2014, issued 2014-07-04 and effective 2014-08-01, imposed STR/KYC-style reporting obligations on Argentine Article-20 obliged entities (sujetos obligados) in respect of virtual-currency operations. The cascade surface is class-level on Argentine obliged entities; no exchange-side Argentina-resident cutoff is documented in this authoring pass, so offramp_cex carries an observation_kind=observed_no_change row with attribution=none. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` http://servicios.infoleg.gob.ar/infolegInternet/anexos/230000-234999/231930/norma.htm
- citation[1]: `supporting_journalism` replayable=`True` https://www.coindesk.com/markets/2014/07/10/argentinian-money-regulator-mandates-reporting-on-bitcoin-activity
- citation[2]: `supporting_journalism` replayable=`True` https://www.cronista.com/finanzasmercados/LA-UIF-expande-el-control-a-las-monedas-virtuales-20140711-0044.html

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
  "queue_id": 8,
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
  "queue_id": 8,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/argentina-uif-resolution-300-2014.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
