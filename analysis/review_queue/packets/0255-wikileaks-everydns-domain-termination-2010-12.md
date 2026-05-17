# v0.3 Review Packet: `wikileaks-everydns-domain-termination-2010-12`

This packet is machine-prepared. It does not constitute human audit, primary-source verification, or release approval.

## Queue

| Field | Value |
| --- | --- |
| queue_id | `255` |
| status | `needs_recheck` |
| priority | `90` |
| bucket | `legacy_draft_promotion_review` |
| next_action | `human_promote_or_defer` |
| reason | Legacy YAML row requires v0.3 primary-source re-extraction before primary_source_verified can be true. |

## Event

| Field | Value |
| --- | --- |
| event_id | `wikileaks-everydns-domain-termination-2010-12` |
| yaml_status | `draft` |
| internal_status | `candidate` |
| verification_state | `legacy_draft_requires_reextraction` |
| origin | `agent_draft` |
| primary_source_verified | `False` |
| requires_v0_3_reextraction | `True` |
| trigger_type | `corporate_policy_change` |
| actor | `EVERYDNS_OPERATOR` |
| event_date | `2010-12-02` |
| source_file | `/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-everydns-domain-termination-2010-12.yaml` |
| target_kind | `entity` |
| target_actor | `WikiLeaks (wikileaks.org domain)` |

## Machine Prescreen

| Check | Count / Value |
| --- | ---: |
| trigger citations | 4 |
| replayable trigger anchors | 4 |
| coverage rows | 6 |
| observations | 1 |
| observation sources | 3 |
| primary observation sources | 1 |
| replayable observation sources | 3 |
| primary replayable observation sources | 1 |

Machine blockers: `none_detected`
Machine notes: `none`

## Scoped Claim

EveryDNS terminated authoritative DNS service for wikileaks.org at ~22:00 EST 2010-12-02 under its TOS clause prohibiting service use that interferes with other members', citing DDoS traffic against the wikileaks.org records; the termination produced worldwide DNS unreachability of wikileaks.org until the relocation to wikileaks.ch the following day. The L4-frontend layer carries the load-bearing direct-attribution observation; this is the foundational pre-crypto DNS-layer corporate-intermediary censorship precedent in the corpus. 

## Trigger Citations

- citation[0]: `primary_corporate` replayable=`True` http://everydns.com/
- citation[1]: `supporting_journalism` replayable=`True` https://www.theregister.com/2010/12/03/wikileaks_loses_dns/
- citation[2]: `supporting_journalism` replayable=`True` https://thenextweb.com/news/wikileaks-is-reportedly-down-worldwide-as-dns-services-pulled
- citation[3]: `supporting_journalism` replayable=`True` https://thenextweb.com/media/2010/12/03/wikileaks-resolves-dns-moves-to-switzerland/

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
  "queue_id": 255,
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
  "queue_id": 255,
  "reason": "Primary-source re-extraction is incomplete or evidence is insufficient."
}
```

## Queue Payload

```json
{
  "pipeline": "legacy_yaml_bootstrap",
  "source_file": "/Users/xyan0559/project/chain-censorship-measurement/censorship-event-database/events/wikileaks-everydns-domain-termination-2010-12.yaml",
  "verification_state": "legacy_draft_requires_reextraction"
}
```
