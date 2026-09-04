# Case Study

## Executive Summary

Hermes Trading OS is a personal systems-engineering project focused on the discipline required to run automated trading workflows safely. The system is designed around controlled signal intake, deterministic risk review, execution-state management, failure recovery, journaling, and monitoring.

The public version documents the operating model and technical governance. It does not publish proprietary signal logic, private deployment details, or account-specific data.

## Problem

Trading automation can fail in ways that are not obvious from a chart or a simple script:

- a duplicate signal may execute twice
- a broker response may be lost after an order is accepted
- a trade may pass strategy logic but fail risk policy
- current-bar calculations may introduce lookahead bias
- manual reviews may be impossible without structured logs
- dashboards may show outcomes without explaining decision quality

Hermes treats these as product and systems problems, not only coding problems.

## Design Goal

Build a controlled trading workflow where every decision can answer:

- What event triggered this decision?
- What data was available at that time?
- Which validation stage accepted or rejected it?
- Was the event already processed?
- Was the broker response confirmed or uncertain?
- What did the journal record?
- What should the operator do next?

## Scope

Public scope:

- architecture
- operating principles
- state lifecycle
- risk governance
- test strategy
- UAT plan
- accuracy measurement plan
- sanitized mock events
- illustrative code

Private scope:

- proprietary strategy rules
- exact thresholds
- exact symbols
- broker and account identifiers
- production logs
- infrastructure details
- operational credentials

## System Outcome

The private implementation has reached controlled forward-testing with:

- deterministic event IDs
- pre-execution risk checks
- safety gate validation
- exactly-once execution coordination
- persistent execution state
- SQLite-style trade journaling
- dashboard reporting
- open-trade excursion tracking
- recovery path for uncertain broker responses

Trading performance is not published yet. The public policy requires 100 fully journaled trades before directional accuracy, expectancy, or profit-factor claims are made.

## What Makes This Project Different

Hermes is not presented as a signal-selling system. The value of the case study is the operating discipline:

- separating signal logic from risk and execution
- designing for failure before designing for speed
- treating rejected trades as valuable data
- making execution state auditable
- delaying performance claims until sample size is meaningful

