# Audit worksheet — `infura-alchemy-tornado-rpc-block-2022`

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `128e1e1` · generated `2026-06-01T00:00:00Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S5_corporate`
- **empirical_shape**: `comparison`
- **status**: `admitted`
- **last_verified**: `2026-05-16`
- **last_human_audit**: `2026-05-16`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `corporate_policy_change`
- **actor**: `consensys_infura`
- **timestamp**: `2022-08-09 00:00:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_corporate` · url=<https://infura.io/terms> · wayback=<https://web.archive.org/web/2022/https://infura.io/terms>  · hash_check=`—`
- [ ] citation[1]: type=`primary_corporate` · url=<https://docs.alchemy.com/reference/compliance-program> · wayback=<https://web.archive.org/web/2022/https://docs.alchemy.com/reference/compliance-program>  · hash_check=`—`
- [ ] citation[2]: type=`supporting_journalism` · url=<https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets> · wayback=<https://web.archive.org/web/2022/https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets>  · hash_check=`—`
- [ ] citation[3]: type=`supporting_journalism` · url=<https://www.theblock.co/post/162680> · wayback=<https://web.archive.org/web/2022/https://www.theblock.co/post/162680>  · hash_check=`—`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "The 2022-08-09 Infura and Alchemy RPC-provider blocks of requests
> touching the 2022-08-08 OFAC Tornado Cash SDN address set constitute
> the first documented L3 RPC-provider sanctions block in the corpus,
> with two named providers' own corporate-policy statements
> (attribution=direct) and a downstream L4 wallet/aggregator UI
> cascade (attribution=plausible, via Infura's MetaMask-default-RPC
> position). The row does not claim ISP-level connectivity blocking,
> consensus-layer (PBS) effect, on-chain asset freeze, or off-ramp
> severance — those are sibling-event rows under tornado-cash-ofac-2022
> / circle-usdc-tornado-2022."
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `l3_rpc` · actor=`rpc_provider:consensys_infura` · event=`infura_rpc_block_of_tornado_cash_sdn_addresses`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2022-08-09 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **sources** (2):
  - [ ] src[0]: type=`primary_corporate` · url=<https://infura.io/terms> · wayback=<https://web.archive.org/web/2022/https://infura.io/terms> · scope_descriptor=(2 keys)  · hash_check=`—`
  - [ ] src[1]: type=`supporting_journalism` · url=<https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets> · wayback=<https://web.archive.org/web/2022/https://cointelegraph.com/news/infura-blocks-some-areas-from-accessing-ethereum-and-its-testnets>  · hash_check=`—`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `l3_rpc` · actor=`rpc_provider:alchemy_insights` · event=`alchemy_rpc_block_of_tornado_cash_sdn_addresses`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2022-08-09 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **sources** (2):
  - [ ] src[0]: type=`primary_corporate` · url=<https://docs.alchemy.com/reference/compliance-program> · wayback=<https://web.archive.org/web/2022/https://docs.alchemy.com/reference/compliance-program> · scope_descriptor=(2 keys)  · hash_check=`—`
  - [ ] src[1]: type=`supporting_journalism` · url=<https://www.theblock.co/post/162680> · wayback=<https://web.archive.org/web/2022/https://www.theblock.co/post/162680>  · hash_check=`—`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.3 · `l4_frontend` · actor=`frontend:wallets_and_aggregators_using_infura_default_rpc` · event=`downstream_wallet_and_aggregator_ui_broke_for_tornado_interactions`

- **observation_kind**: `observed_change`
- **attribution**: `plausible`
- **timestamp**: `2022-08-10 00:00:00+00:00` · precision=`day` · delta_hours=`24`
- **sources** (1):
  - [ ] src[0]: type=`primary_corporate` · url=<https://infura.io/terms> · wayback=<https://web.archive.org/web/2022/https://infura.io/terms> · scope_descriptor=(3 keys)  · hash_check=`—`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `plausible` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

## 4. Recovery

- [ ] recovery[0]: layer=`l3_rpc` · resolved=`False` · resolved_timestamp=`—`
  - [ ] recovery layer is in `changed_layers` for this event (derived/event_metrics.json intersects recovery with changed_layers; a recovery row on a non-changed layer is silently ignored — revise or remove).

## 5. Sign-off

- [ ] Every checkbox above is checked.
- [ ] Update `events/infura-alchemy-tornado-rpc-block-2022.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
