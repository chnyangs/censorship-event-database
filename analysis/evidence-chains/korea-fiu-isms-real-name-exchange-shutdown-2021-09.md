# Evidence chain — `korea-fiu-isms-real-name-exchange-shutdown-2021-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `f54a8ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T09:44:11Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "South Korea's 2021-09-24 FIU registration deadline (amended Specific Financial Information
> Act) made VASP operation contingent on reporting/AML review and real-name verified account
> access for KRW-market activity. Official FSC/FIU result evidence records 42 filed VASPs,
> 29 approvals, 5 deferrals and 8 withdrawals, with four KRW-market exchanges
> (Upbit/Korbit/Coinone/Bithumb). Effect carried at offramp_cex (class-level, partially measured)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `KR_FIU`
- **Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.fsc.go.kr/no010101/76312>
  - body_hash: `sha256:97238a2c90530c783d9207380a9cb926fd99007e705f982bbd51e1f1de78573f`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary-fsc-20210924/www.fsc.go.kr__no010101-76312__9a1cce464a.html`
  > FSC/FIU press release, 2021-07-28, locally captured from fsc.go.kr with a
> browser user-agent after the default capture user-agent was reset. The
> body states that the VASP reporting deadline was 2021-09-24, that VASPs
> should in principle use real-name verified deposit/withdrawal accounts to
> support customer virtual-asset trading, that temporary collection-account
> use persisted only until the Special Financial Information Act reporting
> deadline, and that users faced increased risk of temporary operators
> closing business by that deadline.
- **`primary_government`**
  - URL: <https://www.fsc.go.kr/comm/getFile?srvcId=BBSTY1&upperNo=76312&fileTy=ATTACH&fileNo=2>
  - body_hash: `sha256:cf160bd7d731442ffd829f1f43980564f262e2f38d3fc99eb9eadd906a15a9b5`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary-fsc-20210924-pdf/www.fsc.go.kr__comm-getFile__789dc2a9ba.bin`
  > Official FSC PDF attachment to the 2021-07-28 release. Rendered with
> pdftotext and verified to contain the 2021-09-24 Special Financial
> Information Act reporting deadline, real-name verified account language,
> temporary collection-account transition language, transaction-stop
> measures for disguised accounts, and warnings about operators closing
> business by the deadline.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications>
  - Wayback: <https://web.archive.org/web/20210924170155/https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications/>
  - body_hash: `sha256:a3bea46c09710a5d4288bbe4da6f74afbb1517ebb1d4441072178eee2c036b5f`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary/web.archive.org__web-20210924170155-https-www.coindesk.com-policy-2021-09-24-hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications__84cac51a04.html`
  > CoinDesk, 2021-09-24, reporting the 2021-09-24 South Korean Financial Intelligence
> Unit (FIU) registration deadline under the amended Act on Reporting and Use of Specific
> Financial Information. Virtual-asset service providers had to register with the FIU,
> secure real-name verified bank accounts and a security certification, and meet AML
> requirements to keep operating. Exchanges failing to register had to shut down (or, for
> those with certification but no bank partnership, cease Korean-won fiat trading). The
> captured article documents that only the four exchanges with bank partnerships
> (Upbit, Bithumb, Coinone, Korbit) could continue full won-settlement services, and
> ~40 exchanges faced shutdown. Wayback snapshot 20210924170155 (replayable body_hash).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: South Korean virtual-asset exchanges subject to FIU registration (class)

> The class of South Korean virtual-asset exchanges subject to the FIU registration regime.
> The official FSC/FIU result release states that 42 VASPs filed by the September deadline,
> 29 passed review (24 exchange operators and 5 custody/wallet operators), 5 were deferred
> for re-review, and 8 withdrew their filings. The official result table names the four KRW
> market exchange operators (Upbit, Korbit, Coinone, Bithumb). Unregistered/non-filing
> operators are not exhaustively enumerated here, so enumeration=subset (class-level).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `fiu_registration_deadline_forced_exchange_shutdown_and_fiat_rail_severance`

**Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.fsc.go.kr/comm/getFile?srvcId=BBSTY1&upperNo=76312&fileTy=ATTACH&fileNo=2>
  - body_hash: `sha256:cf160bd7d731442ffd829f1f43980564f262e2f38d3fc99eb9eadd906a15a9b5`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary-fsc-20210924-pdf/www.fsc.go.kr__comm-getFile__789dc2a9ba.bin`
  > Official FSC/FIU 2021-07-28 PDF. It establishes the 2021-09-24 reporting
> deadline, the real-name verified deposit/withdrawal account requirement,
> and the elevated risk that temporary operators would close business by
> the deadline. It also records transaction-stop measures for disguised
> accounts and monitoring through the deadline.
- **`primary_government`**
  - URL: <https://www.korea.kr/common/download.do?fileId=196584688&tblKey=GMN>
  - body_hash: `sha256:0a5e8e1a453d3538e7b35a430ca912a61b7ba63abd4c27be80bd5204add5c7a2`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary-fsc-result-pdf/www.korea.kr__common-download.do__03a2b61fef.bin`
  > Korea.kr government policy briefing copy of the FSC/FIU 2021-12-23 result
> PDF. Rendered with pdftotext and verified to state that 42 VASPs filed by
> September, 29 passed review (24 exchange operators and 5 custody/wallet
> operators), 5 were deferred, and 8 withdrew; withdrawing businesses had to
> terminate all operations from 2021-12-24 and support customer asset
> withdrawals. The result table names four KRW-market exchanges.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications>
  - Wayback: <https://web.archive.org/web/20210924170155/https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications/>
  - body_hash: `sha256:a3bea46c09710a5d4288bbe4da6f74afbb1517ebb1d4441072178eee2c036b5f`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary/web.archive.org__web-20210924170155-https-www.coindesk.com-policy-2021-09-24-hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications__84cac51a04.html`
  > CoinDesk 2021-09-24: at the FIU deadline, unregistered exchanges had to shut down and
> certified-but-unbanked exchanges had to cease won fiat trading; four exchanges
> (Upbit, Bithumb, Coinone, Korbit) had secured bank partnerships for full service,
> ~40 faced shutdown. Retained as same-day English-language corroboration; the
> load-bearing deadline and result facts now come from official FSC/FIU sources.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`korea-fsc-institutional-restriction-2017`](./korea-fsc-institutional-restriction-2017.md)
- [`korea-fsc-ico-ban-2017`](./korea-fsc-ico-ban-2017.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f54a8ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

