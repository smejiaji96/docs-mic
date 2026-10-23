# SDD · Costo de servir

## Summary
It is entered only through the Portal (only people with access to the Portal); it updates on a schedule (last: October 7). Tasks to do: 2.

## 1. Project principles

**Starting point**
- Vulnerability (Low): It is entered only through the Portal; only people with access to the Portal can get in (according to the inventory owner)
- Stability (Low): Scheduled refresh; last: October 7, 2026 (according to the active report in the Portal)
- Scalability (Low): 12 MB model (according to the previous public link)

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | Done | It is entered only through the Portal; only people with access to the Portal can get in. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | Partial | It updates by itself (last: October 7); the failure notice still has to be turned on. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (Done): That only people with a company account get in — It is already entered only through the Portal.
- **US-002A** (Done): That it updates by itself and shows when — It updates by itself and shows its date.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup.
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | Done |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | Done |
| FR-005 | The system SHOULD remove duplicate or hidden pages that have no documented purpose. Delete or document 1 hidden page. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | Done |
| FR-007 | The system MUST show on every report the date and time of its last refresh. | Done |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “Costo de servir” in a private window: it must ask for an account. | Done |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | Done |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| How is Cost to Serve accessed? | It is only entered through the Portal, and only people with access to that Portal can get in. |
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that the people who use it have a company email (Falcon Farms); they should have one.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Access from a single site | Sign in with the company account (Microsoft) from a single entry site, for example the Portal, open to the whole organization | The people who use the tools should have a company account and their roles are already in each record; there is no need to create groups by role. Cost to Serve is already used through the Portal, and unifying avoids loose links. |
| Public links | Withdraw the public links that exist; publishing to the web stays limited to those with Power BI Pro | The people with access can publish and withdraw links on their own; the links that exist stay open to anyone until they are withdrawn (third-party sources consulted). |
| Refresh | Scheduled update in Power BI, with a notice to the owner and the backup if it fails | Removes manual updating and warns of failures. Several reports already have a “Last Refresh” table that is reused. |

### Phases that apply

- Phase 1: Secure access to dashboards
- Phase 2: Reliable and visible refresh
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Viewers who do not yet have or do not use a company account | Verify each dashboard's user list (the roles are already in each record) before withdrawing the links; anyone without a company email is resolved first. |
| Removing the public link interrupts whoever uses it | Warn beforehand, validate the new access and withdraw the link last, one dashboard at a time. |

## 5. Tasks

- [ ] T-001: “Costo de servir” is already entered only through the Portal, which serves as the model for the single site (Done · First)
  - Done when: It opens only with an account, from a single site.
- [ ] T-002: Clean up “Costo de servir”: delete or document 1 hidden page (To do · Next)
  - Done when: No free comments or unexplained hidden pages remain.
- [ ] T-004: Confirm whether “Costo de servir” has failed and turn on the failure notice to the owner and the backup (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Costo de servir” (T-001, T-002, T-004) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-002, T-004 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: confirm that only people with access to the Portal get in | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |
