# Evidence chain — `kenya-cbk-virtual-currency-circular-2015-12`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `0785824` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:44:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Central Bank of Kenya Banking Circular No. 14 of 2015 (2015-12-18) directed regulated
> financial institutions not to open accounts for persons dealing in virtual currencies,
> severing banking rails for Kenya's crypto ecosystem; impact captured at class level at the
> offramp_cex layer."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KE_CBK`
- **Timestamp**: `2015-12-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20151218000000id_/https://www.centralbank.go.ke/uploads/banking_circulars/2075994161_Banking%20Circular%20No%2014%20of%202015%20-%20Virtual%20Currencies%20-%20Bitcoin.pdf>
  - Wayback: <https://web.archive.org/web/20180404165057id_/https://www.centralbank.go.ke/uploads/banking_circulars/2075994161_Banking%20Circular%20No%2014%20of%202015%20-%20Virtual%20Currencies%20-%20Bitcoin.pdf>
  - body_hash: `sha256:e46c749d0c6038c889b613db62b8a3f2df7e0ffde3d80ca2eb081b4ebc3298a4`
  - body_path: `sources/http_captures/kenya-cbk-virtual-currency-circular-2015-12/primary/web.archive.org__web-20151218000000id_-https-www.centralbank.go.ke-uploads-banking_circulars-2075994161_Banking-20Circular-20No-2014-20of-202015-20--20Virtual-20Currenc__10a852500d.bin`
  > Central Bank of Kenya Banking Circular No. 14 of 2015 (PDF, document creation
> date 2015-12-18) to all chief executives of commercial banks, mortgage finance
> companies and microfinance banks: directs financial institutions NOT to open
> accounts for any person dealing in virtual currencies (Bitcoin) and warns of
> remedial action for non-compliance. This debanking directive — distinct from the
> same-day soft public notice — is the load-bearing censorship action (codebook §9).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Kenyan crypto users / dealers served by regulated banks (class)

> Kenyan banks / MFIs / mortgage-finance companies directed not to service any person
> dealing in virtual currencies. Affected the domestic crypto banking-rail ecosystem at
> class level; no specific operator named in the circular.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `bank_account_opening_for_virtual_currency_dealers_prohibited`

**Timestamp**: `2015-12-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20151218000000id_/https://www.centralbank.go.ke/uploads/banking_circulars/2075994161_Banking%20Circular%20No%2014%20of%202015%20-%20Virtual%20Currencies%20-%20Bitcoin.pdf>
  - body_hash: `sha256:e46c749d0c6038c889b613db62b8a3f2df7e0ffde3d80ca2eb081b4ebc3298a4`
  - body_path: `sources/http_captures/kenya-cbk-virtual-currency-circular-2015-12/primary/web.archive.org__web-20151218000000id_-https-www.centralbank.go.ke-uploads-banking_circulars-2075994161_Banking-20Circular-20No-2014-20of-202015-20--20Virtual-20Currenc__10a852500d.bin`
  > attribution=direct (codebook §1.1): the CBK circular is the regulatory
> instrument itself and explicitly mandates the banking cut-off (no accounts for
> virtual-currency dealers), mirroring the nigeria-cbn-crypto-ban-2021 precedent.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `0785824`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

