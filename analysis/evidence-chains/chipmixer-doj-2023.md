# Evidence chain — `chipmixer-doj-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `432aaf5` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ EDPA seizure of ChipMixer on 2023-03-15 produced a direct L4 observed_change within
> 17h (canonical chipmixer.com substituted with an FBI seizure banner). Joint-action footprint:
> US + 4 European cooperating agencies + Europol. Establishes the 'cross-border
> law-enforcement seizure' pattern for Bitcoin mixer frontends."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_EDPA`
- **Timestamp**: `2023-03-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edpa/pr/platform-used-launder-ransomware-proceeds-seized-coordinated-international-operation>
  - body_hash: `sha256:bf9db0c3926262d81d1c79dacf2ee916719cf42412d5666937c5138cb09f2e65`
  - body_path: `sources/http_captures/chipmixer-doj-2023/doj-press-release/www.justice.gov__usao-edpa-pr-platform-used-launder-ransomware-proceeds-seized-coordinated-international-operation__778427a127.html`
  > DOJ USAO Eastern District of Pennsylvania press release for the 2023-03-15 seizure of
> ChipMixer Bitcoin mixer service. Joint operation: USAO EDPA + FBI + BKA (Germany) +
> HSI + Frankfurt ZIT + Poland Cybercrime Bureau + Zurich Cantonal Police + Europol.
> DOJ dismantled infrastructure seized ~1,909 BTC (~$46.5M) and indicted operator
> Minh Quôc Nguyên (Vietnamese national).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `chipmixer`
- **Actor name**: ChipMixer
- **Chains**: `bitcoin`
- **Canonical domains**: `chipmixer.com`

> ChipMixer was a BTC mixer operating since 2017, responsible for laundering approximately
> $3B in cryptocurrency per DOJ (including ransomware proceeds, DPRK-related funds). Target
> identified by canonical domain chipmixer.com. Indictment mentions specific BTC seizure
> amounts but does not enumerate wallet addresses in DOJ-SDN style.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 17.1h

**Event label**: `canonical_domain_seized_by_fbi_and_international_partners`

**Timestamp**: `2023-03-15 17:06:06+00:00` (precision: `minute`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20230315170606/https://chipmixer.com/>
  - body_hash: `sha256:280d29cf15a4a644dc174f059f031e3e067cd56d0bd52b5de305ccdb022eb2bd`
  - body_path: `sources/http_captures/chipmixer-doj-2023/frontend-wayback/web.archive.org__web-20230315170606-https-chipmixer.com__4c13a2baa9.html`
  > Wayback snapshot of chipmixer.com on 2023-03-15 17:06 UTC carrying the FBI seizure
> banner verbatim: "This domain has been seized by the Federal Bureau of
> Investigation in accordance with a seizure warrant issued pursuant to Title 18
> U.S.C. §§ 981(a)(1)(A), 981(b), 982(a)(1), 982(b), and Title 21 U.S.C. §§ 853
> issued by the United States District Court for the Eastern District of
> Pennsylvania as part of a coordinated law enforcement operation and action by:
> USAO EDPA / FBI / Bundeskriminalamt (BKA) / HSI / Generalstaatsanwaltschaft
> Frankfurt Am Main - ZIT / Centralnego Biura Zwalczania Cyberprzestepczosci /
> Kantonspolizei Zurich / Department of Justice / EUROPOL." Primary_legal source
> (banner = judicial notice).
- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20230314171941/https://chipmixer.com/>
  - body_hash: `sha256:2e2844e7df71fd71a4b0c1d257adc370ceb9865dd95e8c9a08102e1584c144e0`
  - body_path: `sources/http_captures/chipmixer-doj-2023/frontend-wayback/web.archive.org__web-20230314171941-https-chipmixer.com__ab048b5f9a.html`
  > Pre-event Wayback snapshot 24h before seizure. Normal ChipMixer-branded page
> (1766 bytes, digest RUUHGEVKNXANWAAEZMWB47KYB2OQZIJF). Confirms pre-event state.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `432aaf5`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

