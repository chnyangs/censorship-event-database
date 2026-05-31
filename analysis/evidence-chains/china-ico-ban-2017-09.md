# Evidence chain — `china-ico-ban-2017-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `3b37c3e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The PBOC 7-Ministry Notice of 2017-09-04 (公告 [2017]) declared ICO
> token-issuance fundraising illegal as unauthorized public financing,
> halted all ICO financing activities from date of issuance, mandated
> refund arrangements for completed ICOs, and prohibited PRC financial
> institutions and non-bank payment agencies from token-related
> services. The asset_onchain layer carries the jurisdiction-wide
> issuer-rail prohibition observation; the offramp_cex layer carries
> the sector-wide CNY-pair delisting observation. Both rest on
> direct attribution from the notice text.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2017-09-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/3374222/index.html>
  - Wayback: <https://web.archive.org/web/2017/http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/3374222/index.html>
  - body_hash: `sha256:48cad3d18bb9d1d59fb58b3ba398bfcc70a1dd74cabf81d554094f9f981983ca`
  - body_path: `sources/http_captures/china-ico-ban-2017-09/primary/web.archive.org__web-20170904083557-http-www.pbc.gov.cn-goutongjiaoliu-113456-113469-3374222-index.html__0aa94d8f93.html`
  > PBOC publication of the "Announcement on Preventing Financial
> Risks from Initial Coin Offerings" (关于防范代币发行融资风险的公告,
> commonly referred to in English as the 9.4 Notice or
> 7-Ministry Notice), issued 2017-09-04 jointly by seven PRC
> central-government regulators: People's Bank of China (PBOC,
> lead), Cyberspace Administration of China (CAC), Ministry of
> Industry and Information Technology (MIIT), State Administration
> for Industry and Commerce (SAIC), China Banking Regulatory
> Commission (CBRC), China Securities Regulatory Commission (CSRC),
> and China Insurance Regulatory Commission (CIRC). Core
> provisions: (1) classified ICO token-issuance fundraising as
> "unauthorized public financing" and declared it illegal;
> (2) ordered immediate halt of all ICO financing activities from
> date of issuance; (3) required organizations and individuals
> who had completed ICOs to make refund arrangements; (4) prohibited
> financial institutions and non-bank payment agencies from
> providing account opening, registration, trading, liquidation,
> settlement, or insurance services involving tokens and virtual
> currencies. The pbc.gov.cn URL path format has drifted since 2017;
> the provisional Wayback anchor uses year-prefix lookup and the
> specific capture timestamp requires re-pinning during human audit
> before this citation may serve as an admission anchor in its own
> right. Marked evidence_use=contextual_unarchived pending that
> re-pin. Primary source is Chinese-language; English secondary
> anchors below provide the working translation context.
- **`supporting_tracker`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2017-10-19/china-regulators-ban-companies-from-raising-money-through-virtual-currencies/>
  - Wayback: <https://web.archive.org/web/2020/https://www.loc.gov/item/global-legal-monitor/2017-10-19/china-regulators-ban-companies-from-raising-money-through-virtual-currencies/>
  > US Library of Congress Global Legal Monitor entry dated
> 2017-10-19, "China: Regulators Ban Companies from Raising Money
> Through Virtual Currencies", providing an English-language
> summary of the 7-Ministry Notice and naming all seven issuing
> agencies. Used here as a contextual translation anchor; the
> live loc.gov URL format is stable and routinely captured by
> Wayback, but the specific snapshot timestamp is to be re-pinned
> during human audit. Marked evidence_use=contextual_unarchived
> pending that re-pin.
- **`supporting_journalism`**
  - URL: <https://www.cnbc.com/2017/09/04/chinese-icos-china-bans-fundraising-through-initial-coin-offerings-report-says.html>
  - Wayback: <https://web.archive.org/web/2017/https://www.cnbc.com/2017/09/04/chinese-icos-china-bans-fundraising-through-initial-coin-offerings-report-says.html>
  > CNBC same-day English-language coverage 2017-09-04: "China bans
> companies from raising money through ICOs, asks local regulators
> to inspect 60 major platforms". Corroborates the 2017-09-04
> issuance date and the cross-ministry origin. Used as an
> English-language anchor because primary PBOC text is
> Chinese-language; wayback year-prefix anchor, specific snapshot
> requires re-pin during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PRC ICO + CNY-pair-exchange ecosystem (class)

> Canonical target is the PRC policy directive itself, addressed to
> (a) ICO token issuers and crypto-fundraising promoters within PRC
> jurisdiction (declared illegal and ordered to refund), and
> (b) PRC financial institutions and non-bank payment agencies
> (prohibited from token/virtual-currency-related services). Named
> affected ICO platforms and CNY-pair-offering exchanges in the
> 2017-09 window include OKCoin, Huobi, BTCC, and ICOage-style
> domestic ICO platforms; these are recorded as implicit second-order
> targets in observation scope rather than enumerated in
> canonical_domains, matching the sibling china-pboc-crypto-ban-2013-12
> and china-pboc-crypto-ban-2021 convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `ico_token_cny_pairs_delisted_sector_wide`

**Timestamp**: `2017-09-04 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/3374222/index.html>
  - Wayback: <https://web.archive.org/web/20170904083557/http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/3374222/index.html>
  - body_hash: `sha256:48cad3d18bb9d1d59fb58b3ba398bfcc70a1dd74cabf81d554094f9f981983ca`
  - body_path: `sources/http_captures/china-ico-ban-2017-09/primary/web.archive.org__web-20170904083557-http-www.pbc.gov.cn-goutongjiaoliu-113456-113469-3374222-index.html__0aa94d8f93.html`
  > The 7-Ministry Notice prohibits PRC financial institutions
> and non-bank payment agencies from providing token-related
> account opening, registration, trading, liquidation,
> settlement, or insurance services. CNY-pair listings for
> ICO tokens at the PRC domestic exchange triad (OKCoin,
> Huobi, BTCC) ceased in compliance. attribution=direct
> because the notice text names the prohibition that drove
> the observed sector-wide CNY-pair delisting. Provisional
> wayback anchor; specific snapshot timestamp requires
> re-pinning during human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.cnbc.com/2017/09/04/chinese-icos-china-bans-fundraising-through-initial-coin-offerings-report-says.html>
  - Wayback: <https://web.archive.org/web/20170904084200/https://www.cnbc.com/2017/09/04/chinese-icos-china-bans-fundraising-through-initial-coin-offerings-report-says.html>
  - body_hash: `sha256:4b10ede20fb7ed959ddcf52630d092ffe2d5fa5598cd2f2f4a228fa5d5dd24dd`
  - body_path: `sources/http_captures/china-ico-ban-2017-09/primary/web.archive.org__web-20170904084200-https-www.cnbc.com-2017-09-04-chinese-icos-china-bans-fundraising-through-initial-coin-offerings-report-says.html__a27d6aec56.html`
  > CNBC 2017-09-04 same-day English coverage corroborating the
> ban announcement and the directive to local regulators to
> inspect ~60 major platforms. Used as English-language
> anchor because primary PBOC text is Chinese-language.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): PRC domestic crypto exchange frontends (OKCoin, Huobi, BTCC) and

## 7. Related events

- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-pboc-exchange-shutdown-2017-09`](./china-pboc-exchange-shutdown-2017-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3b37c3e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

