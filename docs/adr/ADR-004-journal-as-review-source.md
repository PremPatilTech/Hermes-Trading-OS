# ADR-004: Journal as Review Source

## Status

Accepted

## Context

Raw logs are difficult to use for performance review, incident analysis, and signal-type evaluation.

## Decision

Hermes records normalized trade decisions and outcomes in a structured journal. The dashboard and CSV exports are generated from that journal.

## Alternatives Considered

- Console-only output
- Spreadsheet-only manual tracking
- Raw JSONL logs only

## Trade-Offs

A structured journal requires schema discipline. The benefit is that every outcome can be reviewed consistently across signal type, timeframe, MFE, MAE, and exit reason.

## Consequences

- Performance review can wait for a clean 100-trade sample.
- Profit-lock exits can be tracked separately from losing stops.
- Dashboard views can be regenerated without changing source data.

