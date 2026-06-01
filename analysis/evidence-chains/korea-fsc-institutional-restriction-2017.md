# Evidence chain — `korea-fsc-institutional-restriction-2017`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `cba4eca` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The KR FSC 2017-12-13 joint government emergency measure mandated
> real-name verified bank accounts at Korean crypto exchanges, banned
> anonymous virtual accounts, barred minors and foreign nationals from
> opening Korean exchange accounts, and prohibited regulated financial
> institutions from buying, holding, or investing in crypto-assets,
> with the banking-rail real-name mandate effective 2018-01-30 and the
> regulated Korean crypto-exchange sector (Upbit, Bithumb, Coinone,
> Korbit) complying across Q4-2017 / Q1-2018. The offramp_cex layer
> carries the load-bearing direct-attribution observation; L4 frontend
> reactions are consistent with the cascade but require a Wayback-
> capture pass before they may anchor a separate observed_change row.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `KR_FSC`
- **Timestamp**: `2017-12-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/pr010101/22173>
  - Wayback: <https://web.archive.org/web/20210627154808/https://www.fsc.go.kr/eng/pr010101/22173>
  - body_hash: `sha256:f4e8ebd1f268d3ca53fe8f17ebf9b937a5500385969a340e6340610f003f6138`
  - body_path: `sources/http_captures/korea-fsc-institutional-restriction-2017/primary/web.archive.org__web-20210627154808-https-www.fsc.go.kr-eng-pr010101-22173__76c46bcbb5.html`
  > South Korea Financial Services Commission (FSC) press release index
> (English site). Joint government emergency measure announced
> 2017-12-13 by the Office for Government Policy Coordination with
> the FSC named as the financial-sector regulator. The 2017-12-13
> package introduced two load-bearing rules for the Korean crypto
> rail: (1) real-name verified bank accounts mandatory for crypto
> exchange deposits/withdrawals (anonymous virtual accounts at
> Korean exchanges to be phased out), (2) prohibition on minors and
> foreign nationals opening Korean crypto exchange accounts, and
> (3) regulated financial institutions prohibited from buying,
> holding, or investing in crypto-assets. The follow-on FSC
> announcement 2018-01-23 set the 2018-01-30 effective date for the
> real-name banking mandate. The fsc.go.kr URL path drifts; the
> provisional Wayback anchor uses year-prefix lookup and requires
> re-pinning during human audit before this citation may serve as
> an admission anchor in its own right. Marked
> evidence_use=contextual_unarchived pending that re-pin.
- **`semi_primary_wayback`**
  - URL: <https://www.welivesecurity.com/2018/01/23/south-korea-moves-ban-anonymous-cryptocurrency-trading/>
  - Wayback: <https://web.archive.org/web/20180123164626/https://www.welivesecurity.com/2018/01/23/south-korea-moves-ban-anonymous-cryptocurrency-trading/>
  - body_hash: `sha256:02320b41a323d7ba4ff520f8c3ee976855f986de08077ad01ae31b0d588c8e63`
  - body_path: `sources/http_captures/korea-fsc-institutional-restriction-2017/primary/web.archive.org__web-20180123164626-https-www.welivesecurity.com-2018-01-23-south-korea-moves-ban-anonymous-cryptocurrency-trading__c3f8e2a8ef.html`
  > Secondary reporting of the FSC 2018-01-23 confirmation that the
> real-name mandate would take effect 2018-01-30. Used as a
> contextual anchor for the date sequence (2017-12-13 emergency
> package → 2018-01-23 FSC confirmation → 2018-01-30 effective
> date). Wayback timestamp requires re-pinning during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: KR regulated VASP + financial-institution sector (class)

> Canonical target is the KR FSC + Office for Government Policy
> Coordination joint directive, addressed to (a) Korean crypto
> exchanges operating fiat on/off-ramps (real-name verified account
> mandate, anonymous virtual account ban, minor/foreign-national
> account ban), and (b) Korean regulated financial institutions
> (prohibition on buying, holding, or investing in crypto-assets).
> Affected named exchanges in the 2017-12 / 2018-01 window include
> Upbit, Bithumb, Coinone, and Korbit; these are recorded as implicit
> second-order targets in observation scope rather than enumerated in
> canonical_domains, matching the sibling korea-fsc-ico-ban-2017 and
> china-pboc-crypto-ban-2021 convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `real_name_account_mandate_and_institutional_crypto_prohibition`

**Timestamp**: `2017-12-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/pr010101/22173>
  - Wayback: <https://web.archive.org/web/20210627154808/https://www.fsc.go.kr/eng/pr010101/22173>
  - body_hash: `sha256:f4e8ebd1f268d3ca53fe8f17ebf9b937a5500385969a340e6340610f003f6138`
  - body_path: `sources/http_captures/korea-fsc-institutional-restriction-2017/primary/web.archive.org__web-20210627154808-https-www.fsc.go.kr-eng-pr010101-22173__76c46bcbb5.html`
  > KR FSC is the named financial-sector regulator within the
> joint government emergency measure of 2017-12-13. The package
> mandates: (1) real-name verified bank accounts for Korean
> crypto exchange deposits/withdrawals (anonymous virtual
> accounts banned), (2) minors and foreign nationals barred
> from opening Korean crypto exchange accounts, (3) regulated
> financial institutions prohibited from buying, holding, or
> investing in crypto-assets. The 2018-01-23 FSC announcement
> set the 2018-01-30 effective date for the banking-rail real-
> name mandate. Direct attribution: the FSC directive itself
> mandates the behavior across the regulated Korean
> crypto-exchange sector (Upbit, Bithumb, Coinone, Korbit) and
> across the regulated-financial-institution sector.
> Provisional wayback anchor uses year-prefix lookup; specific
> snapshot timestamp requires re-pinning during human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.welivesecurity.com/2018/01/23/south-korea-moves-ban-anonymous-cryptocurrency-trading/>
  - Wayback: <https://web.archive.org/web/20180123164626/https://www.welivesecurity.com/2018/01/23/south-korea-moves-ban-anonymous-cryptocurrency-trading/>
  - body_hash: `sha256:02320b41a323d7ba4ff520f8c3ee976855f986de08077ad01ae31b0d588c8e63`
  - body_path: `sources/http_captures/korea-fsc-institutional-restriction-2017/primary/web.archive.org__web-20180123164626-https-www.welivesecurity.com-2018-01-23-south-korea-moves-ban-anonymous-cryptocurrency-trading__c3f8e2a8ef.html`
  > Secondary anchor to the FSC 2018-01-23 confirmation of the
> 2018-01-30 effective date for the real-name banking mandate.
> The 2018-01-30 effective date is treated as a coda within the
> same regulatory action rather than as a separate event.
> Wayback timestamp requires re-pinning during human audit.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Korean crypto exchange frontends (Upbit, Bithumb, Coinone, Korbit)

## 7. Related events

- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)
- [`korea-fsc-ico-ban-2017`](./korea-fsc-ico-ban-2017.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cba4eca`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

