# Evidence chain — `india-rbi-crypto-ban-2018`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f58fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "RBI Circular of 2018-04-06 severed INR banking channels for Indian crypto exchanges
> effective 2018-07-06 (3-month compliance window). Primary observational axis is
> offramp_cex at industry-aggregate level; multiple exchanges (Zebpay, Unocoin) shut down
> or relocated as a direct consequence."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `IN_RBI`
- **Timestamp**: `2018-04-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NOTI15465B741A10B0E45E896C62A9C83AB938F.PDF>
  - Wayback: <https://web.archive.org/web/20260421144628/https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NOTI15465B741A10B0E45E896C62A9C83AB938F.PDF>
  - body_hash: `sha256:d06e4b01c74822b7a395308abc8820016abf95f64c12dca5b4c02ed58c228fd9`
  - body_path: `sources/http_captures/india-rbi-crypto-ban-2018/rbi-circular/rbidocs.rbi.org.in__rdocs-notification-PDFs-NOTI15465B741A10B0E45E896C62A9C83AB938F.PDF__be75532d01.html`
  > Reserve Bank of India (RBI) Circular DBR.No.BP.BC.104/08.13.102/2017-18 dated
> 2018-04-06 titled "Prohibition on dealing in Virtual Currencies (VCs)". Directed
> all RBI-regulated entities (including scheduled commercial banks, cooperative banks,
> NBFCs, and payment system operators) to cease providing services to any individual
> or business dealing with or settling virtual currencies, and to exit existing
> relationships within three months. Effectively cut off Indian bank access for
> crypto exchanges from 2018-07-06 onward. The 2020-03-04 Supreme Court of India
> ruling in Internet and Mobile Association of India v. RBI is tracked below as the
> recovery anchor for the same off-ramp restriction, rather than as a separate
> admitted event in this row.
- **`primary_legal`**
  - URL: <https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=43574>
  > RBI press release accompanying the 2018-04-05 monetary-policy announcement that first mentioned the VC restrictions.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Indian crypto exchanges (class)

> Indian crypto exchanges and VC service providers as a class — not an enumerated
> entity list. Affected exchanges included Zebpay, Unocoin, CoinSecure, Koinex, WazirX,
> and the broader class of Indian crypto businesses that relied on INR bank rails. Target
> treated as entity-level at the population level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 2184h

**Event label**: `rupee_banking_channel_severed_industry_wide`

**Timestamp**: `2018-07-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NOTI15465B741A10B0E45E896C62A9C83AB938F.PDF>
  - body_hash: `sha256:d06e4b01c74822b7a395308abc8820016abf95f64c12dca5b4c02ed58c228fd9`
  - body_path: `sources/http_captures/india-rbi-crypto-ban-2018/rbi-circular/rbidocs.rbi.org.in__rdocs-notification-PDFs-NOTI15465B741A10B0E45E896C62A9C83AB938F.PDF__be75532d01.html`
  > The RBI circular text itself is the legal instrument mandating the banking
> cut-off. It gives a 3-month compliance deadline from issuance (2018-04-06), so
> effective-observation timestamp is 2018-07-06. attribution=direct because the
> circular specifies the regulatory mandate and timing.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Indian exchange frontends (zebpay.com, unocoin.com, wazirx.com, etc.) remained

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f58fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

