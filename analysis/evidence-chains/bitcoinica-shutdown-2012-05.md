# Evidence chain — `bitcoinica-shutdown-2012-05`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `fd81985` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2012-05-11, the Bitcoinica operator (Zhou Tong / Intersango /
> Tihan Seale) closed the bitcoinica.com leveraged-bitcoin trading
> platform following a second hot-wallet intrusion (~18,547 BTC /
> ~$87,000-$92,500) layered on top of the 2012-03 Linode hot-wallet
> breach (~43,000 BTC) and a parallel Mt. Gox-account compromise of
> $200,000+ affecting Bitcoinica's exchange-held balances. The
> operator-led shutdown is a comparison-class corporate-policy event
> at the offramp_cex cascade axis (attribution=plausible: causally
> consistent with the hack but not a regulator-attributed compliance
> action). Admission-anchor-grade promotion pending pinned archive
> captures."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `BITCOINICA_OPERATOR`
- **Timestamp**: `2012-05-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://bitcointalk.org/index.php?topic=81045.0>
  - body_hash: `sha256:80fa473578d432c6cc17587e137986a6b76cbb01412f5bd9d469678e6f2c2530`
  - body_path: `sources/http_captures/bitcoinica-shutdown-2012-05/v0_3_primary_repair/bitcointalk.org__index.php__55a567b6fd.html`
  > Bitcointalk emergency announcement thread titled "[Emergency ANN]
> Bitcoinica site is taken offline for security investigation".
> The opening Zhou Tong post on 2012-05-11 records the suspicious
> 18,547.66867623 BTC transaction, Rackspace server suspension,
> and operator investigation context. This is the first-party
> operator/community-forum anchor for the initial platform
> takedown.
- **`primary_corporate`**
  - URL: <https://bitcointalk.org/index.php?topic=81045.840>
  - body_hash: `sha256:da16c8ed0a0056ab469eaf11f79f0d1b297b02b2e2628475b13b723624aa7939`
  - body_path: `sources/http_captures/bitcoinica-shutdown-2012-05/v0_3_primary_repair/bitcointalk.org__index.php__019b83ef1f.html`
  > Later page of the same Bitcointalk emergency thread preserving
> the Bitcoinica blog post-mortem text. The captured page includes
> the operator statement that Bitcoinica would remain offline until
> a rebuilt platform could be created and that availability would
> likely be measured in months. Human audit should still compare
> this forum-preserved text with the original archived Bitcoinica
> blog page if recoverable.
- **`supporting_journalism`**
  - URL: <https://bitcoinmagazine.com/business/bitcoinica-stolen-from-again>
  - Wayback: <https://web.archive.org/web/2012/https://bitcoinmagazine.com/business/bitcoinica-stolen-from-again>
  > Bitcoin Magazine coverage of the 2012-05-11 Bitcoinica hot-wallet
> intrusion (~18,547 BTC, worth ~$87,000-$92,500 at the time) and
> the operator's decision to shutter the trading platform shortly
> after the intrusion. Provides the canonical journalism anchor
> for the date and the operator's shutdown framing.
> DRYRUN: wayback wildcard pointer in lieu of pinned-timestamp
> snapshot; evidence_use=contextual_unarchived because no
> body_hash+body_path pair has been captured into
> sources/http_captures/ in this session.
- **`supporting_journalism`**
  - URL: <https://www.bitdefender.com/en-us/blog/hotforsecurity/exchange-site-bitcoinica-hacked-us90000-stolen>
  - Wayback: <https://web.archive.org/web/2012/https://www.bitdefender.com/en-us/blog/hotforsecurity/exchange-site-bitcoinica-hacked-us90000-stolen>
  > Bitdefender HotForSecurity 2012-05 coverage ("Exchange Site
> Bitcoinica Hacked, US$90,000 Stolen") corroborating the May-2012
> intrusion magnitude (~18,500 BTC / ~$90,000) and the resulting
> platform shutdown. Independent security-press confirmation.
> evidence_use=contextual_unarchived; body_hash capture deferred.
- **`supporting_journalism`**
  - URL: <https://medium.com/coinmonks/bitcoinica-40bed6569354>
  - Wayback: <https://web.archive.org/web/2012/https://medium.com/coinmonks/bitcoinica-40bed6569354>
  > Coinmonks / Kevin Finnerty retrospective ("Bitcoinica. The Rise
> and Fall of a Pioneering Exchange") narrating the full arc:
> Zhou Tong launches Bitcoinica 2011-09, Intersango/Tihan Seale
> acquires operational control early 2012, 2012-03 Linode hot-wallet
> breach (~43,000 BTC / ~$220,000) targeting Bitcoin-flagged
> Linode customers, 2012-05-11 second intrusion (~18,547 BTC via
> compromised Rackspace-hosted email) and platform closure shortly
> after with the operator citing insolvency. evidence_use=
> contextual_unarchived; body_hash capture deferred.
- **`supporting_journalism`**
  - URL: <https://crypto.bi/2012-hacks/>
  - Wayback: <https://web.archive.org/web/2012/https://crypto.bi/2012-hacks/>
  > crypto.bi "2012 Bitcoin and Altcoin Hacks" retrospective
> recording the 2012-03 Linode hack and 2012-05-11 second
> Bitcoinica intrusion, plus the operator-led shutdown decision.
> Also notes the related Mt. Gox-account compromise impacting
> Bitcoinica's exchange balances. Secondary journalism corroboration
> for the date and the operator-shutdown framing. evidence_use=
> contextual_unarchived; body_hash capture deferred.
- **`supporting_journalism`**
  - URL: <https://bitcoinmagazine.com/business/tihan-seale-announces-bitcoinica-liquidation-1343945511>
  - Wayback: <https://web.archive.org/web/2012/https://bitcoinmagazine.com/business/tihan-seale-announces-bitcoinica-liquidation-1343945511>
  > Bitcoin Magazine 2012-08-02 follow-up ("Tihan Seale Announces
> Bitcoinica Liquidation") confirming that Intersango/Tihan Seale,
> the operational acquirer after Zhou Tong stepped back, proceeded
> to formal liquidation of Bitcoinica downstream of the 2012-05-11
> shutdown. Establishes the operator-led closure trajectory.
> evidence_use=contextual_unarchived; body_hash capture deferred.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bitcoinica

> Target is the Bitcoinica leveraged-trading platform (bitcoinica.com)
> as operated under Zhou Tong / subsequently Intersango (Tihan Seale)
> operational control. subset because the enumerated target is the
> single bitcoinica.com operator-entity and trading platform rather
> than the broader class of 2012-era leveraged-bitcoin exchanges. The
> operator-led shutdown action is jurisdictionally global (no national
> regulator named) and operates on the Bitcoinica corporate-entity
> surface.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `operator_led_shutdown_of_bitcoinica_trading_platform_after_hack`

**Timestamp**: `2012-05-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://bitcointalk.org/index.php?topic=81045.0>
  - Wayback: <https://web.archive.org/web/20130426085224/https://bitcointalk.org/index.php?topic=81045.0>
  - body_hash: `sha256:c9ca1b3ac58c319fdb8de960533eaa092ea894d3e90051144b8e5de887c43fe0`
  - body_path: `sources/http_captures/bitcoinica-shutdown-2012-05/primary/web.archive.org__web-20120601000000-https-bitcointalk.org-index.php__09f020ab4e.html`
  > Bitcointalk operator thread documenting the Bitcoinica 2012-05
> shutdown / trading suspension following the platform compromise.
> Operator-statement primary_corporate anchor. Wayback 20130426085224
> pinned.
- **`semi_primary_wayback`**
  - URL: <https://bitcoinmagazine.com/business/bitcoinica-stolen-from-again>
  - Wayback: <https://web.archive.org/web/20210413045351/https://bitcoinmagazine.com/business/bitcoinica-stolen-from-again>
  - body_hash: `sha256:eed6e31b295a126116cb49a714a5abd156f41c7a8c0583f304d600336296e217`
  - body_path: `sources/http_captures/bitcoinica-shutdown-2012-05/primary/web.archive.org__web-20120701000000-https-bitcoinmagazine.com-business-bitcoinica-stolen-from-again__d87097d3d1.html`
  > Bitcoin Magazine coverage of the Bitcoinica compromise and shutdown.
> Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-june-2011-hack-trading-suspension`](./mtgox-june-2011-hack-trading-suspension.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `fd81985`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

