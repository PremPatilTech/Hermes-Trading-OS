# Traceability Matrix

| Requirement | Design Component | Validation |
| --- | --- | --- |
| Prevent duplicate execution | Execution state store, deterministic signal ID | T-001, T-002 |
| Reject unsafe risk | Risk engine | T-003 |
| Reject unsafe operations | Safety gate | T-004, T-009 |
| Block conflicting exposure | Open-position policy | T-008 |
| Handle broker rejection | Execution coordinator | T-005 |
| Recover uncertain response | Reconciliation workflow | T-006, T-007 |
| Preserve audit trail | Journal and state records | T-010, T-011 |
| Track trade quality | MFE/MAE journal fields | T-012, T-013 |
| Support review dashboards | CSV and HTML reporting | T-014, T-015 |
| Delay performance claims | Accuracy policy | 100-trade review gate |

