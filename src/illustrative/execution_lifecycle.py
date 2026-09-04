"""Illustrative execution lifecycle only.

This file is intentionally sanitized. It demonstrates the state-oriented
design pattern used by Hermes Trading OS without publishing proprietary
strategy logic, broker configuration, or operational execution code.
"""

from dataclasses import dataclass
from enum import Enum


class ExecutionState(str, Enum):
    SIGNAL_CREATED = "SIGNAL_CREATED"
    VALIDATING = "VALIDATING"
    RISK_REJECTED = "RISK_REJECTED"
    SAFETY_REJECTED = "SAFETY_REJECTED"
    APPROVED = "APPROVED"
    EXECUTING = "EXECUTING"
    EXECUTED = "EXECUTED"
    BROKER_REJECTED = "BROKER_REJECTED"
    UNKNOWN = "UNKNOWN"
    RECONCILING = "RECONCILING"
    RECONCILED_EXECUTED = "RECONCILED_EXECUTED"
    UNKNOWN_NEEDS_REVIEW = "UNKNOWN_NEEDS_REVIEW"
    OPEN_MONITORING = "OPEN_MONITORING"
    CLOSED = "CLOSED"


TERMINAL_STATES = {
    ExecutionState.RISK_REJECTED,
    ExecutionState.SAFETY_REJECTED,
    ExecutionState.BROKER_REJECTED,
    ExecutionState.UNKNOWN_NEEDS_REVIEW,
    ExecutionState.CLOSED,
}


@dataclass(frozen=True)
class DecisionEvent:
    signal_id: str
    instrument_class: str
    timeframe: str
    side: str
    signal_type: str


def should_submit(state: ExecutionState) -> bool:
    """Return whether an event can move to broker submission."""
    return state == ExecutionState.APPROVED


def requires_manual_review(state: ExecutionState) -> bool:
    """Return whether the operator must inspect the event before any retry."""
    return state == ExecutionState.UNKNOWN_NEEDS_REVIEW

