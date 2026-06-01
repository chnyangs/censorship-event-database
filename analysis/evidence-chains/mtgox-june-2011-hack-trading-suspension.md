# Evidence chain — `mtgox-june-2011-hack-trading-suspension`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b6c6fae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Mt. Gox suspended all trading globally from 2011-06-20 to
> 2011-06-26 after a 2011-06-19 user-database compromise was used to
> flood the order book with sell orders and crash the nominal BTC
> price to ~$0.01. The row claims only this single-layer offramp_cex
> operator-suspension observation, coded as attribution=plausible
> because the suspension is an operator-policy choice in response to
> a hack rather than externally compelled censorship. Discovery-only
> tier; not used in main statistical denominators."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `MTGOX_OPERATOR`
- **Timestamp**: `2011-06-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://mtgox.com/press_release_20110630.html>
  - Wayback: <https://web.archive.org/web/20110919162635/https://mtgox.com/press_release_20110630.html>
  - body_hash: `sha256:07b38074c76209cced93f984b203250f31e27b35c17f7751a0987233f1b8ccfd`
  - body_path: `sources/http_captures/mtgox-june-2011-hack-trading-suspension/v0_3_primary_repair/web.archive.org__web-20110919162635-https-mtgox.com-press_release_20110630.html__4b025a9909.html`
  > Mt. Gox official 2011-06-30 press release archived by Wayback
> at 2011-09-19. The release explains the compromised admin
> account, the 2011-06-20 sell-off, the user-database/password
> leak, Mt. Gox's responsibility for the site's security, and the
> plan to launch the new site on 2011-06-26. Used as the primary
> corporate anchor for the post-hack operator suspension/relaunch
> chronology; the body_hash is over the timestamped Wayback HTML.
- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/Mt._Gox>
  - Wayback: <https://web.archive.org/web/2011/https://en.wikipedia.org/wiki/Mt._Gox>
  > Mt. Gox Wikipedia summary documenting the 2011-06-19 incident: a
> compromised auditor / user-database credential was used to flood
> the Mt. Gox order book with sell orders that nominally drove the
> BTC price to ~$0.01, triggering an operator-initiated trading
> suspension on 2011-06-20 through 2011-06-26 while Mt. Gox rolled
> back the fraudulent trades. evidence_use=contextual_unarchived:
> no body_hash captured into sources/http_captures/ in this session.
- **`supporting_journalism`**
  - URL: <https://blockonomi.com/mt-gox-hack/>
  - Wayback: <https://web.archive.org/web/2011/https://blockonomi.com/mt-gox-hack/>
  > Blockonomi long-form retrospective on the Mt. Gox 2011-06-19 hack
> and the trader-account flood that crashed the BTC nominal price
> to ~$0.01 on Mt. Gox, prompting the operator-initiated trading
> halt and trade-rollback. evidence_use=contextual_unarchived: no
> body_hash captured into sources/http_captures/ in this session.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mt. Gox
- **Chains**: `bitcoin`
- **Canonical domains**: `mtgox.com`

> All Mt. Gox trading-platform customers globally during the 2011-06-20
> to 2011-06-26 suspension window. Mt. Gox suspended all trading after
> a compromised auditor / user-database credential was used to flood
> the order book with sell orders and drive the nominal BTC price to
> ~$0.01. No on-chain BTC address enumeration; the action is an
> operator-layer offramp trading suspension.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 24h

**Event label**: `trading_suspended_post_hack_2011_06`

**Timestamp**: `2011-06-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://mtgox.com/press_release_20110630.html>
  - Wayback: <https://web.archive.org/web/20110919162635/https://mtgox.com/press_release_20110630.html>
  - body_hash: `sha256:4b99f943253828c51a24ffeb55912dcebb0e53813e3bc06e9319f83886f4950f`
  - body_path: `sources/http_captures/mtgox-june-2011-hack-trading-suspension/primary/web.archive.org__web-20110701000000-http-mtgox.com-press_release_20110630.html__1d37e9103b.html`
  > Mt. Gox operator press release (2011-06-30) following the
> 2011-06-19/20 security breach: documents the trading suspension and
> rollback of fraudulent trades. Operator primary-corporate anchor.
> Wayback 20110919162635 pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-coinlab-civil-2013`](./mtgox-coinlab-civil-2013.md)
- [`mtgox-usd-withdrawal-suspension-2013-06`](./mtgox-usd-withdrawal-suspension-2013-06.md)
- [`mtgox-dhs-dwolla-wells-fargo-seizure-2013`](./mtgox-dhs-dwolla-wells-fargo-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b6c6fae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

