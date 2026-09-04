# UAT Plan

## Objective

Validate that Hermes Trading OS can be operated safely in controlled forward-testing with clear evidence for accepted, rejected, executed, and closed events.

## UAT Entry Criteria

- Bridge/interface health check passes.
- Dashboard service is reachable through approved access path.
- Journal database is writable.
- State store is writable.
- No conflicting open-position state exists unless testing the block condition.
- Latest code version is verified.

## UAT Scenarios

| ID | Scenario | Expected Result |
| --- | --- | --- |
| UAT-001 | Start dashboard services | Tracker, renderer, and private HTTP service stay running |
| UAT-002 | Generate no-signal cycle | System records no execution and remains idle |
| UAT-003 | Process valid candidate event | Event moves through validation and execution lifecycle |
| UAT-004 | Re-run same event | Duplicate is blocked |
| UAT-005 | Risk-invalid event | Journal shows risk rejection |
| UAT-006 | Existing-position event | New execution is blocked |
| UAT-007 | Open trade monitoring | MFE/MAE and high/low update |
| UAT-008 | Closed trade reconciliation | Final result and R result update |
| UAT-009 | Dashboard refresh | Browser reflects refreshed HTML |
| UAT-010 | Stop services | PID files are cleaned and processes stop |

## Exit Criteria

- All P0 UAT cases pass.
- Any P1 failure has an owner and mitigation plan.
- No private data is exposed in exported reports.
- Accuracy metrics remain unpublished until 100 closed journal records.

## UAT Sign-Off Notes

The UAT plan validates operating behavior, not trading profitability. Performance review is governed by [Accuracy Measurement](10-accuracy-measurement.md).

