# v0.3 Review Packet: `argentina-cnv-psav-registration-2024`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `7` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `argentina-cnv-psav-registration-2024` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `regulatory_enforcement` |
| actor | `AR_CNV` |
| event_date | `2024-03-25` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/argentina-cnv-psav-registration-2024.yaml` |
| target_kind | `entity` |
| target_actor | `PSAVs operating in or into Argentina (Ley 27.739 / CNV RG 994/2024)` |

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

Resolución General CNV N° 994/2024, published 2024-03-25, established the Argentine PSAV (Proveedor de Servicios de Activos Virtuales) registration regime under Ley 27.739. The cascade surface is class-level on PSAVs operating in or into Argentina; no exchange-side Argentina-resident cutoff is documented in this authoring pass, so offramp_cex carries an observation_kind=observed_no_change row with attribution=none. 

## Trigger Citations

- citation[0]: `primary_legal` replayable=`True` https://www.boletinoficial.gob.ar/detalleAviso/primera/305110/20240325
- citation[1]: `supporting_tracker` replayable=`True` https://digitalpolicyalert.org/event/18948-implemented-cnv-resolution-on-registry-of-virtual-asset-service-providers-resolution-9942024
- citation[2]: `supporting_journalism` replayable=`True` https://www.marval.com/publicacion/se-reglamenta-la-inscripcion-de-los-proveedores-de-servicios-de-activos-virtuales-15792?lang=en

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
  "queue_id": 7,
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
  "queue_id": 7,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/argentina-cnv-psav-registration-2024.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
