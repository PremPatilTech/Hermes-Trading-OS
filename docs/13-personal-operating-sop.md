# Personal Operating SOP

## Purpose

This SOP defines how Hermes Trading OS is reviewed, operated, and improved during controlled forward-testing.

It exists to prevent emotional changes, duplicate execution, undocumented intervention, and premature performance conclusions.

## Daily Start Checklist

1. Confirm system health.
2. Confirm journal storage is available.
3. Confirm dashboard service is reachable through the approved private access path.
4. Confirm no unexpected open-position conflict exists.
5. Confirm latest code version is known.
6. Confirm no kill-switch or incident state is active.

## During Operation

- Do not rerun the same execution event manually.
- Do not change risk policy during an open trade.
- Do not modify TP/SL rules without recording a management version.
- Treat rejected events as useful data, not as system failure.
- Keep dashboard and journal running before judging performance.

## After Each Closed Trade

Review:

- final result label
- MFE and MAE
- signal type
- timeframe
- whether trade management was modified
- whether the result supports or weakens the current hypothesis
- whether any incident response note is required

## Weekly Review

Focus on process quality:

- Were all trades journaled?
- Were rejected events explainable?
- Did the dashboard reflect current state?
- Were any manual actions untagged?
- Did any uncertain execution state occur?
- Were any assumptions changed too early?

## Change-Control Rule

No strategy, TP/SL, or trade-management rule should be changed because of one emotional trade result.

Policy changes require:

- journal evidence
- clear hypothesis
- version label
- UAT checklist update
- rollback plan

## 100-Trade Review Gate

Accuracy, expectancy, and signal-type ranking should not be treated as reliable until 100 fully journaled trades are available.

Until then, the main target is operational quality.

