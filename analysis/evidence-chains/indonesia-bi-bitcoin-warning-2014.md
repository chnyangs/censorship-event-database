# Evidence chain — `indonesia-bi-bitcoin-warning-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `698540a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Bank Indonesia's 2014-02-06 Siaran Pers No. 16/6/Dkom stated the
> class-level administrative position that Bitcoin and other virtual
> currencies are not legal tender in Indonesia under Law No. 7 of
> 2011 on Currency, are not regulated by Bank Indonesia, and are used
> at the user's own risk. The advisory did not direct ISP-level
> blocking, banking-rail prohibition, or exchange-side action; the
> cascade surface is class-level on Indonesian residents/businesses,
> and no exchange-side Indonesia-resident cutoff is documented in
> the public record within the 90-day post-release window, so the
> event admits as a historical-baseline null_event / null_case with
> an observed_no_change row at offramp_cex.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `ID_BI`
- **Timestamp**: `2014-02-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_160614.aspx>
  - body_hash: `sha256:05873b354ce37efb8320aca28a82c99f4a2ddabf1b3107ca25c8d99714520571`
  - body_path: `sources/http_captures/indonesia-bi-bitcoin-warning-2014/primary/www.bi.go.id__id-publikasi-ruang-media-news-release-Pages-sp_160614.aspx__273672b3e5.html`
  > Bank Indonesia (BI) Siaran Pers (press release) No. 16/6/Dkom
> dated 2014-02-06, titled "Pernyataan Bank Indonesia Terkait
> Bitcoin dan Virtual Currency Lainnya" (Bank Indonesia Statement
> Regarding Bitcoin and Other Virtual Currencies). Core position
> articulated by BI: (1) Bitcoin and other virtual currencies are
> not currency and not a lawful payment instrument in Indonesia
> under Law No. 7 of 2011 on Currency (Undang-Undang Mata Uang),
> which establishes the Rupiah as the sole legal medium of
> payment in the Republic; (2) Bitcoin and other virtual
> currencies are not regulated by Bank Indonesia; (3) all risks
> attaching to ownership and use of Bitcoin and other virtual
> currencies are borne by the owner/user (citizens use at their
> own risk). The statement is an administrative warning /
> advisory under BI's monetary-authority remit; it does not
> order ISP-level blocking, banking-rail prohibition, or
> exchange-side action. The bi.go.id URL path is the canonical
> publication anchor; specific Wayback snapshot timestamp and
> body_hash require re-pinning in human audit before this
> citation may serve as an admission anchor.
- **`semi_primary_wayback`**
  - URL: <https://en.antaranews.com/news/168747/bitcoin-is-not-lawfully-accepted-payment-instrument-in-indonesia-bi>
  - Wayback: <https://web.archive.org/web/20210225073817/https://en.antaranews.com/news/168747/bitcoin-is-not-lawfully-accepted-payment-instrument-in-indonesia-bi>
  - body_hash: `sha256:4c49217f2b6cc408379ad151fe6e6f05f9b1317e957d512a5941684fbe170f3b`
  - body_path: `sources/http_captures/indonesia-bi-bitcoin-warning-2014/primary/web.archive.org__web-20210225073817-https-en.antaranews.com-news-168747-bitcoin-is-not-lawfully-accepted-payment-instrument-in-indonesia-bi__a7b45fe427.html`
  > ANTARA News (Indonesian state news agency) English-language
> report on the BI position that Bitcoin is not a lawfully
> accepted payment instrument in Indonesia. Used as contextual
> English-language translation anchor for the bi.go.id press
> release. Specific Wayback snapshot timestamp requires re-pinning
> in human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Indonesia-resident bitcoin/VC users
- **Chains**: `bitcoin`

> Target is the class of Indonesian residents and Indonesian
> businesses transacting in or contemplating use of Bitcoin and
> other virtual currencies as a payment instrument. The BI
> statement does not enumerate specific exchanges, specific
> counterparties, or specific domains; it states a class-level
> administrative position that Bitcoin/VCs are not legal tender,
> not regulated by BI, and used at the user's own risk. No
> specific exchange is named, so canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_measured_exchange_side_cutoff_of_indonesia_residents`

**Window**: `2014-02-06 00:00:00+00:00` → `2014-05-07 00:00:00+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_160614.aspx>
  - body_hash: `sha256:05873b354ce37efb8320aca28a82c99f4a2ddabf1b3107ca25c8d99714520571`
  - body_path: `sources/http_captures/indonesia-bi-bitcoin-warning-2014/primary/www.bi.go.id__id-publikasi-ruang-media-news-release-Pages-sp_160614.aspx__273672b3e5.html`
  > BI press release No. 16/6/Dkom is the administrative
> instrument. It states the class-level position that
> Bitcoin/VCs are not legal tender, are not regulated by BI,
> and that risk is borne by the user, but it does not name
> any specific exchange as having implemented an Indonesia-
> resident cutoff in response. The observation_kind=
> observed_no_change row records that the cascade surface at
> offramp_cex is class-level (Indonesian residents as a class)
> rather than exchange-specific in the available public record.
> attribution=none per schema convention for observed_no_change
> rows. Live bi.go.id capture 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`indonesia-bappebti-illegal-exchange-block-2023`](./indonesia-bappebti-illegal-exchange-block-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `698540a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

