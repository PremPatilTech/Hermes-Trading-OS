# ADR-003: Adapter-Based Execution Interface

## Status

Accepted

## Context

Execution systems can become hard to maintain when strategy, risk policy, and broker-specific API behavior are coupled together.

## Decision

Hermes uses an adapter boundary for the execution interface. Risk and coordination layers call generic adapter methods rather than embedding terminal-specific logic throughout the system.

## Alternatives Considered

- Direct terminal calls from strategy code
- Broker-specific risk engine
- One monolithic execution script

## Trade-Offs

The adapter introduces an extra abstraction, but it protects the risk and state layers from broker-interface details.

## Consequences

- MT5-compatible execution can be documented without exposing private operational details.
- Future adapters can be evaluated without rewriting governance logic.
- Tests can use controlled adapter doubles.

