"""Public illustrative journal schema for Hermes Trading OS."""

from dataclasses import dataclass


@dataclass(frozen=True)
class JournalRow:
    signal_id: str
    timestamp: str
    instrument_class: str
    timeframe: str
    side: str
    signal_type: str
    entry: float
    sl: float
    tp: float
    status: str
    final_result: str | None = None
    mfe_r: float | None = None
    mae_r: float | None = None
    notes: str | None = None

