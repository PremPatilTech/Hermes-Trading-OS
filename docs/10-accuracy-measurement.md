# Accuracy Measurement

## Current Status

Hermes Trading OS is in active controlled forward-testing.

No public accuracy, expectancy, or profit-factor claim is made at this stage.

## Publication Threshold

The first public performance review requires:

- 100 fully journaled trades
- complete result labels
- MFE/MAE recorded where available
- skipped/rejected events counted separately
- manual interventions marked clearly
- signal-type segmentation included

## Metrics to Publish After 100 Trades

| Metric | Reason |
| --- | --- |
| Directional accuracy | Measures whether accepted direction was correct |
| Win rate | Basic closed-trade outcome rate |
| Profit factor | Total gains divided by total losses |
| Average R | Normalized expectancy per trade |
| Median R | Reduces distortion from outliers |
| Maximum drawdown | Measures downside pressure |
| TP hit rate | Shows target achievement |
| SL loss rate | Shows true protective-stop failures |
| Profit-lock exit rate | Tracks future management-rule exits |
| MFE by signal type | Shows whether targets are too conservative |
| MAE by signal type | Shows whether entries need more room |
| Rejection rate | Measures risk/safety filtering |
| Reconciliation count | Measures execution uncertainty |

## Review Rules

- No TP/SL policy change before the review window closes unless a safety issue exists.
- No signal-type promotion before sample size is meaningful.
- No public profit claim without journal-backed evidence.
- Any manually modified trade is tagged separately.
- Any future trailing rule gets its own management version.

## Example Reporting Language

Acceptable:

```text
Forward-testing in progress. Performance review planned after 100 fully journaled trades.
```

Not acceptable:

```text
High accuracy system.
Guaranteed profit.
Proven live performance.
```

## Why 100 Trades

Small samples can look impressive and still be meaningless. The 100-trade threshold forces patience, reduces emotional decision-making, and creates enough data to compare signal types, timeframes, MFE, MAE, and exit labels.

