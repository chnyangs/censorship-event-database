# Evidence chain — `celsius-multistate-cease-desist-earn-2021-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-09-17 New Jersey's official Celsius cease-and-desist PDF and Texas's
> same-day official notice/hearing PDF anchored a state-regulator wave against
> Celsius's Earn Rewards / Earn Interest-Bearing Account product. The event
> models a single-layer S4 state-regulator lending/off-ramp restriction, with
> New Jersey as the load-bearing official order artifact (body_hash-pinned,
> pdfinfo-confirmed) and Texas as independent corroborating primary_legal
> context. No L0/L1/L3/L4 or asset-onchain effects are claimed."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `US_NJ_BUREAU_OF_SECURITIES`
- **Timestamp**: `2021-09-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.nj.gov/oag/newsreleases21/Celsius-Order-9.17.21.pdf>
  - body_hash: `sha256:18efa19cba2ec30ccf0e54eb42702a0cdc7cf91fcd31b3d9a7c37fb7b3d6cce1`
  - body_path: `sources/http_captures/celsius-multistate-cease-desist-earn-2021-09/primary/www.nj.gov__oag-newsreleases21-Celsius-Order-9.17.21.pdf__7854d9917f.bin`
  > Official New Jersey PDF captured from nj.gov/oag on 2026-05-31
> (HTTP 200, application/pdf, 15 pages, SHA-256 pinned). `pdfinfo`
> identifies the file title as "_Celsius Cease and Desist 9.17.21.pdf",
> author GeroldC, produced by Microsoft Print To PDF, with creation and
> modification timestamps on 2021-09-17. The PDF is image/scanned and
> not text-extractable locally; the Texas Notice of Hearing (separately
> captured, text-extractable) corroborates the Celsius Earn product
> identity and the 2021-09-17 regulatory wave.
- **`primary_legal`**
  - URL: <https://www.ssb.texas.gov/sites/default/files/2021-09/20210917_FINAL_Celsius_NOH_js_signed.pdf>
  - body_hash: `sha256:076fd36529cf24c4e5b8b9668615a634d5f29be6f2015d4a3c50dc005f49074c`
  - body_path: `sources/http_captures/celsius-multistate-cease-desist-earn-2021-09/primary/www.ssb.texas.gov__sites-default-files-2021-09-20210917_FINAL_Celsius_NOH_js_signed.pdf__5db9ed62fd.bin`
  > Texas State Securities Board Notice of Hearing PDF captured from the
> official ssb.texas.gov site on 2026-05-31. `pdftotext` confirms that
> the hearing was for determining whether to enter a cease-and-desist
> order against Celsius Network entities; it identifies the Celsius Earn
> Interest-Bearing Account / Earn Rewards program as unregistered
> cryptocurrency interest-earning accounts and states that Texans and
> other investors could purchase the product through Celsius's website or
> smartphone application. This is corroborating official context, not the
> sole observed-change anchor, because it is a notice/hearing document.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Celsius Network Earn Rewards / Earn Interest-Bearing Account
- **Canonical domains**: `celsius.network`

> Celsius Network entities and the Celsius Earn Rewards / Earn
> Interest-Bearing Account product, as addressed by the captured New Jersey
> PDF and corroborated by the Texas Notice of Hearing. The broader regulatory
> wave involved New Jersey, Texas, Alabama, and Kentucky; this event pins
> New Jersey as the load-bearing official order artifact and Texas as
> independent corroborating context. Other state orders are not enumerated.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `celsius_earn_interest_accounts_ordered_to_cease_new_jersey`

**Timestamp**: `2021-09-17 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.nj.gov/oag/newsreleases21/Celsius-Order-9.17.21.pdf>
  - body_hash: `sha256:18efa19cba2ec30ccf0e54eb42702a0cdc7cf91fcd31b3d9a7c37fb7b3d6cce1`
  - body_path: `sources/http_captures/celsius-multistate-cease-desist-earn-2021-09/primary/www.nj.gov__oag-newsreleases21-Celsius-Order-9.17.21.pdf__7854d9917f.bin`
  > Official New Jersey Bureau of Securities PDF artifact for the
> Celsius cease-and-desist action (body_hash-pinned, served from
> nj.gov/oag). Attribution is direct: the legal instrument is issued
> by the regulator and the PDF title/metadata ("Celsius Cease and
> Desist 9.17.21.pdf", author GeroldC, creation 2021-09-17) confirm
> it names the Celsius entity. The NJ PDF is image/scanned and not
> text-extractable locally; the Texas Notice of Hearing (separately
> captured and text-extractable) provides corroborating official
> confirmation of the same Celsius Earn product restriction.
- **`primary_legal`**
  - URL: <https://www.ssb.texas.gov/sites/default/files/2021-09/20210917_FINAL_Celsius_NOH_js_signed.pdf>
  - body_hash: `sha256:076fd36529cf24c4e5b8b9668615a634d5f29be6f2015d4a3c50dc005f49074c`
  - body_path: `sources/http_captures/celsius-multistate-cease-desist-earn-2021-09/primary/www.ssb.texas.gov__sites-default-files-2021-09-20210917_FINAL_Celsius_NOH_js_signed.pdf__5db9ed62fd.bin`
  > Official Texas notice corroborates the same Celsius Earn product and
> the 2021-09-17 state-regulator wave, but it is a notice of hearing
> rather than a final immediate cease-and-desist order. It supports
> product identity and multi-state context only.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`blockfi-multistate-cease-desist-bia-2021-07`](./blockfi-multistate-cease-desist-bia-2021-07.md)
- [`sec-nexo-earn-lending-product-cease-2023-01`](./sec-nexo-earn-lending-product-cease-2023-01.md)
- [`genesis-sec-gemini-earn-2023`](./genesis-sec-gemini-earn-2023.md)
- [`celsius-bankruptcy-mashinsky-doj-2023`](./celsius-bankruptcy-mashinsky-doj-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

