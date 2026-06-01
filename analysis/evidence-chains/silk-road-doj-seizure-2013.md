# Evidence chain — `silk-road-doj-seizure-2013`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `038e378` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2013-10-02 DOJ/FBI Silk Road takedown produced an immediate L4
> frontend seizure of the clearnet domain silkroadmarket.org and the
> silkroad6ownowfk.onion hidden service; the row claims only this single-
> layer marketplace-domain-seizure observation and not transaction-level
> on-chain forfeiture coding."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2013-10-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://www.justice.gov/usao/nys/pressreleases/October13/SilkRoadSeizurePR.php>
  - Wayback: <https://web.archive.org/web/20140123062431/http://www.justice.gov/usao/nys/pressreleases/October13/SilkRoadSeizurePR.php>
  - body_hash: `sha256:15991a51631d63b80e58e271b4ea3c0457d1f3fc073ef38344b7c5c154e5ea61`
  - body_path: `sources/http_captures/silk-road-doj-seizure-2013/wayback_doj_press_snapshot/web.archive.org__web-20131005034400-http-www.justice.gov-usao-nys-pressreleases-October13-SilkRoadSeizurePR.php__8bd95fcf2e.html`
  > Wayback-replayable capture of the original 2013 SDNY press release
> "Manhattan U.S. Attorney Announces Seizure Of Additional $28 Million
> Worth Of Bitcoins Belonging To Ross William Ulbricht, Alleged Owner
> And Operator Of 'Silk Road' Website." Documents the broader DOJ/FBI
> action against Silk Road including the 2013-10-02 site/server seizure
> and the follow-on 2013-10-25 supplemental bitcoin seizure. Original
> justice.gov host now redirects to a modern URL; the Wayback memento
> from 2014-01-23 is used as the admission anchor.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-seizure-additional-28-million-worth-bitcoins-belonging>
  - body_hash: `sha256:dfb6515605619b7582aa3a4964ad88dc2c9eefc322224c73004e641e8e17c104`
  - body_path: `sources/http_captures/silk-road-doj-seizure-2013/primary/www.justice.gov__usao-sdny-pr-manhattan-us-attorney-announces-seizure-additional-28-million-worth-bitcoins-belonging__53580512e8.html`
  > Current canonical justice.gov URL for the same press release. Live
> capture (2026-05-16) returned a 3,062-byte AkamaiGHost bot-block stub
> rather than the press-release body; retained as contextual_unarchived
> pointer to the canonical URL. The Wayback memento above carries the
> evidentiary content.

## 2. Target

- **Kind**: `domain`
- **Enumeration**: `subset`
- **Actor name**: Silk Road
- **Chains**: `bitcoin`
- **Canonical domains**: `silkroadmarket.org`, `silkroad6ownowfk.onion`

> Silk Road marketplace as a Tor hidden service plus its clearnet domain.
> canonical_domains lists silkroadmarket.org (clearnet) and the v2
> silkroad6ownowfk.onion address as the public surface that was replaced by
> the FBI "This Hidden Site Has Been Seized" banner. No on-chain BTC
> addresses are enumerated at this event level; ~26,000 BTC from the site
> plus ~144,000 BTC from Ross Ulbricht's wallet were seized in parallel
> civil/criminal forfeiture actions documented under SDNY case 13 MAG 2328.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `tor_marketplace_and_clearnet_domain_seized_by_fbi`

**Timestamp**: `2013-10-02 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <http://www.justice.gov/usao/nys/pressreleases/October13/SilkRoadSeizurePR.php>
  - Wayback: <https://web.archive.org/web/20140123062431/http://www.justice.gov/usao/nys/pressreleases/October13/SilkRoadSeizurePR.php>
  - body_hash: `sha256:15991a51631d63b80e58e271b4ea3c0457d1f3fc073ef38344b7c5c154e5ea61`
  - body_path: `sources/http_captures/silk-road-doj-seizure-2013/wayback_doj_press_snapshot/web.archive.org__web-20131005034400-http-www.justice.gov-usao-nys-pressreleases-October13-SilkRoadSeizurePR.php__8bd95fcf2e.html`
  > SDNY press release names the seizure of the Silk Road website and
> related server infrastructure in coordination with the FBI; the
> seizure operation and the post-takedown FBI banner replacement of
> silkroadmarket.org are documented in the contemporaneous record.
- **`semi_primary_wayback`**
  - URL: <http://silkroadmarket.org/>
  - Wayback: <https://web.archive.org/web/20131018043042/http://silkroadmarket.org/>
  - body_hash: `sha256:52dbf3406dac80addb1f9b9d3235a7307cac655d05b5d1911c8db350ae4ecdb6`
  - body_path: `sources/http_captures/silk-road-doj-seizure-2013/wayback_seizure_banner/web.archive.org__web-20131003130000-http-silkroadmarket.org__dc22e516cd.html`
  > Wayback snapshot of silkroadmarket.org dated 2013-10-18 (~16 days
> after the takedown). The marketplace surface is gone; the domain
> serves a generic landing/parking page instead of the Apache+PHP
> marketplace shown in earlier mementos. Corroborates the L4 seizure
> observation. The contemporaneous FBI "This Hidden Site Has Been
> Seized" banner that briefly replaced the page is documented in the
> DOJ primary source above; this snapshot is the closest replayable
> post-takedown state on the public web for the clearnet domain.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`alphabay-hansa-doj-2017`](./alphabay-hansa-doj-2017.md)
- [`hydra-doj-2022`](./hydra-doj-2022.md)
- [`bitzlato-doj-2023`](./bitzlato-doj-2023.md)
- [`btc-e-doj-2017`](./btc-e-doj-2017.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `038e378`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

