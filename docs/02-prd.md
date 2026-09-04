# Product Requirements Document

## Product Name

Hermes Trading OS

## Product Summary

Hermes Trading OS is a risk-controlled trading automation workflow for gold and currency-market instruments. It receives market decision events, normalizes them, validates risk and safety constraints, coordinates execution through an adapter interface, and records outcomes in an auditable journal.

## Goals

- Convert eligible signal events into controlled execution decisions.
- Prevent duplicate processing of the same decision event.
- Reject events that violate risk, safety, or operational constraints.
- Persist state before execution to support failure recovery.
- Record accepted, rejected, executed, and closed outcomes.
- Provide a dashboard-ready journal for operational review.
- Support controlled forward-testing before public performance claims.

## Non-Goals

- Publish proprietary strategy rules.
- Publish exact entry or exit formulas.
- Publish account, broker, or infrastructure details.
- Optimize for high-frequency execution.
- Make unverified profitability claims.
- Replace human review of system changes.

## Users and Stakeholders

- System operator
- Strategy reviewer
- Risk reviewer
- Technical maintainer
- Incident reviewer

See [Personas](03-personas.md).

## Functional Requirements

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-001 | Generate deterministic IDs for decision events | P0 |
| FR-002 | Reject duplicate event IDs before execution | P0 |
| FR-003 | Validate risk before execution | P0 |
| FR-004 | Validate symbol, volume, margin, and operational state | P0 |
| FR-005 | Persist `EXECUTING` state before broker submission | P0 |
| FR-006 | Reconcile uncertain broker responses before retry | P0 |
| FR-007 | Log all execution outcomes to journal | P0 |
| FR-008 | Track open-trade high/low excursion | P1 |
| FR-009 | Generate dashboard and CSV reports | P1 |
| FR-010 | Run controlled signal watcher for forward-testing | P1 |

## Non-Functional Requirements

| ID | Requirement | Target |
| --- | --- | --- |
| NFR-001 | Determinism | Same closed-bar input produces same event ID |
| NFR-002 | Auditability | Every execution decision can be reviewed from journal/state |
| NFR-003 | Safety | Unknown states fail closed |
| NFR-004 | Maintainability | Risk, execution, and adapter layers remain separate |
| NFR-005 | Portability | Public artifacts remain broker-agnostic and sanitized |

## Acceptance Criteria

- Duplicate events do not create duplicate execution attempts.
- Open-position conflicts block new execution.
- Risk rejection records a journal row.
- Broker rejection records a terminal state.
- Lost broker response enters reconciliation before manual review.
- Journal exports include signal ID, side, entry, SL, TP, status, result, MFE, MAE, and high/low.
- Accuracy reporting remains withheld until the 100-trade threshold.

## Dependencies

- Market data source
- MT5-compatible execution adapter
- Persistent state store
- Trade journal database
- Dashboard renderer
- Operational monitoring scripts

## Risks

See [Risk Governance](06-risk-governance.md) and [Incident Response](12-incident-response.md).

