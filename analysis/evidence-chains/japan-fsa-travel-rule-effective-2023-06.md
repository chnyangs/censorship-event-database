# Evidence chain — `japan-fsa-travel-rule-effective-2023-06`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `cba4eca` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Japan's 2023-06-01 effective date for the revised Act on Prevention
> of Transfer of Criminal Proceeds (APTCP) operationalized the FATF
> Travel Rule for FSA-registered Crypto-Asset Exchange Service
> Providers (CAESPs), requiring originator + beneficiary metadata for
> CAESP-to-CAESP crypto-asset transfers without a de-minimis threshold.
> Anchored as a metadata-layer null_event in the global Travel Rule
> cascade (parent: FATF R.15 2019; siblings: KR FSC 2022, EU TFR 2023)."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `JP_FSA`
- **Timestamp**: `2023-06-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.fsa.go.jp/en/laws_regulations/index.html>
  - body_hash: `sha256:1c357c9cc30c03fdce6b8bf5cdab98386f20c215918159aeaf1ef1ed49b53cf4`
  - body_path: `sources/http_captures/japan-fsa-travel-rule-effective-2023-06/primary/www.fsa.go.jp__en-laws_regulations-index.html__e848e1f222.html`
  > FSA Laws & Regulations index — the regulator-of-record's
> official legal-framework hub for the Act on Prevention of
> Transfer of Criminal Proceeds (APTCP / 犯罪収益移転防止法)
> amendment package that implemented the FATF Travel Rule for
> FSA-registered Crypto-Asset Exchange Service Providers (CAESPs /
> 暗号資産交換業者) effective 2023-06-01. The APTCP amendment was
> promulgated by the Cabinet Secretariat in December 2022; the FSA
> ran a public consultation on the APTCP guidelines through
> 2023-03-03; the Travel Rule entered into force 2023-06-01 without
> a de-minimis threshold (all CAESP-to-CAESP crypto-asset transfers
> carry the originator/beneficiary metadata obligation regardless
> of amount). Live fsa.go.jp capture 2026-05-21. The specific
> 2023-era APTCP cabinet-order URL on the FSA news index is no
> longer live (404) and has no Wayback memento; the contemporaneous
> effective-date detail is anchored via the two semi_primary_wayback
> sources below.
- **`semi_primary_wayback`**
  - URL: <https://www.sygna.io/blog/japan-travel-rule-starts-1-june-an-in-depth-guide-for-vasps/>
  - Wayback: <https://web.archive.org/web/20230716104514/https://www.sygna.io/blog/japan-travel-rule-starts-1-june-an-in-depth-guide-for-vasps/>
  - body_hash: `sha256:a75232e7c102060a11e91fb13f36bf58a8e75ed293b2879ad9832e96d32b7218`
  - body_path: `sources/http_captures/japan-fsa-travel-rule-effective-2023-06/primary/web.archive.org__web-20230716104514-https-www.sygna.io-blog-japan-travel-rule-starts-1-june-an-in-depth-guide-for-vasps__081e9666a3.html`
  > Sygna (Travel Rule compliance solution provider) in-depth guide
> documenting the 2023-06-01 Japan APTCP Travel Rule effective date
> and the no-threshold CAESP obligation. Wayback memento
> 20230716104514 (contemporaneous with the event) captured
> 2026-05-21. Independent semi-primary anchor 1 of 2.
- **`semi_primary_wayback`**
  - URL: <https://www.shyft.network/newsroom/japan-to-enforce-crypto-travel-rule-from-june-1st>
  - Wayback: <https://web.archive.org/web/20230529181004/https://www.shyft.network/newsroom/japan-to-enforce-crypto-travel-rule-from-june-1st>
  - body_hash: `sha256:36dbb5976073bac7b9ba5444b387f5d894b829d0c3033fd8d3b295535e1a3cea`
  - body_path: `sources/http_captures/japan-fsa-travel-rule-effective-2023-06/primary/web.archive.org__web-20230529181004-https-www.shyft.network-newsroom-japan-to-enforce-crypto-travel-rule-from-june-1st__303f881e1a.html`
  > Shyft Network (blockchain compliance infrastructure) newsroom
> post (2023-05-29, three days before the effective date)
> documenting the 2023-06-01 Japan APTCP Travel Rule enforcement.
> Wayback memento 20230529181004 captured 2026-05-21. Independent
> semi-primary anchor 2 of 2.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Japanese registered CAESPs (FSA-licensed)

> FSA-registered Crypto-Asset Exchange Service Providers (CAESPs /
> 暗号資産交換業者) operating in Japan as of 2023-06-01 — approximately
> 30 licensed CAESPs at that date (bitFlyer, Coincheck, bitbank, GMO
> Coin, DMM Bitcoin, Rakuten Wallet, SBI VC Trade, etc.). The Travel
> Rule obligation operates at the VASP/sector level rather than via
> address enumeration: CAESPs must collect and transmit originator +
> beneficiary information for crypto-asset transfers to other VASPs.
> Downstream effect: friction on transfers to self-custody / unhosted
> wallets and to non-Sunrise-compliant overseas VASPs via regulated
> Japanese exchanges.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `jp_aptcp_travel_rule_effective_no_threshold_for_caesps`

**Window**: `2023-06-01 00:00:00+00:00` → `2023-12-31 23:59:59+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://www.fsa.go.jp/en/laws_regulations/index.html>
  - body_hash: `sha256:1c357c9cc30c03fdce6b8bf5cdab98386f20c215918159aeaf1ef1ed49b53cf4`
  - body_path: `sources/http_captures/japan-fsa-travel-rule-effective-2023-06/primary/www.fsa.go.jp__en-laws_regulations-index.html__e848e1f222.html`
  > observed_no_change at the offramp_cex layer: the APTCP revision
> imposes a metadata-transmission obligation on all FSA-registered
> CAESPs from 2023-06-01 forward, but the corpus has no replayable
> measurement of downstream transfer behavior. The trigger is the
> regulatory effective date itself; this row anchors the
> regulator-decreed information-collection requirement as a
> metadata-layer null_event in the Travel Rule cascade alongside
> fatf-r15-vasp-travel-rule-2019 (parent), korea-travel-rule-2022
> (Asia sibling), and eu-tfr-recast-2023 (EU sibling). FSA
> primary_government anchor; live fsa.go.jp capture 2026-05-21.
- **`semi_primary_wayback`**
  - URL: <https://www.sygna.io/blog/japan-travel-rule-starts-1-june-an-in-depth-guide-for-vasps/>
  - Wayback: <https://web.archive.org/web/20230716104514/https://www.sygna.io/blog/japan-travel-rule-starts-1-june-an-in-depth-guide-for-vasps/>
  - body_hash: `sha256:a75232e7c102060a11e91fb13f36bf58a8e75ed293b2879ad9832e96d32b7218`
  - body_path: `sources/http_captures/japan-fsa-travel-rule-effective-2023-06/primary/web.archive.org__web-20230716104514-https-www.sygna.io-blog-japan-travel-rule-starts-1-june-an-in-depth-guide-for-vasps__081e9666a3.html`
  > Sygna contemporaneous guide (Wayback 20230716104514)
> documenting the no-threshold 2023-06-01 CAESP Travel Rule.
> Independent semi-primary anchor 1 of 2.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)
- [`eu-tfr-recast-2023`](./eu-tfr-recast-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cba4eca`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

