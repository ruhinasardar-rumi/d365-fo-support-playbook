# Finance Process Cheat Sheet (for support)

| Area | Typical flow | Where support issues usually appear |
|---|---|---|
| General ledger | Journal > validate > post; ledger calendar periods | Closed/on-hold period, missing or invalid financial dimension combination, journal approval stuck |
| Accounts payable | Vendor invoice > approval > posting > payment proposal > payment journal | Invoice workflow stuck, three-way match differences, blocked vendor, payment journal errors |
| Accounts receivable | Free text invoice / sales invoice > posting > customer payment > settlement | Wrong posting profile, unapplied payments, settlement problems |
| Cash and bank management | Bank statement import > reconciliation | Import format errors, unmatched transactions |
| Fixed assets | Acquisition > depreciation proposal > posting | Depreciation not posted, wrong book or profile |
| Expenses | Expense report > workflow approval > posting | Approver missing, policy violations, receipts |
| Procurement | Purchase requisition > PO > product receipt > invoice | Approval hierarchy, receipt/invoice mismatch |
| Intercompany | Intercompany journal or PO/SO across legal entities | Missing intercompany setup, due-to/due-from imbalance |
| Month-end | Subledger close, revaluation, depreciation, accruals, period lock | Open transactions, batch failures, revaluation not run before lock |

Tip: always ask "which legal entity?" first. Many "bugs" are a user working in the wrong company.
