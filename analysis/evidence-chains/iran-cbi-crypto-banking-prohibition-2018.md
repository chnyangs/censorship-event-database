# Evidence chain — `iran-cbi-crypto-banking-prohibition-2018`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `96a9483` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `IR_CENTRAL_BANK`
- **Timestamp**: `2018-04-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://maint.loc.gov/law/help/cryptocurrency/iran.php>
  - Wayback: <https://web.archive.org/web/2018/https://maint.loc.gov/law/help/cryptocurrency/iran.php>
  > Library of Congress Law Library — "Regulation of Cryptocurrency: Iran".
> Reports that the Central Bank of Iran (CBI) announced on 2018-04-22 a
> prohibition on Iranian financial institutions (banks, credit institutions,
> currency exchanges) from handling cryptocurrencies. Per the CBI statement,
> the underlying decision was made 2017-12-30 by Iran's High Council on
> Anti-Money Laundering, then formalized and published 2018-04-22. Rationale:
> AML / CFT alignment with FATF action plan. DRYRUN: wayback anchor stub
> pending body_hash + body_path capture in a future audit pass.
- **`supporting_journalism`**
  - URL: <https://www.ccn.com/iran-central-bank-bans-banks-from-cryptocurrency-dealings/>
  - Wayback: <https://web.archive.org/web/2018/https://www.ccn.com/iran-central-bank-bans-banks-from-cryptocurrency-dealings/>
  > CCN coverage of the 2018-04-22 CBI prohibition naming banks, credit
> institutions, and currency exchanges as in-scope. DRYRUN: wayback stub.
- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/Cryptocurrency_in_Iran>
  - Wayback: <https://web.archive.org/web/2018/https://en.wikipedia.org/wiki/Cryptocurrency_in_Iran>
  > Wikipedia "Cryptocurrency in Iran" — secondary aggregate confirming the
> 2018-04-22 CBI prohibition and the December 2017 origin decision.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Iranian banks and credit institutions (class)

> Iranian banks, credit institutions, and currency exchanges as a regulated
> class — not an enumerated entity list. The CBI prohibition operates at the
> population of CBI-regulated financial institutions; individual exchange or
> bank names are not enumerated in the order itself. Class-level subset coded
> per codebook §7.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `rial_banking_channel_severed_industry_wide`

**Timestamp**: `2018-04-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/law/help/cryptocurrency/iran.php>
  - Wayback: <https://web.archive.org/web/20180729055635/https://www.loc.gov/law/help/cryptocurrency/iran.php>
  - body_hash: `sha256:8189e301ae83d082efbed89a8e4ea96f9cd465373e11e446855f98a30396f970`
  - body_path: `sources/http_captures/iran-cbi-crypto-banking-prohibition-2018/primary/web.archive.org__web-20180729055635-https-www.loc.gov-law-help-cryptocurrency-iran.php__1b62e6d7e6.html`
  > Library of Congress Law Library — "Regulation of Cryptocurrency: Iran"
> summarizes the CBI 2018-04-22 prohibition mandating Iranian banks,
> credit institutions, and currency exchanges cease handling
> cryptocurrencies. attribution=direct because the CBI order itself
> names the regulated-institution class as the target and the regulatory
> mandate as the cause; the actor publicly references the action and
> the trigger names the target population (codebook §1, §1.5 boundary
> for nation-state administrative orders). DRYRUN: wayback stub
> pending body_hash + body_path capture.
- **`semi_primary_wayback`**
  - URL: <https://www.ccn.com/iran-central-bank-bans-banks-from-cryptocurrency-dealings/>
  - Wayback: <https://web.archive.org/web/20180423124611/https://www.ccn.com/iran-central-bank-bans-banks-from-cryptocurrency-dealings/>
  - body_hash: `sha256:95ed3ebf5ac056dc8a0dd03d1a22f8ff8157567c99558474eac424fa86e2381b`
  - body_path: `sources/http_captures/iran-cbi-crypto-banking-prohibition-2018/primary/web.archive.org__web-20180423124611-https-www.ccn.com-iran-central-bank-bans-banks-from-cryptocurrency-dealings__5b9793f8e5.html`
  > CCN contemporaneous reporting corroborates the 2018-04-22 CBI
> prohibition and identifies banks, credit institutions, and currency
> exchanges as the named scope. DRYRUN: wayback stub.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Iranian exchange / wallet frontends not bracketed for this event. The

## 7. Related events

- [`iran-ransomware-ofac-2018`](./iran-ransomware-ofac-2018.md)
- [`irgc-ransomware-ofac-2022`](./irgc-ransomware-ofac-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `96a9483`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

