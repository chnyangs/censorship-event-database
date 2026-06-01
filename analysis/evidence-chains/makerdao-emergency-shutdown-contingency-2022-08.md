# Evidence chain — `makerdao-emergency-shutdown-contingency-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b6c6fae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Between 2022-08-08 (OFAC Tornado Cash SDN designation) and
> 2022-08-31, the MakerDAO governance community publicly debated
> three discretionary protocol-level censorship-response postures
> — Emergency Shutdown of the Maker Protocol, migration of ~33%
> of DAI collateral away from USDC/USDP toward ETH, and
> abandonment of the DAI USD peg — none of which was enacted in
> the debate window. The row carries no observed_change and
> functions as a counterfactual-contingency denominator control
> for the S5 DAO-governance-response-to-sanctions stratum,
> scoping the 'debated but not enacted' baseline against which
> contemporaneous S5 enacted-response rows (Circle USDC Tornado
> freeze, Aave Tornado frontend block, dYdX Tornado account
> block) can be compared. Foundational DAO-governance-response-to-
> sanctions case."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `MAKERDAO_GOVERNANCE`
- **Timestamp**: `2022-08-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://forum.makerdao.com/search/query.json?term=USDC%20Tornado%20Cash>
  - body_hash: `sha256:e734f0cb863bd383c37d603fb8c97b4a0c744a5e836f815c6c6ae7355c8028d7`
  - body_path: `sources/http_captures/makerdao-emergency-shutdown-contingency-2022-08/v0_3_primary_repair/forum.makerdao.com__search-query.json__b739eca00a.json`
  > MakerDAO Discourse search API snapshot for "USDC Tornado Cash".
> The result set includes the 2022-08-08 governance topic
> "Circle started freezing USDC which went through Tornado Cash"
> and the 2022-08-12 topic "The Real Legal Risks", anchoring the
> Maker governance forum as the first-party discussion surface.
> This is a governance-surface anchor for the debate, not a
> substitute for a full on-chain audit of PSM / ESM state.
- **`primary_corporate`**
  - URL: <https://forum.makerdao.com/t/circle-started-freezing-usdc-which-went-through-tornado-cash/17101.json>
  - body_hash: `sha256:b6ef9c09a692eafc7774c8bdbd73f15a5a4cdee6532a664e9ba36b97ecd03dbb`
  - body_path: `sources/http_captures/makerdao-emergency-shutdown-contingency-2022-08/v0_3_primary_repair/forum.makerdao.com__t-circle-started-freezing-usdc-which-went-through-tornado-cash-17101.json__25e3081f17.json`
  > MakerDAO forum topic opened 2022-08-08 on Circle freezing USDC
> that had passed through Tornado Cash. The topic metadata and
> post stream provide a first-party governance-forum anchor for
> the USDC/Tornado Cash risk discussion that precedes the
> emergency-shutdown contingency journalism.
- **`supporting_journalism`**
  - URL: <https://thedefiant.io/news/defi/tornado-impact-makerdao-dai>
  - Wayback: <https://web.archive.org/web/2022/https://thedefiant.io/news/defi/tornado-impact-makerdao-dai>
  > The Defiant 2022-08-18 coverage "MakerDAO May Execute 'Emergency
> Shutdown' If Sanctions Hit DAI" — the primary contemporaneous
> anchor for the MakerDAO governance debate triggered by the
> 2022-08-08 OFAC Tornado Cash SDN designation and Circle's
> 2022-08-08 USDC freeze of Tornado Cash addresses. Reports
> Rune Christensen's Discord-posted contingency plan to execute
> an Emergency Shutdown of the Maker Protocol if its core
> USDC-PSM (Peg Stability Module) contracts were sanctioned, and
> the parallel proposal to migrate DAI collateral away from
> USDC/USDP toward ETH and to consider de-pegging DAI from the
> US dollar. The "Endgame Plan" framing on the MakerDAO governance
> forum is the canonical contemporaneous discussion locus.
> DRYRUN: wayback wildcard pointer in lieu of pinned-timestamp
> snapshot; evidence_use=contextual_unarchived because no
> body_hash+body_path pair has been captured into
> sources/http_captures/makerdao-emergency-shutdown-contingency-2022-08/
> in this session.
- **`supporting_journalism`**
  - URL: <https://decrypt.co/107273/makerdao-founder-dai-drop-dollar-peg-tornado-cash-usdc>
  - Wayback: <https://web.archive.org/web/2022/https://decrypt.co/107273/makerdao-founder-dai-drop-dollar-peg-tornado-cash-usdc>
  > Decrypt 2022-08-12 coverage "MakerDAO Founder Calls on DAI to
> Drop Dollar Peg Amid Tornado Cash Fallout" — quotes Rune
> Christensen's Discord posts arguing for de-pegging DAI from the
> USD to insulate the protocol from Circle / USDC sanctions
> exposure (USDC PSM held ~$3.56B / ~33% of DAI collateral at the
> time). DRYRUN: wayback wildcard pointer in lieu of pinned
> snapshot.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/business/2022/08/18/makerdao-prepares-emergency-shutdown-contingency-in-case-of-usdc-sanctions>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/08/18/makerdao-prepares-emergency-shutdown-contingency-in-case-of-usdc-sanctions>
  > CoinDesk 2022-08-18 contemporaneous coverage of the MakerDAO
> governance debate over Emergency Shutdown contingency planning
> in response to the Tornado Cash OFAC SDN designation and the
> Circle USDC PSM exposure. Triangulation source on the day-level
> anchor (2022-08-18) for the Christensen Discord posts and
> forum-thread escalation. DRYRUN: wayback wildcard pointer
> pending body_hash capture.
- **`supporting_journalism`**
  - URL: <https://cryptoslate.com/makerdao-plans-against-sanctions-from-usdc-exposure/>
  - Wayback: <https://web.archive.org/web/2022/https://cryptoslate.com/makerdao-plans-against-sanctions-from-usdc-exposure/>
  > CryptoSlate contemporaneous coverage of the same MakerDAO
> governance debate, retained for community-reaction context on
> the USDC-PSM collateral exposure (~33% of DAI backing) and the
> proposed asset-allocation migration toward ETH. DRYRUN: wayback
> wildcard pointer pending body_hash capture.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `makerdao`
- **Actor name**: MakerDAO governance community (MKR voters + Maker Foundation contributors)
- **Chains**: `ethereum`
- **Canonical domains**: `makerdao.com`, `forum.makerdao.com`, `vote.makerdao.com`

> Target is the MakerDAO governance community + the MKR / DAI holder
> class — the population that holds MKR governance tokens (voting
> rights over Maker Protocol parameters including PSM collateral
> composition, Emergency Shutdown trigger, and surplus-buffer policy)
> and the DAI holder class whose redemption / peg backing depends on
> the underlying collateral pool (~33% USDC PSM exposure at the time).
> enumeration=subset because the affected class is an open-ended
> population (all MKR voters and DAI holders during the 2022-08
> Tornado-Cash-fallout governance window) rather than a closed
> enumerable set; the governance debate addresses the class
> collectively via the Discord channel and governance.makerdao.com
> forum.
> 
> This row codes the **governance-debate / contingency-discussion
> action** — MakerDAO governance publicly weighing Emergency
> Shutdown, USDC-collateral migration toward ETH, and DAI USD-peg
> abandonment as contingency responses to the 2022-08-08 OFAC
> Tornado Cash SDN designation and Circle's parallel USDC freeze of
> Tornado Cash addresses. No protocol parameter is changed during
> the August 2022 debate window — neither Emergency Shutdown is
> executed, nor is USDC collateral materially divested, nor is the
> DAI USD peg abandoned. The debate itself is the artifact; the
> counterfactual contingency framing is the analytical interest.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### asset_onchain — `makerdao_emergency_shutdown_not_triggered_collateral_composition_unchanged_during_tornado_cash_fallout_debate`

**Window**: `2022-08-08 00:00:00+00:00` → `2022-08-31 23:59:59+00:00`

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xdb1f3c8c48762feea71745c114d7ba0be1ae8019618f8bf3afd12f3762edc97b>
  - tx_hash: `0xdb1f3c8c48762feea71745c114d7ba0be1ae8019618f8bf3afd12f3762edc97b`
  > MakerDAO PSM-USDC-A (MCD_PSM_USDC_A 0x89B78CfA322F6C5dE0aBcEecab66Aee45393cC5A)
> sellGem tx 2022-08-17 (~325,947 USDC -> DAI), one day before the 2022-08-18
> Emergency-Shutdown-contingency debate. Demonstrates the PSM minting DAI against
> USDC normally during the Tornado/USDC sanctions fallout window; Emergency Shutdown
> was NOT triggered and the USDC-PSM was NOT cut. Companion reverse-direction buyGem
> tx 0xf559861f5f79061876122aa89f1937fbd9b64a25db1d005e7f3eb08c85d85116 (block 15399442,
> 2022-08-23) confirms two-way operation through the debate window.
- **`primary_corporate`**
  - URL: <https://forum.makerdao.com/search/query.json?term=USDC%20Tornado%20Cash>
  - body_hash: `sha256:e734f0cb863bd383c37d603fb8c97b4a0c744a5e836f815c6c6ae7355c8028d7`
  - body_path: `sources/http_captures/makerdao-emergency-shutdown-contingency-2022-08/v0_3_primary_repair/forum.makerdao.com__search-query.json__b739eca00a.json`
  > MakerDAO Discourse search API snapshot showing first-party
> forum topics opened during the Tornado Cash / USDC risk
> window, including "Circle started freezing USDC which went
> through Tornado Cash" (2022-08-08) and "The Real Legal Risks"
> (2022-08-12). This anchors the governance discussion substrate
> and supports the "debated but not enacted in this row" framing;
> it is not, by itself, a complete on-chain PSM / ESM no-change
> proof.
- **`primary_corporate`**
  - URL: <https://forum.makerdao.com/t/the-real-legal-risks/17207.json>
  - body_hash: `sha256:13d6d0b007f3da004ce29b5ab2c534fdbdc24fb8c16aa1bfef113ad2371d54f6`
  - body_path: `sources/http_captures/makerdao-emergency-shutdown-contingency-2022-08/v0_3_primary_repair/forum.makerdao.com__t-the-real-legal-risks-17207.json__2415a7533f.json`
  > MakerDAO forum topic "The Real Legal Risks" opened 2022-08-12
> by a former Maker Foundation legal contributor. The post
> explicitly situates the Tornado Cash sanctions and USDC
> freeze/blocking risk inside MakerDAO's regulatory-risk debate.
> It is primary governance-surface evidence for the discussion
> path, now paired with the verified PSM-USDC-A sellGem on-chain
> anchor that grounds the no-change claim for release prose.
- **`supporting_journalism`**
  - URL: <https://thedefiant.io/news/defi/tornado-impact-makerdao-dai>
  - Wayback: <https://web.archive.org/web/2022/https://thedefiant.io/news/defi/tornado-impact-makerdao-dai>
  > The Defiant 2022-08-18 coverage documents the MakerDAO
> governance contingency debate — Christensen's Emergency
> Shutdown proposal, the USDC-collateral migration discussion,
> and the DAI USD-peg abandonment proposal — while
> contemporaneously confirming that no Emergency Shutdown is
> executed and the USDC-PSM ~33% collateral exposure remains
> materially unchanged through the 2022-08 window. The article
> serves as the falsifiability anchor for the observed_no_change
> claim: a discretionary protocol-level censorship-response
> action was publicly debated, but the protocol parameters
> governing DAI backing and Emergency Shutdown remained
> unchanged during the debate window. attribution=none per
> codebook §1 (observed_no_change rows require
> attribution=none). DRYRUN: wayback wildcard pointer in lieu
> of pinned-timestamp snapshot.
- **`supporting_journalism`**
  - URL: <https://decrypt.co/107273/makerdao-founder-dai-drop-dollar-peg-tornado-cash-usdc>
  - Wayback: <https://web.archive.org/web/2022/https://decrypt.co/107273/makerdao-founder-dai-drop-dollar-peg-tornado-cash-usdc>
  > Decrypt 2022-08-12 piece anchors the de-pegging proposal as
> a governance-debate artifact rather than an enacted policy
> — confirms that no peg-abandonment vote was advanced through
> on-chain governance during the August 2022 window. Companion
> falsifiability source for the observed_no_change row.
> DRYRUN: wayback wildcard pointer pending body_hash capture.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)
- [`aave-arc-fireblocks-whitelist-2022-01`](./aave-arc-fireblocks-whitelist-2022-01.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b6c6fae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

