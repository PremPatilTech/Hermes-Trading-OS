# Personas

## System Operator

Needs:

- know whether the system is running
- see active trade state
- confirm whether a signal was accepted, rejected, or skipped
- avoid running duplicate execution commands
- review the dashboard without touching private server internals

Primary artifacts:

- dashboard
- journal CSV
- execution lifecycle
- incident response SOP

## Strategy Reviewer

Needs:

- inspect whether a signal type performs consistently
- compare outcome by setup type, timeframe, and market condition
- evaluate MFE/MAE before changing TP or trade-management policy
- separate system quality from trading performance

Primary artifacts:

- accuracy measurement plan
- trade journal schema
- roadmap
- sanitized journal rows

## Risk Reviewer

Needs:

- prove that risk checks happen before execution
- verify duplicate execution prevention
- review rejection reasons
- understand failure branches and escalation

Primary artifacts:

- risk governance
- state machine
- traceability matrix
- test strategy

## Technical Maintainer

Needs:

- understand component boundaries
- add adapters without changing risk policy
- debug uncertain execution states
- validate changes before forward-testing

Primary artifacts:

- architecture document
- ADRs
- UAT plan
- incident response SOP

## Incident Reviewer

Needs:

- reconstruct what happened
- identify the last known safe state
- determine whether a position exists
- decide whether manual review is required

Primary artifacts:

- execution state
- audit event
- journal row
- failure recovery flow

