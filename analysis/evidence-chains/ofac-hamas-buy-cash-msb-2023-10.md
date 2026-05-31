# Evidence chain — `ofac-hamas-buy-cash-msb-2023-10`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71ac901` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-10-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1816>
  - Wayback: <https://web.archive.org/web/20231018131253/https://home.treasury.gov/news/press-releases/jy1816>
  - body_hash: `sha256:a043b8acb03268236237950413f59e2c5fafcfb6c3436209e80a7a7fc672eb2c`
  - body_path: `sources/http_captures/ofac-hamas-buy-cash-msb-2023-10/primary/web.archive.org__web-20231018131253-https-home.treasury.gov-news-press-releases-jy1816__2acb79624c.html`
  > US Treasury press release jy1816 (2023-10-18): "Following Terrorist
> Attack on Israel, Treasury Sanctions Hamas Operatives and Financial
> Facilitators." First post-October 7 OFAC action: designates ten
> Hamas operatives across Gaza, Sudan, Turkey, Algeria, and Qatar,
> plus the Gaza-based virtual-currency MSB "Buy Cash Money and Money
> Transfer Company" (Khan Yunis) with at least one attached digital-
> currency address. Cleanest geopolitical-trigger sanctions cascade
> since Tornado Cash 2022-08. v0.3 audit 2026-05-20 (c) Batch C-1:
> Wayback memento 20231018131253 pinned (176777 bytes), grep verifies
> 115xHamas variants + 20xBuy Cash + 14xjy1816 + 14xGaza + 12xvirtual
> currency + 11xSDN variants.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20231018>
  - Wayback: <https://web.archive.org/web/20231018160335/https://ofac.treasury.gov/recent-actions/20231018>
  - body_hash: `sha256:33326cbd390fe44b26bd87803ad887f81b660aaf82221baac68a694430f415f0`
  - body_path: `sources/http_captures/ofac-hamas-buy-cash-msb-2023-10/primary/web.archive.org__web-20231018160335-https-ofac.treasury.gov-recent-actions-20231018__acf8500722.html`
  > OFAC Recent Actions page for 2023-10-18 (Counter Terrorism
> Designations). Companion to jy1816; carries the SDN list entries
> and the attached digital-currency address roster. v0.3 audit
> 2026-05-20 (c) Batch C-1: Wayback memento 20231018160335 pinned
> (86493 bytes), grep verifies 16xSDN + 10xHAMAS + 5xGaza + 3xKhan
> Yunis + 3xBUY CASH + 1xjy1816.
- **`supporting_journalism`**
  - URL: <https://www.trmlabs.com/resources/blog/us-doj-charges-hamas-leaders-with-october-7-attacks-details-hamas-use-of-cryptocurrencies>
  - Wayback: <https://web.archive.org/web/20250328082128/https://www.trmlabs.com/resources/blog/us-doj-charges-hamas-leaders-with-october-7-attacks-details-hamas-use-of-cryptocurrencies>
  - body_hash: `sha256:0cfc282602b581e4c0351be29591f98af9d80acfa1d34bebce6249837550d706`
  - body_path: `sources/http_captures/ofac-hamas-buy-cash-msb-2023-10/primary/web.archive.org__web-20250328082128-https-www.trmlabs.com-resources-blog-us-doj-charges-hamas-leaders-with-october-7-attacks-details-hamas-use-of-cryptocurrencies__16d300ec9d.html`
  > TRM Labs chain-analytics blog summarising the OFAC 2023-10-18
> designation and subsequent enforcement context (Buy Cash MSB,
> Hamas-linked USDT wallets). Triangulation source for the
> designation's chain-analytics framing. v0.3 audit 2026-05-20
> (c) Batch C-1: Wayback memento 20250328082128 pinned (138465 bytes),
> grep verifies 112xhamas variants + 17xGaza + 2xOctober 18 + 1xjy1816.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Buy Cash Money and Money Transfer Company (Khan Yunis, Gaza)
- **Chains**: `bitcoin`
- **Addresses**: 1 total (enumerated in event YAML)

> The 2023-10-18 SDN action enumerates ten Hamas-affiliated individuals
> plus the Gaza-based virtual-currency MSB "Buy Cash Money and Money
> Transfer Company" (Khan Yunis). v0.3 audit 2026-05-20 (c) Batch C-1
> factual correction: full enumeration confirmed from OFAC RA HTML —
> Buy Cash MSB carries EXACTLY ONE digital-currency address, a Bitcoin
> XBT address `19D1iGzDr7FyAdiy3ZZdxMd6ttHj1kj6WW`. The original draft
> incorrectly inferred Ethereum/USDT chain involvement from contemporary
> Tether freeze sweeps (those sweeps target OTHER Hamas-affiliated
> addresses across the broader RA, NOT Buy Cash's single XBT address).
> enumeration=complete (was subset) now reflects the correct 1-address
> scope. This event scopes the target to the Buy Cash MSB entity (the
> virtual-currency / off-ramp node of the action) because that is the
> load-bearing actor for the offramp_cex severance layer. The ten
> individual operatives are listed in the same press release but are
> not the focal target here.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sdn_designation_of_buy_cash_msb_severs_us_ramp_access`

**Timestamp**: `2023-10-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1816>
  - Wayback: <https://web.archive.org/web/20231018131253/https://home.treasury.gov/news/press-releases/jy1816>
  - body_hash: `sha256:a043b8acb03268236237950413f59e2c5fafcfb6c3436209e80a7a7fc672eb2c`
  - body_path: `sources/http_captures/ofac-hamas-buy-cash-msb-2023-10/primary/web.archive.org__web-20231018131253-https-home.treasury.gov-news-press-releases-jy1816__2acb79624c.html`
  > Treasury press release jy1816 names the action (SDN designation
> of Buy Cash MSB) and the mechanism (US-property block + 50%
> rule + secondary-sanctions exposure for any non-US ramp that
> services the entity). attribution=direct because the source is
> the designating authority naming the action.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20231018>
  - Wayback: <https://web.archive.org/web/20231018160335/https://ofac.treasury.gov/recent-actions/20231018>
  - body_hash: `sha256:33326cbd390fe44b26bd87803ad887f81b660aaf82221baac68a694430f415f0`
  - body_path: `sources/http_captures/ofac-hamas-buy-cash-msb-2023-10/primary/web.archive.org__web-20231018160335-https-ofac.treasury.gov-recent-actions-20231018__acf8500722.html`
  > OFAC Recent Actions page (2023-10-18) carries the Buy Cash SDN
> entry and at least one attached digital-currency address.
> Independent legal-source anchor for the offramp_cex severance
> claim.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No canonical Buy Cash MSB web frontend has been pinned by the
- **l4_frontend** (`not_measured`): No canonical Buy Cash MSB frontend pinned. Status remains

## 7. Related events

- [`tether-doj-pig-butchering-freeze-2023`](./tether-doj-pig-butchering-freeze-2023.md)
- [`suex-ofac-2021`](./suex-ofac-2021.md)
- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71ac901`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

