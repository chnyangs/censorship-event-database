# Evidence chain — `netherlands-dnb-binance-warning-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b6c6fae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DNB's 2021-08-18 warning and subsequent 2022 fine establish an official
> Netherlands regulatory-enforcement action against Binance for offering
> crypto exchange and custodian-wallet services without the legally required
> DNB registration. The retained observation is limited to that CEX/off-ramp
> regulatory service surface; it does not claim ISP blocking, frontend
> unavailability, app-store removal, on-chain asset action, fiat-rail shutdown,
> or the later 2023 Binance Netherlands market exit."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `NL_DNB`
- **Timestamp**: `2021-08-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.dnb.nl/en/general-news/news-2021/dnb-warns-against-binance/?rel=outbound>
  - body_hash: `sha256:3e0b848fbd2cc8f85bcd564322f9aab46623b538844984630e8dfe9e18c5d7af`
  - body_path: `sources/http_captures/netherlands-dnb-binance-warning-2021/primary/www.dnb.nl__en-general-news-news-2021-dnb-warns-against-binance__0309d4ff6a.html`
  > DNB warning page published 2021-08-18. The page states that Binance
> was providing crypto services in the Netherlands without the required
> DNB registration under the Wwft and identifies the affected services
> as exchange between virtual and fiat currencies and custodian wallets.
> Captured and pinned with body_hash/body_path during the 2026-06-01
> quality-loop repair.
- **`primary_legal`**
  - URL: <https://www.dnb.nl/algemeen-nieuws/nieuwsbericht-2022/boete-voor-binance-holdings-ltd-vanwege-het-zonder-de-wettelijk-vereiste-registratie-aanbieden-van-cryptodiensten/>
  - body_hash: `sha256:08203adbf0008a92f2a43d9c4a2c24c8d4a9bb60b25a2d19d5427a21a5a1b37e`
  - body_path: `sources/http_captures/netherlands-dnb-binance-warning-2021/primary/www.dnb.nl__algemeen-nieuws-nieuwsbericht-2022-boete-voor-binance-holdings-ltd-vanwege-het-zonder-de-wettelijk-vereiste-registratie-aanbieden-van-cryptodiensten__1c9531968d.html`
  > DNB enforcement page announcing the EUR 3.325 million administrative
> fine imposed on 2022-04-25 and made irrevocable after Binance withdrew
> its objection on 2022-07-27. The page reiterates that Binance offered
> crypto services in the Netherlands without the legally required DNB
> registration and links the fine to the earlier 2021-08-18 public
> warning. Captured and pinned with body_hash/body_path.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Ltd. (NL cohort)
- **Canonical domains**: `binance.com`

> Binance Holdings Ltd. and the Binance operators providing crypto services
> to Netherlands residents through binance.com without DNB registration. The
> DNB warning covers Binance Holdings Limited as owner of the intellectual
> property rights and the Binance operator entities serving the Netherlands.
> Target is coded as the Binance-Netherlands customer cohort, not a complete
> legal-entity tree or address set.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `dnb_warning_and_fine_for_binance_unregistered_crypto_services`

**Timestamp**: `2021-08-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.dnb.nl/en/general-news/news-2021/dnb-warns-against-binance/?rel=outbound>
  - body_hash: `sha256:3e0b848fbd2cc8f85bcd564322f9aab46623b538844984630e8dfe9e18c5d7af`
  - body_path: `sources/http_captures/netherlands-dnb-binance-warning-2021/primary/www.dnb.nl__en-general-news-news-2021-dnb-warns-against-binance__0309d4ff6a.html`
  > DNB 2021-08-18 warning names Binance and states that Binance was
> providing Netherlands crypto services without required legal
> registration, including exchange and custody services. Attribution is
> direct because the legal source itself names the target and the
> unregistered service surface.
- **`primary_legal`**
  - URL: <https://www.dnb.nl/algemeen-nieuws/nieuwsbericht-2022/boete-voor-binance-holdings-ltd-vanwege-het-zonder-de-wettelijk-vereiste-registratie-aanbieden-van-cryptodiensten/>
  - body_hash: `sha256:08203adbf0008a92f2a43d9c4a2c24c8d4a9bb60b25a2d19d5427a21a5a1b37e`
  - body_path: `sources/http_captures/netherlands-dnb-binance-warning-2021/primary/www.dnb.nl__algemeen-nieuws-nieuwsbericht-2022-boete-voor-binance-holdings-ltd-vanwege-het-zonder-de-wettelijk-vereiste-registratie-aanbieden-van-cryptodiensten__1c9531968d.html`
  > DNB 2022 enforcement page records the EUR 3.325 million fine,
> reiterates that offering crypto services in the Netherlands without
> DNB registration is prohibited, and states that the fine became
> irrevocable after Binance withdrew its objection on 2022-07-27.
> Retained as official corroboration and finality evidence for the
> regulatory-enforcement observation.
- **`primary_legal`**
  - URL: <https://www.dnb.nl/media/0jxfaxck/besluit-tot-het-opleggen-van-een-bestuurlijke-boete-aan-binance-gelakte-versie-pdf.pdf>
  - body_hash: `sha256:89e39ced6f6f0b910bc13684670b767e6567951228e67420a20e2d90b2714543`
  - body_path: `sources/http_captures/netherlands-dnb-binance-warning-2021/primary/www.dnb.nl__media-0jxfaxck-besluit-tot-het-opleggen-van-een-bestuurlijke-boete-aan-binance-gelakte-versie-pdf.pdf__e1747784aa.bin`
  > DNB's redacted administrative-fine decision PDF, captured as a binary
> artifact and pinned by hash. The HTML warning and fine pages remain
> the text-greppable load-bearing anchors; the PDF is retained as the
> official decision artifact.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)
- [`binance-netherlands-exit-2023-07`](./binance-netherlands-exit-2023-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b6c6fae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

