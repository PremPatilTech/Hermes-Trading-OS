# ADR-001: Deterministic Execution Identity

## Status

Accepted

## Context

Automated trading workflows may process the same market event more than once because of repeated commands, service restarts, or duplicate polling cycles.

## Decision

Every candidate decision receives a deterministic signal ID derived from sanitized event attributes such as instrument class, timeframe, setup category, event time, and direction.

## Alternatives Considered

- Random UUID per execution attempt
- Timestamp-only identity
- Broker-ticket-only identity

## Trade-Offs

Deterministic identity requires careful event normalization, but it prevents repeated processing of the same market decision.

## Consequences

- Duplicate execution attempts can be blocked before broker submission.
- Journal rows can be merged by signal ID.
- Backtesting, forward-testing, and review artifacts can refer to the same event consistently.

