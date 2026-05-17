# v0.3 Review Packet: `bitcoinica-shutdown-2012-05`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `19` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `bitcoinica-shutdown-2012-05` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `BITCOINICA_OPERATOR` |
| event_date | `2012-05-11` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitcoinica-shutdown-2012-05.yaml` |
| target_kind | `entity` |
| target_actor | `Bitcoinica` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 7 |
| replayable trigger anchors | 7 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 5 |
| primary observation sources | 2 |
| replayable observation sources | 5 |
| primary replayable observation sources | 2 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

"On 2012-05-11, the Bitcoinica operator (Zhou Tong / Intersango / Tihan Seale) closed the bitcoinica.com leveraged-bitcoin trading platform following a second hot-wallet intrusion (~18,547 BTC / ~$87,000-$92,500) layered on top of the 2012-03 Linode hot-wallet breach (~43,000 BTC) and a parallel Mt. Gox-account compromise of $200,000+ affecting Bitcoinica's exchange-held balances. The operator-led shutdown is a comparison-class corporate-policy event at the offramp_cex cascade axis (attribution=plausible: causally consistent with the hack but not a regulator-attributed compliance action). Admission-anchor-grade promotion pending pinned archive captures." 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` https://bitcointalk.org/index.php?topic=81045.0
- citation[1]: `primary_corporate` replayable=`True` https://bitcointalk.org/index.php?topic=81045.840
- citation[2]: `supporting_journalism` replayable=`True` https://bitcoinmagazine.com/business/bitcoinica-stolen-from-again
- citation[3]: `supporting_journalism` replayable=`True` https://www.bitdefender.com/en-us/blog/hotforsecurity/exchange-site-bitcoinica-hacked-us90000-stolen
- citation[4]: `supporting_journalism` replayable=`True` https://medium.com/coinmonks/bitcoinica-40bed6569354
- citation[5]: `supporting_journalism` replayable=`True` https://crypto.bi/2012-hacks/
- citation[6]: `supporting_journalism` replayable=`True` https://bitcoinmagazine.com/business/tihan-seale-announces-bitcoinica-liquidation-1343945511

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
  "queue_id": 19,
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
  "queue_id": 19,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/bitcoinica-shutdown-2012-05.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
