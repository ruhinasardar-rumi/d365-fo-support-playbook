# Runbook: Workflow Approval Stuck

**Symptoms:** document submitted but no approver sees it; approver sees it but cannot act; workflow shows an error.

**Steps**
1. Check the document's workflow status and open **Workflow history** to see which step it is on and who it is assigned to.
2. Verify the assignee: is the user active, in the correct legal entity, and did they set a delegation or go on leave?
3. Check the workflow configuration for the module: is the right version active, does the condition match this document (amount, entity, type)?
4. Check the approval hierarchy or role/position assignments if the step uses them.
5. Resolve: reassign or delegate the work item, fix the configuration, or cancel and resubmit the workflow if the instance is broken.
6. Confirm with the user and add the cause to the ticket.

**Common root causes:** approver missing a security role, hierarchy gap, condition not matching, workflow version not activated after a change.
