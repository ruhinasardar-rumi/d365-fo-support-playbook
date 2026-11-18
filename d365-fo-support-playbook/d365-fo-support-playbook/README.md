# D365 Finance & Operations Support Playbook

A portfolio project showing how I would approach functional support for **Microsoft Dynamics 365 Finance & Operations (F&O)**: triage, root-cause investigation, runbooks, UAT, month-end support, and spotting recurring issues.

## Honest scope
- I do not have access to a live D365 Finance & Operations environment. This project is based on **Microsoft Learn documentation and training I completed** (see `docs/study-log.md`), plus my background in IT support and ticket handling.
- The runbooks describe the approach I would follow and should be checked against a real environment.
- All tickets, users and data in `/data` are **synthetic**. No real company data is used.
- The UAT cases are written as examples and have not been run in D365.

## What's inside
| Folder | What it shows |
|---|---|
| `docs/support-process.md` | End-to-end support approach: intake, diagnosis, root cause, escalation, user communication |
| `docs/finance-process-cheatsheet.md` | GL, AP, AR, cash management, fixed assets, expenses, procurement, intercompany and where each commonly breaks |
| `docs/study-log.md` | My log of Microsoft Learn modules and documentation I studied (fill in as you go) |
| `runbooks/` | Troubleshooting guides: batch jobs, workflow approvals, data import (DMF), security roles, month-end close |
| `testing/uat-test-cases.csv` | Sample user acceptance test cases for a release or config change |
| `data/` | Synthetic support tickets and a synthetic security role assignment file |
| `scripts/ticket_analysis.py` | Finds recurring issues, resolution time, and top modules from the ticket log |
| `scripts/sod_check.py` | Flags users holding role combinations that conflict (segregation of duties) |

## Run the scripts
Python 3.8+, no extra libraries needed.
```
python scripts/ticket_analysis.py data/sample_tickets.csv
python scripts/sod_check.py data/sample_role_assignments.csv data/sod_rules.csv
```

## Skills demonstrated
Functional troubleshooting, finance process understanding (GL/AP/AR/month-end), security roles and access, data import validation, UAT, documentation, recurring-issue analysis, clear communication with finance and IT.
