# Evidence chain — `china-pboc-crypto-ban-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4acc680` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:34:29Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Within 13-37 hours of the 2021-09-24 PBOC joint notice going public, both
> Huobi and Binance published official statements citing the notice and
> committing to end of services for mainland-China users; broader
> network-layer (L0) and frontend-layer (L4) reactions are not included in
> this scoped claim because independent measurement evidence for them
> is not yet attached to this event.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2021-09-24 10:51:05+00:00` (precision: `minute`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/4348521/index.html>
  - Wayback: <https://web.archive.org/web/20210924105105/http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/4348521/index.html>
  - body_hash: `sha256:a5c7da7da584c23c3e880f394b445cea75f0ad11aee41f79b10d2da4b2884a84`
  - body_path: `sources/archived_htmls/china-pboc-crypto-ban-2021/pbc-notice-20210924.html`
  > PBOC "Notice on Further Preventing and Dealing with the Risk of Speculation in Virtual Currency Trading" (关于进一步防范和处置虚拟货币交易炒作风险的通知) issued jointly with nine other PRC agencies on 2021-09-24, declaring virtual-currency-related business activities illegal in the PRC and foreign-exchange services serving PRC residents in violation. The earliest Wayback snapshot is 2021-09-24 10:51:05 UTC; five independent snapshots from the same day (10:51, 11:12, 11:36, 12:49, 16:34 UTC) corroborate that the page was public by mid-morning UTC. The authoritative PBOC origin URL currently returns 404 (the page moved); the locally archived Wayback body is the load-bearing evidence for this trigger.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Canonical domains**: `binance.com`, `www.okx.com`, `huobi.com`, `tronscan.org`, `etherscan.io`

> Canonical target is the PRC policy directive itself. Named overseas exchanges and virtual-currency services serving PRC residents are implicit second-order targets; we record them in scope_descriptor fields on L0 observations rather than enumerating them at the event level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 37.15h

**Event label**: `mainland_china_user_accounts_retired`

**Timestamp**: `2021-09-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.huobi.com/support/en-us/detail/54886961978434>
  - Wayback: <https://web.archive.org/web/20260421115421/https://www.htx.com/support/54886961978434>
  - body_hash: `sha256:833dd244f7b1f75665dbec8115c4cca7eef923c49680fe5a2fdb2c7374b5a1a4`
  - body_path: `sources/http_captures/china-pboc-crypto-ban-2021/exchange-announcements/www.huobi.com__support-en-us-detail-54886961978434__1d0e101edc.html`
  > Huobi Global (now HTX) official support-center announcement
> titled "Huobi Global to Gradually Retire Existing Mainland
> China Users", dated 2021-09-26 in announcement text. The
> announcement explicitly cites "recent regulatory policies
> in mainland China" (the 2021-09-24 PBOC joint notice) as the
> reason and commits to ceasing new-user registration from
> mainland China effective 2021-09-24 (UTC+8) and retiring all
> existing mainland-China accounts by 24:00 (UTC+8)
> 2021-12-31. The current URL redirects to the HTX support
> domain; the archived body_hash is of the
> 2026-04-21 fetch of the live page.

### offramp_cex · attribution: `direct` · Δt = 13.15h

**Event label**: `china_pboc_update_announcement`

**Timestamp**: `2021-09-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/115001414292>
  - Wayback: <https://web.archive.org/web/20211024130516/https://www.binance.com/en/support/announcement/115001414292>
  - body_hash: `sha256:eab5dfa958bc428daae595a895a464e3e015aaffa8da5b05c7e91efc9d61b74b`
  - body_path: `sources/archived_htmls/china-pboc-crypto-ban-2021/binance-pboc-update-2021-10-24.html`
  > Binance official support-center announcement titled "China
> PBoC Update" (announcement id 115001414292). The live page
> bot-blocks automated fetchers; the archived Wayback snapshot
> from 2021-10-24 (30 days after the PBOC notice) contains the
> full primary-corporate statement and is saved locally with
> the recorded body_hash. Binance subsequently announced on
> 2021-12-17 that it would halt its P2P trading service for
> mainland-China users by end of 2021 (see supporting SCMP
> article as corroboration).
- **`supporting_journalism`**
  - URL: <https://www.scmp.com/business/article/3152241/binance-halt-peer-peer-trading-service-china-severing-final-link-market>
  - Wayback: <https://web.archive.org/web/20260421115638/https://www.scmp.com/business/article/3152241/binance-halt-peer-peer-trading-service-china-severing-final-link-market>
  - body_hash: `sha256:df269c5406d20bae152e57121479d411a296707aee19e47d461c6337d0baf429`
  - body_path: `sources/http_captures/china-pboc-crypto-ban-2021/exchange-announcements/www.scmp.com__business-article-3152241-binance-halt-peer-peer-trading-service-china-severing-final-link-market__858b1edd34.html`
  > South China Morning Post contemporaneous report on Binance halting its P2P trading service for China by end of 2021, providing journalist-attested corroboration for the primary_corporate anchor above.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **l4_frontend** (`not_measured`): Crypto exchange frontends serving PRC residents reacted with phased withdrawal / account-freeze timelines in the months following. Evidence collection (Wayback snapshots + exchange announcement pages) not yet performed for this event.

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4acc680`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

