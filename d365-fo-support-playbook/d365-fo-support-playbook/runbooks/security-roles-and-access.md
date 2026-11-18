# Runbook: User Access and Security Roles

**Where:** System administration > Users, and Security configuration.

**Symptoms:** user cannot see a menu item, button greyed out, "access denied," or cannot see a legal entity.

**Steps**
1. Confirm the user is enabled and the role assignment covers the right **legal entities** (assignments can be organization-scoped).
2. Check assigned roles. Compare to a colleague who can do the task.
3. Identify the missing duty/privilege through the role > duties > privileges hierarchy.
4. Request approval from the data owner/manager, assign the role, and have the user sign out and back in to test.
5. Check segregation of duties before granting (e.g. the same person should not create vendors and approve payments). See `scripts/sod_check.py`.
6. Document the request, approver and date for audit.

**Principle:** least privilege. Prefer standard roles; avoid custom roles without a need.
