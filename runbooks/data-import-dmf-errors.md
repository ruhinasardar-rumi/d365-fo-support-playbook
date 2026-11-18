# Runbook: Data Import Errors (Data Management Framework)

**Where:** Data management workspace > Import (data project), then Execution summary.

**Steps**
1. Open the import job's **Execution summary** and view staging and target errors.
2. Staging errors usually mean file format issues (wrong column mapping, wrong delimiter, bad date/number format).
3. Target errors usually mean data/validation issues (missing main account, invalid dimension combination, vendor/customer does not exist, duplicate key).
4. Fix the source file and re-import. Use validation before copying to target where available.
5. Confirm the records landed (open the form and spot check) and compare row counts.

**Checklist for users:** correct template/entity, correct legal entity, no extra blank rows, dates and decimals in expected format, reference data exists first (e.g. vendor groups before vendors).
