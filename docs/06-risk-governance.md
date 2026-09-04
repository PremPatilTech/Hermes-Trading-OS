# Risk Governance

## Risk Philosophy

Hermes uses layered risk controls. A candidate decision must be safe at the strategy level, account level, broker-interface level, and operational-state level before execution is allowed.

Public docs intentionally describe risk categories rather than publishing exact production thresholds.

## Control Layers

| Layer | Purpose |
| --- | --- |
| Decision quality | Ensure signal event meets strategy eligibility |
| Position sizing | Ensure requested size is expressible and within configured constraints |
| Account state | Confirm account and margin context support the action |
| Symbol policy | Ensure only approved market instruments are processed |
| Open-position policy | Prevent conflicting or duplicate exposure |
| Idempotency | Prevent duplicate submission of the same event |
| Kill switch | Allow immediate operational stop |
| Reconciliation | Prevent blind retry after uncertain response |

## Fail-Closed Conditions

The system rejects or pauses when:

- required data is missing
- market data is stale
- risk cannot be calculated
- requested size violates constraints
- an open-position conflict exists
- account state is not acceptable
- broker response is uncertain
- duplicate signal ID already exists
- kill switch is active

## Profit-Lock Policy Status

Profit-lock trailing is under design review. It will not be mixed into historical results retroactively.

Planned labeling:

| Exit label | Meaning |
| --- | --- |
| `TP` | Intended target reached |
| `SL_LOSS` | Original stop closed trade at a loss |
| `PROFIT_LOCK` | Modified protective stop closed trade in profit |
| `BREAKEVEN` | Modified stop closed near entry |
| `MANUAL_CLOSE` | Human or external close |

This avoids counting a profitable protective-stop exit as a normal losing stop.

## Risk Register

| Risk | Impact | Probability | Mitigation |
| --- | --- | --- | --- |
| Duplicate execution | Critical | Medium | Deterministic IDs, state store, execution log |
| Lost broker response | Critical | Low | Persist `EXECUTING`, reconcile before retry |
| Wrong instrument | High | Low | Approved-symbol policy and adapter validation |
| Stale data | High | Medium | Closed-bar rule and timestamp validation |
| Over-sized position | Critical | Medium | Broker-spec-driven sizing and risk guard |
| Manual command error | High | Medium | SOPs, explicit flags, dashboard visibility |
| Misleading statistics | High | Medium | 100-trade threshold and result taxonomy |
| Public data leak | Critical | Low | Portfolio notice and security checklist |

