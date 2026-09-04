# Roadmap

## Current Phase: Controlled Forward-Testing

Focus:

- keep journal and dashboard active
- collect clean trade outcomes
- verify close reconciliation
- avoid premature performance conclusions

## Near-Term Roadmap

| Phase | Workstream | Outcome |
| --- | --- | --- |
| P0 | Observability stability | Always-on tracker, dashboard refresh, journal export |
| P1 | Signal watcher | Automatic polling of selected timeframes with explicit enable flag |
| P1 | Close reconciliation | Final result taxonomy and journal close automation |
| P2 | Dashboard v2 | Open trade panel, MFE/MAE charts, signal-type summaries |
| P2 | Profit-lock v1 | Conservative breakeven/profit-lock rule after clean baseline |
| P3 | Replay comparison | Compare fixed exits versus staged trade management |
| P3 | 100-trade review | Publish first performance summary if data quality is sufficient |

## Profit-Lock Roadmap

Planned rule evaluation:

- fixed TP/SL baseline
- breakeven after favorable movement
- small profit buffer after favorable movement
- staged protection after stronger favorable movement
- signal-type-specific management

Profit-lock logic will not be activated retroactively. It must be tagged with a management version so results remain comparable.

## Public Repo Roadmap

- add polished architecture diagrams
- add dashboard screenshot gallery
- add traceability matrix
- add sample UAT evidence pack
- add 100-trade review after enough journaled outcomes exist

