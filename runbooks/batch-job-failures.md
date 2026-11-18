# Runbook: Batch Job Failures

**Where:** System administration > Inquiries > Batch jobs (and Batch job history).

**Symptoms:** job in Error status, job stuck in Waiting or Executing, scheduled job never ran, results missing (e.g. no posted revaluation).

**Steps**
1. Open the batch job, note status, batch group, recurrence, and who created it.
2. View the batch job history / log and read the infolog message for the failing task.
3. Common causes:
   - User who created the job was disabled or lost permissions.
   - Batch group has no batch server assigned.
   - Job depends on another job that failed.
   - Locked or closed period, missing setup data, or bad data in the records processed.
4. Fix the cause, then re-run and confirm the output (e.g. posted transactions).
5. If it keeps failing with no data/config cause, collect log text, job ID, time and escalate to the technical team.

**Prevent:** document the owner of each recurring job; monitor Error status daily during month-end.
