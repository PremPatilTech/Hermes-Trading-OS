# Incident Response

## Incident Philosophy

Trading automation incidents must be handled slowly and visibly. The priority is to prevent duplicate execution, preserve evidence, and determine the true state before any corrective action.

## Severity Levels

| Severity | Definition | Response |
| --- | --- | --- |
| SEV-1 | Possible duplicate execution, unknown broker state, or uncontrolled exposure | Stop automation, inspect positions, preserve logs |
| SEV-2 | Dashboard/journal failure while execution is healthy | Stop reporting service or repair journal path |
| SEV-3 | Non-critical documentation or reporting mismatch | Fix in normal maintenance |

## Playbook: Unknown Execution State

1. Stop automated signal intake.
2. Do not retry the same event.
3. Inspect persistent execution state.
4. Inspect open positions through execution interface.
5. Inspect recent deal history.
6. Mark event as reconciled or manual review.
7. Record incident notes.

## Playbook: Duplicate Signal Attempt

1. Verify deterministic signal ID.
2. Confirm state store contains the event.
3. Confirm no second submission occurred.
4. If duplicate reached execution interface, escalate as SEV-1.
5. Add regression test if a new path caused the duplicate.

## Playbook: Dashboard Not Updating

1. Confirm tracker process is running.
2. Confirm journal database timestamp updates.
3. Confirm dashboard renderer is running.
4. Confirm HTTP service is serving the report.
5. Confirm browser cache or tunnel is not stale.

## Playbook: Public Data Leak

1. Remove the exposed artifact.
2. Rotate any affected credential or access token.
3. Rewrite public history if required.
4. Add the pattern to security checklist.
5. Document root cause privately.

