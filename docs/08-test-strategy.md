# Test Strategy

## Testing Philosophy

Hermes testing prioritizes execution safety and state correctness before performance claims.

Trading systems can pass a backtest and still fail operationally. The test suite therefore focuses on:

- risk rejection
- safety rejection
- duplicate prevention
- state persistence
- broker-response uncertainty
- journal correctness
- dashboard/report generation

## Core Test Categories

| ID | Category | Scenario |
| --- | --- | --- |
| T-001 | Idempotency | Valid event executes once and stores executed state |
| T-002 | Idempotency | Duplicate signal does not submit a second request |
| T-003 | Risk | Oversized or invalid risk is rejected |
| T-004 | Safety | Unsupported account/instrument state is rejected |
| T-005 | Broker | Broker rejection is persisted without retry |
| T-006 | Recovery | Lost response reconciles if matching open position exists |
| T-007 | Recovery | Lost response enters manual review if not confirmed |
| T-008 | Exposure | Existing open position blocks new event |
| T-009 | Symbol policy | Mismatched instrument is rejected |
| T-010 | Journal | Trade journal records executed event |
| T-011 | Journal | Broker reference is preserved on status refresh |
| T-012 | Journal | MFE and MAE are updated from open trade tracking |
| T-013 | Journal | Closed trade is classified from execution history |
| T-014 | Reporting | CSV export is generated |
| T-015 | Reporting | Dashboard HTML is generated |

## Edge Cases

- signal repeats after process restart
- broker accepts order but response is lost
- broker rejects order with invalid stops
- position exists before new event
- journal refresh occurs without broker payload
- current price moves in favor then reverses
- trade closes outside intended TP/SL labels

## Test Evidence Policy

Public repository:

- includes test plan and representative scenario descriptions
- includes sanitized mock events
- excludes private test fixtures that reveal strategy or infrastructure details

Private implementation:

- tracks executable unit/integration tests
- requires test pass before operational changes
- validates new management rules separately before activation

