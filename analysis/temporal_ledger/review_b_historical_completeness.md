# Review B — Historical Completeness 2008-2016

Snapshot: v0.2.0-rc-dryrun · cutoff 2026-05-16. Read-only review.

## TL;DR

2008-2012 `discovery_only` is defensible. 2013-2016 `historical_baseline` has 12 candidate_found rows / 11 distinct stubs but 0 admitted; ≥4 strong events are not in the candidate ledger (Liberty Reserve, Mt. Gox, NYDFS BitLicense, PBOC China 2013). State reads as incomplete backlog; the ledger README is ambiguous about whether v0.2 will admit any.

## Q1 — In-scope per `docs/methodology.md §3`?

§3.1: identifiable legal-authority actor + machine-checkable primary source + concrete target + datable. Paper §0 adds: ≥1 independently archivable evidence surface.

| event_name | year | in_scope | ledger_status | priority | rationale |
| --- | --- | --- | --- | --- | --- |
| PayPal blocks Bitcoin Foundation account | 2010 | N | not_found | skip | Corporate AUP, not regulator; no archivable crypto-layer reaction. |
| Silk Road 1.0 operation begins | 2011 | N | not_found | skip | Not a censorship event — context only. |
| FinCEN FIN-2013-G001 guidance | 2013-03 | N | searched_no_candidate | skip | Class-level guidance, no concrete target; correctly screened. |
| Liberty Reserve takedown (DOJ + FinCEN §311) | 2013-05 | **Y** | **not_found** | **P0** | DOJ indictment + domain seizure (libertyreserve.com); clean S3 anchor predating BTC-e by 4 years. Caveat: centralized digital-currency precursor, not a chain — frame-fit best as methodological pre-anchor. **MISSING.** |
| SEC v. Trendon Shavers / BTCST | 2013-07 | Y (marginal) | candidate_found | P2 | Ponzi enforcement; unclear cross-layer reaction surface per ledger triage. |
| DHS seizure of Mt. Gox / Dwolla accounts | 2013-05 | **Y** | **not_found** | **P1** | DHS warrant cutting Mt. Gox USD rails; primary court filing + press. **MISSING.** |
| Silk Road DOJ marketplace seizure | 2013-10 | **Y** | candidate_found | **P0** | Domain seizure + ~144k BTC wallet forfeiture + DOJ indictment; multi-layer with primary on-chain receipts. Highest-evidence-density candidate currently tracked. |
| PBOC China "Notice on Preventing Bitcoin Risks" | 2013-12 | **Y** | **not_found** | **P0** | Direct sibling to admitted `china-pboc-crypto-ban-2021`. National central-bank action; primary government source; same-week CEX bank cutoffs (BTC China, OKCoin, Huobi). **MISSING — most defensible cross-stratum baseline omission.** |
| IRS Notice 2014-21 (crypto = property) | 2014-03 | N | searched_no_candidate | skip | Tax classification, not censorship action; correctly screened. |
| SEC v. Voorhees / SatoshiDICE | 2014-06 | Y (marginal) | candidate_found | P2 | Unregistered-securities settlement; reaction surface thin (SatoshiDICE blocked US users — possible Wayback frontend row). |
| Mt. Gox bankruptcy / DOJ proceedings | 2014-02 | **Y** | **not_found** | **P1** | JP civil rehab + US DOJ; day-level withdrawal-freeze sequence. Strong CEX-offramp anchor. **MISSING.** |
| DOJ v. Shrem / Faiella (BitInstant / BTCKing) | 2014-09 | Y | candidate_found | P2 | DOJ exchange/MSB plea; BitInstant operational reaction in press. |
| SEC v. Burnside / BTC Trading & LTC-Global | 2014-12 | Y | candidate_found | P2 | SEC virtual stock-exchange action; archived exchange state likely recoverable. |
| Powell unlicensed Bitcoin exchange | 2014-12 | Y (marginal) | candidate_found | skip | Likely baseline-only per ledger triage; small target. |
| FinCEN Ripple Labs settlement (first VC BSA penalty) | 2015-05 | Y | candidate_found | P1 | Primary FinCEN settlement; structural-anchor value as first BSA penalty against a VC exchanger. |
| NYDFS BitLicense final rule | 2015-06 | **Y** | **not_found** | **P0** | NY state regulator triggered ShapeShift / Kraken / Bitfinex / Poloniex NY-exits — clean multi-frontend L4 cascade documented in 2015-2016 press + Wayback. **MISSING — strongest L4 cascade candidate of the period.** |
| CFTC v. Coinflip / Derivabit | 2015-09 | Y | candidate_found | P2 | Concrete target, small platform. |
| CFTC v. TeraExchange | 2015-09 | Y (marginal) | candidate_found | skip | Narrow market-venue case, likely baseline-only per ledger. |
| FinCEN ISIL Bitcoin advisory | 2015 | N | not_found | skip | Advisory, no concrete target. |
| CFTC v. Bitfinex (retail commodity) | 2016-06 | Y | candidate_found | P2 | Bitfinex US-user service changes plausibly recoverable. |
| Bitfinex hack | 2016-08 | N | not_found | skip | Operator-incident, not regulator-triggered. |
| Ethereum DAO hard-fork | 2016-07 | N | not_found | skip | Community-driven; no §3.1 trigger. |
| IRS John Doe summons (Coinbase) | 2016-11 | Y | candidate_found | P2 | Court-authorized summons; promotion needs Coinbase response evidence. |

In-scope set (Y or Y-marginal): 14 events. Not-found-but-in-scope: 5 (Liberty Reserve, Mt. Gox×2, NYDFS BitLicense, PBOC China 2013).

## Q2 — Why no promotions?

Of the 11 distinct `candidate_found` stubs in 2013-2016:

- All carry `registry_status: candidate` plus a "Promotion needs X" triage note — legitimately blocked by absent replayable evidence (archived platform snapshots, wallet receipts, response artifacts).
- No event has had its per-layer §4 procedure run; no Wayback / on-chain backfill on these stubs.

Liberty Reserve, Mt. Gox, NYDFS BitLicense, PBOC China 2013 don't reach `candidate_found` because source frames are too narrow:

- `us_federal_enforcement_archives` (the only S3 frame) is `planned:` — Liberty Reserve (FinCEN §311 + DOJ) in scope but not surfaced.
- `non_us_state_archives` is also `planned:` — PBOC China 2013 cannot surface.
- NYDFS BitLicense is a US state regulator action — not OFAC (S1) / federal (S3) / corporate (S5) / cleanly S4. **The frame has no "US state regulator" slot.** Frame-design gap, not just a backlog.

## Q3 — Is `discovery_only_2008_2012` right?

**Yes, defensible.** Pre-2013 has: no concrete state/regulatory actions naming Bitcoin (first FinCEN guidance is 2013-03); no exchange enforcement with archivable cross-layer reactions; PayPal 2010 is contractual AUP, not regulator/state. Earliest in-scope §3.1 trigger is plausibly the 2013-05 Liberty Reserve + Mt. Gox/Dwolla pair. 2008-2012 is the right cutoff; 300 pending rows can remain pending without changing v0.2 shape.

## Q4 — Backlog or "no admission" decision?

The temporal ledger README is **ambiguous**:

- "rows **may** become full event YAMLs" — backlog language.
- They "stay out of 2017+ comparable denominators" — deliberate-non-admission language for the comparable corpus.
- `docs/final-collection-protocol.md` is similarly soft.

Operationally a backlog with no work scheduled (12 candidates, 0 admitted, all 11 stubs with "Promotion needs X"). README does not state (a) which candidates v0.2 will admit, (b) the US-state-regulator frame-design gap, (c) the missing-stub cluster. Most defensible v0.2 fix: add an explicit historical-baseline admission roadmap, or an explicit "v0.1 admits no 2013-2016 event" statement, to the temporal ledger README.

## Q5 — Strongest 2013-2016 candidate v0.2 should not ship without

**`china-pboc-crypto-ban-2013-12`** — PBOC "Notice on Preventing Bitcoin Risks" (2013/289).

Rationale:

1. Direct cross-temporal sibling to admitted `china-pboc-crypto-ban-2021`; admitting both lets the paper claim "2021 was the second pass; 2013 was the first" — currently impossible.
2. Same-stratum (S4) parallel to admitted India RBI 2018, Nigeria CBN 2021, Turkey CBRT 2021; closes the "where is the first PBOC?" reviewer objection.
3. Multi-layer reaction: BTC China, OKCoin, Huobi announced bank-account closures within ~10 days; CNY/BTC volume collapsed within the week. Both `offramp_cex` and `l4_frontend` recoverable from Wayback + Reuters / Coindesk.
4. Primary source: PBOC Notice 2013/289, on Wayback for a decade, widely translated.
5. Frame-fit: clean S4 candidate the non-US state frame is supposed to surface.

## Top 3 P0 events v0.2 should admit (ranked)

1. **`china-pboc-crypto-ban-2013-12`** — PBOC Notice 2013/289 (above).
2. **`silk-road-doj-seizure-2013-10`** — existing `candidate_found` stub; domain seizure + ~144k BTC forfeiture + DOJ indictment; multi-layer with highest evidence density in the period.
3. **`nydfs-bitlicense-2015-06`** — BitLicense final rule; clean L4 frontend cascade (ShapeShift / Kraken / Bitfinex / Poloniex NY-exits + frontend geofences). Closes the US-state-regulator frame-design gap.

## Verdict

2008-2016 shape is **partially defensible, with two specific holes the paper must call out**:

- **Defensible**: `discovery_only_2008_2012` and its 300 pending rows.
- **Coverage gap**: 2013-2016 has 4-5 in-scope events absent from the candidate ledger because non-US state + US federal source frames are `planned:` not ingested, plus a frame-design gap for US state regulators. Paper §0 / §3 must either admit the top-3 P0 events or carry an explicit historical-baseline scope-limitation paragraph naming Liberty Reserve, Mt. Gox, NYDFS BitLicense, PBOC China 2013 as known omissions.
- **README clarity fix**: temporal ledger README should state whether v0.2 will admit any historical-baseline candidates, and which.
