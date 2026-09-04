# ADR-002: Fail-Closed Risk Governance

## Status

Accepted

## Context

Trading automation should not assume missing data is safe. If risk cannot be calculated, if account context is unclear, or if execution state is uncertain, the safest action is to stop.

## Decision

Hermes rejects or pauses execution when required inputs are missing, stale, conflicting, or uncertain.

## Alternatives Considered

- Continue with fallback defaults
- Retry until successful
- Allow operator override inside the execution path

## Trade-Offs

Fail-closed behavior may skip valid opportunities. The trade-off is accepted because preventing uncontrolled execution is more important than capturing every signal.

## Consequences

- Rejected events become useful audit data.
- Unknown states require reconciliation or manual review.
- Safety behavior is explainable after the fact.

