# D365 F&O Support Process

## 1. Intake
Capture in every ticket: legal entity, module, user and role, exact steps, exact error text (screenshot), time it happened, business impact (e.g. blocks payment run, month-end deadline), and whether it ever worked before.

## 2. Triage
| Priority | Example | Target response |
|---|---|---|
| P1 | Cannot post/close, payment run blocked, system down | Immediate |
| P2 | Workflow stuck for a team, batch job failing repeatedly | Same business day |
| P3 | Single-user issue with a workaround | 1-2 business days |
| P4 | Question / enhancement request | Scheduled |

## 3. Diagnose (work from simplest to most complex)
1. **Is it the user?** Security role, legal entity selected, document status, missing setup data.
2. **Is it the data?** Wrong dimension, closed ledger period, missing main account, blocked vendor/customer, wrong posting profile.
3. **Is it the configuration?** Workflow version/assignment, number sequence, parameters, posting setup.
4. **Is it a process/batch problem?** Batch job status, batch group, recurrence, dependencies.
5. **Is it a code/platform/integration issue?** Reproduce in a test environment, collect logs, escalate to the technical team or Microsoft/partner with evidence.

## 4. Root cause and fix
Record the root cause, not just the fix. Ask: could this happen again? If yes, add a runbook entry, a validation, or a user tip.

## 5. Escalation checklist
Before escalating: steps to reproduce, environment (prod/UAT), entity, exact error text, what has already been tried, business impact and deadline.

## 6. Communicate
Update the user at acknowledgement, when the cause is found, and on resolution. Plain language, no jargon, state what was changed and how to confirm it works.

## 7. Close the loop
Document the solution, tag the ticket with module and root-cause category, and review monthly for recurring issues (see `scripts/ticket_analysis.py`).
