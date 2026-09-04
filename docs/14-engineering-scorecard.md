# Engineering Scorecard

## Purpose

This scorecard tracks system maturity without making premature trading-performance claims.

## Current Maturity Snapshot

| Area | Status | Evidence |
| --- | --- | --- |
| Architecture separation | Strong | Signal, risk, safety, execution, adapter, journal layers are separated |
| Idempotency | Strong | Deterministic signal identity and persistent state model |
| Risk governance | Strong | Fail-closed policy and multi-layer guardrails |
| Execution recovery | Strong | Unknown states route to reconciliation/manual review |
| Observability | Strong | Structured journal, dashboard, CSV export, MFE/MAE tracking |
| Test planning | Strong | 15 representative execution/journal/reporting scenarios |
| UAT process | Strong | Operational acceptance plan included |
| Public security boundary | Strong | Sanitized repo and explicit exclusion policy |
| Accuracy evidence | In progress | Public metrics pending 100 completed journal records |
| Trade-management optimization | In progress | Profit-lock trailing planned after baseline data |

## Maturity Scale

| Level | Meaning |
| --- | --- |
| 1 | Concept only |
| 2 | Prototype with unclear operating rules |
| 3 | Working flow with manual review |
| 4 | Risk-governed system with state and journal |
| 5 | Forward-tested system with measured performance and versioned trade management |

## Current Level

Hermes is currently assessed at **Level 4**.

The system is operationally governed and forward-testing is active. The project should not be considered Level 5 until the 100-trade review produces enough evidence to compare signal types, risk behavior, MFE/MAE, exit quality, and management-policy versions.

## What Moves It to Level 5

- 100 fully journaled trades
- published performance review
- signal-type segmentation
- profit-lock policy comparison
- dashboard v2 with open/closed trade analytics
- incident review summary
- updated roadmap based on measured data

