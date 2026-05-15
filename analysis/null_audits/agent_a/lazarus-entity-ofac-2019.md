# Null-case audit · lazarus-entity-ofac-2019 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Entity-level designation with no on-chain addresses on the RA page makes this a structurally weak null case; the trigger is well anchored, but the off-ramp CEX `measured` coding rests on the trigger page + scope_descriptor only, and there is no concrete address cohort to look for, which makes the absence search less falsifiable.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2019-09-13T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20190913 with body_hash + body_path; Treasury press release sm774 with note only). Solid trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window); all others `not_applicable`. The actor is three entity-level designations (Lazarus Group, Bluenoroff, Andariel) with no on-chain addresses on the RA page.
- is the null-case claim properly bounded? The `scoped_claim` text says only "first state-sponsored-cyber-group OFAC action; historical anchor for the DPRK-laundering event thread" — appropriately modest, no over-reach. The `analysis_notes` properly note that addresses surface in downstream events.

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA) + `scope_descriptor` (providers, time_window, addresses_cohort=`lazarus_entity_designation` — which is an entity label, not an address set).
  - verdict: concerns — the absence search has no address cohort to anchor against, since the RA page lists no digital-currency addresses for these entities. The "no public CEX statement" claim therefore reduces to "no exchange mentioned Lazarus/Bluenoroff/Andariel by name in 14 days" which is plausible but not artifact-anchored.

## Coverage status honesty
- `offramp_cex`: `measured` — concerning. Without any on-chain address cohort, the "exchange policy statement" denominator is even weaker than for the address-bearing null cases. `partially_measured` might be more honest. Acceptable only under the "public-disclosure entity-name null" reading.
- `l1_consensus`: `not_applicable` — defensible (pre-Merge by 1097 days noted in YAML).
- All other layers `not_applicable` — defensible for entity-only designation with no addresses, domains, or canonical web presence.

## Issues / concerns
- The address cohort label `lazarus_entity_designation` is essentially the entity name, not an enumerated address set; this is structurally weak. The pre-audit flagged this as "needs human attention" for exactly this reason.
- Treasury press-release citation has no body_hash + body_path.
- No aggregator query artifact (e.g. a captured search-results page for "Lazarus Group exchange policy 2019-09-13") is pinned.

## Recommendation for human reviewer
Human should consider whether an entity-only designation with zero on-chain addresses can defensibly carry an `offramp_cex: measured` row. Options: (a) downgrade to `partially_measured` and re-cast the observation as an entity-name-mention null; (b) keep `measured` and tighten the `analysis_notes` to explicitly say "no address cohort exists at this event; CEX-statement absence is entity-name-only"; (c) downgrade the observation to a `coverage_gap` row given the structural difficulty. Either way, this event should not be used as a narrative spotlight.
