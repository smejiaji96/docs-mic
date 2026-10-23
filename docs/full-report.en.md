# MIC tool inventory · Full report (English)

General analysis of the 17 tools, summary and the analysis of each one, plus that of the FIT application. Version 1.20. It contains no people names, emails, phone numbers, rates or links; it is internal information.

## Contents

1. Project Constitution (the principles that are not negotiable): mic-tools-governance
2. Feature Specification (what is needed): MIC tool governance: secure access and reliable refresh
3. Implementation Plan (how it is done): MIC tool governance: secure access and reliable refresh
4. Task Breakdown (the tasks): MIC tool governance: secure access and reliable refresh
5. Glossary in plain words
6. Action plan to load the work list: 001-secure-reliable-mic-tools
7. Summary of each tool
8. SDD · Sprouts Execution Report
9. SDD · Performance Audit Walmart
10. SDD · SPR Sales Report
11. SDD · Walmart Audit
12. SDD · Costo de servir
13. SDD · Last Visit
14. SDD · Visit FS
15. SDD · Costco Report
16. SDD · AFS Error Report
17. SDD · Travel Approval Request
18. Spec · Incident Reporting Route
19. SDD · Walmart Audit
20. SDD · Time Correction
21. Spec · DSD Store Master
22. Spec · DSD Route Master
23. Spec · DSD FS Route Master
24. Spec · Plan de visitas (Unify)
25. Spec · Stores Contact List
26. SDD · FIT

---

# Project Constitution (the principles that are not negotiable): mic-tools-governance

## What this is for

These are the principles that govern the mic-tools-governance project. The whole specification, plan and tasks must respect them. An exception needs a written justification in the plan.

## Starting point (where we are today)

- The Power BI dashboard links that exist today are public: anyone who has the link can open them, with no account.
- The forms can also be opened and answered by anyone who has the link.
- Cost to Serve is the only dashboard entered through a Portal, and only people with access to that Portal can get in.
- The Excel databases, on SharePoint, do ask for a company account and permission.
- Only people with Power BI (Power BI Pro) access can publish links to the web; it is a limited permission.

---

## Principle I: Sign in with the company account

Whoever enters a tool with sensitive information does so with their company account (Falcon Farms email).

**What it means:**
- If something must be public, it is justified and approved.
- Managers and other users see all the information in their dashboards. What each person sees is not limited.
- Freely written comments are never published.

---

## Principle II: Data in a company place

Data lives in a company place, with an owner and reviewed permissions; never in someone's personal account.

**What it means:**
- There is a single master list of stores.
- The Excel databases can be moved to a server, for security (suggestion).

---

## Principle III: Up-to-date information

Each report updates by itself and shows when; each file notes when and by whom it was updated.

**What it means:**
- Updating by hand is only valid as a noted exception.
- If an update fails, the owner and the backup are told.

---

## Principle IV: Owners

Each tool has an owner and a backup, both people.

**What it means:**
- A team or department cannot be the only person in charge.
- There is a plan for when the owner, the creator or the license changes.

---

## Principle V: Document and change in an orderly way

Each tool has its record up to date on 7 topics, and changes are written down before they are made.

**What it means:**
- Each item is marked as verified, inferred, pending or suggestion; pending items are reviewed every quarter.
- These documents carry no people names, emails, phone numbers or rates.

---

## Approved tools

### Approved list
| Topic | Tool | Needs approval to change? |
|---|---|---|
| Reports | Power BI | Yes |
| Sign in with the company account | Company accounts (Microsoft) | Yes |
| Forms | Microsoft Forms | No |
| Master databases | Database server (suggested); today Excel on SharePoint | No |
| Work list | Azure DevOps or GitHub (to decide) | To decide |

### How a tool is changed

Changing an approved tool requires:
1. A short note with the decision and the reason
2. Checking which parts of the specification are affected
3. Updating the principles if the change touches them

---

## Changes to the principles

| # | Date | What changed | Why |
|---|---|---|---|
| 1 | 2026-10-13 | Initial principles | Project start |
| 2 | 2026-10-13 | Identity expected: company-domain accounts (to verify) | Clarification answers |

---

# Feature Specification (what is needed): MIC tool governance: secure access and reliable refresh

## Overview (summary)

**Feature Name:** MIC tool governance: secure access and reliable refresh
**Feature Number:** 001
**Date:** 2026-10-13
**Author:** Generated from the MIC inventory documentation
**Status:** Draft

### Problem Statement (what is wrong)

The dashboards, forms and databases in the MIC inventory hold sensitive information that is key to the operation, but some are public to anyone with the link, part of the information is refreshed by hand and several files or tools depend on a single person or a personal account.

### Proposed Solution (what is proposed)

That every tool has controlled access, information that refreshes by itself and in plain view, a registered owner and backup, and tidy sources, so the team trusts the figures and the operation does not depend on one person.

### Target Users (who it is for)

- Inventory owner: coordinates documentation and changes.
- Tool administrator: maintains a dashboard, form or file.
- Report consumer: managers, supervisors and teams who use the dashboards.
- IT and BI team: approves access and platform changes.

---

## User Stories (what people need)

### US-001: Secure access to dashboards
As a company person who uses the dashboards, I want to sign in with my company account, So that the operation's information is not open to anyone.

**Acceptance Criteria (how to check it):**
- Given a dashboard with sensitive information, When someone opens its link without signing in, Then they cannot see the content
- Given a person with a company account, When opens the dashboard with their account, Then can see the content

**Independent Test (how to test it on its own):** Open each dashboard in a private window and confirm it asks for sign-in.
**Priority:** Must Have (essential)

### US-002A: Automatic and visible refresh
As a person who reads the reports, I want to that each report updates by itself and shows when it was updated, So that I can trust that the figures are up to date.

**Acceptance Criteria (how to check it):**
- Given a report with a schedule, When the scheduled time arrives, Then its data refreshes without manual intervention
- Given an open report, When its header is looked at, Then it shows the date and time of its last update

**Independent Test (how to test it on its own):** Check that each report updates by itself and shows its date and time.
**Priority:** Must Have (essential)

### US-002B: Notice if an update fails
As a tool owner, I want to to know if an update fails, So that I can fix it before anyone uses old figures.

**Acceptance Criteria (how to check it):**
- Given an update that fails, When it ends with an error, Then the owner and the backup receive a notice
- Given the refresh history, When it is reviewed with the administrator, Then it is known whether there were failures

**Independent Test (how to test it on its own):** Cause a test failure and confirm the notice arrives.
**Priority:** Must Have (essential)

### US-003A: Registered owner
As a inventory owner, I want to that each tool has its owner recorded (its creator), So that it is known who answers for it.

**Acceptance Criteria (how to check it):**
- Given a tool in the inventory, When its record is consulted, Then it shows an owner who is a person

**Independent Test (how to test it on its own):** Review the 17 records and confirm all have an owner.
**Priority:** Must Have (essential)

### US-003B: Registered backup
As a inventory owner, I want to that each tool has a backup recorded, So that continuity does not depend on a single person.

**Acceptance Criteria (how to check it):**
- Given a person leaves their role, When their replacement is assigned, Then the tool keeps operating without losing access

**Independent Test (how to test it on its own):** Review the 17 records and confirm all have a backup.
**Priority:** Must Have (essential)

### US-004: Tidy data sources
As a data analyst, I want to the master databases in a company place, with a single master list of stores, So that figures match and key files are not lost.

**Acceptance Criteria (how to check it):**
- Given a master file, When its location is consulted, Then it is on a team site, not in a personal account
- Given two reports that use the store master, When the same data point is compared, Then both show the same value

**Independent Test (how to test it on its own):** Confirm the location and permissions of the 4 files and compare one master data point in two reports.
**Priority:** Should Have (important)

### US-005: Controlled forms
As a form administrator, I want to that only company people respond and that responses have a destination, So that there are no false responses and no responses are lost.

**Acceptance Criteria (how to check it):**
- Given a form limited to company accounts, When someone without a company account tries to respond, Then they cannot submit the response
- Given a form with responses, When where they are stored is consulted, Then a destination and retention time are defined

**Independent Test (how to test it on its own):** Try to respond to each form from a non-company account and from a company account.
**Priority:** Should Have (important)

### US-006: Shared definitions
As a data analyst, I want to a glossary with the definitions of the key figures, So that everyone interprets them the same way.

**Acceptance Criteria (how to check it):**
- Given a key figure in a report, When its definition is looked up, Then there is a written definition and a documented formula

**Independent Test (how to test it on its own):** Pick 5 key figures and verify each has a definition and a formula.
**Priority:** Should Have (important)

---

## Functional Requirements (what must be met)

### Access

**FR-001:** The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created.
**FR-002:** The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design.
**FR-003:** The system MUST hide or restrict pages with free-text comments.
**FR-004:** The system MUST keep giving managers and other users access to all the information in their dashboards, without limiting what each person sees.
**FR-005:** The system SHOULD remove duplicate or hidden pages that have no documented purpose.

### Refresh

**FR-006:** The system MUST refresh every report on a defined schedule.
**FR-007:** The system MUST show on every report the date and time of its last refresh.
**FR-008:** The system MUST notify the owner and the backup when a refresh fails.

### Ownership and Documentation

**FR-009:** Every tool MUST have its owner recorded (its creator).
**FR-010:** Every tool MUST have a backup recorded, who is a person.
**FR-011:** The system MUST keep the 7-area documentation per tool.
**FR-012:** The system SHOULD maintain a glossary with the definitions and formulas of the key figures.

### Data and Forms

**FR-013:** The system MUST keep every master database in a company-controlled place, never in a personal account, with reviewed permissions. Moving them to a server is suggested, for security.
**FR-014:** The system SHOULD keep a single master list of stores and retire the copies.
**FR-015:** The system MUST limit who can respond to each form to people with a company account.
**FR-016:** The system MUST define the destination and retention time of each form's responses.

---

## Entity Overview (what this document talks about)

Tool: A dashboard, form, Excel database or application in the inventory, with a type, a use and a status.
Report: A dashboard-type tool, made of pages, some of them hidden.
Data Source: System or file that feeds one or more tools.
Responsible Person: Owner or backup of a tool.
Access Group: Set of people authorized to see one or more tools.
Refresh Schedule: Frequency and time at which a report refreshes, with its history.

---

## Success Criteria (how we will know it worked)

SC-001: 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions.
SC-002: 100% of reports refresh on a schedule and show the date and time of their last refresh.
SC-003: 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded).
SC-004: No master file remains in a personal account.
SC-005: A failed refresh is detected by its owner in less than 1 business day.
SC-006: The pending documentation lines drop from 32 to fewer than 10.

---

## Assumptions & Dependencies (what we take for granted and what we depend on)

### Assumptions
- The current inventory documentation is the baseline.
- The people who use the dashboards (district managers, regional managers, field supervisors and administration) should have a company email with the Falcon Farms email; this is verified when the access groups are created.
- The people who fill in the forms should have a company account; this is verified before limiting access. Today they do not sign in.
- The 4 remaining applications are outside this version; FIT is analysed separately.
- Cost to Serve is already consumed through the Portal and its direct link can be withdrawn, according to the inventory owner.
- The Excel files are updated as needed, not on a schedule.
- Managers need access to all the information in their dashboards.

### Dependencies
- Approval from IT and from the reporting platform administrator to change the access configuration.
- Owners of the external sources (Zona DSD, CopCot and others) to document their method and frequency.
- The administrators of each tool to record owner and backup.

---

## Scope Boundaries (what is in and out)

### In Scope
- 8 dashboards, 5 forms and 4 Excel databases.
- Access, refresh, owners, sources, forms and glossary.

### Out of Scope
- The 4 remaining applications (Tallie, AFS Console, Staffing Request and Portal). FIT has its own analysis, separate from this one.
- Rebuilding the reports or changing the definition of business figures.

### Future Considerations
- Centralized monitoring and alerts.
- Consolidating the monthly Unify files into a database.

---

## Clarifications Log (questions and answers)

| # | Question | Answer | Date | Impact |
|---|---|---|---|---|
| 1 | How is Cost to Serve accessed? | It is only entered through the Portal, and only people with access to that Portal can get in. | 2026-10-12 | FR-001, FR-002 |
| 2 | Who owns each report? | Its creator. | 2026-10-12 | FR-009 |
| 3 | Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. | 2026-10-12 | FR-006 |
| 4 | Who receives each form's responses? | Its administrator, who also updates it. | 2026-10-12 | FR-009, FR-016 |
| 5 | Who are the external viewers of the public dashboards and do they have company accounts? | They are district managers, regional managers and field supervisors, who should have a company email (Falcon Farms), and administration, which should also have one. Anyone with the link can see the information today. It remains to verify that everyone has a company email. | 2026-10-13 | FR-001, US-001 |
| 6 | Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. | 2026-10-13 | FR-002 |
| 7 | Must the people who respond to the forms sign in? | Not today; the people who fill them in should have the company email, to be verified. | 2026-10-13 | FR-015, US-005 |
| 8 | Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. | 2026-10-13 | Principle 1, FR-001, FR-002 |
| 9 | Are access groups created by role? | No; the roles are already listed in each tool and access is for people with the company email. | 2026-10-13 | FR-001 |
| 10 | How often are the Excel files updated? | As needed. | 2026-10-13 | US-004 |
| 11 | Could the Excel databases be migrated to a server? | Yes, as a suggestion for security. | 2026-10-13 | FR-013, US-004 |
| 12 | Who can publish to the web? | The people with Power BI (Power BI Pro) access; it is a limited permission. | 2026-10-13 | FR-002 |
| 13 | Should each person see only their own? | No: managers need access to all the information. | 2026-10-13 | FR-004 |

### Open Questions

- None: all clarification questions are answered.

---

# Implementation Plan (how it is done): MIC tool governance: secure access and reliable refresh

## Plan Metadata

| Field | Value |
|---|---|
| Feature | 001-secure-reliable-mic-tools |
| Date | 2026-10-13 |
| Spec | [spec.md](./spec.md) |
| Constitution | [constitution.md](../../constitution.md) |

---

## Pre-Implementation Gates (check before starting)

Before moving on, check that the principles are respected:

- [ ] Principle 1: Sign in with the company account: account access and the withdrawal of public links are planned (US-001).
- [ ] Principle 2: Data in a company place: the single master list and the controlled place are planned (US-004).
- [ ] Principle 3: Up-to-date information: scheduled update, visible date and failure notices are planned (US-002A, US-002B).
- [ ] Principle 4: Owners: owner and backup per tool are defined (US-003A, US-003B).
- [ ] Principle 5: Document and change in an orderly way: the 7-topic documentation and the glossary are planned (US-006).

---

## Architecture Overview (how it all fits)

### System Context (where we are)

This plan changes how people get in, who is responsible and where the data of the 17 tools of the MIC inventory lives. Nothing new is programmed.

### Data Flow (how data travels)

The sources (other systems and the master Excel files) feed the data models of the reports. People see the reports by signing in with their account. The forms store their responses in a defined destination, and one of them feeds a dashboard.

### Technology Decisions (choices of tools)

| Topic | What is chosen | Why |
|---|---|---|
| Access from a single site | Sign in with the company account (Microsoft) from a single entry site, for example the Portal, open to the whole organization | The people who use the tools should have a company account and their roles are already in each record; there is no need to create groups by role. Cost to Serve is already used through the Portal, and unifying avoids loose links. |
| Public links | Withdraw the public links that exist; publishing to the web stays limited to those with Power BI Pro | The people with access can publish and withdraw links on their own; the links that exist stay open to anyone until they are withdrawn (third-party sources consulted). |
| Refresh | Scheduled update in Power BI, with a notice to the owner and the backup if it fails | Removes manual updating and warns of failures. Several reports already have a “Last Refresh” table that is reused. |
| Master databases | Move the 4 Excel databases to a server (suggested), with a single master list of stores | Improves security compared with Excel files and avoids different figures across reports. |
| Forms | Forms owned by a group, only for company people, with responses stored in a company place | The form does not depend on one person and responses have a defined destination and retention time. |
| Registry and documentation | This inventory page as the registry, reviewed every quarter | It already has the 7-topic documentation and the risk matrix. |
| Work list | Azure DevOps (organization “FALCON FARMS”; project “Inventario de herramientas”) | It is loaded with a ready-to-import CSV file (see point 6); the direct connection is optional. |

---

## Project Structure (how files are organized)

```
mic-tools-governance/
├── constitution.md
├── registry/tools.csv
├── docs/                 # one record per tool (7 areas)
├── access/               # sign-in rollout, link retirement, hidden pages
├── refresh/              # schedules, freshness card, failure notices
├── ownership/            # owners, backups, continuity plan
├── data/                 # master files, permissions, single store master
├── forms/                # respondents, responses, backups
├── review/               # integration, success criteria, security
└── glossary.md
```

**Structure Decision:** A folder of documents and configuration (no code), organized by topic: access, refresh, owners, data and forms.

---

## Implementation Phases

### Phases 1 to 6: one per need
Each phase solves one need and can be delivered on its own, in priority order (see the tasks).

### Final phase: close
Review with IT, check of the success criteria and inventory update.

---

## Definitions for US-003 (resolved, no tasks)

- **D-1 Owner:** The owner of each tool is its creator (report, form or file), as recorded in the inventory. For forms, it is the person who administers them and receives the responses.
- **D-2 Backup:** The backup is a person on the same team, different from the owner, designated by the area lead and recorded in the “Backup” field of the record. A team or department cannot be the backup or the sole administrator.
- **D-3 Continuity plan:** If the owner, the creator or the license changes: (1) the backup takes over; (2) ownership of the report, form or file is transferred on the platform; (3) the inventory is updated; (4) access is reviewed; (5) whoever manages the license or capacity is informed.
- **D-4 Quarterly review:** Every quarter the documentation, owners and backups, pending items, access and refresh schedules are reviewed. The date of each review is recorded in the inventory.

---

## Risk Assessment (risks and how to avoid them)

| Risk | Impact | Probability | How to avoid it |
|---|---|---|---|
| Viewers who do not yet have or do not use a company account | High | Medium | Verify each dashboard's user list (the roles are already in each record) before withdrawing the links; anyone without a company email is resolved first. |
| Removing the public link interrupts whoever uses it | Medium | High | Warn beforehand, validate the new access and withdraw the link last, one dashboard at a time. |
| IT does not agree with the access change | High | Medium | Present the risk matrix to them before starting. |
| Scheduling refresh requires credentials or a gateway | Medium | Medium | Document each model's source and test refresh on one report before generalizing. |
| The owner or creator changes role during the project | Medium | Medium | Record a backup from Phase 1. |
| Large models take long to refresh (Last Visit, 331 MB) | Medium | Low | Measure refresh time before scheduling it. |
| Form respondents will have to sign in for the first time | Medium | Medium | Announce beforehand, test with a few people and keep the same link. |
| Moving the Excel databases to a server interrupts whoever uses them today | Medium | Medium | Move one database at a time, warn beforehand and keep the original file until the result is validated. |

---

## Complexity Tracking (how hard each part is)

| Component | Estimate | Confidence | Notes |
|---|---|---|---|
| Shared store master | L | Low | Affects all 8 models. |
| Withdrawal of public links | S | High | Once the new access is validated. |
| Scheduled refresh | M | Medium | Depending on credentials and model size. |
| Controlled forms | S | Medium | Five forms, configuration change. |

---

# Task Breakdown (the tasks): MIC tool governance: secure access and reliable refresh

## How to read the tasks

- **[P]** = can be done at the same time as others
- **[Story: USX]** = which need the task belongs to
- **[Dep: T-NNN]** = cannot start until task T-NNN is finished
- File paths are relative to the project folder
- Tasks follow the plan's structure
- Code tests are not required; review tasks are used instead

---

## Phase 1: Secure access to dashboards

Essential.

- [ ] T-001: Move the public dashboards, one at a time, to company-account access from a single site (for example the Portal) and withdraw the direct public links (Cost to Serve already enters through the Portal) [Story: US-001]
  - Done when: Each one opens only with an account and from a single site; the public links no longer open without an account (tested in a private window).

- [ ] T-002: Clean up the dashboards: hide the free-comment pages and delete or document the 13 hidden pages (SPR 1, Walmart Audit 3, Cost to Serve 1, Last Visit 5, Costco 3) [P] [Story: US-001]
  - Done when: No free comments or unexplained hidden pages remain.

---

## Phase 2: Reliable and visible refresh

Essential.

- [ ] T-003: Schedule the update of Performance Audit Walmart and Sprouts Execution Report, and add the visual with the date and time of the last update where it is missing (Costco Report) [P] [Story: US-002]
  - Done when: Both update by themselves and every report shows its update date and time.

- [ ] T-004: Confirm whether the updates have failed and turn on the failure notice to the owner and the backup; review with the administrator the history of SPR, Walmart Audit and Costco [Dep: T-003] [Story: US-002]
  - Done when: It is known whether there were failures and a test failure notifies both.

---

## Phase 3: Owner and backup per tool

No tasks: resolved by rules D-1 to D-4 (see plan) and the “Backup” field of each inventory record.

---

## Phase 4: Tidy databases

Important.

- [ ] T-005: Move the 4 Excel databases to a server, with a single master list of stores; review permissions, note who updates them and when, and take the files out of personal accounts [Story: US-004]
  - Done when: The databases are on the server, show their last update and who has access, and no file remains in personal accounts.

---

## Phase 5: Controlled forms

Important.

- [ ] T-006: Limit the 5 forms to people with a company account and define where the responses are stored [P] [Story: US-005]
  - Done when: An outside account cannot respond and each form has a response destination.

---

## Phase 6: Shared definitions

Important.

- [ ] T-007: Create the glossary of abbreviations and key figures (SL, DL, RTV, AUR, effective visit, evaluated store, Audit Rating %) [P] [Story: US-006]
  - Done when: Each term has a written definition.

---

## Final phase: Close

Depends on everything above.

- [ ] T-008: Final review with IT: check the success criteria and update the inventory documentation [Dep: T-001, T-002, T-003, T-004, T-005, T-006, T-007]
  - Done when: The 6 criteria are measured and pending items drop below 10.

---

## Previous tasks

- ~~T-001 to T-026 (v1.7): Tasks of earlier versions~~ — Replaced: merged into 8 tasks with no repeats. The Phase 0 setup and the IT inquiry about publishing were removed, and the tasks that made the same step were joined (access and single link; database and its register).

## What goes first

```
T-001                                  → US-001
T-002 (in parallel)                    → US-001
T-003 ── T-004                         → US-002A / US-002B
T-005                                  → US-004
T-006                                  → US-005
T-007                                  → US-006
T-001 to T-007 ── T-008               → close
```

## How they are loaded into the work list

| Task | GitHub Issue Label | Azure DevOps Type | Priority |
|------|--------------------|-------------------|----------|
| T-001..T-002 | `story:US-001` | PBI (under Feature) | P0-P1 |
| T-003..T-004 | `story:US-002` | PBI (under Feature) | P0-P1 |
| T-005 | `story:US-004` | PBI (under Feature) | P1 |
| T-006 | `story:US-005` | PBI (under Feature) | P0 |
| T-007 | `story:US-006` | PBI (under Feature) | P2 |
| T-008 | `phase:integration` | Task (under Feature) | P1 |

---

# Glossary in plain words

- **Publish to web:** A Power BI option that gives a link open to anyone, with no account required. It is what the public dashboards use today. The people with Power BI Pro access can use it.
- **Portal:** The company site from which Cost to Serve is entered. It asks for a sign-in.
- **Company account:** The user with a Falcon Farms email that each person uses to get into the systems.
- **Report data model (semantic model):** Where the report stores and organizes its data. Several reports can use the same one.
- **Scheduled update:** The report updates by itself, at a fixed time, without anyone doing it by hand.
- **DirectQuery (live query):** The report asks the source for the data every time it is opened, instead of keeping a copy.
- **Database server:** A central, protected place where data lives, better than loose Excel files.
- **Owner and backup:** The owner answers for the tool; the backup replaces them when they are away. Both are people.
- **Verified, Inferred, Pending, Suggestion:** Verified: confirmed. Inferred: deduced, not confirmed. Pending: information missing. Suggestion: recommendation.
- **Risk, priority and term:** Risk: how serious it would be. Priority: what to handle first. Term: when to act (Quick win = fast and easy).
- **Project principles (constitution):** The rules that are not negotiable and guide everything else.
- **People's needs (user stories):** What someone needs, written as “As a ___, I want ___, so that ___”. Numbered US-001, US-002...
- **What must be met (requirements, FR):** Each concrete point that must be achieved. Numbered FR-001, FR-002...
- **How we will know it worked (criteria, SC):** Goals that can be measured. Numbered SC-001, SC-002...
- **Tasks (T):** The concrete work steps. Numbered T-001, T-002... and P means it can be done at the same time as another.
- **Work list (backlog):** Where the team keeps the pending tasks, for example in Azure DevOps or GitHub.
- **spec-driven-dev skill:** The Claude tool that organized this plan into principles, needs, requirements, plan and tasks.

---

# Action plan to load the work list: 001-secure-reliable-mic-tools

The backlog.csv file is ready to import into Azure DevOps. No connection is needed.

## Steps
1. Choose where the work list lives: Azure DevOps, in the “FALCON FARMS” organization, “Inventario de herramientas” project
   - Who: Inventory owner | When: Day one
2. Check the project type (Agile, Scrum or Basic) in the project settings. The file is built for Agile (Epic, Feature, User Story); if it is Scrum, “User Story” is changed to “Product Backlog Item”
   - Who: Inventory owner, with whoever administers Azure DevOps | When: Day one
3. Import the backlog.csv file: in Azure DevOps, Boards → Queries → Import work items; review and save. It creates 1 Epic, 7 Features and 8 tasks, with priority and “done when”
   - Who: Inventory owner | When: Day one
4. Assign each task its owner and date, and order the list by priority. Start with the essential ones: T-001, T-003 and T-006
   - Who: Inventory owner, with the team | When: First week
5. Every week, mark the finished tasks. If something about what is needed changes, this document is updated first and then the list
   - Who: Inventory owner | When: Every week
6. Optional, later: for Claude to create and update the tasks by itself, the ado-sync.md file is used with Claude Code. IT approves that connection
   - Who: Inventory owner and IT | When: When decided

## Where each file goes
```
mic-tools-governance/
├── constitution.md
├── glossary.md
└── specs/001-secure-reliable-mic-tools/
    ├── spec.md  plan.md  tasks.md
    ├── research.md  data-model.md
    ├── backlog.csv   (import into Azure DevOps)
    └── ado-sync.md   (optional direct connection)
```

---

# Summary of each tool

| Tool | Summary | Tasks to do |
|---|---|---|
| Sprouts Execution Report | Its link is public (anyone with the link opens it); it is updated by hand (last: week 40). Tasks to do: 5. | 5 |
| Performance Audit Walmart | Its link is public (anyone with the link opens it); it is updated by hand (last: October 5). Tasks to do: 4. | 4 |
| SPR Sales Report | Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 4. | 4 |
| Walmart Audit | Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 3. | 3 |
| Costo de servir | It is entered only through the Portal (only people with access to the Portal); it updates on a schedule (last: October 7). Tasks to do: 2. | 2 |
| Last Visit | Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 4. | 4 |
| Visit FS | Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 3. | 3 |
| Costco Report | Its link is public (anyone with the link opens it); it updates on a schedule (last: October 11). Tasks to do: 5. | 5 |
| AFS Error Report | Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1. | 1 |
| Travel Approval Request | Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1. | 1 |
| Incident Reporting Route | It is a notice, not an approval; it is loaded into the database by hand every week. Tasks to do: 17. | 17 |
| Walmart Audit | Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1. | 1 |
| Time Correction | Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1. | 1 |
| DSD Store Master | It requires a company account and permission; it is updated every day or every other day. Tasks to do: 20. | 20 |
| DSD Route Master | Route catalog and cost to serve; the cost assumptions are inside the queries. Tasks to do: 33. | 33 |
| DSD FS Route Master | FS route book; cost is computed in 104 files and pasted. Tasks to do: 31. | 31 |
| Plan de visitas (Unify) | Monthly route plan; one book per month and manual adjustments. Tasks to do: 25. | 25 |
| Stores Contact List | Contact master of active stores; the Route Master reads it by column letter. Tasks to do: 23. | 23 |
| FIT | It asks for an account and an Admin’s approval; it updates live. Tasks to do: 7. | 7 |

---

# SDD · Sprouts Execution Report

## Summary
Its link is public (anyone with the link opens it); it is updated by hand (last: week 40). Tasks to do: 5.

## 1. Project principles

**Starting point**
- Vulnerability (High): Public with no sign-in; shows staff names and auditor remarks
- Stability (Medium): Refreshed manually; last: week 40
- Scalability (Low): 2 MB model; grows every week

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Today the link is public: anyone who has it opens it without an account. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | To do | It is updated by hand; scheduling it and the failure notice are missing. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (To do): That only people with a company account get in — Today the link is public.
- **US-002A** (To do): That it updates by itself and shows when — It is updated by hand: scheduling is missing.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup.
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-006** (To do): That the figures have a clear definition — The definitions of the standards and the compliance % are missing.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | To do |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | To do |
| FR-003 | The system MUST hide or restrict pages with free-text comments. Hide the “Remarks” page. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | To do |
| FR-007 | The system MUST show on every report the date and time of its last refresh. | Done |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-012 | The system SHOULD maintain a glossary with the definitions and formulas of the key figures. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “Sprouts Execution Report” in a private window: it must ask for an account. | To do |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | To do |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that everyone has a company email (Falcon Farms); they should have one.

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
- Phase 6: Shared definitions
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Viewers who do not yet have or do not use a company account | Verify each dashboard's user list (the roles are already in each record) before withdrawing the links; anyone without a company email is resolved first. |
| Removing the public link interrupts whoever uses it | Warn beforehand, validate the new access and withdraw the link last, one dashboard at a time. |
| Scheduling refresh requires credentials or a gateway | Document each model's source and test refresh on one report before generalizing. |

## 5. Tasks

- [ ] T-001: Move “Sprouts Execution Report” to company-account access from the single site and withdraw its public link (To do · First)
  - Done when: It opens only with an account and from a single site; its public link no longer opens without an account.
- [ ] T-002: Clean up “Sprouts Execution Report”: hide the “Remarks” page (To do · Next)
  - Done when: No free comments or unexplained hidden pages remain.
- [ ] T-003: Schedule the update of “Sprouts Execution Report” (To do · First)
  - Done when: It updates by itself and every page shows its date.
- [ ] T-004: Confirm whether “Sprouts Execution Report” has failed and turn on the failure notice to the owner and the backup (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.
- [ ] T-007: Add to the glossary what concerns “Sprouts Execution Report”: the standards and the compliance % (To do · Last)
  - Done when: Each term has a written definition.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Sprouts Execution Report” (T-001, T-002, T-003, T-004, T-007) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-001, T-003 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: open it in a private window and confirm it asks for an account | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Performance Audit Walmart

## Summary
Its link is public (anyone with the link opens it); it is updated by hand (last: October 5). Tasks to do: 4.

## 1. Project principles

**Starting point**
- Vulnerability (High): Public with no sign-in; shows staff names and auditor remarks
- Stability (Medium): Refreshed manually (last: October 5)
- Scalability (Low): 2 MB model

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Today the link is public: anyone who has it opens it without an account. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | To do | It is updated by hand; scheduling it and the failure notice are missing. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (To do): That only people with a company account get in — Today the link is public.
- **US-002A** (To do): That it updates by itself and shows when — It is updated by hand: scheduling is missing.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup.
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | To do |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | To do |
| FR-003 | The system MUST hide or restrict pages with free-text comments. Hide the “Comments” page. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | To do |
| FR-007 | The system MUST show on every report the date and time of its last refresh. | Done |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “Performance Audit Walmart” in a private window: it must ask for an account. | To do |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | To do |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that everyone has a company email (Falcon Farms); they should have one.

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
| Scheduling refresh requires credentials or a gateway | Document each model's source and test refresh on one report before generalizing. |

## 5. Tasks

- [ ] T-001: Move “Performance Audit Walmart” to company-account access from the single site and withdraw its public link (To do · First)
  - Done when: It opens only with an account and from a single site; its public link no longer opens without an account.
- [ ] T-002: Clean up “Performance Audit Walmart”: hide the “Comments” page (To do · Next)
  - Done when: No free comments or unexplained hidden pages remain.
- [ ] T-003: Schedule the update of “Performance Audit Walmart” (To do · First)
  - Done when: It updates by itself and every page shows its date.
- [ ] T-004: Confirm whether “Performance Audit Walmart” has failed and turn on the failure notice to the owner and the backup (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Performance Audit Walmart” (T-001, T-002, T-003, T-004) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-001, T-003 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: open it in a private window and confirm it asks for an account | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · SPR Sales Report

## Summary
Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 4.

## 1. Project principles

**Starting point**
- Vulnerability (High): Public with no sign-in; shows customer sales and inventory; 1 hidden page
- Stability (Medium): Scheduled refresh; last: October 12, 2026; a page showing zeros
- Scalability (Medium): 44 MB model with 16 tables and about 148 slicers

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Today the link is public: anyone who has it opens it without an account. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | Partial | It updates by itself (last: October 12); the failure notice still has to be turned on. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (To do): That only people with a company account get in — Today the link is public.
- **US-002A** (Done): That it updates by itself and shows when — It updates by itself and shows its date.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup (and review its history).
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-006** (To do): That the figures have a clear definition — The definitions of SL, DL, RTV and AUR are missing.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | To do |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | To do |
| FR-005 | The system SHOULD remove duplicate or hidden pages that have no documented purpose. Delete or document 1 hidden page. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | Done |
| FR-007 | The system MUST show on every report the date and time of its last refresh. | Done |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-012 | The system SHOULD maintain a glossary with the definitions and formulas of the key figures. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “SPR Sales Report” in a private window: it must ask for an account. | To do |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | Done |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that everyone has a company email (Falcon Farms); they should have one.

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
- Phase 6: Shared definitions
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Viewers who do not yet have or do not use a company account | Verify each dashboard's user list (the roles are already in each record) before withdrawing the links; anyone without a company email is resolved first. |
| Removing the public link interrupts whoever uses it | Warn beforehand, validate the new access and withdraw the link last, one dashboard at a time. |

## 5. Tasks

- [ ] T-001: Move “SPR Sales Report” to company-account access from the single site and withdraw its public link (To do · First)
  - Done when: It opens only with an account and from a single site; its public link no longer opens without an account.
- [ ] T-002: Clean up “SPR Sales Report”: delete or document 1 hidden page (To do · Next)
  - Done when: No free comments or unexplained hidden pages remain.
- [ ] T-004: Confirm whether “SPR Sales Report” has failed and turn on the failure notice to the owner and the backup (review its update history) (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.
- [ ] T-007: Add to the glossary what concerns “SPR Sales Report”: SL, DL, RTV and AUR (To do · Last)
  - Done when: Each term has a written definition.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “SPR Sales Report” (T-001, T-002, T-004, T-007) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-001 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: open it in a private window and confirm it asks for an account | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Walmart Audit

## Summary
Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 3.

## 1. Project principles

**Starting point**
- Vulnerability (High): Public with no sign-in; shows names and free-text comments; 3 hidden pages
- Stability (Low): Scheduled refresh; last: October 12, 2026
- Scalability (Low): 5 MB model

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Today the link is public: anyone who has it opens it without an account. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | Partial | It updates by itself (last: October 12); the failure notice still has to be turned on. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (To do): That only people with a company account get in — Today the link is public.
- **US-002A** (Done): That it updates by itself and shows when — It updates by itself and shows its date.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup (and review its history).
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | To do |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | To do |
| FR-003 | The system MUST hide or restrict pages with free-text comments. Hide the “other reason” details. | To do |
| FR-005 | The system SHOULD remove duplicate or hidden pages that have no documented purpose. Delete or document 3 hidden pages. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | Done |
| FR-007 | The system MUST show on every report the date and time of its last refresh. | Done |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “Walmart Audit” in a private window: it must ask for an account. | To do |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | Done |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that everyone has a company email (Falcon Farms); they should have one.

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

- [ ] T-001: Move “Walmart Audit” to company-account access from the single site and withdraw its public link (To do · First)
  - Done when: It opens only with an account and from a single site; its public link no longer opens without an account.
- [ ] T-002: Clean up “Walmart Audit”: hide the “other reason” details and delete or document 3 hidden pages (To do · Next)
  - Done when: No free comments or unexplained hidden pages remain.
- [ ] T-004: Confirm whether “Walmart Audit” has failed and turn on the failure notice to the owner and the backup (review its update history) (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Walmart Audit” (T-001, T-002, T-004) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-001 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: open it in a private window and confirm it asks for an account | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

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

---

# SDD · Last Visit

## Summary
Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 4.

## 1. Project principles

**Starting point**
- Vulnerability (High): Public with no sign-in; shows staff names, hours and turnover; 5 hidden pages
- Stability (Low): Refresh scheduled several times a day; 5 hidden pages and duplicates
- Scalability (Medium): 331 MB model with 34 tables of mixed topics; the largest

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Today the link is public: anyone who has it opens it without an account. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | Partial | It updates by itself (last: October 12); the failure notice still has to be turned on. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (To do): That only people with a company account get in — Today the link is public.
- **US-002A** (Done): That it updates by itself and shows when — It updates by itself and shows its date.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup.
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-006** (To do): That the figures have a clear definition — The definitions of effective visit and requisition statuses are missing.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | To do |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | To do |
| FR-005 | The system SHOULD remove duplicate or hidden pages that have no documented purpose. Delete or document 5 hidden pages. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | Done |
| FR-007 | The system MUST show on every report the date and time of its last refresh. | Done |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-012 | The system SHOULD maintain a glossary with the definitions and formulas of the key figures. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “Last Visit” in a private window: it must ask for an account. | To do |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | Done |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that everyone has a company email (Falcon Farms); they should have one.

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
- Phase 6: Shared definitions
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Viewers who do not yet have or do not use a company account | Verify each dashboard's user list (the roles are already in each record) before withdrawing the links; anyone without a company email is resolved first. |
| Removing the public link interrupts whoever uses it | Warn beforehand, validate the new access and withdraw the link last, one dashboard at a time. |
| Large models take long to refresh (Last Visit, 331 MB) | Measure refresh time before scheduling it. |

## 5. Tasks

- [ ] T-001: Move “Last Visit” to company-account access from the single site and withdraw its public link (To do · First)
  - Done when: It opens only with an account and from a single site; its public link no longer opens without an account.
- [ ] T-002: Clean up “Last Visit”: delete or document 5 hidden pages (To do · Next)
  - Done when: No free comments or unexplained hidden pages remain.
- [ ] T-004: Confirm whether “Last Visit” has failed and turn on the failure notice to the owner and the backup (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.
- [ ] T-007: Add to the glossary what concerns “Last Visit”: effective visit and requisition statuses (To do · Last)
  - Done when: Each term has a written definition.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Last Visit” (T-001, T-002, T-004, T-007) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-001 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: open it in a private window and confirm it asks for an account | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Visit FS

## Summary
Its link is public (anyone with the link opens it); it updates on a schedule (last: October 12). Tasks to do: 3.

## 1. Project principles

**Starting point**
- Vulnerability (High): Public with no sign-in; shows compliance and hours per supervisor
- Stability (Low): Daily scheduled refresh
- Scalability (Low): 8 MB model

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Today the link is public: anyone who has it opens it without an account. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | Partial | It updates by itself (last: October 12); the failure notice still has to be turned on. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (To do): That only people with a company account get in — Today the link is public.
- **US-002A** (Done): That it updates by itself and shows when — It updates by itself and shows its date.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup.
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-006** (To do): That the figures have a clear definition — The definitions of the compliance % and the hours by visit type are missing.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | To do |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | Done |
| FR-007 | The system MUST show on every report the date and time of its last refresh. | Done |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-012 | The system SHOULD maintain a glossary with the definitions and formulas of the key figures. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “Visit FS” in a private window: it must ask for an account. | To do |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | Done |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that everyone has a company email (Falcon Farms); they should have one.

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
- Phase 6: Shared definitions
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Viewers who do not yet have or do not use a company account | Verify each dashboard's user list (the roles are already in each record) before withdrawing the links; anyone without a company email is resolved first. |
| Removing the public link interrupts whoever uses it | Warn beforehand, validate the new access and withdraw the link last, one dashboard at a time. |

## 5. Tasks

- [ ] T-001: Move “Visit FS” to company-account access from the single site and withdraw its public link (To do · First)
  - Done when: It opens only with an account and from a single site; its public link no longer opens without an account.
- [ ] T-004: Confirm whether “Visit FS” has failed and turn on the failure notice to the owner and the backup (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.
- [ ] T-007: Add to the glossary what concerns “Visit FS”: the compliance % and the hours by visit type (To do · Last)
  - Done when: Each term has a written definition.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Visit FS” (T-001, T-004, T-007) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-001 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: open it in a private window and confirm it asks for an account | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Costco Report

## Summary
Its link is public (anyone with the link opens it); it updates on a schedule (last: October 11). Tasks to do: 5.

## 1. Project principles

**Starting point**
- Vulnerability (High): Public with no sign-in; shows sales, targets and store comments; 3 hidden pages
- Stability (Medium): It updates by itself (last: October 11, 2026); the date and time of the last update are not shown in the report
- Scalability (Medium): DirectQuery (queries the live source); 30 MB model with 23 tables

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Today the link is public: anyone who has it opens it without an account. |
| 2 | Data in a company place | Not applicable | The data lives in its sources; this dashboard only shows it. |
| 3 | Up-to-date information | Partial | It updates by itself; the visual with the date and time of the last update and the failure notice are missing. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 1 pending item remains to be closed. |

## 2. What is needed

### People's needs

- **US-001** (To do): That only people with a company account get in — Today the link is public.
- **US-002A** (Partial): That it updates by itself and shows when — It updates by itself. The visual with the date and time of the last update is missing.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether it fails and to turn on the notice to the owner and the backup (and review its history).
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-006** (To do): That the figures have a clear definition — The definitions of the sales, RTV and labor targets are missing.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-001 | The system MUST require signing in with a company account (Falcon Farms email) to view any report with staff or operational data; no role groups are created. | To do |
| FR-002 | The system MUST unify the tool links in a single site and withdraw the direct public links; no dashboard remains public by design. | To do |
| FR-003 | The system MUST hide or restrict pages with free-text comments. Hide the “Detail Comments” page. | To do |
| FR-005 | The system SHOULD remove duplicate or hidden pages that have no documented purpose. Delete or document 3 hidden pages. | To do |
| FR-006 | The system MUST refresh every report on a defined schedule. | Done |
| FR-007 | The system MUST show on every report the date and time of its last refresh. The visual with the date and time is missing. | To do |
| FR-008 | The system MUST notify the owner and the backup when a refresh fails. It remains to confirm whether it fails and to turn on the notice. | To confirm |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-012 | The system SHOULD maintain a glossary with the definitions and formulas of the key figures. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-001 | 100% of reports with sensitive information require sign-in; none opens with just a link, except approved exceptions. | Open “Costco Report” in a private window: it must ask for an account. | To do |
| SC-002 | 100% of reports refresh on a schedule and show the date and time of their last refresh. | Its last update matches the schedule and the date and time are visible. | To do |
| SC-005 | A failed refresh is detected by its owner in less than 1 business day. | A test failure notifies the owner and the backup. | To confirm |
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 1). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who owns each report? | Its creator. |
| Which reports refresh on a schedule? | All except Performance Audit Walmart and Sprouts Execution Report, which are refreshed by hand. |
| Is there any dashboard that must deliberately remain public? | Not necessarily public; what is needed is that people with the company email have access. |

### To answer

- Verify that everyone has a company email (Falcon Farms); they should have one.

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
- Phase 6: Shared definitions
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Viewers who do not yet have or do not use a company account | Verify each dashboard's user list (the roles are already in each record) before withdrawing the links; anyone without a company email is resolved first. |
| Removing the public link interrupts whoever uses it | Warn beforehand, validate the new access and withdraw the link last, one dashboard at a time. |

## 5. Tasks

- [ ] T-001: Move “Costco Report” to company-account access from the single site and withdraw its public link (To do · First)
  - Done when: It opens only with an account and from a single site; its public link no longer opens without an account.
- [ ] T-002: Clean up “Costco Report”: hide the “Detail Comments” page and delete or document 3 hidden pages (To do · Next)
  - Done when: No free comments or unexplained hidden pages remain.
- [ ] T-003: Add to “Costco Report” the visual with the date and time of the last update (To do · First)
  - Done when: The report shows the date and time of its last update.
- [ ] T-004: Confirm whether “Costco Report” has failed and turn on the failure notice to the owner and the backup (review its update history) (To do · Next)
  - Done when: It is known whether it has failed and a test failure notifies both.
- [ ] T-007: Add to the glossary what concerns “Costco Report”: the sales, RTV and labor targets (To do · Last)
  - Done when: Each term has a written definition.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Costco Report” (T-001, T-002, T-003, T-004, T-007) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-001, T-003 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: open it in a private window and confirm it asks for an account | Tool owner | First week |
| 4 | Note the backup in the record and close the pending documentation item | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · AFS Error Report

## Summary
Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medium): Public link: anyone who has it can open it and respond; collects screenshots and names
- Stability (Medium): The administrator receives and updates it; response destination to confirm

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Anyone with the link can respond, with no account. |
| 2 | Data in a company place | To do | Where the responses are stored and for how long still has to be defined. |
| 3 | Up-to-date information | Not applicable | It is filled in when the event happens; it is not updated on a schedule. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 4 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its administrator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-005** (To do): That only company people respond and it is known where the responses go — Who can respond and the destination of the responses still have to be limited and defined.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-015 | The system MUST limit who can respond to each form to people with a company account. | To do |
| FR-016 | The system MUST define the destination and retention time of each form's responses. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 4). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who receives each form's responses? | Its administrator, who also updates it. |
| Must the people who respond to the forms sign in? | Not today; the people who fill them in should have the company email, to be verified. |

### To answer

- Verify that the people who fill it in have a company email (Falcon Farms); they should have one.
- Where responses are stored (Excel, SharePoint or Power Automate); they are received by the administrator.
- Form owner and license.
- Response retention and who can download them.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Forms | Forms owned by a group, only for company people, with responses stored in a company place | The form does not depend on one person and responses have a defined destination and retention time. |

### Phases that apply

- Phase 5: Controlled forms
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Form respondents will have to sign in for the first time | Announce beforehand, test with a few people and keep the same link. |

## 5. Tasks

- [ ] T-006: Limit “AFS Error Report” to company accounts and define where its responses are stored (To do · First)
  - Done when: An outside account cannot respond and the form has a response destination.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “AFS Error Report” (T-006) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-006 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: try to respond from a non-company account | Tool owner | First week |
| 4 | Note the backup in the record and close the 4 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Travel Approval Request

## Summary
Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medium): Public link: anyone who has it can open it and respond; collects name and employee ID
- Stability (Medium): The administrator receives and updates it; response destination to confirm

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Anyone with the link can respond, with no account. |
| 2 | Data in a company place | To do | Where the responses are stored and for how long still has to be defined. |
| 3 | Up-to-date information | Not applicable | It is filled in when the event happens; it is not updated on a schedule. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 4 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its administrator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-005** (To do): That only company people respond and it is known where the responses go — Who can respond and the destination of the responses still have to be limited and defined.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-015 | The system MUST limit who can respond to each form to people with a company account. | To do |
| FR-016 | The system MUST define the destination and retention time of each form's responses. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 4). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who receives each form's responses? | Its administrator, who also updates it. |
| Must the people who respond to the forms sign in? | Not today; the people who fill them in should have the company email, to be verified. |

### To answer

- Verify that the people who fill it in have a company email (Falcon Farms); they should have one.
- Where responses are stored (Excel, SharePoint or Power Automate); they are received by the administrator.
- Form owner and license.
- Response retention and who can download them.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Forms | Forms owned by a group, only for company people, with responses stored in a company place | The form does not depend on one person and responses have a defined destination and retention time. |

### Phases that apply

- Phase 5: Controlled forms
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Form respondents will have to sign in for the first time | Announce beforehand, test with a few people and keep the same link. |

## 5. Tasks

- [ ] T-006: Limit “Travel Approval Request” to company accounts and define where its responses are stored (To do · First)
  - Done when: An outside account cannot respond and the form has a response destination.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Travel Approval Request” (T-006) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-006 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: try to respond from a non-company account | Tool owner | First week |
| 4 | Note the backup in the record and close the 4 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# Spec · Incident Reporting Route

> **English version pending.** This document is currently available in Spanish only.

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m16 (inventario MIC) |
| Tipo | Formulario de Microsoft Forms con flujo de Power Automate, base en SharePoint y dashboard de Execution Team |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Formulario donde FS, DM y RM reportan cada ruta que **no se ejecutó según lo planeado**, con su motivo, la secuencia de tiendas visitadas y una justificación. No es una solicitud de aprobación: es un aviso, y cada respuesta se notifica por correo en el momento. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Respuestas | 832, del 2026-08-03 al 2026-10-20 (≈ 74 por semana) | Dueño |
| Quién reporta | 62 personas: FS 74 % · DM 25 % · RM 1 % | Dueño |
| Tipos de cambio | Day Change 51 % · Order Change 40 % · Split 5 % · Order+Day 4 % | Dueño |
| Motivos | Ausencia temporal 84 % · Contingencia de tienda 16 % · Festivo 0,7 % | Dueño |
| Rutas combinadas | 27 % de las respuestas (varios IDs separados con «-») | Dueño |
| Formulario | 17 secciones y 194 preguntas, con una sección por DM (14) | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Alto ⚠️ C-06 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🔴 **No se puede agregar otro DM:** Microsoft Forms permite 200 preguntas, el formulario tiene 194 y cada sección de DM ocupa 13. [Dueño]
2. 🟠 **El correo del flujo llega incompleto** en algunos casos (rutas *split* sin fechas, paradas faltantes o repetidas) y el email del FS se escribe a mano. [Dueño]
3. 🟠 **Los dos reportes no cuadran:** el dashboard cuenta 736 registros y el análisis de cumplimiento 707; el ID 429 no está en ninguna base. [Dueño]
4. 🟠 **La suplente todavía no tiene accesos** a los 6 componentes (formulario, flujo, agente, carpeta, dashboard y buzón). [Dueño]
5. ⚠️ **El formulario no es público ni pide aprobación**, al contrario de lo que decía el análisis inicial (C-01 y C-02). [Dueño]

**Funciona bien:** la consolidación y la carga son fieles. El consolidado coincide al 100 % con el export y la base coincide campo por campo. [Dueño]

**Contradicciones:** 6 detectadas; 4 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (IRR-A01, IRR-A02, IRR-A03, IRR-A04, IRR-A13, IRR-A17) y la pregunta Q-17. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Dejar registrado, y avisar de inmediato, cada vez que una ruta de supervisión no se ejecuta como estaba planeada, para que Execution Team y la jerarquía sepan qué cambió, por qué y qué tiendas se visitaron, y para medir el cumplimiento de rutas.

- **Problema que resuelve:** sin este registro no se sabe cuándo ni por qué una ruta cambió de día, de orden o se partió en dos días. [Dueño]
- **Qué logra:** una respuesta por evento (`ID`), con tipo de cambio, motivo, fechas, hasta 7 paradas por DM y una justificación, más un correo automático. [Dueño]
- **Éxito:** todo evento reportado llega a la base, el correo sale completo y los dos reportes de cumplimiento muestran la misma cifra (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: el formulario (17 secciones), el flujo de Power Automate «Incident Reporting Process» y su correo, la carga semanal a `Incident Reporting Process Database.xlsx` (`Table1`), la copia `Cleandata` y el agente o script de consolidación.

**No incluye** ❓: el dashboard de Execution Team, el archivo de análisis de cumplimiento de PERFORMANCE, el Route Master y el Store Master, que son dependencias.

**Futuro** [Dueño]: que el mismo flujo agregue cada respuesta a la base (IRR-A06), rediseñar la captura de tiendas (IRR-A07) y validar los IDs contra el Route Master (IRR-A10).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| FS, DM y RM (62 personas) | Reportan cada ruta que no se ejecutó según el plan | 832 respuestas | Dueño |
| Responsable del formulario (el dueño) | Recibe las respuestas, hace la carga semanal y mantiene el formulario y el flujo | Carga semanal | Dueño |
| Execution Team | Ve el dashboard que lee la base | Se refresca a diario | Dueño |
| PERFORMANCE | Usa `Cleandata` para el análisis de cumplimiento de rutas | — | Dueño |
| RM, DM, FS y quien reportó | Reciben el correo «New Route Event» | Cada respuesta | Dueño |
| Buzón `route.request` | Recibe cada aviso | Cada respuesta | Dueño |

**Acceso**

- Se llena con la cuenta corporativa. [Dueño] ⚠️ C-01
- Formulario no anónimo: el dueño ve el nombre y el correo de quien responde. [Inicial]
- La base está en SharePoint › Analizer Routes › EXCEPCIONES DE RUTA, y el dashboard en la carpeta de Teams de Execution Team. [Dueño]
- ❓ Falta la lista de personas con acceso a la base y a las carpetas, y quién la aprueba (Q-18). [Inicial]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño · Inicial]

- Es el propietario del formulario y recibe las respuestas.
- Hace la carga semanal, mantiene el flujo y actualiza el formulario y el correo cuando cambia un DM, un RM o una tienda.
- Aprobó su análisis el 2026-10-20 (v1.4).

## Administrador técnico

**Jeronimo Sanchez**, administra el formulario y el flujo. [Inicial]

- El flujo, sus conexiones (Forms y Outlook), el agente de consolidación y la carga dependen de sus cuentas. [Dueño]
- ❓ Quiénes reciben el buzón `route.request` (Q-13).

## Suplente

**Jennifer Guarin.** [Dueño] Todavía no tiene los accesos para operar la herramienta.

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Formulario | Ser copropietaria | ⬜ Pendiente (IRR-A01) |
| Flujo de Power Automate y sus conexiones | Copropiedad y conexiones propias | ⬜ Pendiente (IRR-A01) |
| Agente de consolidación o script | Poder correrlo | ⬜ Pendiente (IRR-A01) |
| Carpeta de SharePoint | Editar la base | ⬜ Pendiente (IRR-A01) |
| Carpeta de Teams del dashboard | Acceso a la carpeta | ⬜ Pendiente (IRR-A01) |
| Buzón `route.request` | Recibir los avisos | ⬜ Pendiente (IRR-A01) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| Respuestas del formulario | Lo que FS, DM y RM escriben; nombre, email y fechas de envío los pone Forms | Quienes reportan | Dueño |
| Export de Forms (200 columnas) | Se descarga cada semana | Dueño | Dueño |
| Consolidado semanal (29 columnas) | El agente de Claude o `consolidate_incident_report.py` reduce 200 columnas a 29 | Dueño | Dueño |
| `Incident Reporting Process Database.xlsx` (`Table1`) | Base del dashboard; se pegan las filas nuevas | Dueño | Dueño |
| `Cleandata.xlsx` | Copia con IDs corregidos y la columna `Count?`; insumo del análisis de cumplimiento | Dueño y PERFORMANCE | Dueño |
| Catálogos dentro del formulario | RMs, DMs y tiendas por DM | Dueño | Dueño |
| Route Master | De él salen los IDs de ruta, pero se escriben a mano | Equipo del Route Master | Dueño |

**Cómo fluyen los datos** [Dueño]

1. **Captura:** FS o DM llenan el formulario.
2. **Aviso:** el flujo envía el correo «New Route Event» al buzón `route.request`, con copia al RM, DM, FS y a quien reportó.
3. **Carga semanal (manual):** export de Forms → recorte a los IDs nuevos → consolidación a 29 columnas → pegado en `Table1`.
4. **Consumo:** el dashboard de Execution Team lee la base y `Cleandata` alimenta el análisis de cumplimiento.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | Microsoft Forms · Power Automate (conexiones de Forms y Outlook) · buzón `route.request` · SharePoint · carpeta de Teams de Execution Team · agente de Claude o script |
| Archivos | Base `Table1` · `Cleandata` · Route Master |
| Personas | El dueño o su suplente |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| Dashboard de Execution Team | Lee `Table1` y se refresca a diario | Execution Team |
| Análisis de cumplimiento de rutas | Usa `Cleandata` | PERFORMANCE |
| Jerarquía de campo | Recibe el correo de cada evento | RM, DM y FS |

## Procesos operativos

[Dueño] Se llena cada vez que ocurre un evento (≈ 74 por semana) y la base se actualiza **una vez por semana**, a mano. ⚠️ C-04

1. Descargar el export de Forms.
2. **Recortarlo** a los IDs mayores que el último de `Table1` (hoy es 737, así que el próximo lote empieza en **738**). Comprobar que no falte ningún ID.
3. Pasarlo al agente de Claude (o correr `consolidate_incident_report.py`) y revisar sus advertencias.
4. Pegar las filas al final de `Table1`.
5. Si aplica, agregar las mismas filas a `Cleandata` para PERFORMANCE.
6. Al día siguiente, verificar que el dashboard muestre el lote (se refresca a diario).
7. Revisar en Power Automate si hubo ejecuciones fallidas del flujo.

**Cuando cambia un DM, un RM o una tienda:** actualizar el formulario (listas y sección) **y** el correo del flujo. Hoy no hay cupo para crear la sección de un DM nuevo.

**Cuando cambia un DM, un RM o una tienda** [Dueño]: actualizar el formulario (listas y sección) **y** el correo del flujo. Hoy no hay cupo para crear la sección de un DM nuevo.

## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- Es un aviso, no una solicitud de aprobación: cada respuesta se notifica en el momento.
- El primer ID de cada lote debe ser el último de la base más 1, sin saltos.
- Una respuesta es un evento y puede abarcar varias rutas combinadas.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Evento** | Una respuesta del formulario (`ID`). Puede abarcar varias rutas combinadas |
| **Fecha del evento** | Order Change → `Date of Route Execution` · Day y Order+Day → `New Execution Date` · Split → `First Route Execution Date` |
| **Motivo** | **A** ausencia temporal · **C** contingencia de la tienda · **H** festivo |
| **Global Route ID / Route ID** | Códigos del Route Master: `G` o `R` + estado + 3 dígitos (ej. `GFL001`, `RFL002`). Las rutas combinadas se separan con "-" |
| **Parada (Stop 1–8)** | El nuevo orden en que se ejecutaron las tiendas ese día, con formato número + cadena (ej. `101Sprouts`) |
| **Jerarquía** | RM → DM → FS. Cada DM tiene un solo RM |
| **`Count?`** | Criterio del archivo de PERFORMANCE: `No` = no se tiene en cuenta en **ese** análisis. No aplica al dashboard |
| **Registro de prueba** | Respuesta del administrador para probar el formulario o el flujo (IDs 1, 15 y 16) |
| **Lote semanal** | IDs nuevos que se cargan cada semana. El primer ID debe ser el último de la base + 1 |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | El formulario MUST registrar cada ruta no ejecutada según el plan, con tipo de cambio, motivo, tiendas y justificación | Must Have | ✅ 832 respuestas | Dueño |
| FR-02 | El correo del flujo MUST salir completo: fechas de las rutas *split*, todas las paradas y todos los DM | Must Have | ⚠️ Incompleto en varios casos (IRR-A03) | Dueño |
| FR-03 | El formulario SHOULD permitir agregar un DM sin rediseñarse | Should Have | ❌ 194 de 200 preguntas (IRR-A07) | Dueño |
| FR-04 | Los campos clave MUST validarse: email del FS y IDs de ruta contra el Route Master | Must Have | ❌ Texto libre; 7–9 % de los IDs fuera de formato (IRR-A10) | Dueño |
| FR-05 | La base del dashboard MUST contener todas las respuestas, sin pruebas, y coincidir con el reporte de cumplimiento | Must Have | ❌ 736 frente a 707; falta el ID 429 (IRR-A02, IRR-A05) | Dueño |
| FR-06 | La carga a la base SHOULD ser automática, o tener un control de lo cargado | Should Have | ⚠️ Semanal y manual (IRR-A06) | Dueño |
| FR-07 | La suplente MUST poder operar los 6 componentes | Must Have | ❌ 0 de 6 (IRR-A01) | Dueño |
| FR-08 | La descripción del formulario MUST decir lo que hace: un aviso, sin validación previa | Should Have | ⚠️ Promete una validación que no existe (IRR-A08) ⚠️ C-02 | Dueño · Inicial |
| FR-09 | El formulario MUST pedir cuenta de la empresa a quien responde | Must Have | ❓ El dueño dice que sí; el análisis inicial decía que era público ⚠️ C-01 | Dueño · Inicial |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Respuestas del formulario cargadas en la base | 737 de 832 (falta el lote 738–832 y el ID 429) | 832 de 832 | Dueño |
| SC-02 | Registros del dashboard frente al análisis de cumplimiento | 736 frente a 707 | La misma cifra | Dueño |
| SC-03 | Correos con todos los datos (fechas *split*, paradas) | 40 *split* sin fechas | 0 | Dueño |
| SC-04 | IDs de ruta fuera de formato | 7 % a 9 % | 0 (validados contra el Route Master) | Dueño |
| SC-05 | Componentes que opera la suplente | 0 de 6 | 6 de 6 | Dueño · Inicial |
| SC-06 | Margen de preguntas del formulario | 6 (194 de 200) | Espacio para al menos un DM nuevo (13 preguntas) | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Recopila nombres, emails y justificaciones; el email del FS es texto libre; el flujo y el agente dependen de cuentas personales | Inicial · Dueño |
| Estabilidad | Alto | Todo depende de una persona, la suplente no tiene accesos, un reporte real se perdió y los dos reportes no cuadran ⚠️ C-06 | Inicial · Dueño |
| Escalabilidad | Alto | 194 de 200 preguntas: no cabe otro DM; la carga semanal es manual ⚠️ C-06 | Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🔴 Crítica | **No se puede agregar otro DM.** Microsoft Forms permite 200 preguntas, el formulario tiene 194 y cada sección de DM ocupa 13. Hay que rediseñar cómo se capturan las tiendas. | Dueño |
| R2 | 🟠 Alta | **El correo del flujo llega incompleto en algunos casos:** Las rutas *split* (40 casos) llegan sin fechas. Falta la parada 8 (sección de un DM). En la parada 3 falta la tienda de un DM y la de otro DM sale repetida. El email del FS se escribe a mano y va en copia: si está mal escrito (11 casos), el envío probablemente falla. | Dueño |
| R3 | 🟠 Alta | **Los dos reportes no cuadran.** El dashboard cuenta 736 registros, sin las ≈ 160 correcciones de IDs y con 3 pruebas del administrador (IDs 1, 15 y 16). El archivo de PERFORMANCE usa `Cleandata` y cuenta 707. | Dueño |
| R4 | 🟠 Alta | **Se perdió un reporte real:** el **ID 429** (Route Day Change, GTX055, 2026-09-16) no está en ninguna de las dos bases. | Dueño |
| R5 | 🟠 Alta | **La suplente todavía no tiene accesos.** El formulario, el flujo (y sus conexiones), el agente y la carga dependen de las cuentas de Jeronimo Sanchez. | Dueño |
| R6 | 🟠 Alta | **Hay campos clave en texto libre:** el email del FS y los IDs de ruta. Entre el 7 % y el 9 % de los IDs no siguen el formato, aunque todos salen del Route Master. | Dueño |
| R7 | 🟡 Media | **Otros detalles:** Tope de 7 paradas por DM: 61 reportes llegaron al tope. La descripción del formulario habla de una "validación previa" que no existe. La justificación es un campo de una sola línea. | Dueño |
| R8 | 🟠 Alta | Los nombres y justificaciones que recopila el formulario no tienen una regla de retención ni de quién puede descargarlos (Q-17) | Inicial |
| R9 | 🟠 Alta | Si el dueño cambia de rol o sale, se pierde el control del formulario y del flujo | Inicial · Dueño |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Cargar el lote pendiente, recuperar el ID 429 y completar el correo del flujo | Los reportes cuadran y el aviso sale completo | IRR-A02, IRR-A03, IRR-A04 | Dueño |
| Corto plazo | Alinear las correcciones de IDs con PERFORMANCE y ajustar el formulario (email del FS, justificación larga, ayuda y descripción) | Una sola cifra y menos errores de captura | IRR-A05, IRR-A08 | Dueño |
| Mediano plazo | Que el mismo flujo agregue cada respuesta a la base y rediseñar la captura de tiendas | Sin export, recorte ni pegado manual; sin tope de 7 paradas | IRR-A06, IRR-A07 | Dueño |
| Largo plazo | Validar los IDs contra el Route Master, reglas de calidad y columnas derivadas; mover la base a SQL | Datos validados al entrar | IRR-A10, IRR-A11, IRR-A12 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| IRR-A01 | Dar a Jennifer Guarin acceso a los 6 componentes (formulario, flujo, agente, carpeta, dashboard, buzón) | P0 | Dueño y suplente | Dueño | T-001 |
| IRR-A02 | Cargar el lote 738–832 y recuperar el ID 429 | P0 | Dueño | Dueño | T-005 |
| IRR-A03 | Completar el correo (fechas *split*, parada 8, parada 3 de dos DM) | P0 | Dueño | Dueño | T-006 |
| IRR-A04 | Proteger la copia al FS de emails inválidos y activar las alertas de falla | P0 | Dueño | Dueño | T-007 |
| IRR-A05 | Con PERFORMANCE: llevar las correcciones de IDs a la base del dashboard, quitar las pruebas y documentar `Count?` | P1 | Dueño y PERFORMANCE | Dueño | T-008 |
| IRR-A06 | Que el mismo flujo agregue cada respuesta a `Table1` (elimina el export, el recorte, el agente y el pegado manual) | P1 | Dueño | Dueño | T-030 |
| IRR-A07 | Rediseñar la captura de tiendas para liberar preguntas y quitar el tope de 7 paradas | P1 | Dueño | Dueño | T-020 |
| IRR-A08 | Ajustes al formulario: email del FS, justificación larga, sección de un DM, ayuda en el cargo, motivo "vacante" y nueva descripción | P1 | Dueño | Dueño | T-010 a T-015 |
| IRR-A09 | Mover exports y consolidados a SharePoint | P2 | Dueño | Dueño | T-002 |
| IRR-A10 | Validar los IDs contra el Route Master | P2 | Dueño | Dueño | T-031 |
| IRR-A11 | Reglas de calidad | P2 | Dueño | Dueño | T-032 |
| IRR-A12 | Columnas derivadas para el dashboard | P2 | Dueño | Dueño | T-034 |
| IRR-A13 | Confirmar en la configuración de Forms que solo responden cuentas de la empresa, y que el formulario no es público | P0 | Dueño | Inicial | C-01 |
| IRR-A14 | Definir cuánto tiempo se conservan las respuestas y quién puede descargarlas | P1 | Dueño y PM | Inicial | Q-17 |
| IRR-A15 | Hacer la revisión técnica con IT: datos de personas y flujo atado a cuentas personales | P1 | IT | Inicial | — |
| IRR-A16 | Guardar esta spec, el paquete del flujo y el script de consolidación en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| IRR-A17 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |

**Canceladas por el dueño:** T-040 Flujo de aprobación: cancelado (es un aviso, no una solicitud).


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-05b | ¿En qué se diferencian el Global Route ID y el Route ID, y dónde está el Route Master? | Dueño del Route Master | Dueño |
| Q-06b | ¿Por qué falta el ID 429? | Jeronimo Sanchez | Dueño |
| Q-07 | ¿La vacante necesita un motivo propio? | Operaciones y RMs | Dueño |
| Q-08 | ¿Cuál es el plazo para reportar? | Operaciones y RMs | Dueño |
| Q-09 | ¿En qué zona horaria están las marcas de tiempo? | Jeronimo Sanchez | Dueño |
| Q-10 | Dos DM no tienen reportes. ¿Faltan reportes o sus rutas no tienen excepciones? Según el Store Master, los dos están activos | RMs | Dueño |
| Q-13 | ¿Quiénes reciben el buzón `route.request`? | Administración de correo | Dueño |
| Q-15 | En una ruta *split*, ¿las paradas cubren los dos días? | Jeronimo Sanchez y FS | Dueño |
| Q-16 | ¿Quién mantiene `Cleandata`? | Jeronimo Sanchez y PERFORMANCE | Dueño |
| Q-17 | ¿Cuánto tiempo se conservan las respuestas y quién puede descargarlas? | Dueño y PM | Inicial |
| Q-18 | ¿Quiénes tienen acceso a la base y a las carpetas, y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |
| Q-19 | ¿El formulario exige iniciar sesión con la cuenta de la empresa, o puede responderlo quien tenga el enlace? | Dueño | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Acceso al formulario | Inicial: el enlace es público y quien responde no inicia sesión. Dueño: se llena con la cuenta corporativa | Cuenta corporativa; confirmar en Forms que solo responden cuentas de la empresa (Q-19) | ❓ Por confirmar |
| C-02 | Aviso o aprobación | Inicial: toda excepción exige justificación y validación previa. Dueño: es un aviso, y la «validación previa» no existe | Es un aviso; corregir la descripción del formulario (IRR-A08) | ✅ Resuelta a favor del dueño |
| C-03 | Dónde se guardan las respuestas | Inicial: por confirmar. Dueño: Forms → correo de Power Automate → `Table1` en SharePoint, con carga semanal manual | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-04 | Frecuencia | Inicial: bajo demanda. Dueño: ≈ 74 respuestas por semana y carga semanal a la base | Se llena a demanda y la base se actualiza cada semana | ✅ Resuelta a favor del dueño |
| C-05 | Quién recibe las respuestas | Inicial: el administrador. Dueño: el buzón `route.request` y la jerarquía, por correo | Lo del dueño; falta saber quiénes reciben el buzón (Q-13) | ✅ Resuelta a favor del dueño |
| C-06 | Nivel de riesgo | Inicial: estabilidad y vulnerabilidad «Medio». Dueño: tope de 200 preguntas, correo incompleto, reportes que no cuadran y suplente sin accesos | Estabilidad «Alto», escalabilidad «Alto» y vulnerabilidad «Medio» | ❓ Por confirmar |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de datos, mapa de las 200 columnas, revisión del flujo pregunta por pregunta, registro de aclaraciones y estadísticas) todavía no están integrados.
- La distribución de reportes por RM y DM está en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/incident-reporting-route/spec.md`. [Inicial]
- Incluir en el mismo repositorio el paquete exportado del flujo «Incident Reporting Process» y el script `consolidate_incident_report.py`, sin respuestas ni datos de personas. [Dueño · Inicial]
- Describir la estructura del formulario (secciones, preguntas y lógica de ramificación) en un archivo, para poder rehacerlo y para controlar el tope de 200 preguntas. [Inicial]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Modelar una tabla de eventos (clave primaria `ID`) y una tabla de paradas (una fila por parada, de 1 a 8), en lugar de 200 columnas. [Dueño · Inicial]
2. Hacer que el mismo flujo de Power Automate escriba cada respuesta en SQL: elimina el export, el recorte, el agente y el pegado (IRR-A06). [Dueño]
3. Validar el ID de ruta contra el Route Master al cargar (IRR-A10). [Dueño]
4. Dejar `Cleandata` como una vista con las correcciones de IDs y la columna `Count?`, para que el dashboard y el análisis de cumplimiento lean la misma fuente. [Dueño · Inicial]
5. Conservar el nombre de la hoja y los encabezados que hoy lee el dashboard, mediante una vista de compatibilidad. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; la descripción del formulario es incorrecta |
| Responsables | 2 | Dueño definido; la suplente no tiene ningún acceso |
| Operación documentada | 3 | Lista de verificación semanal escrita |
| Control de acceso | 2 | Cuenta corporativa por confirmar; flujo y agente atados a cuentas personales |
| Contrato de datos | 2 | Campos clave en texto libre; 200 columnas a 29 por un agente |
| Calidad y validación | 2 | 7 % a 9 % de IDs fuera de formato; emails con error |
| Automatización e integración | 2 | El flujo envía el correo; la carga a la base es manual |
| Trazabilidad de cambios | 2 | Un reporte real perdido; las dos bases no cuadran |
| Entornos y pruebas | 2 | Las pruebas del administrador quedaron en la base |

**Nivel global: 2,2 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.

---

# SDD · Walmart Audit

## Summary
Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medium): Public link: anyone who has it can open it and respond; collects supervisor names; feeds the Walmart Audit dashboard
- Stability (Medium): The administrator receives and updates it; response destination to confirm; changing its questions may break the dashboard

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Anyone with the link can respond, with no account. |
| 2 | Data in a company place | To do | Where the responses are stored and for how long still has to be defined. |
| 3 | Up-to-date information | Not applicable | It is filled in when the event happens; it is not updated on a schedule. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 4 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its administrator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-005** (To do): That only company people respond and it is known where the responses go — Who can respond and the destination of the responses still have to be limited and defined.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-015 | The system MUST limit who can respond to each form to people with a company account. | To do |
| FR-016 | The system MUST define the destination and retention time of each form's responses. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 4). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who receives each form's responses? | Its administrator, who also updates it. |
| Must the people who respond to the forms sign in? | Not today; the people who fill them in should have the company email, to be verified. |

### To answer

- Verify that the people who fill it in have a company email (Falcon Farms); they should have one.
- Where responses are stored (Excel, SharePoint or Power Automate); they are received by the administrator.
- Form owner and license.
- Response retention and who can download them.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Forms | Forms owned by a group, only for company people, with responses stored in a company place | The form does not depend on one person and responses have a defined destination and retention time. |

### Phases that apply

- Phase 5: Controlled forms
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Form respondents will have to sign in for the first time | Announce beforehand, test with a few people and keep the same link. |

## 5. Tasks

- [ ] T-006: Limit “Walmart Audit” to company accounts and define where its responses are stored (To do · First)
  - Done when: An outside account cannot respond and the form has a response destination.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Walmart Audit” (T-006) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-006 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: try to respond from a non-company account | Tool owner | First week |
| 4 | Note the backup in the record and close the 4 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Time Correction

## Summary
Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medium): Public link: anyone who has it can open it and respond; collects supervisor names
- Stability (Medium): The administrator receives and updates it; response destination to confirm

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | To do | Anyone with the link can respond, with no account. |
| 2 | Data in a company place | To do | Where the responses are stored and for how long still has to be defined. |
| 3 | Up-to-date information | Not applicable | It is filled in when the event happens; it is not updated on a schedule. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 4 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its administrator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-005** (To do): That only company people respond and it is known where the responses go — Who can respond and the destination of the responses still have to be limited and defined.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-015 | The system MUST limit who can respond to each form to people with a company account. | To do |
| FR-016 | The system MUST define the destination and retention time of each form's responses. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 4). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| Who receives each form's responses? | Its administrator, who also updates it. |
| Must the people who respond to the forms sign in? | Not today; the people who fill them in should have the company email, to be verified. |

### To answer

- Verify that the people who fill it in have a company email (Falcon Farms); they should have one.
- Where responses are stored (Excel, SharePoint or Power Automate); they are received by the administrator.
- Form owner and license.
- Response retention and who can download them.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Forms | Forms owned by a group, only for company people, with responses stored in a company place | The form does not depend on one person and responses have a defined destination and retention time. |

### Phases that apply

- Phase 5: Controlled forms
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Form respondents will have to sign in for the first time | Announce beforehand, test with a few people and keep the same link. |

## 5. Tasks

- [ ] T-006: Limit “Time Correction” to company accounts and define where its responses are stored (To do · First)
  - Done when: An outside account cannot respond and the form has a response destination.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Time Correction” (T-006) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-006 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: try to respond from a non-company account | Tool owner | First week |
| 4 | Note the backup in the record and close the 4 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# Spec · DSD Store Master

> **English version pending.** This document is currently available in Spanish only.

> Versión final recomendada, lista para revisión final y aprobación. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado `data-sql`. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m19 (inventario MIC) |
| Tipo | Base de datos: archivo maestro en Excel |
| Versión | 3.0 |
| Estado | Lista para revisión final y aprobación |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

DSD Store Master es la tabla maestra de las tiendas que Falcon Farms atiende, atendió o atenderá: una fila por tienda, con su ubicación, jerarquía de campo (RM → DM → FS), estado en el programa y parámetros de replenishment y merchandising. Ruteo, replenishment, supervisión de campo, costos, RR. HH. y los reportes de desempeño dependen de ella. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 21.367 filas × 76 columnas, en 1 hoja y 1 tabla (`StoreMaster`) ⚠️ C-02 | Dueño |
| Clientes | 16: DSD (Walmart, Sprouts, Michaels, Costco), convenience (CVS, Walgreens, QuikTrip) y 9 inactivos, legacy o piloto | Dueño |
| Tiendas | Activas 2.610 · Pendientes 7 · Inactivas 310 · Sin estado 18.440 (convenience) | Dueño |
| Activas por cliente | Walmart 1.813 · Sprouts 507 · Michaels 173 · Costco 91 · Walgreens 18 · CVS 8 | Dueño |
| Jerarquía | 4 RMs DSD y 1 DM de convenience · 14 DMs · 106 FS (24,7 tiendas por FS; rango 7–42) | Dueño |
| Actividad | 500 versiones en 40 días, en 34 de ellos; todas del dueño ⚠️ C-04 | Dueño |
| Nivel de riesgo | Medio en vulnerabilidad, estabilidad y escalabilidad ⚠️ C-13 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. Otros archivos leen la tabla por el nombre de sus columnas: renombrar o borrar una columna los rompe, y no hay regla de aviso previo. [Dueño]
2. Depende de una persona, aunque la suplente ya está definida, y casi no hay historial: SharePoint guarda unos 40 días de versiones y no registra qué cambió. [Dueño]
3. Ya existe una réplica en SQL cargada desde este archivo, sin dueño ni frecuencia documentados. [Dueño] ⚠️ C-05
4. El inventario apuntaba a una copia vieja en un OneDrive personal. [Inicial] ⚠️ C-01
5. Funciona bien: la llave `Store Number WF` es única, las tiendas DSD activas tienen dirección, coordenadas y jerarquía completas, y `Same Store` es coherente en el 99 % de ellas. [Dueño]

**Contradicciones:** 13 detectadas; 6 resueltas a favor del dueño y 7 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (A01 a A07 y A20) y las preguntas Q-02 y Q-14. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Tener **una sola respuesta** compartida a qué tiendas están activas, dónde están, quién las supervisa y cómo se abastecen. Un maestro único, mantenido a diario por un responsable con nombre y una suplente, evita que cada equipo guarde su propia copia.

- **Problema que resuelve:** ruteo, replenishment, supervisión de campo, asignación de costos y reportes necesitan la misma lista de tiendas y la misma jerarquía. [Dueño]
- **Qué logra:** una fila por tienda con identificación, dirección y coordenadas, zonificación del cliente, jerarquía de campo (por persona y por posición), estado en el programa y parámetros de replenishment y merchandising. [Dueño]
- **Éxito:** los equipos y los archivos que la leen nunca se rompen ni muestran tiendas distintas; ver los criterios de éxito en «Requisitos funcionales consolidados». [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: identificación y ubicación de tiendas; zonificación del cliente; jerarquía de campo de Falcon Farms; estado en el programa; parámetros de replenishment y de merchandising; location de RR. HH. y contabilidad.

**No incluye** [Dueño]: diseño de rutas (Route Master), datos de producto (Product Master), calendarios (Date Master), datos maestros de empleados y nómina (iSolved), generación de pedidos (Retalon), ventas de tienda, el Convenience Store Master y los archivos que leen el Store Master (DSD Route Master, DSD_DisplayFill y la réplica SQL), que son herramientas aparte.

**Futuro** [Dueño · Inicial]: un maestro de posiciones con fechas de vigencia; un registro de cambios; sincronización automática desde el Convenience Store Master; mover el maestro a una lista o base de datos con validación y auditoría (ver «Oportunidades de mejora»).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Responsable del mantenimiento (el dueño) | Crea, actualiza y cierra tiendas; mantiene la jerarquía y los datos de replenishment | Ediciones en 34 de los últimos 40 días | Dueño |
| Suplente | Cubre al responsable | — | Dueño |
| Administrador de convenience | Es dueño de los datos de las tiendas de convenience | 18.466 filas | Dueño |
| Replenishment y Retalon | Usan DC, calendarios, display y ABC para planear pedidos | 35 columnas | Dueño |
| Execution Team | Usa la jerarquía, el servicio de merch y el estado | 31 columnas | Dueño |
| Operations Performance Team | Usa la zonificación, la zona de iSolved y la location | 3 columnas | Dueño |
| RR. HH., AFS, Demand Planning y Training | Leen la lista de tiendas y la jerarquía | — | Dueño |
| Dueños de archivos dependientes | Leen el Store Master desde otros archivos | 3 archivos | Dueño |

**Acceso**

- Está en SharePoint (sitio DSD Business Analysis › DSD Data Master) con **permisos propios**, no heredados del sitio. Exige cuenta de la empresa y permiso; no tiene enlace público. [Dueño · Inicial]
- Tiene la opción «recomendado de solo lectura» con una contraseña de escritura registrada a nombre de otra persona; se mantiene a propósito. [Dueño]
- La protección de hoja está configurada pero no activada, y los 4 rangos de edición permitida no tienen contraseña. Un filtro guardado (4 clientes DSD y un FS específico) oculta 21.337 filas a quien abre el archivo. [Dueño]
- ❓ Falta la lista de personas con acceso y su permiso, y quién aprueba los accesos nuevos (Q-16). [Inicial]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño · Inicial]

- Mantiene al día los cambios que llegan cada día o día por medio: tiendas nuevas, cierres, jerarquía, posiciones y datos de replenishment.
- Aprueba cualquier cambio de columnas y define las reglas de negocio y el diccionario.
- Avisa a Execution Team y a Replenishment de las aperturas, cierres y cambios de FS, y a los dueños de los archivos dependientes antes de cambiar columnas.
- Custodia la contraseña de escritura (confirmado el 2026-10-22).
- Aprueba esta spec junto con el administrador.

## Administrador técnico

**Jeronimo Sanchez**, administra el archivo (según el inventario). [Inicial]

- Administra el archivo en SharePoint y Excel, con sus permisos propios. [Dueño]
- ❓ La réplica SQL `sqldb-dsd-gold` la administra otro equipo, por confirmar entre Data/BI e IT (Q-02). [Dueño]
- ❓ Quién aprueba los accesos nuevos al archivo (Q-16). [Inicial]

## Suplente

**Jennifer Guarin.** Edita el archivo con la contraseña de escritura (confirmado el 2026-10-22). [Dueño] ⚠️ C-06

Para que la suplencia funcione necesita acceso a cada componente:

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| `DSD Store Master.xlsx` y su contraseña de escritura | Editar el archivo | ✅ Edita con la contraseña |
| Datos de convenience | Recibir el export del Convenience Store Master para el reemplazo completo y tener contacto con su administrador | ⬜ Pendiente (A01) |
| Archivos dependientes | Saber quiénes son sus dueños, para avisarles antes de cambiar columnas | ⬜ Pendiente (A01) |
| Solicitudes y notificaciones | Estar en la distribución donde llegan aperturas, cierres y cambios de posición, y saber a quién notificar | ⬜ Pendiente (A01) |
| Guía de operación | Esta spec y la lista de verificación de «Procesos operativos» | ✅ Este documento |

**Quién hace qué** [Dueño]

| Actividad | Ejecuta | Aprueba | Consulta | Informa |
| --- | --- | --- | --- | --- |
| Crear, activar o cerrar una tienda DSD | Dueño (suplente en su ausencia) | Dueño | Replenishment y Execution Team | Operations Performance y dependientes |
| Actualizar la jerarquía (RM, DM, FS, posiciones) | Dueño o suplente | Dueño | Execution Team | Replenishment, Operations Performance y dependientes |
| Actualizar datos de replenishment | Dueño o suplente | Replenishment | — | Dependientes |
| Actualizar las filas de convenience | Dueño o suplente | Administrador de convenience | — | Execution Team y dependientes |
| Actualizar la zona y la location de iSolved | Dueño o suplente | Operations Performance | — | Dependientes |
| Agregar, renombrar o borrar una columna | Dueño | Dueño | Todos los equipos | Dueños de archivos dependientes, con aviso previo |
| Definir las reglas de negocio (diccionario) | Dueño | Dueño | Todos los equipos | Dependientes |

## Fuentes de datos

| Fuente | Qué alimenta | Quién | Columnas |
| --- | --- | --- | --- |
| Cambios de tiendas Walmart, Sprouts, Michaels y Costco | Tiendas nuevas, cierres, direcciones, jerarquía, posiciones y replenishment | El dueño los escribe a mano, según solicitudes de Execution Team, Replenishment y Operations Performance | — |
| Convenience Store Master | Todas las filas de CVS, Walgreens y QuikTrip (reemplazo completo, según `Asignacion de Columnas Convenience.xlsx`) | Lo administra el administrador de convenience; lo pega el dueño | 3 |
| Replenishment | Identificación, DC, calendarios, display, Retalon, ABC, Segmentation, Zona AFS y BA | Equipo de Replenishment | 35 |
| Execution Team | Jerarquía y posiciones, contactos de tienda, zonificación, Active, Same Store, servicio de merch y zona horaria | Execution Team | 31 |
| Route Master | Merch Days y Merch Visit Duration | DSD Route Master (misma carpeta) | — |
| iSolved | Isolved Zone, Zone name y Location | Operations Performance Team | 3 |
| Retalon | Calendario Wk2 (no se usa) | Dueño de Retalon | 3 |
| Geocodificación y API de Python | Latitude, Longitude y Zona Horaria | Se calculan a partir de la dirección y se pegan | — |

Origen de todas las filas: [Dueño]. `CVP - WM` es la única columna sin documentar.

**Cómo llegan los datos al archivo** [Dueño]

- Escritos a mano para los clientes DSD.
- Reemplazados completos, a mano, para CVS, Walgreens y QuikTrip, cada columna fuente en la que indica el archivo de mapeo. El Store Master no tiene consultas ni vínculos externos.
- Fórmulas dentro del archivo: `Same Store` (filas 2–2.902) y las columnas espejo.
- Calculados afuera y pegados: coordenadas y zona horaria.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Archivos | Convenience Store Master · archivo de mapeo de columnas · Route Master · libro de documentación de columnas (hoy solo en un computador) |
| Sistemas | SharePoint (sitio DSD Business Analysis) · Excel · iSolved · Retalon · script o API de Python para zonas horarias |
| Procesos | Alta y cierre de tiendas · cambios de jerarquía y posiciones · cambios de replenishment · sincronización de convenience · geocodificación |
| Personas | Responsable y suplente disponibles (los cambios llegan cada día o día por medio) · administrador de convenience |

**Archivos que dependen del Store Master** (herramientas aparte; se avisa a sus dueños antes de cambiar columnas) [Dueño]

| Archivo dependiente | Qué toma | Dueño |
| --- | --- | --- |
| DSD Route Master | Lista de tiendas, jerarquía y estado (también para costos de FS y DM) | Tendrá su propia spec próximamente |
| DSD_DisplayFill | Lista de tiendas y datos de display | Desconocido (Q-13) |
| Réplica SQL `sqldb-dsd-gold › DSDStoreMaster` | Copia programada del Store Master | Por confirmar (Q-02) |

**Copias que circulan** [Dueño]: 5 copias locales desactualizadas en Descargas y 1 en la carpeta; no deben usarse como fuente (A02).

## Procesos operativos

Los cambios llegan **cada día o día por medio**. [Dueño] ⚠️ C-04

**Lista de verificación por cambio** (responsable o suplente) [Dueño]

1. Antes de editar: **quitar todos los filtros** (o usar una Vista de hoja personal) para que nada quede oculto para los demás.
2. **Tienda nueva:** agregar la fila **dentro** de la tabla (para que se extiendan las fórmulas) con la llave `<número><Cliente>`. Llenar los campos mínimos: identificación, dirección, coordenadas, zona horaria, jerarquía y posiciones, `Active = P`, `Program Start date`, Service Model, FF Facility, Merch Days y Merch Visit Duration (del Route Master), y los campos de replenishment del cliente.
3. **Activación:** en la fecha de inicio cambiar `P` → `Y`; `Same Store` pasa a `NEW` automáticamente si la fila tiene la fórmula.
4. **Cierre:** `Active = N` y `Program End date`. Liberar el FS. No borrar la fila.
5. **Cambio de jerarquía:** actualizar la persona **y** la posición (`FF Field Supervisor` + `FF Field Supervisor Position`, y lo mismo para DM y RM). Verificar que las columnas espejo se actualicen.
6. **Cambio de replenishment:** DC, días del calendario, tamaño del display y ramos, DC de Retalon, ABC y Segmentation.
7. **Convenience:** reemplazar las filas de CVS, Walgreens y QuikTrip con el Convenience Store Master vigente, según el archivo de mapeo. No corregir valores de convenience en el Store Master: el siguiente reemplazo los sobrescribe; pedirle al administrador de convenience que los corrija en la fuente.
8. Antes de guardar: ningún duplicado resaltado en `Store Number WF`, ningún `#N/A` ni `#NAME?`, sin espacios al final en los valores nuevos.
9. Después de guardar: notificar a **Execution Team y Replenishment** las aperturas, cierres y cambios de FS.
10. Antes de cualquier cambio de **columnas** (renombrar, borrar, cambiar el tipo o renombrar la tabla `StoreMaster`): avisar a los dueños de los archivos dependientes (ver «Dependencias»). Agregar una columna al final es seguro.

**Por evento** [Dueño]

| Disparador | Mantenimiento | Impacto si no se hace |
|------------|---------------|-----------------------|
| Se aprueba una tienda nueva | Fila con `Active = P`, fecha de inicio, FS y datos de replenishment | Los equipos y los archivos dependientes no ven la tienda |
| La tienda empieza a operar | `P` → `Y` | La tienda no cuenta como activa; Same Store queda mal |
| La tienda cierra | `Active = N`, fecha de fin, liberar el FS | Carga de FS y costos sobrestimados |
| Cambia un FS, DM o RM (persona o posición) | Columnas de nombre y posición; columnas espejo | Asignación errada en costos de FS/DM, rutas y jerarquía de incidentes |
| Cambio de replenishment | Columnas de calendario, DC, display y Retalon | Pedidos errados en Retalon |
| Cambio en convenience | Reemplazo completo desde el Convenience Store Master, según el archivo de mapeo | Cifras de convenience desactualizadas |
| Se agrega una columna al Convenience Store Master | Agregarla al archivo de mapeo (y al Store Master al final, si hace falta) | Datos de convenience perdidos o pegados en la columna equivocada |
| Se pide una columna nueva | Acordar nombre y tipo; agregarla al final; actualizar el diccionario | Columna sin documentar (como `CVP - WM` hoy) |
| Se renombra o borra una columna | **Avisar primero a los dueños de los archivos dependientes** | Los archivos dependientes dejan de actualizarse |

## Reglas de negocio

**Principios que gobiernan el maestro** [Dueño]

- **Art. I. Una fila = una tienda, una llave.** `Store Number WF` es única, nunca se reutiliza y no se edita después de creada. Las tiendas se desactivan, no se borran.
- **Art. II. La estructura de columnas es un contrato.** Los nombres y tipos de las 76 columnas y el nombre de la tabla `StoreMaster` son estables. Renombrar, borrar o cambiar el tipo de una columna requiere avisar antes a los dueños de los archivos dependientes y registrar el cambio en este documento. Aprueba: El dueño.
- **Art. III. Un significado documentado por columna y canal.** Dentro de DSD, una columna tiene el mismo tipo de valor para todos los clientes. Convenience puede reutilizar una columna solo a través del archivo de mapeo, y el diccionario indica ese significado.
- **Art. IV. Los valores codificados salen de listas.** Estado, códigos de día, facilities, clasificaciones y locations usan valores documentados (sin escritura libre ni espacios al final).
- **Art. V. Sin dependencias ocultas.** Ninguna fórmula del maestro puede depender de archivos personales o de archivos fuera de la carpeta DSD Data Master.
- **Art. VI. Todo cambio es trazable.** Cada cambio tiene fecha, autor y motivo, y se conserva al menos 12 meses.
- **Art. VII. Continuidad.** El responsable o la suplente pueden completar cualquier cambio sin pedir accesos.
- **Art. VIII. El archivo se deja limpio.** Sin filtros guardados, sin filas ocultas y sin datos de prueba al guardar.
- **Art. IX. Privacidad.** Los nombres de colaboradores y contactos de tienda se usan solo para la operación interna.

**Definiciones** [Dueño]

| # | Término | Definición |
|---|---------|------------|
| D1 | **Tienda (registro)** | Una fila = una ubicación de un cliente que Falcon Farms atiende, atendió o está por atender. Las filas nunca se borran: se desactivan |
| D2 | **Store Number WF** | Llave única: `<Customer Store Number><nombre corto del cliente>` sin espacios (ej. `1042Walmart`, `110Sprouts`). Los duplicados se resaltan automáticamente |
| D3 | **Canal** | **DSD:** Walmart, Sprouts, Michaels, Costco (se mantienen en este archivo). **Convenience:** CVS, Walgreens, QuikTrip (vienen del Convenience Store Master). **Legacy o piloto:** clientes inactivos que se conservan como historia |
| D4 | **Estado (Active)** | **Y** en servicio · **P** pendiente: aprobada, con `Program Start date` futura · **N** ya no se atiende (con `Program End date`) · vacío: no se maneja con esta marca (convenience hoy) |
| D5 | **Program Start / End date** | Primer y último día de la tienda en el programa de Falcon Farms. Hoy se usa "NA" cuando no hay fecha de fin |
| D6 | **Same Store** | **NEW**: fecha de inicio dentro de los últimos 365 días · **SS**: un año o más en el programa · **NS** y **CLOSED**: se usan pero no están definidos (Q-04). Fórmula: `IF(Program Start date > TODAY()-365, "NEW", "SS")` |
| D7 | **Service Model** | **DC**: el producto se entrega a través del centro de distribución del cliente · **DSD**: lo entrega directamente en la tienda una facility de Falcon Farms |
| D8 | **FF Facility** | Facility de Falcon Farms que atiende o despacha a la tienda: **FFM** Miami · **FFG** Georgia · **FFT** Texas · **FFZ** Arizona · **FFC** California · **FFK** Kentucky. "FF" en las filas de convenience viene del campo de Convenience "DC/WF Falcon"; su significado está por confirmar con el administrador de convenience |
| D9 | **ABC Classification** | Clase de la tienda por volumen de venta: AA (la más alta), A, B, C, D, E (solo Walmart); "NA" = sin clasificar |
| D10 | **Segmentation** | Segmento propio de cada cliente. Sprouts: Lead / Gold / Silver / Bronze. Walmart: A–E. Walgreens: tipo de farmacia. Cada esquema necesita su propia definición |
| D11 | **Calendario de replenishment** | `Store Pull Day` (día en que se hace el pull del pedido), `Facility Departure Day`, `Store Arrival Day`, `DC Arrival Day`. Códigos de día MO TU WE TH FR SA SU unidos con "-" (ej. `TH-MO`). Los usa Retalon. El juego "Wk2" no se usa |
| D12 | **Capacidad del display** | `Display Size in Buckets` × `Bunches per Bucket` = `Total Bunches per Store` (exacto en Walmart y Costco; en Sprouts, los ramos por balde se derivan como total ÷ baldes). Mínimo de ramos en display por producto: Roses, Mixes, CB |
| D13 | **Customer DC / Virtual DC Retalon** | DC del cliente que recibe la entrega, y nombre del DC que se usa en Retalon |
| D14 | **Servicio de merchandising** | `Merch Days` (días de visita, del Route Master) y `Merch Visit Duration (mins)`. En Michaels, por diseño: el día de pull es igual al día de merch, Receiving Manager = "Serving" y `Route (Cstore ONLY)` tiene la ruta del router |
| D15 | **Jerarquía de campo** | RM → DM → FS, por persona ("APELLIDO, NOMBRE") y por **posición** (`RM_<región>`, `DM_<distrito>`, `FS_<territorio>`). La posición se mantiene cuando cambia la persona. Cada DM pertenece a un solo RM y **cada FS tiene exactamente una posición** (confirmado). Excepción por diseño: Un RM también figura como DM de la región South (Costco), así que sus tiendas muestran `RM_South` como posición de DM |
| D16 | **Distrito de ventas de Falcon Farms** | `Customer District (Sales)`, `District` y `FF District Manager Position` describen casi el mismo territorio del DM con nombres distintos (ej. GASCAL = Mid Atlantic) |
| D17 | **Zonificación del cliente** | `Region`, `Area`, `Zone`, `Customer District #`: la estructura propia del cliente (ej. zona de Walmart "Durham II NC") |
| D18 | **Zona AFS** | Distrito de replenishment (Sprouts y Costco) |
| D19 | **Zona de iSolved, Zone name, Location** | Zona de RR. HH./nómina y location contable (ej. `2930 Texas Walmart C2S`), de iSolved |
| D20 | **Zona horaria (`Zona Horaria`)** | Nombre IANA (ej. `America/Chicago`), calculado a partir de las coordenadas con un script / API de Python |
| D21 | **VIP** | Tienda de Sprouts cercana a personal corporativo |
| D22 | **CVP - WM** | Marca de Walmart: **"Yes" = hay que registrar inventario en la tienda** (217 tiendas Walmart activas); "0" = no se registra inventario |
| D23 | **BA** | Analista de negocio asignado a la tienda |

## Requisitos funcionales consolidados

#### Identificación y ciclo de vida
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-001 | El maestro MUST tener una fila por tienda con una llave única `Store Number WF` | Must Have | ✅ 0 duplicados, se resaltan si aparecen | Dueño |
| FR-002 | El maestro MUST registrar el estado (Y, P, N) y las fechas de inicio y fin de cada tienda DSD | Must Have | ✅ DSD. Convenience: la fuente no tiene estado, queda vacío | Dueño |
| FR-003 | El maestro MUST clasificar cada tienda activa como NEW o SS a partir de su fecha de inicio | Must Have | ⚠️ 2.591 de 2.617 coherentes; fórmula solo en las filas 2–2.902 | Dueño |
| FR-004 | El maestro SHOULD definir cada código de estado que usa | Should Have | ❌ "NS" y "CLOSED" sin definir; pasa al backlog (Q-04) | Dueño |
| FR-005 | El maestro MUST conservar las tiendas cerradas (sin borrarlas) | Must Have | ✅ 310 filas inactivas conservadas | Dueño |
| FR-006 | El maestro MUST guardar dirección, coordenadas y zona horaria de cada tienda activa | Must Have | ✅ DSD 100 %; ⚠️ convenience sin zona horaria | Dueño |

#### Jerarquía
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-010 | Cada tienda activa MUST tener un RM, un DM y un FS, por nombre y por posición | Must Have | ✅ DSD; ❌ posiciones de convenience | Dueño |
| FR-011 | Cada FS MUST corresponder a exactamente una posición y cada DM a exactamente un RM | Must Have | ⚠️ 1 FS con 2 posiciones (error, en corrección). Que un RM figure también como DM es intencional | Dueño |
| FR-012 | La jerarquía MUST NOT depender de otros archivos | Must Have | ✅ Lookups quitados el 2026-10-21 | Dueño |
| FR-013 | La jerarquía SHOULD guardarse una sola vez (sin columnas espejo) | Should Have | ❌ 4 columnas espejo | Dueño |
| FR-014 | Los cambios de jerarquía SHOULD conservar su historia (fechas de vigencia) | Should Have | ❌ | Dueño |

#### Replenishment y servicio
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-020 | El maestro MUST tener DC, días del calendario, capacidad del display y DC de Retalon de las tiendas que se abastecen con Retalon | Must Have | ✅ Sprouts y Costco al 100 % | Dueño |
| FR-021 | Los campos codificados MUST usar listas documentadas (días, facility, ABC, segmentation, display location) | Must Have | ⚠️ variantes de escritura | Dueño |
| FR-022 | Cada columna MUST tener un solo tipo de valor documentado dentro de DSD, y su significado en convenience MUST estar documentado | Must Have | ⚠️ Minutos de Walmart en Merch Visits per day; el formato Walmart en Store Size es una excepción aceptada; ≈ 24 significados de convenience solo en el archivo de mapeo | Dueño |
| FR-023 | Los días y la duración de merch MUST coincidir con el Route Master | Must Have | ❓ Sin cruzar todavía con el Route Master | Dueño |

#### Contrato de datos
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-030 | Los nombres y tipos de las columnas MUST estar documentados y ser estables | Must Have | ❌ | Dueño |
| FR-031 | Se MUST avisar a los dueños de los archivos dependientes antes de renombrar o borrar una columna | Must Have | ❌ sin regla | Dueño |
| FR-032 | Las columnas de número y fecha MUST contener solo números o fechas (sin "NA", formatos ni códigos) | Must Have | ❌ texto en Zip Code, Store Size, Program End date | Dueño |
| FR-033 | La carga de la réplica SQL MUST estar documentada (fuente, frecuencia, dueño) | Must Have | ⚠️ Fuente confirmada (este archivo, programada); falta dueño y frecuencia (Q-02) | Dueño |
| FR-034 | El mapeo de columnas de convenience MUST mantenerse junto al maestro y actualizarse cuando cualquiera de los dos maestros cambie columnas | Must Have | ⚠️ Existe en otro sitio; la documentación no lo menciona | Dueño |

#### Gobierno y programa
| ID | Requisito | MoSCoW | Estado | Origen |
|----|-----------|--------|--------|---|
| FR-040 | Todo cambio MUST ser trazable (fecha, autor, motivo) durante 12 meses | Must Have | ❌ | Dueño |
| FR-041 | El responsable y su suplente (una persona registrada) MUST poder operar el maestro | Must Have | ✅ La suplente edita con la contraseña de escritura (confirmado el 2026-10-22) | Dueño · Inicial |
| FR-042 | El archivo compartido MUST guardarse sin filtros ni filas ocultas | Should Have | ❌ | Dueño |
| FR-043 | La protección SHOULD evitar ediciones accidentales en las columnas de llave y de fórmula | Should Have | ❌ protección no activada | Dueño |
| FR-050 | La documentación de la herramienta (ficha de 7 áreas y esta spec) MUST estar completa, sin pendientes sin responsable y fecha | Must Have | ⚠️ Spec completa; quedan 9 pendientes en la ficha y 10 preguntas abiertas | Inicial |
| FR-051 | El maestro MUST existir en un solo lugar oficial, controlado por la empresa y con permisos revisados; las copias locales y las de cuentas personales MUST retirarse | Must Have | ⚠️ Está en un sitio de equipo; hay 5 copias locales y 1 en la carpeta; la copia del inventario está por confirmar ⚠️ C-01 | Inicial · Dueño |
| FR-052 | La spec, el diccionario y los scripts de la herramienta MUST guardarse en un repositorio privado de GitHub de Falcon (`data-sql`) | Must Have | ❌ El repositorio aún no existe | Inicial (instructivo de GHT) |
| FR-053 | Los datos MUST estar en SQL | Must Have | ⚠️ Existe una réplica (`sqldb-dsd-gold`) cargada de forma programada desde el archivo; el archivo sigue siendo la fuente ⚠️ C-05 | Dueño · Inicial (instructivo de GHT) |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-001 | Llaves de tienda únicas | 100 % (0 duplicados) | 100 % | Dueño |
| SC-002 | Columnas documentadas con tipo y valores permitidos | 0 de 76 (75 descritas sin tipos) | 76 de 76 | Dueño |
| SC-003 | Valores de FS que dependen de archivos externos o personales | 20 → 0 (cumplido el 2026-10-21) | 0 | Dueño |
| SC-004 | Filas de Walmart con minutos en `Merch Visits per day` · significados de convenience documentados | 253 · 0 de ≈ 24 | 0 · todos | Dueño |
| SC-005 | Celdas con error (`#NAME?`, `#N/A`) | 118 | 0 | Dueño |
| SC-006 | Celdas con texto en columnas de número o fecha | ≈ 2.900 | 0 | Dueño |
| SC-007 | Tiendas activas o pendientes con `Same Store` coherente con la fecha de inicio | 2.591 de 2.617 (99,0 %) | 100 % | Dueño |
| SC-008 | Tiendas activas con FS asignado, y pendientes con FS antes de su inicio | 2.610 de 2.610 activas; 5 de 7 pendientes | 100 % | Dueño |
| SC-009 | Historial de cambios disponible | 40 días, sin detalle por campo | 12 meses o más, con detalle por campo | Dueño |
| SC-010 | Componentes que puede operar la suplente | 2 de 5 | 5 de 5 | Dueño · Inicial |
| SC-011 | Filas de convenience iguales al Convenience Store Master tras cada reemplazo | Sin medir | 100 % | Dueño |
| SC-012 | Días que tarda un cambio de jerarquía en llegar al maestro | Sin medir | 1 día hábil o menos | Dueño |
| SC-013 | Copias del maestro fuera de la carpeta oficial (Descargas, otras carpetas y cuentas personales) | 6 o más, más la del inventario por confirmar | 0 | Inicial |
| SC-014 | La carga a SQL tiene documentados su fuente, su frecuencia y su dueño | Fuente confirmada; sin dueño ni frecuencia | Los tres documentados | Inicial |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Guarda nombres de empleados y contactos de tiendas; exige cuenta y permiso; la protección de hoja no está activada y falta la lista de permisos | Inicial · Dueño |
| Estabilidad | Medio | Dueño y suplente definidos; sin registro de cambios y con solo 40 días de versiones; falta confirmar que la copia del OneDrive personal ya no se usa ⚠️ C-13 | Inicial · Dueño |
| Escalabilidad | Medio | 21.367 filas × 76 columnas en una sola tabla que se mantiene a mano; ya existe una réplica SQL | Inicial · Dueño |

| # | Riesgo | Impacto | Probabilidad | Mitigación | Origen |
| --- | --- | --- | --- | --- | --- |
| R1 | Una columna renombrada o borrada rompe los archivos que leen el Store Master | Alto | Media (ya hay 3 columnas marcadas «Eliminar») | A10 | Dueño |
| R2 | El responsable no está y los cambios se acumulan; no hay respaldo confirmado | Alto | Media | A01, Q-18 | Dueño · Inicial |
| R3 | No hay trazabilidad de los cambios de jerarquía ni de estado | Medio | Confirmada | A13, A18 | Dueño |
| R4 | Texto en columnas de número o fecha | Medio | Confirmada | A09, A11 | Dueño |
| R5 | Un filtro guardado hace pensar que faltan tiendas | Bajo | Confirmada | A05 | Dueño |
| R6 | Se usan copias locales o de cuentas personales en lugar del maestro | Medio | Media | A02 | Dueño · Inicial |
| R7 | La réplica SQL se desincroniza del archivo y no tiene dueño ni frecuencia documentados | Medio | Desconocida | A03 | Dueño · Inicial |
| R8 | Nombres de empleados y teléfonos de contactos sin regla de retención | Medio | Confirmada | Q-17 | Inicial |
| R9 | Un esquema SQL que cambie los nombres de las columnas rompería los archivos dependientes | Alto | Media | Vista de compatibilidad (ver «Recomendaciones para migración a SQL») | Inicial |
| R10 | Pasar el maestro a un servidor interrumpe a quienes lo usan hoy | Medio | Media | Migrar en paralelo y conservar el archivo hasta validar | Inicial |
| R11 | La protección de hoja está apagada y la contraseña de escritura está a nombre de otra persona | Bajo | Confirmada | A18 | Dueño |

**Calidad de los datos hoy** [Dueño]

| Campo | Problema | Filas |
|-------|----------|------:|
| `Store Size (SqFt)` | Walmart: formato de tienda en lugar de pies cuadrados (Supercenter 1.171 · Neighborhood Market 217 · Priority 8). Excepción aceptada | 1.396 |
| `Merch Visits per day` | Walmart: minutos (50/60/80) en lugar de visitas | 253 |
| Columnas de convenience | *Intencional, no es un error:* Merch Visits per day = "Every Day Service", Merch Visit Duration = "24 Hours", FS Visit Duration = "Stop #", Region/Area = códigos del cliente, Segmentation = "Store Description" (ver «Mapeo de columnas de convenience» en el Anexo). Problema: no está en el diccionario | ≈ 18.466 filas |
| `Segmentation` | Niveles de Sprouts y letras de Walmart en la misma columna; "Regular " y "B " con espacios al final | — |
| `FF Field Supervisor Position` | Un FS con dos posiciones; una posición con dos FS (error confirmado, en corrección) | 2 personas |
| `Same Store` | CVS marcadas NS aunque empezaron hace más de un año | 8 |
| `Program Start date` | Walgreens activas sin fecha de inicio | 18 |
| `Zip Code` | 4 dígitos (perdió el cero inicial) | 16 |
| `Zip Code` | Walgreens con "_" (ej. `33331_4665`) | 18 |
| `Program End date` | "NA" escrito en una columna de fecha (todas las filas) | 1.490 |
| `Merch Days`, `Merch Visit Duration` | `#NAME?` (Fiesta inactivas) | 58 + 58 |
| `Isolved Zone`, `Zone name` | `#N/A` | 1 + 1 |
| `Display Location` | 8 escrituras para 4 valores; filas con escritura no estándar (todas las filas) | 58 |
| `DC Arrival Day` | "N/A" y "NA" | 33 |
| `Store Number WF` | El sufijo no coincide con Customer (QuikTrip "Quiktrip", Tawa, Latin Fresh); espacio al final (3016Walgreens) | 226 |
| `State` | "MA " con espacio al final (Tawa inactiva) | 1 |
| `Latitude` / `Longitude` | Vacías, 0,0 o fuera de EE. UU. (convenience inactivas) | 3 |
| Tiendas pendientes | Sin FS (954Sprouts, 59Sprouts) | 2 |
| Michaels | `Location`, `Isolved Zone`, `Zone name`, `BA` y `Virtual DC Retalon` vacíos | 173 |
| Encabezados | `VIP ` y `FF Regional Manager  ` terminan en espacio; `ABC Clasification` mal escrito (mantenerlo: los archivos dependientes usan ese nombre exacto) | 3 |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Quitar el filtro guardado, corregir los datos, publicar el diccionario y esta spec junto al archivo, y adoptar la regla de «avisar antes de renombrar o borrar una columna» | Menos sorpresas, continuidad y un contrato escrito | A04 a A07, A10 | Dueño |
| Corto plazo | Listas de validación en las columnas codificadas; código postal como texto de 5 dígitos; `Program End date` vacío en lugar de «NA»; fórmula de `Same Store` en todas las filas DSD | Datos limpios y consistentes | A08, A09, A11, A12 | Dueño |
| Corto plazo | Un registro de cambios de solo agregar y un límite de versiones más alto | 12 meses o más de trazabilidad | A13 | Dueño · Inicial |
| Mediano plazo | Un maestro de posiciones (posición → persona, RM → DM → FS, con vigencia); quitar las columnas espejo tras avisar a los dependientes | Una sola fuente para la jerarquía, con historia | A16 | Dueño |
| Mediano plazo | Traer las filas de convenience automáticamente desde el Convenience Store Master, o mantenerlas en una tabla aparte con la misma llave | Sin copia manual y con propiedad clara | A17 | Dueño |
| Largo plazo | Mover el maestro a una lista o base de datos con formularios, validación, auditoría y un export programado a la réplica SQL | Validación y auditoría incorporadas; menos trabajo manual | A19 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza la acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. | Se entrega cuando |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Completar los accesos de la suplente: export de convenience, dueños de archivos dependientes y canales de solicitudes | P0 | Dueño y suplente | Dueño | T-001 | Completa un cambio de tienda de principio a fin sin ayuda |
| A02 | Confirmar cuál es la copia vigente; retirar la del OneDrive personal y las 5 copias locales y la de la carpeta; marcarlas como obsoletas y corregir el inventario | P0 | Dueño | Inicial · Dueño | T-002 y C-01 | Hay una sola copia vigente y el inventario apunta a ella |
| A03 | Averiguar qué es la base `sqldb-dsd-gold` y documentar su fuente, su dueño y cada cuánto se carga | P0 | Data/BI e IT | Dueño · Inicial | T-003 y C-05 | Dueño, ubicación y frecuencia anotados |
| A04 | Publicar el diccionario de columnas y este documento junto al archivo, en `DSD Data Master` | P0 | Dueño | Dueño | T-002 | Ambos están en la carpeta del archivo |
| A05 | Quitar el filtro guardado; usar vistas de hoja para los filtros personales | P0 | Dueño | Dueño | T-010 | El archivo se abre sin filtros ni filas ocultas |
| A06 | Corregir los problemas de datos: FS de las tiendas pendientes, posiciones de un FS, zips, `#NAME?`, `#N/A` y espacios al final (ver «Calidad de los datos hoy») | P0 | Dueño | Dueño | T-012 | Sin celdas con error |
| A07 | Activar las 7 tiendas pendientes de Sprouts en su fecha de inicio: 576 y 495 (inicio el 2026-10-23), 50, 58 y 185 (inicio el 2026-10-30), 954 y 59 (inicio el 2026-11-06); 954 y 59 no tienen FS | P0 | Dueño | Dueño | T-013 | Las 7 tiendas figuran como activas |
| A08 | Completar el diccionario: tipo, valores permitidos, fuente y dueño de las 76 columnas (agregar `CVP - WM`) y el significado en convenience; mantener el archivo de mapeo junto al maestro | P1 | Dueño | Dueño | T-020 | 76 de 76 columnas documentadas |
| A09 | Agregar listas de validación a las columnas codificadas y corregir las variantes | P1 | Dueño | Dueño | T-021 | Sin variantes de escritura |
| A10 | Escribir la regla de cambio de columnas (aprueba el dueño; aviso previo a los dueños de los archivos dependientes) y aplicarla antes de borrar SubRegion y las columnas de Senior Sales Lead | P1 | Dueño | Dueño | T-022 y C-07 | Los dueños dependientes confirman antes de cada cambio |
| A11 | Sacar los minutos de `Merch Visits per day` en 253 filas de Walmart | P1 | Dueño | Dueño | T-023 | 0 filas con minutos |
| A12 | Definir NS y CLOSED y extender la fórmula de `Same Store` a todas las filas DSD | P1 | Dueño y administrador de convenience | Dueño | T-024 y C-11 | Same Store coherente en 100 % |
| A13 | Crear un registro de cambios de solo agregar y subir el límite de versiones de la biblioteca | P1 | Dueño | Dueño · Inicial | T-030 y C-13 | 12 meses de cambios con fecha, autor y motivo |
| A14 | Hacer la revisión técnica con IT o Arquitectura: el archivo guarda datos de personas y alimenta una base SQL | P1 | IT y Arquitectura | Inicial | — | Revisión firmada |
| A15 | Guardar esta spec, el diccionario y los scripts en el repositorio privado `data-sql` cuando exista | P1 | PM | Inicial (GHT) | FR-052 | Archivos en el repositorio |
| A16 | Crear un maestro de posiciones con fechas de vigencia y quitar las columnas espejo, avisando antes a los dueños dependientes | P2 | Dueño | Dueño | T-031 | Una sola fuente para la jerarquía, con historia |
| A17 | Automatizar el reemplazo completo de convenience usando el archivo de mapeo | P2 | Dueño y administrador de convenience | Dueño | T-032 | Ninguna columna pegada en el lugar equivocado |
| A18 | Activar la protección de hoja en las columnas de llave y de fórmula | P2 | Dueño | Dueño | T-034 | Protección efectiva |
| A19 | Pasar el Store Master a SQL como fuente única (tanda 1 de la migración a SQL), partiendo de la réplica existente | P2 | Arquitectura y dueño | Inicial · Dueño | T-035 | SQL es la fuente; el archivo queda solo de consulta |
| A20 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — | Firmas en el pull request |

**Ya hechas:** T-000 Definir responsable y suplente · T-011 Quitar los 20 lookups de FS a un archivo sin relación y el vínculo externo (2026-10-21).

## Preguntas abiertas

Las fechas límite son una propuesta, para resolverlas antes de firmar la spec.

| ID | Pregunta | Responsable | Fecha límite | Desbloquea |
| --- | --- | --- | --- | --- |
| Q-02 | ¿Qué es la base `sqldb-dsd-gold` (dónde está alojada, quién la administra) y quién corre su carga y con qué frecuencia? | Data/BI e IT | 2026-11-27 | A03, FR-053, C-05 |
| Q-04 | ¿Qué significan NS y CLOSED en Same Store? ¿Debe ser fórmula en todas las filas DSD? | Administrador de convenience (NS) y dueño (CLOSED y fórmula) | 2026-11-27 | A12, C-11 |
| Q-06 | ¿Qué significa «FF» en las filas de convenience (1.449 filas, de «DC/WF Falcon»)? | Administrador de convenience | 2026-11-27 | Definición D8 |
| Q-13 | ¿Quién es el dueño de DSD_DisplayFill? | Dueño | 2026-11-27 | A10 |
| Q-14 | ¿Cuál es la copia vigente: el archivo del sitio DSD Business Analysis o el del OneDrive del inventario? ¿Se puede retirar la otra? | Dueño | 2026-11-27 | A02, C-01 |
| Q-15 | ¿Las hojas ZoningBonus y Sheet1 a Sheet3 de la copia anterior existen en algún archivo vigente? ¿Se usan? | Dueño | 2026-11-27 | C-02 |
| Q-16 | ¿Quiénes tienen acceso al archivo y quién aprueba los accesos nuevos? | Dueño e IT | 2026-11-27 | Usuarios |
| Q-17 | ¿Cuánto tiempo se conservan los nombres de personas que ya no trabajan en Falcon? | Dueño y PM | 2026-12-11 | Riesgo R8 |
| Q-18 | ¿Hay un respaldo fuera de SharePoint y cómo se restaura una versión anterior? | Dueño e IT | 2026-11-27 | Riesgo R2 |
| Q-19 | ¿Cuándo conviene pasar el maestro a una base de datos con validación y auditoría? | Dueño y Arquitectura | 2027-01-22 | A19 |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Ubicación del archivo | Inicial: un OneDrive personal (riesgo de estabilidad «Alto»). Dueño: sitio de equipo DSD Business Analysis, con permisos propios, creado ahí el 2025-09-11 | Sitio de equipo. Confirmar que la copia del OneDrive ya no se usa y retirarla (Q-14, A02). El riesgo de estabilidad baja a «Medio» | ❓ Por confirmar |
| C-02 | Tamaño y estructura | Inicial: 21.358 filas, 82 columnas y 5 hojas (3 ocultas, entre ellas ZoningBonus). Dueño: 21.367 filas × 76 columnas y 1 hoja | Lo del dueño, leído en el archivo vigente. Confirmar que las hojas extra no se usan (Q-15) | ❓ Por confirmar |
| C-03 | Suplente | Inicial: sin suplente registrado. Dueño: hay suplente y edita con la contraseña de escritura | Suplente registrada (confirmado el 2026-10-22) | ✅ Resuelta a favor del dueño |
| C-04 | Frecuencia de actualización | Inicial: «según la necesidad». Dueño: cada día o día por medio (34 de los últimos 40 días) | Diaria o día por medio | ✅ Resuelta a favor del dueño |
| C-05 | Migración a SQL | Inicial: propone pasar la base a un servidor, partiendo de cero. Dueño: ya existe una réplica en SQL cargada de forma programada desde este archivo | La migración parte de la réplica existente; falta saber quién la administra (Q-02) | ✅ Resuelta a favor del dueño; ❓ dueño de la réplica |
| C-06 | Verificación de la suplente | El análisis del dueño pide verificar el permiso de la suplente; el dueño confirmó el 2026-10-22 que edita con la contraseña de escritura | Cumplido. Falta solo completar sus accesos a convenience, dependientes y solicitudes (A01) | ✅ Resuelta a favor del dueño |
| C-07 | Columnas marcadas «Eliminar» | La documentación marca SubRegion, FF Senior Sales Lead y su posición como «Eliminar», pero DSD Route Master las lee | No borrarlas hasta avisar a su dueño (A10) | ⚠️ Abierta |
| C-08 | Documentación frente a los datos | La documentación dice que `Store Size (SqFt)` y las columnas de managers no tienen datos, pero varios clientes las tienen llenas | Actualizar el diccionario (A08) | ⚠️ Abierta |
| C-09 | `Route (Cstore ONLY)` en Michaels | Se documenta como «solo convenience», pero está llena en todas las tiendas Michaels | Intencional; documentarlo | ✅ Resuelta a favor del dueño |
| C-10 | Un RM que también figura como DM | Un RM aparece como DM de las mismas 99 tiendas (posición de DM «RM_South») | Intencional; documentarlo | ✅ Resuelta a favor del dueño |
| C-11 | `Same Store` calculada o escrita a mano | Está documentada como calculada, pero la fórmula solo cubre las filas 2–2.902 y NS y CLOSED se escriben a mano | Definir NS y CLOSED y extender la fórmula (A12, Q-04) | ❓ Por confirmar |
| C-12 | Columna `District` dividida | Un mismo DM aparece dividido en dos nombres de distrito (106 y 53 tiendas) | Cosmético; confirmar la regla de nombres | ❓ Por confirmar |
| C-13 | Nivel de riesgo de estabilidad | Inicial: «Alto» por estar en una cuenta personal. Dueño: dueño y suplente definidos, ubicación en sitio de equipo | «Medio», condicionado a C-01 y a que se cree el registro de cambios (A13) | ❓ Depende de C-01 |

**Sin medir o sin cruzar** [Dueño]

- ❓ Los días y la duración de merch frente al Route Master (FR-023).
- ❓ SC-011 y SC-012: no tienen línea base.
- ❓ El significado en convenience de unas 24 columnas está solo en el archivo de mapeo (A08).

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

1. Guardar esta spec en un repositorio **privado** de la organización de Falcon (`data-sql`), en `specs/dsd-store-master/spec.md`, junto con el diccionario y los scripts de carga y de validación. [Inicial]
2. Proteger la rama `main`: la spec solo cambia con un pull request aprobado por el dueño (archivo CODEOWNERS). [Inicial]
3. Incluir un `CHANGELOG.md` con cada versión de la spec y una plantilla de pull request que pida actualizar la spec antes de cambiar columnas. [Inicial]
4. No guardar en el repositorio datos de personas ni de tiendas, solo la estructura, el diccionario y los scripts. [Inicial]
5. Registrar al dueño y a la suplente en `CODEOWNERS` y en el catálogo del repositorio de gobierno. [Inicial]
6. Mantener el archivo de mapeo de convenience y el diccionario en el mismo repositorio, versionados juntos. [Dueño · Inicial]

## Recomendaciones para migración a SQL

1. Partir de la réplica `sqldb-dsd-gold › DSDStoreMaster`: validar su contenido contra el archivo y documentar su dueño y su frecuencia (A03) antes de decidir motor y servidor. [Dueño] ⚠️ C-05
2. Llave primaria `Store Number WF`; una sola maestra de tiendas. [Dueño · Inicial]
3. Cargar primero en un área de paso (`stg`), limpiar y pasar a tablas con claves; Power BI y otros lectores leen solo vistas. [Inicial]
4. Exponer una vista con los **nombres actuales de las columnas** (incluida `ABC Clasification`, mal escrita) para que DSD Route Master y DSD_DisplayFill sigan funcionando. [Dueño]
5. Mantener la carga de convenience como un proceso aparte, con el mismo archivo de mapeo. [Dueño]
6. Definir quién actualiza cada tabla y con qué mecanismo (plantilla Excel validada o pantalla de mantenimiento), porque el responsable no es administrador de bases de datos. [Inicial]
7. Operar cuatro semanas en paralelo con el archivo en solo lectura, y archivarlo solo cuando no queden lectores. [Inicial]
8. Programar un respaldo diario y probar una restauración al mes. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 4 | Spec completa, con requisitos, criterios, reglas y plan |
| Responsables | 4 | Dueño y suplente definidos y operando; falta completar los accesos de la suplente |
| Operación documentada | 4 | Lista de verificación y mantenimiento por evento |
| Control de acceso | 3 | Cuenta y permiso; protección de hoja apagada y filtro guardado |
| Contrato de datos | 2 | 75 de 76 columnas descritas, sin tipos ni regla de cambio |
| Calidad y validación | 2 | Sin listas de validación; 118 celdas con error y ≈ 2.900 con texto en columnas numéricas |
| Automatización e integración | 2 | Reemplazo manual de convenience; carga SQL programada pero sin dueño documentado |
| Trazabilidad de cambios | 1 | Unos 40 días de versiones, sin detalle |
| Entornos y pruebas | 1 | Un solo archivo en producción; circulan copias |

**Nivel global: 2,6 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo.

## Anexo · Diccionario de datos (76 columnas)

Contiene el nivel de llenado por cliente y, al final, el mapeo de las columnas de convenience.

Nivel de llenado: **DSD activas** = tiendas activas de Walmart / Sprouts (incluye pendientes) / Michaels / Costco; **Conv.** = todas las filas de CVS / Walgreens / QuikTrip, cuyo significado por columna está en el Anexo, «Mapeo de columnas de convenience». El texto "NA" cuenta como lleno. *Doc* = equipo fuente y utilidad según el libro de documentación (Repl = Replenishment, Exec = Execution Team, OpsPerf = Operations Performance, Conv = Convenience).

| # | Columna | Doc | DSD activas % (WM/SP/MI/CO) | Conv. % (CVS/WAG/QT) | Notas |
|---|---------|-----|:---:|:---:|-------|
| 1 | Customer | Repl · Sí | 100/100/100/100 | 100/100/100 | 16 valores |
| 2 | Store Number WF | Repl · Sí | 100 | 100 | **Llave**, única |
| 3 | Customer Store Number | Repl · Sí | 100 | 100 | Número entero |
| 4 | Store Address | Repl · Sí | 100 | 100 | |
| 5 | City | Repl · Sí | 100 | 100 | |
| 6 | State | Repl · Sí | 100 | 100 | 1 espacio al final |
| 7 | Zip Code | Repl · Sí | 100 | 100 | ⚠️ Números y texto mezclados; ceros iniciales perdidos |
| 8 | Phone Number | Repl · Sí | 0/90/98/100 | 72/91/0 | Walmart sin teléfono |
| 9 | Latitude | Repl · Sí | 100 | 100 | A partir de la dirección |
| 10 | Longitude | Repl · Sí | 100 | 100 | A partir de la dirección |
| 11 | Store Size (SqFt) | Repl · Sí | 77/63/0/100 | 100/100/100 | Walmart: formato de tienda (excepción aceptada); Conv.: "WF Customer" |
| 12 | Store Manager | Exec · Sí | 0/0/97/56 | 100/87/99 | |
| 13 | Receiving Manager | Exec · Sí | 0/0/100/7 | 0/0/0 | Michaels = "Serving" |
| 14 | Merch Manager | Exec · Sí | 0/0/0/7 | 0 | |
| 15 | Receiving Window | Exec · Sí | 0/0/0/100 | 0 | Costco "2:00 AM - 8:30 AM" |
| 16 | Customer District (Sales) | Exec · Sí | 100 | 0 | ≈ nombre del territorio del DM |
| 17 | Region | Exec · Sí | 100 | 100/92/0 | DSD: región del RM; CVS/WAG: códigos numéricos |
| 18 | District | Exec · Sí | 100 | 0 | ≈ nombre del territorio del DM |
| 19 | Area | Exec · Sí | 100 | 100/92/0 | DSD: agrupación por ciudad; CVS/WAG: códigos numéricos |
| 20 | Zone | Exec · Sí | 98/100/100/100 | 100 | Zona del cliente (ej. "Durham II NC") |
| 21 | FF District Manager | Exec · Sí | 100 | 0 | 14 DMs |
| 22 | FF Field Supervisor | Exec · Sí | 100 | 15/18/100 | Valores escritos (lookups quitados el 2026-10-21) |
| 23 | Program Start date | Repl · Sí | 100 | 15/2/10 | Fecha |
| 24 | Program End date | Repl · Sí | 77/17/0/0 | 0 | ⚠️ Texto "NA" en una columna de fecha |
| 25 | Active | Exec · Sí | 100 | 0 | Y / P / N |
| 26 | Same Store | Exec · Sí | 100 | 15/19/100 | Fórmula en las filas 2–2.902; NEW / SS / NS / CLOSED |
| 27 | Service Model | Repl · Sí | 100/100/2/100 | 0 | DC / DSD |
| 28 | FF Facility | Repl · Sí | 100 | 9/20/100 | FFM Miami, FFG Georgia, FFT Texas, FFZ Arizona, FFC California, FFK Kentucky; "FF" (convenience) desconocido |
| 29 | ABC Clasification | Repl · Sí | 100/100/31/100 | 9/18/100 | AA, A–E, NA |
| 30 | Segmentation | Repl · Sí | 14/100/100/0 | 5/100/0 | ⚠️ Tres esquemas |
| 31 | Customer DC | Repl · Sí | 0/100/0/26 | 100 | |
| 32 | Store Pull Day Wk1 | Repl · Sí | 0/100/100/100 | 0 | Códigos de día; Michaels = Merch Days |
| 33 | Facility Departure Day Wk1 | Repl · Sí | 0/100/100/100 | 0 | Códigos de día |
| 34 | Store Arrival Day Wk1 | Repl · Sí | 0/100/0/100 | 0 | Códigos de día |
| 35 | Store Pull Day Wk2 | Retalon · No | 0 | 0 | No se usa |
| 36 | Facility Departure Day Wk2 | Retalon · No | 0 | 0 | No se usa |
| 37 | Store Arrival Day Wk2 | Retalon · No | 0 | 0 | No se usa |
| 38 | Display Size in Buckets | Repl · Sí | 78/100/0/100 | 9/18/99 | |
| 39 | Bunches per Bucket | Repl · Sí | 30/100/0/100 | 9/18/100 | Sprouts: con decimales (derivado) |
| 40 | Total Bunches per Store | Repl · Sí | 16/100/0/100 | 9/18/99 | = baldes × ramos |
| 41 | Merch Days | Exec · Sí | 100 | 9/18/100 | Del Route Master |
| 42 | Merch Visit Duration (mins) | Exec · Sí | 100/100/1/100 | 18/92/100 | Conv.: "24 Hours" |
| 43 | Merch Visits per day | Exec · No | 37/0/0/100 | 100 | ⚠️ Minutos en Walmart; Conv.: "Every Day Service" |
| 44 | FS Visit Duration (mins) | Exec · Sí | 0 | 9/18/100 | Conv.: "Stop #" |
| 45 | Back Cooler | Repl · Sí | 0/100/0/100 | 0 | "Y" o vacío |
| 46 | Display Location | Conv · Sí | 0 | 2/16/100 | ⚠️ 8 escrituras para 4 valores |
| 47 | Min amount of bunches in display Roses | Repl · Sí | 0/100/0/100 | 0 | El encabezado tiene un doble espacio |
| 48 | Min amount of bunches in display Mixes | Repl · Sí | 0/0/0/100 | 0 | El encabezado tiene un doble espacio |
| 49 | Min amount of bunches in display CB | Repl · Sí | 0/100/0/100 | 9/18/99 | El encabezado tiene un doble espacio |
| 50 | Virtual DC Retalon | Repl · Sí | 0/100/0/100 | 9/18/100 | |
| 51 | Route (Cstore ONLY) | Conv · No | 0/0/100/0 | 9/18/100 | También rutas del router de Michaels |
| 52 | Store Max Capacity | Conv · No | 0 | 9/18/100 | |
| 53 | VIP␣ | Repl · Sí | 0/4/0/0 | 1/2/6 | El encabezado termina en espacio; "VIP" o "Y" |
| 54 | Zona AFS | Repl · Sí | 100/100/1/100 | 0 | Walmart = "NA" |
| 55 | FF Regional Manager | Exec · Sí | 100 | 9/18/100 | 4 RMs DSD; Conv.: District Manager de convenience |
| 56 | FF Area Manager | Exec · No | 100/100/1/100 | 100/18/100 | DSD = "NA"; convenience: áreas de DC |
| 57 | SubRegion | Repl · No (eliminar) | 15/98/100/100 | 100/100/10 | ⚠️ La lee DSD Route Master: avisar antes de borrar |
| 58 | Customer District # | Repl · Sí | 0/99/0/100 | 92/92/0 | Formatos mezclados ("District 10", "TX", números) |
| 59 | BA | Repl · Sí | 0/82/0/100 | 15/19/100 | |
| 60 | Planned Visits | Exec · No sé | 6/0/0/0 | 9/18/100 | No se usa en DSD (dueño); Conv.: "Frequency" |
| 61 | Isolved Zone | OpsPerf · Sí | 100/100/0/100 | 0 | De iSolved |
| 62 | Zone name | OpsPerf · Sí | 100/100/0/100 | 19/20/100 | De iSolved |
| 63 | Location | OpsPerf · Sí | 100/100/0/100 | 100 | Location contable; convenience = "Convenience" |
| 64 | DC Arrival Day | Repl · Sí | 1/100/0/26 | 0 | "N/A" y "NA" |
| 65 | FF Regional Manager␣␣ | Exec · No | 100 | 0 | Espejo (fórmula); el encabezado termina en 2 espacios |
| 66 | FF Regional Manager Position | Exec · Sí | 100 | 0 | RM_East Coast, RM_Central, RM_West Coast, RM_South |
| 67 | FF District Manager2 | Exec · No | 100 | 0 | Espejo (fórmula) |
| 68 | FF District Manager Position | Exec · Sí | 100 | 0 | 13 posiciones DM_ + RM_South |
| 69 | FF Area Manager2 | Exec · No (Training) | 0/0/100/0 | 0 | Solo Michaels |
| 70 | FF Area Manager Position | Exec · No (Training) | 0 | 0 | Solo "NA" |
| 71 | FF Field Supervisor2 | Exec · No | 100 | 0 | Espejo (fórmula) |
| 72 | FF Field Supervisor Position | Exec · Sí | 100 | 0 | FS_<territorio>, 106 valores |
| 73 | FF Senior Sales Lead | Exec · No (eliminar) | 0 | 0 | Solo "NA" |
| 74 | FF Senior Sales Lead Position | Exec · No (eliminar) | 0 | 0 | Solo "NA" |
| 75 | Zona Horaria | Exec · Sí | 100 | 0 | IANA, API de Python |
| 76 | CVP - WM | *Sin documentar* | 100 | 100 | "Yes" = registrar inventario en esta tienda Walmart (217); "0" en el resto |

### Mapeo de columnas de convenience

Fuente: `Asignacion de Columnas Convenience.xlsx` (Sales Administration › General › Masters Changes). En las filas de convenience (CVS, Walgreens, QuikTrip), estas columnas del Store Master contienen el campo del Convenience Store Master que se indica. Las columnas que no aparecen quedan vacías en convenience.

| Columna del Store Master | Campo de Convenience | ¿Mismo significado? |
|--------------------------|----------------------|:---:|
| Customer · Store Number WF · Customer Store Number | Retailer · Store Number WF · Number | ✅ |
| Store Address · City · State · Zip Code · Phone Number · Latitude · Longitude | Mismos nombres | ✅ |
| Store Size (SqFt) | WF Customer (ej. "WALGREENS MIAMI") | ❌ |
| Store Manager | Store Manager Name | ✅ |
| Region · Area | Region · Area (códigos del cliente) | ❌ |
| Zone | Cluster | ❌ |
| FF Field Supervisor | FS | ✅ |
| Program Start date · Same Store | Program Start Date · Same Store | ✅ (NS sin definir) |
| FF Facility | DC/WF Falcon | ≈ |
| ABC Clasification | Store Type | ❌ |
| Segmentation | Store Description | ❌ |
| Customer DC | Cluster xxx | ❌ |
| Display Size in Buckets · Total Bunches per Store | Mismos nombres | ✅ |
| Bunches per Bucket | Display Type (AB) - Sales | ❌ |
| Merch Days | Days of Service | ≈ |
| Merch Visit Duration (mins) | 24 Hours (Y/N) | ❌ |
| Merch Visits per day | Every Day Service (YES/N/Closed) | ❌ |
| FS Visit Duration (mins) | Stop # | ❌ |
| Display Location · VIP · BA | Mismos nombres | ✅ |
| Min amount of bunches in display CB | Cantidad de Displays | ❌ |
| Virtual DC Retalon | Route_ID_WF | ❌ |
| Route (Cstore ONLY) | Route_ID_AFS | ≈ |
| Store Max Capacity | Route | ❌ |
| FF Regional Manager | District Manager (convenience) | ❌ |
| FF Area Manager | DC | ❌ |
| SubRegion | County | ❌ |
| Customer District # | District | ≈ |
| Planned Visits | Frequency | ≈ |
| Zone name | Customer_ID | ❌ |
| Location | Channel ("Convenience") | ❌ |

**Cambios seguros:** agregar una columna al final; cambiar valores que mantienen su tipo. **Cambios que requieren avisar a los dueños de los archivos dependientes:** renombrar o borrar una columna (incluidas las marcadas "Eliminar"), renombrar la tabla `StoreMaster`, mover el archivo o escribir texto en columnas de número o fecha.

---

# Spec · DSD Route Master

> **English version pending.** This document is currently available in Spanish only.

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m20 (inventario MIC) |
| Tipo | Base de datos: libro de Excel (catálogo de rutas de merchandising DSD y cálculo del costo de servir) con Power Query |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Catálogo de las rutas de merchandising DSD de Walmart, Sprouts y Costco, más el cálculo del **costo de servir** de cada ruta. Las rutas se crean, editan y analizan en App Routes; el Route Master las guarda y las publica. Execution Team y todos los FS, DM y RM lo consultan en modo lectura; solo el dueño y su co-responsable lo editan. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 3.664 filas (3.221 paradas + 443 `BREAK`) × 49 columnas ⚠️ C-02 | Dueño |
| Cobertura | 2.416 tiendas: Walmart 1.813 · Sprouts 512 · Costco 91. Michaels (173 tiendas) no está todavía: entrará en 2 a 4 meses | Dueño |
| Rutas | 1.305 Route ID · 1.060 Global ID · 105 Cluster FS | Dueño |
| Jerarquía | 4 RMs · 14 DMs · 105 FS | Dueño |
| Costo de servir | 1.301 rutas: 1.003 `MultiStore` + 298 `OUTLIER` | Dueño |
| Libro | 10 hojas (8 ocultas) · 12 consultas de Power Query · 5 vínculos externos ⚠️ C-01 | Dueño |
| Actividad | 500 versiones en 42 días: dueño 368 · co-responsable 132 ⚠️ C-05 | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Medio ⚠️ C-07 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🔴 **Los supuestos del costo de servir están escritos dentro de las consultas y sin documentar:** 0,76 USD por milla, visitas por semana, cargas por cliente, gastos generales y umbrales. [Dueño]
2. 🔴 **Las fórmulas buscan en el Store Master por letra de columna:** una columna nueva en medio desplazaría los datos sin dar error. [Dueño]
3. 🟠 **Un filtro guardado oculta 3.659 de 3.664 filas,** más 9 columnas y 8 hojas ocultas. [Dueño]
4. 🟠 **`FS-CLUSTER` ya no coincide con el Store Master** (`#FS` vale 0 en 345 paradas) y hay 3 columnas con `#REF!`. [Dueño]
5. 🟠 **Dependencias personales:** dos vínculos al OneDrive de la suplente y uno a una copia local. [Dueño]
6. ⚠️ **El inventario lo daba como leído por Last Visit y Visit FS;** el dueño menciona otros lectores (C-04). [Inicial]

**Funciona bien:** **Rutas y jerarquía:** ninguna ruta tiene dos FS; RM, DM y FS coinciden al 100 % con el Store Master; todas las tiendas con ruta existen en el Store Master. **IDs y datos de cada parada:** los IDs cumplen el patrón en las 3.664 filas; todas las paradas tienen días de servicio y coordenadas válidas. **Actualización y control:** la copia del Store Master está al día (solo 2 Sprouts activadas hoy difieren) y el control `CHECK` marca OK 1.298 de 1.301 rutas. **Respaldo:** ambos co-responsables pueden editar. [Dueño]

**Contradicciones:** 7 detectadas; 5 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (DRM-A01, DRM-A02, DRM-A03, DRM-A04, DRM-A05, DRM-A06, DRM-A07, DRM-A08, DRM-A09, DRM-A33) y las preguntas Q-19 y Q-20. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Tener en un solo lugar el catálogo de las rutas de merchandising DSD y el costo de servir de cada ruta, para que Execution Team y los FS, DM y RM consulten las rutas aprobadas.

- **Problema que resuelve:** las rutas se analizan en App Routes y necesitan un catálogo oficial, con su costo, que otros archivos puedan leer. [Dueño]
- **Qué logra:** una fila por parada con ruta, orden, tienda, frecuencia, minutos de visita, millas, manejo, mercaderista y tarifa, más el costo de servir por ruta. [Dueño]
- **Éxito:** los supuestos del costo están documentados, ninguna columna cambia sin aviso y todas las rutas se calculan (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: solo el Route Master (catálogo de rutas y cálculo del costo de servir).

**No incluye** [Dueño]: el Store Master (ya tiene su análisis); el DSD FS Route Master (tiene el suyo); App Routes, Route Studio, las copias y los pilotos, que son herramientas aparte.

**Futuro** [Dueño]: incluir Michaels en rutas existentes (DRM-A20, DRM-A11), protección de hoja (DRM-A27) y evaluar una base de datos (DRM-A28).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Co-responsables (el dueño y su suplente) | Analizan, aprueban y editan el libro; ambos tienen la contraseña de escritura | 368 y 132 versiones | Dueño |
| Execution Team, FS, DM y RM | Consultan las rutas en modo lectura | — | Dueño |
| Aprobadores de los supuestos del costo | Otra persona del equipo y la suplente | — | Dueño |
| Dueños de archivos que lo copian o leen | DSD FS Route Master, DSD Route Master Copy, DSD Michaels Router Pilot y el análisis de incidentes | 4 archivos | Dueño |

**Acceso**

- Está en SharePoint › DSD Business Analysis › DSD Data Master, con permisos propios. [Dueño]
- Exige cuenta de la empresa y permiso. [Inicial · Dueño]
- Todos los FS, DM y RM abren el libro y las hojas ocultas de costo no están protegidas. [Dueño]
- ❓ Falta la lista de personas con acceso, quién aprueba los accesos nuevos y a quién se deben mostrar las hojas de costo por FS y DM (Q-20, DRM-A12). [Inicial · Dueño]

## Dueño funcional

**Jeronimo Sanchez**, co-responsable. [Dueño · Inicial]

- Analiza las propuestas de cambio en App Routes y edita el Route Master.
- Avisa al FS, DM y RM cuando se aprueba un cambio.
- Aprobó su análisis el 2026-10-21 (v1.3).

## Administrador técnico

**Jeronimo Sanchez**, administra el libro. [Inicial]

- Administra el libro en SharePoint, sus 12 consultas de Power Query y sus 5 vínculos externos. [Dueño]
- ❓ Quién aprueba los accesos nuevos (Q-20).

## Suplente

**Jennifer Guarin.** Es co-responsable: cada uno respalda al otro. Ella analiza los costos y las variables, **aprueba o no** el cambio y cubre al dueño; tiene la contraseña de escritura. [Dueño] ⚠️ C-03

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Libro y contraseña de escritura | Editar el libro | ✅ Edita cuando es necesario |
| Aprobación de rutas y de supuestos del costo | Aprobar | ✅ Aprueba |
| Archivos en su OneDrive (cambio de ABC y organigrama) | Estar en una carpeta compartida | ⬜ Pendiente (DRM-A01) |
| Permisos del libro | Verificarlos | ⬜ Pendiente (DRM-A01) |
| Flujo de cambio de ruta | Seguir un procedimiento escrito | ⬜ Pendiente (DRM-A10) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| App Routes (`Route_Analysis.xlsx`) | Rutas, orden, frecuencia, millas, manejo y `BREAK` (traspaso manual, por confirmar) | PERFORMANCE | Dueño |
| DSD Store Master | Jerarquía, zona, coordenadas y dirección (consulta de Power Query y búsquedas por letra de columna) | Dueño | Dueño |
| Requis ID Book | ID de iSolved y de requisición | Otro equipo | Dueño |
| Stores Contact List | Correos y teléfonos de RM, DM y FS | Dueño | Dueño |
| Cambio de ABC en Sprouts y organigrama DSD | Archivos en el OneDrive de la suplente | Suplente | Dueño |
| DSD FS Route Master | Costo por milla del FS (`C2S FS/MILES`) | Dueño | Dueño |
| Archivo de salarios (sitio PG) | Salario por FS y DM para el costo | Otro equipo | Dueño |
| Escritos en el libro | Duración de visita, mercaderista y tarifa | Co-responsables | Dueño |

**Cómo se cambia una ruta (todo por correo)** [Dueño]

1. Un FS o DM (a veces un RM) pide el cambio a los dos co-responsables.
2. El dueño analiza la propuesta en App Routes y comparte el archivo exportado.
3. La suplente analiza costos y variables y **aprueba o no**.
4. Si aprueba, el dueño cambia el Route Master y **avisa al FS, DM y RM**.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | App Routes (con el servicio público OSRM) · SharePoint · Excel con Power Query |
| Archivos | Store Master · DSD FS Route Master · Requis ID Book · Stores Contact List · archivos del OneDrive de la suplente · archivo de salarios |
| Personas | Los dos co-responsables · los aprobadores de los supuestos del costo |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| DSD FS Route Master | Su costo por milla lo lee el Route Master (`C2S FS/MILES`) y el libro apunta a una copia local de este | Dueño |
| Plan de visitas (Unify) | Su generador lee la hoja `RouteMaster` | Dueño y suplente |
| Stores Contact List | Lee la dirección de la hoja `StoreMaster DSD`; el Route Master le lee los contactos (dependencia cruzada) | Dueño |
| DSD Route Master Copy y DSD Michaels Router Pilot | Copian el libro | Dueño |
| Análisis de incidentes | Usa los IDs de ruta | Execution Team |
| Last Visit y Visit FS ❓ | El inventario los lista como lectores; el dueño no los menciona (Q-19) | PERFORMANCE |

## Procesos operativos

[Dueño] Cada vez que se crea o cambia una ruta, o cambia un supuesto del costo: 500 versiones en 42 días. ⚠️ C-05

1. **Antes de editar:** quitar el filtro de la tabla (hoy `GNJ002`) o usar una Vista de hoja personal.
2. **Ruta nueva o cambiada:** analizarla en **App Routes** (plan A vs B, costo, millas y manejo con OSRM, `BREAK` automático) y esperar la **aprobación de Jennifer Guarin**. Luego agregar o actualizar las filas **dentro** de la tabla con los 3 IDs, `stop` secuencial, tienda, frecuencia, duración, millas, manejo, mercaderista y tarifa.
3. **Cambio de orden o de tienda:** actualizar `stop`, millas y manejo de toda la ruta. **No ordenar la tabla:** `Start Time` depende de la fila de arriba.
4. **Cambio de frecuencia o duración:** actualizar **primero el Store Master** (`Merch Days`, `Merch Visit Duration`, que es quien manda) y después el Route Master.
5. **FS nuevo o cambio de FS:** actualizar `FS-CLUSTER` (a mano) y el costo del FS.
6. **Registrar el cambio** en `Observation` y `Last Date Up`.
7. **Actualizar las consultas** y revisar que no haya `0`, `#N/A` ni `#REF!` en RM, DM, FS o `#FS`.
8. **Antes de guardar:** sin filtros ni filas ocultas. **Después:** avisar por correo al **FS, DM y RM** afectados y a los dueños de los archivos dependientes.
9. **Cambios de columnas:** avisar antes. Agregar una columna al final del Store Master o del Route Master es seguro; insertarla en medio, no.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- El Store Master manda sobre `Merch Days` y `Merch Visit Duration`: cuando una ruta cambia, primero se actualiza el Store Master.
- Despejar el salario de cada FS es intencional: así se calcula el FS Cost.
- Se usan dos modelos de costo a propósito (App Routes y Route Master); falta medir cuánto se separan.
- Agregar una columna al final del Store Master o del Route Master es seguro; insertarla en medio, no.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Parada (fila)** | Una visita planeada a una tienda dentro de una ruta. Una tienda puede tener varias filas (642 de 2.416) |
| **Route ID / Global Route ID / Cluster FS** | `R` / `G` / `C` + estado + 3 dígitos. Route ID = ruta de un FS; Cluster FS = agrupación por FS. ⚠️ Falta definir la diferencia entre Global y Route ID (Q-07) |
| **stop** | Número de la parada dentro de la ruta; la parada 1 abre a las 7:00 |
| **Frequency / Duration** | Días de visita (`MO-WE-FR-SA`) y minutos de visita (45 a 240; 60 min en 47 % de las paradas) |
| **MO … SU** | Minutos de cada día: `Duration` si el día está en `Frequency` |
| **Milleage / Driving Time** | Millas y minutos de manejo **hasta la siguiente parada**; la última parada de la ruta tiene 0. Los calcula App Routes con OSRM |
| **BREAK** | Descanso del mercaderista: App Routes lo inserta (30 min) cuando el tiempo acumulado supera 240 min (443 filas, 35 estados) |
| **RATE** | Tarifa del mercaderista: por hora (rutas de varias tiendas) o por visita (rutas de una tienda) |
| **MultiStore / OUTLIER** | `OUTLIER` = `RATE` ≥ 35 (ruta de una sola tienda pagada por visita) ⚠️ por confirmar |
| **Cargas** | **Cargas parafiscales** que se tienen en cuenta en el costo de servir. Factor por cliente: Walmart 1,13 · Sprouts 1,23 · Costco 1,14 (en App Routes, un 1,18 único) |
| **Cost to Serve** | Costo por parada = mercaderista + FS + DM + gastos generales + costo por milla del FS. `MultiStore`: `(((servicio + manejo) ÷ 60 × tarifa) + millas × 0,76) ÷ paradas` |
| **FS$ / DM$** | Salario anual × 1,18 ÷ (tiendas × visitas por semana × 52); es el FS Cost |
| **Tip** | `Active` del Store Master (Y activa, P pendiente) |
| **#FS** | Número consecutivo del FS en la hoja `FS-CLUSTER` |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | Cada parada MUST tener los 3 IDs de ruta, `stop` secuencial, tienda, frecuencia, duración, millas y manejo | Must Have | ✅ Los IDs cumplen el patrón en las 3.664 filas | Dueño |
| FR-02 | Ninguna ruta MUST tener dos FS, y RM, DM y FS MUST coincidir con el Store Master | Must Have | ✅ 100 % | Dueño |
| FR-03 | Los supuestos del costo MUST estar en una hoja visible `Parametros` con valor, fecha y aprobador | Must Have | ❌ Escritos dentro de las consultas (DRM-A03) | Dueño |
| FR-04 | Las búsquedas al Store Master MUST hacerse por referencia de tabla, no por letra de columna | Must Have | ❌ (DRM-A04) | Dueño |
| FR-05 | El libro MUST abrirse sin filtros, filas ocultas ni `#REF!` | Must Have | ❌ El filtro oculta 3.659 de 3.664 filas; 3 columnas con `#REF!` (DRM-A05, DRM-A08) | Dueño |
| FR-06 | `#FS` y `FS-CLUSTER` MUST coincidir con el Store Master | Must Have | ❌ `#FS` = 0 en 345 paradas (DRM-A07) | Dueño |
| FR-07 | `RATE` MUST tener una sola unidad, y las rutas «Third parties» MUST decidirse | Must Have | ❌ Tres unidades; 4 rutas no entran al costo (DRM-A13) | Dueño |
| FR-08 | Los vínculos MUST apuntar a carpetas compartidas, no a archivos personales | Must Have | ❌ 2 al OneDrive de la suplente y 1 a una copia local (DRM-A01, DRM-A06) | Dueño |
| FR-09 | `Frequency` y `Duration` MUST seguir al Store Master | Should Have | ⚠️ 10 y 48 tiendas distintas (DRM-A17) | Dueño |
| FR-10 | El flujo de un cambio de ruta MUST tener identificador y registro | Should Have | ❌ Solo vive en correos (DRM-A10, DRM-A19) | Dueño |
| FR-11 | Se MUST avisar antes de renombrar, borrar o mover columnas | Must Have | ❌ Sin regla (DRM-A14, DRM-A21) | Dueño |
| FR-12 | Michaels MUST poder incluirse sin que el costo quede vacío | Should Have | ⚠️ Falta su factor en `Cargas` (DRM-A11) | Dueño |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Filas visibles al abrir el libro | 5 de 3.664 | 3.664 de 3.664 | Dueño |
| SC-02 | Columnas con `#REF!` | 3 | 0 | Dueño |
| SC-03 | Paradas con `#FS = 0` | 345 | 0 | Dueño |
| SC-04 | Lugares donde viven los supuestos del costo | Dentro de las consultas | Una hoja `Parametros` | Dueño |
| SC-05 | Rutas con el control `CHECK` en OK | 1.298 de 1.301 | 1.301 de 1.301 | Dueño |
| SC-06 | Vínculos a archivos personales o copias locales | 3 | 0 | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Tarifas, costos por supervisor y contactos del personal; todos los FS, DM y RM abren el libro y las hojas de costo no están protegidas; falta la lista de permisos | Inicial · Dueño |
| Estabilidad | Alto | Supuestos del costo sin documentar, búsquedas por letra de columna, `#REF!`, dependencias personales y poco historial ⚠️ C-07 | Inicial · Dueño |
| Escalabilidad | Medio | 3.664 filas × 49 columnas, 12 consultas (4 sin uso) y una tabla dinámica oculta con 23.587 registros viejos; Michaels aún no tiene su factor | Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🔴 Crítica | **Los supuestos del costo de servir están escritos dentro de las consultas y sin documentar.** 0,76 USD por milla, 3,74 / 3,78 / 14 visitas por semana, cargas parafiscales por cliente (1,13 / 1,23 / 1,14), un 1,18 sobre el salario, un salario por defecto, gastos generales de 5 o 13 y los umbrales 35 y 55. Los aprueban otra persona del equipo y Jennifer Guarin. **Despejar el salario de cada FS es intencional** (así se calcula el FS Cost); el riesgo que queda es que todos los FS, DM y RM abren el libro y las hojas ocultas no están protegidas. | Dueño |
| R2 | 🟡 Media | **Se usan dos modelos de costo a propósito.** App Routes: 0,725 por milla, multiplicador 1,18, FS 15 y DM 3,4 por parada, cargo fijo 5. Route Master: 0,76, cargas por cliente, FS y DM por salario, gasto general 5 o 13. El dueño dice que dan resultados muy aproximados; falta medir cuánto se separan. | Dueño |
| R3 | 🟠 Alta | **Los archivos se leen en círculo.** El Route Master lee `C2S FS/MILES` de una hoja del DSD FS Route Master, y ese archivo apunta a una **copia local** (la carpeta Descargas del dueño). Se resolverá en el análisis del DSD FS Route Master. | Dueño |
| R4 | 🔴 Crítica | **Las fórmulas buscan en el Store Master por letra de columna** (`B`, `BC`, `BI`, `BW`, `BY`…). Una columna nueva en medio del Store Master desplazaría los datos **sin dar error**. **Regla: agregar columnas solo al final y avisar antes de renombrar o borrar.** | Dueño |
| R5 | 🟠 Alta | **Un filtro guardado oculta 3.659 de 3.664 filas** (`ROUTE ID GLOBAL = GNJ002`), más 9 columnas y 8 hojas ocultas. | Dueño |
| R6 | 🟠 Alta | **`FS-CLUSTER` (escrita a mano) ya no coincide con el Store Master:** 57 de 93 `# STORE` difieren y 12 FS no están. Por eso `#FS` vale 0 en **345 paradas**. | Dueño |
| R7 | 🟠 Alta | **Tres columnas rotas (`#REF!`)** de un cambio de ABC en Sprouts (julio 2026): `ABC New` (3.637 celdas), `New Time` y `Validacion` (561 cada una). | Dueño |
| R8 | 🟠 Alta | **Dependencias personales:** dos vínculos van al OneDrive de Jennifer Guarin y los contactos de RM, DM y FS se copian de `Stores Contact List` en vez de salir del Store Master. | Dueño |
| R9 | 🟠 Alta | **`RATE` mezcla tres unidades** (por hora 15,5–20, por visita 35–50 y el texto "Third parties"). Las 4 rutas "Third parties" de Costco **no entran al costo** y nada lo avisa. | Dueño |
| R10 | 🟠 Alta | **Poco historial y ningún registro de cambios:** 500 versiones (≈ 2 meses), texto libre en `Observation` (34 %) y un flujo de solicitud, aprobación y aviso que solo vive en correos, sin identificador. | Dueño |
| R11 | 🟡 Media | **Pesa de más:** tabla dinámica oculta con 23.587 registros viejos y 4 consultas sin uso. | Dueño |
| R12 | 🟠 Alta | **Michaels llega en 2 a 4 meses y la tabla `Cargas` no tiene su factor.** Sin él, el costo de esas paradas quedaría vacío o incompleto. Hay que probar las consultas con ese cliente antes de incluirlo. | Dueño |
| R13 | 🟡 Media | **`Frequency` y `Duration` no siguen al Store Master, que es quien manda** sobre `Merch Days` y `Merch Visit Duration` (10 y 48 tiendas distintas). Cuando una ruta cambia, primero se actualiza el Store Master. | Dueño |
| R14 | 🟠 Alta | Contiene tarifas, costos y contactos del personal, y la lista de permisos no está revisada (Q-20) | Inicial |
| R15 | 🟡 Media | Si Last Visit y Visit FS leen este libro, un cambio de columnas los rompe sin aviso (Q-19) | Inicial |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Hoja visible `Parametros`, referencias de tabla, reparar `#REF!`, completar `FS-CLUSTER`, quitar el filtro y los vínculos personales y corregir los datos | Costo documentado y libro sin errores | DRM-A03, DRM-A04, DRM-A05, DRM-A06, DRM-A07, DRM-A08, DRM-A09 | Dueño |
| Corto plazo | Documentar el flujo de un cambio de ruta, preparar Michaels, regla de cambio de columnas, `RATE` en tipo y valor, alinear `Frequency` y `Duration`, diccionario y registro de cambios | Menos sorpresas y trazabilidad | DRM-A10, DRM-A11, DRM-A14, DRM-A13, DRM-A17, DRM-A18, DRM-A19 | Dueño |
| Mediano plazo | Incluir Michaels en rutas existentes, avisos a los dueños dependientes y catálogo de IDs | Cobertura completa y sin roturas | DRM-A20, DRM-A21, DRM-A16 | Dueño |
| Largo plazo | Limpiar consultas y pivote, retirar copias, documentar los dos modelos de costo, protección de hoja y evaluar una base de datos | Libro liviano y validado | DRM-A23, DRM-A24, DRM-A25, DRM-A27, DRM-A28 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| DRM-A01 | Verificar permisos de ambos co-responsables y pasar a la carpeta compartida los archivos del OneDrive de Jennifer | P0 | Dueño y suplente | Dueño | T-001 |
| DRM-A02 | Publicar este resumen y el diccionario junto al libro | P0 | Dueño | Dueño | T-002 |
| DRM-A03 | Hoja visible `Parametros` con todos los supuestos del costo (valor, fecha, aprobador) | P0 | Dueño | Dueño | T-003 |
| DRM-A04 | Reemplazar las búsquedas por letra de columna por referencias de tabla | P0 | Dueño | Dueño | T-004 |
| DRM-A05 | Reparar o borrar `#REF!` | P0 | Dueño | Dueño | T-006 |
| DRM-A06 | Quitar vínculos a archivos personales | P0 | Dueño | Dueño | T-007 |
| DRM-A07 | Completar `FS-CLUSTER` | P0 | Dueño | Dueño | T-008 |
| DRM-A08 | Quitar filtro guardado y ocultos | P0 | Dueño | Dueño | T-010 |
| DRM-A09 | Corregir fechas, `stop` y la celda con fórmula | P0 | Dueño | Dueño | T-011 |
| DRM-A10 | Documentar el flujo de un cambio de ruta (plantilla de correo e identificador por solicitud) | P1 | Dueño | Dueño | T-026 |
| DRM-A11 | Preparar Michaels: factor en `Cargas` y pruebas de las consultas | P1 | Dueño | Dueño | T-027 |
| DRM-A12 | Revisar la audiencia del libro y proteger las hojas de costo por FS y DM si se decide | P1 | Dueño | Dueño | T-009 |
| DRM-A13 | Separar `RATE` en tipo y valor; resolver "Third parties" | P1 | Dueño | Dueño | T-012 |
| DRM-A14 | Regla de cambio de columnas | P1 | Dueño | Dueño | T-013 |
| DRM-A15 | `Start Time` sin depender del orden | P1 | Dueño | Dueño | T-014 |
| DRM-A16 | Catálogo de IDs | P1 | Dueño | Dueño | T-015 |
| DRM-A17 | Alinear Frequency y Duration con el Store Master (que manda) | P1 | Dueño | Dueño | T-016 |
| DRM-A18 | Diccionario y validaciones | P1 | Dueño | Dueño | T-017/T-018 |
| DRM-A19 | Registro de cambios | P1 | Dueño | Dueño | T-019 |
| DRM-A20 | Incluir Michaels en rutas existentes (2 a 4 meses) | P1 | Dueño | Dueño | T-020 |
| DRM-A21 | Avisos a dueños de archivos dependientes | P1 | Dueño | Dueño | T-022 |
| DRM-A22 | Vínculo de FS Route Master (en su propio análisis) | P1 | Dueño | Dueño | T-005 |
| DRM-A23 | Limpiar consultas y pivote | P2 | Dueño | Dueño | T-021 |
| DRM-A24 | Retirar copias | P2 | Dueño | Dueño | T-023 |
| DRM-A25 | Documentar los dos modelos de costo y medir su diferencia | P2 | Dueño | Dueño | T-025 |
| DRM-A26 | Documentar Route Studio | P2 | Dueño | Dueño | T-028 |
| DRM-A27 | Protección de hoja | P2 | Dueño | Dueño | T-033 |
| DRM-A28 | Evaluar una base de datos | P2 | Dueño | Dueño | T-040 |
| DRM-A29 | Confirmar si Last Visit y Visit FS leen este libro y, si no, corregir el inventario | P1 | Dueño y PERFORMANCE | Inicial | C-04 |
| DRM-A30 | Revisar la lista de personas con acceso al libro y quién aprueba los accesos nuevos | P1 | Dueño e IT | Inicial | Q-20 |
| DRM-A31 | Hacer la revisión técnica con IT: tarifas, costos y contactos del personal | P1 | IT | Inicial | — |
| DRM-A32 | Guardar esta spec, el código de las consultas de Power Query y la hoja de parámetros en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| DRM-A33 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-18 | ¿Qué diferencia entre el costo de App Routes y el C2S del Route Master es aceptable? ¿Se comparó con rutas reales? | Jennifer Guarin | Dueño |
| Q-06 a Q-13 | `RATE` y "Third parties", Global vs Route ID, visitas repetidas de Costco, columnas ABC, hojas ocultas, regla de duración por ABC, vigencia de archivos externos y copias. Ver el documento completo | Varios | Dueño |
| Q-19 | ¿Last Visit y Visit FS leen este libro, o solo los archivos que menciona el dueño? | Dueño y PERFORMANCE | Inicial |
| Q-20 | ¿Quiénes tienen acceso al libro y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Hojas visibles y ocultas | Inicial: 7 visibles y 3 ocultas. Dueño: 10 hojas, 8 ocultas | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-02 | Tamaño | Inicial: ≈ 3.658 filas × 56 columnas. Dueño: 3.664 filas × 49 columnas | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-03 | Responsables y suplente | Inicial: creador y administrador el dueño, sin suplente. Dueño: son co-responsables, ambos tienen la contraseña y cada uno respalda al otro | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-04 | Quién lo lee | Inicial (inventario): Last Visit y Visit FS. Dueño: Execution Team y FS, DM y RM en lectura; lo copian o leen el DSD FS Route Master, el Route Master Copy, el Michaels Router Pilot y el análisis de incidentes | Lo del dueño; confirmar con PERFORMANCE (Q-19) | ❓ Por confirmar |
| C-05 | Frecuencia | Inicial: según la necesidad. Dueño: 500 versiones en 42 días, con cada cambio de ruta | Cada cambio de ruta; casi diaria | ✅ Resuelta a favor del dueño |
| C-06 | Cómo se alimenta | Inicial: por confirmar; sugería relación con Isolved y AFS. Dueño: desde App Routes (traspaso manual), el Store Master y archivos externos, entre ellos el Requis ID Book con el ID de iSolved | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-07 | Nivel de riesgo | Inicial: estabilidad «Medio» y escalabilidad «Bajo». Dueño: supuestos del costo sin documentar, búsquedas por letra de columna, `#REF!`, dependencias personales y poco historial | Estabilidad «Alto» y escalabilidad «Medio» | ❓ Por confirmar |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, inventario de consultas y fórmulas, calidad de datos y backlog completo) todavía no están integrados.
- Las preguntas menores Q-06 a Q-13 (`RATE` y «Third parties», Global frente a Route ID, visitas repetidas de Costco, columnas ABC, hojas ocultas, regla de duración por ABC, vigencia de archivos externos y copias) están en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/dsd-route-master/spec.md`. [Inicial]
- Incluir el código de las 12 consultas de Power Query y la hoja `Parametros` del costo, sin datos de rutas, tarifas ni salarios. [Dueño · Inicial]
- Mantener en el mismo repositorio la documentación de los dos modelos de costo (App Routes y Route Master) y su comparación. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Modelar rutas y paradas como tablas (ruta, parada, tienda) con clave `Route ID` más `stop`. [Dueño · Inicial]
2. Guardar los supuestos del costo en una tabla de parámetros con valor, fecha y aprobador (DRM-A03). [Dueño]
3. Leer la jerarquía del Store Master por nombre de columna o desde la réplica SQL, no por letra de columna (DRM-A04). [Dueño · Inicial]
4. Calcular el costo de servir en SQL y medir la diferencia con App Routes (DRM-A25). [Dueño]
5. Exponer una vista con los nombres actuales de las tablas `RouteMaster` y `StoreMaster_DSD` para el DSD FS Route Master, el Plan de visitas y el Stores Contact List. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 4 | Dos co-responsables que se respaldan; falta mover los archivos personales |
| Operación documentada | 2 | Flujo de cambio por correo y lista de verificación propuesta |
| Control de acceso | 2 | Todos los FS, DM y RM abren el libro; hojas de costo sin proteger |
| Contrato de datos | 1 | Supuestos del costo en las consultas; búsquedas por letra de columna |
| Calidad y validación | 2 | Los IDs cumplen el patrón; `#REF!` y `#FS = 0` |
| Automatización e integración | 2 | Consultas de Power Query, pero el traspaso desde App Routes es manual |
| Trazabilidad de cambios | 1 | Solo 500 versiones (≈ 2 meses) y un flujo en correos sin identificador |
| Entornos y pruebas | 2 | Hay copias y pilotos; falta probar Michaels |

**Nivel global: 2,1 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.

---

# Spec · DSD FS Route Master

> **English version pending.** This document is currently available in Spanish only.

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m21 (inventario MIC) |
| Tipo | Base de datos: libro de Excel (rutero de los supervisores de campo) alimentado desde un planner web y Power Query |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Rutero de los **supervisores de campo (FS)**. Cada fila es un paso del día de un FS: salir de su tienda base, visitar tiendas en un orden, almorzar (`BREAK`) y volver. Guarda millas y manejo, gastos de viaje y el **costo por tienda**; la jerarquía, las coordenadas y la dirección salen de una copia del Store Master. Sirve para ver la mejor manera en que cada FS visita sus tiendas y para organizar el costo de cada uno (hoja `Costs`: presupuesto mensual por FS; hoja oculta `C2SFS`: costo promedio por visita, que el DSD Route Master lee como `C2S FS/MILES`). [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 4.232 filas (2.503 visitas a tiendas + 1.158 filas de tienda base + 571 `BREAK`) × 35 columnas | Dueño |
| Rutas | 579 (`FSTN001`…), 4,3 tiendas por ruta en promedio, 71 con gastos de viaje | Dueño |
| Cobertura | 104 FS de los 105 con tiendas activas · 2.503 tiendas: Walmart 1.773 · Sprouts 475 · Michaels 163 · Costco 88 | Dueño |
| Jerarquía | 4 RMs · 14 DMs · 104 FS | Dueño |
| Libro | 11 hojas (9 ocultas) · 14 consultas de Power Query (3 en uso real) · 2 vínculos externos ⚠️ C-01 | Dueño |
| Actividad | 357 versiones en 75 días: 356 del dueño y 1 de la suplente ⚠️ C-04 | Dueño |
| Fuente | 104 archivos `Routes` y 105 `Stores` en 107 carpetas de FS | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Medio ⚠️ C-06 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🟠 **El costo por tienda se calcula en 104 archivos distintos** y llega pegado como valor: el 0,725 por milla está escrito en cada fórmula y no hay hoja de parámetros. [Dueño]
2. 🟠 **Copiar y pegar sin control:** coinciden 578 de las 579 rutas con `Router Test` y nadie avisa cuando el libro se queda atrás. [Dueño]
3. 🟠 **La copia del Store Master está atrás** (32 tiendas con otro FS, 34 con otro `Active`) y se lee por letra de columna (13 columnas). [Dueño]
4. 🟠 **92 tiendas activas sin ruta,** 4 filas con tienda inactiva o inexistente y 5 rutas con tiendas de dos FS. [Dueño]
5. 🟠 **Todo depende de una persona** (356 de 357 versiones) y el procedimiento no está escrito. [Dueño]
6. ⚠️ **El inventario lista a Last Visit y Visit FS como lectores;** el dueño solo menciona al DSD Route Master (C-03). [Inicial]

**Funciona bien:** **Estructura de las rutas:** las 579 empiezan y terminan en la tienda base; `stop` es secuencial en las 579; ninguna tienda se repite ni está en dos rutas. **Datos de cada paso:** duración y frecuencia coinciden al 100 % con `Router Test`. **Tienda base:** 92 de 93 coinciden con `Field-Supervisors_home_stores.xlsx`. **Costos:** `C2SFS` tiene los 104 FS con valor. [Dueño]

**Contradicciones:** 7 detectadas; 5 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (FSR-A01, FSR-A02, FSR-A03, FSR-A04, FSR-A05, FSR-A06, FSR-A07, FSR-A08, FSR-A09, FSR-A31) y las preguntas Q-19 y Q-20. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Ver la mejor manera en que cada FS visita sus tiendas y **organizar el costo de cada uno**: presupuesto mensual por FS y costo promedio por visita, que alimenta el costo del DSD Route Master.

- **Problema que resuelve:** FS, DM y RM necesitan coordinar sus viajes y rutas, y el costo de cada FS debe salir de un solo lugar. [Dueño]
- **Qué logra:** un rutero con todos los pasos del día de cada FS, millas, manejo, gastos de viaje y costo por tienda. [Dueño]
- **Éxito:** el costo sale de parámetros únicos, el libro coincide con `Router Test` y cada tienda activa tiene su ruta (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: el FS Route Master y el proceso que lo alimenta (carpeta `Tiendas x FS` y `Router Test`).

**No incluye** [Dueño]: el Store Master y el Route Master de mercaderistas (ya tienen su análisis); el planner web, `DM Costs`, `Travel Monthly Budget` y `Convertidor plan`, que se listan como dependencias.

**Futuro** [Dueño]: cargar sin copiar y pegar (FSR-A22), evaluar una base de datos (FSR-A23), validaciones y protección (FSR-A24) y documentar el planner (FSR-A25).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| FS, DM y RM | Consultan el rutero para coordinar sus viajes y rutas; todos tienen permiso de lectura y saben dónde está | 104 FS · 14 DM · 4 RM | Dueño |
| Responsable (el dueño) | Alimenta todo el libro | 356 de 357 versiones | Dueño |
| Suplente | Aprueba los parámetros del costo | — | Dueño |
| DSD Route Master | Lee `C2SFS` como `C2S FS/MILES` | — | Dueño |
| Presupuesto de viaje por FS (hoja `Costs`) | Presupuesto mensual por FS, tomado de `DM Costs.xlsx` | — | Dueño |

**Acceso**

- Está en SharePoint › DSD Business Analysis › DSD Data Master, con permisos propios; las fuentes están en otro sitio (Sales Administration › Field Routes › Tiendas x FS). [Dueño]
- Exige cuenta de la empresa y permiso. [Dueño · Inicial]
- La cuenta del planner la paga Falcon y la usan la suplente, el dueño y otras personas: el acceso no es el riesgo. [Dueño]
- ❓ Falta la lista de personas con acceso al libro y a la carpeta, y quién aprueba los accesos nuevos (Q-20). [Inicial]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño · Inicial]

- Alimenta todo el libro: diseña las rutas en el planner, las guarda en la carpeta del FS y las pega en el rutero.
- Completa en cada `Routes` el `#Stores`, los gastos de viaje, `Visits x Month` y las fórmulas de costo, y asigna el `ROUTE ID GLOBAL`.
- Aprobó su análisis el 2026-10-21 (v1.5).

## Administrador técnico

**Jeronimo Sanchez**, administra el libro. [Inicial]

- Administra el libro en SharePoint, su Power Query y los archivos de la carpeta `Tiendas x FS`. [Dueño]
- ❓ Quién aprueba los accesos nuevos (Q-20).

## Suplente

**Jennifer Guarin.** Aprueba los parámetros del costo y ya tiene acceso al planner; faltan sus accesos a la carpeta y a `DM Costs` y el procedimiento escrito. [Dueño]

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Planner web | Diseñar y descargar rutas | ✅ Tiene acceso |
| Parámetros del costo | Aprobarlos | ✅ Los aprueba |
| Carpeta `Tiendas x FS` | Editar los archivos de cada FS | ⬜ Pendiente (FSR-A01) |
| `DM Costs.xlsx` | Leerlo para el presupuesto | ⬜ Pendiente (FSR-A01) |
| Procedimiento de alta, baja y cambio | Seguirlo sin ayuda | ⬜ Pendiente (FSR-A02) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| `Stores` y `Routes` por FS | Tiendas y rutas diseñadas en el planner; una carpeta por DM y, dentro, una por FS | Dueño | Dueño |
| `Router Test.xlsx` | Consulta de Power Query que une la hoja `Combined` de todos los `Routes` | Dueño | Dueño |
| `Field-Supervisors_home_stores.xlsx` | Tienda base de cada FS | Dueño | Dueño |
| Copia del Store Master (`StoreMaster DSD`) | Jerarquía, coordenadas y dirección; 13 búsquedas por letra de columna | Dueño | Dueño |
| `DM Costs.xlsx` | Presupuesto mensual por FS (`Costs`) | Dueño | Dueño |
| Cotizaciones de viaje | Gastos de viaje de las rutas | La persona que cotiza los viajes | Dueño |

**Cómo se alimenta** [Dueño]

1. Las rutas se diseñan en el planner web: se sube el `Stores`, se diseñan las rutas y se descarga el `Routes`, que se guarda en la carpeta del FS.
2. `Router Test` toma la hoja `Combined` de todos los `Routes` y la une en una tabla.
3. De las 35 columnas del rutero, 14 se copian y pegan desde `Router Test`, 6 se escriben a mano, 13 son búsquedas al Store Master y `#FS` y `Start Time` son fórmulas.
4. **Baja de un FS:** se borran sus archivos y sus filas. **Alta:** se crean sus archivos y rutas, se corre la consulta y se pegan solo las filas del FS nuevo, al final.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | Planner web · SharePoint · Excel con Power Query |
| Archivos | Carpeta `Tiendas x FS` · `Router Test` · `Field-Supervisors_home_stores` · Store Master · `DM Costs` |
| Personas | El dueño y su suplente |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| DSD Route Master | Lee la hoja oculta `C2SFS` como `C2S FS/MILES` | Dueño del DSD Route Master |
| Plan de visitas (Unify) | Su generador lee el costo diario del FS (consulta `CostFS`) | Dueño y suplente |
| FS, DM y RM | Consultan sus rutas y su presupuesto de viaje | — |
| Last Visit y Visit FS ❓ | El inventario los lista como lectores; el dueño no los menciona (Q-19) | PERFORMANCE |

## Procesos operativos

[Dueño] Se actualiza con cada cambio de rutas y con cada alta o baja de FS: 357 versiones en 75 días, casi todas del dueño. ⚠️ C-04

1. **Antes:** confirmar que el FS existe en el Store Master con RM, DM y tiendas; actualizar la copia `StoreMaster DSD`.
2. **Planner:** subir el `Stores` del FS; **escribir `Home Store` y `Home Store (end)` exactamente así** (hoy hay 11 variantes); diseñar y descargar el archivo `MyRouteOnline_…xlsx`.
2b. **Completar y guardar:** renombrarlo `Routes - Apellido, Nombre - (m-d-aaaa).xlsx`, ponerlo en la carpeta del FS y agregar `#Stores`, gastos de viaje (cotizados con la persona que cotiza los viajes), `Visits x Month`, las fórmulas de `Totals` y las 7 columnas de `Combined`.
3. **Consolidar:** actualizar `Router Test` y comparar filas y rutas con el libro.
4. **Pegar:** reemplazar (cambio de ruta) o agregar al final (FS nuevo); **no ordenar la tabla**; construir `ROUTE ID GLOBAL`.
5. **Baja:** borrar archivos y filas; actualizar `Costs`, `DM Costs` y los archivos dependientes.
6. **Revisar:** sin `#N/A` en `STATE`, `Active`, RM, DM o FS; el FS nuevo aparece en `C2SFS` (el Route Master lo lee).
7. **Registrar:** `Last Date Up` y una nota del cambio.
8. **Avisar:** a los dueños de los archivos dependientes.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- Una ruta empieza y termina en la tienda base, y cada tienda está en una sola ruta.
- `Start Time` es la hora de finalización de cada paso; el encabezado dice «inicio» pero es intencional.
- `Milleage` significa «desde la parada anterior» aquí, y «hasta la siguiente» en el Route Master de mercaderistas.
- Los costos se repiten en cada fila de la ruta: sumar la columna cuenta cada gasto varias veces.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Ruta (`ROUTE ID GLOBAL`)** | Un día de trabajo de un FS: sale de la tienda base, visita de 1 a 10 tiendas y regresa. `FS` + estado predominante entre las tiendas + consecutivo del estado (`FSTN001`). Lo creó un generador en la carga masiva (578 de 579 rutas cumplen la regla). Hoy lo asigna el dueño: ruta nueva = estado predominante + último ID del estado + 1; rediseñada = conserva el ID salvo que cambie el estado predominante; eliminada = su número no se reutiliza |
| **Home Store** | Tienda base del FS, donde empieza y termina el día (2 filas por ruta, duración 0) |
| **FFM** | Tienda base especial de 13 rutas de Florida ⚠️ por confirmar |
| **BREAK** | Descanso de 30 minutos que inserta el planner (571 de 579 rutas) |
| **Duration** | 60 minutos por tienda (todas), 30 por `BREAK`, 0 en la tienda base |
| **Frequency x Month** | Veces al mes que se recorre la ruta: 2 (475 rutas), 1 (83), 4 (19), 0,5 (2) |
| **Milleage / Driving Time** | Millas y minutos **desde la parada anterior** (la fila de regreso trae el viaje de vuelta) |
| **Start Time** | **Hora de finalización** de cada paso (7:00 + minutos acumulados); el encabezado dice "inicio" |
| **Cost x Route / Month / Store** | Millas × 0,725 · × visitas al mes (+ viaje) · ÷ n.º de tiendas. Se calcula en cada `Routes` y se pega |
| **Promedio Daily Visit Cost (`C2SFS`)** | Promedio por FS de `COST x Store ÷ 4,3 ÷ 3,75` (Costco `÷ 7`); es el `C2S FS/MILES` del Route Master. Es una consulta que promedia el costo por visita de las rutas de cada FS; los parámetros los aprueba Jennifer Guarin ⚠️ unidad por confirmar |
| **Budget x Month (`Costs`)** | Presupuesto mensual por FS, tomado de `DM Costs.xlsx` |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | Cada ruta MUST empezar y terminar en la tienda base, con `stop` secuencial | Must Have | ✅ 579 de 579 rutas | Dueño |
| FR-02 | Cada tienda activa con FS MUST estar en una sola ruta | Must Have | ❌ 92 sin ruta; 5 rutas con tiendas de 2 FS (FSR-A07, FSR-A21) | Dueño |
| FR-03 | El costo por tienda MUST calcularse con parámetros únicos y documentados | Must Have | ❌ 0,725 escrito en 104 archivos (FSR-A10) | Dueño |
| FR-04 | El libro MUST coincidir con `Router Test` en conteo de filas y rutas | Must Have | ⚠️ 578 de 579; `FSME001` con una fila de más (FSR-A08) | Dueño |
| FR-05 | La copia del Store Master MUST estar al día y leerse por nombre de columna | Must Have | ❌ 32 FS y 34 `Active` distintos; 13 columnas por letra (FSR-A04, FSR-A05) | Dueño |
| FR-06 | Las columnas heredadas MUST completarse o retirarse (`#FS`, `CLUSTER FS`) | Should Have | ❌ `#N/A` en 1.437 filas; vacía en 4.232 (FSR-A06) | Dueño |
| FR-07 | `C2SFS` MUST tener valor para todos los FS | Must Have | ✅ 104 de 104 | Dueño |
| FR-08 | El alta, la baja y el cambio de FS MUST seguir un procedimiento escrito y probado | Must Have | ❌ (FSR-A02) | Dueño |
| FR-09 | Se MUST avisar a los dueños de los archivos dependientes antes de renombrar o mover columnas | Must Have | ❌ Sin regla (FSR-A14) | Dueño |
| FR-10 | Todo cambio MUST ser trazable | Should Have | ❌ Solo versiones de SharePoint (FSR-A16) | Dueño |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Rutas que coinciden con `Router Test` | 578 de 579 | 579 de 579 | Dueño |
| SC-02 | Tiendas activas con ruta, o con motivo documentado | 92 sin ruta | 0 | Dueño |
| SC-03 | Lugares donde viven las constantes del costo | 104 archivos + consulta + `Convertidor plan` | 1 hoja `Parametros` | Dueño |
| SC-04 | Filas con `#N/A` en `#FS` | 1.437 | 0 (columna completada o retirada) | Dueño |
| SC-05 | Hojas ocultas sin lector revisadas y retiradas por etapas | 0 de 3 sin lector · 0 de 3 de la isla | Todas revisadas | Dueño |
| SC-06 | Componentes que opera la suplente | 2 de 5 | 5 de 5 | Dueño · Inicial |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Costos, presupuesto y datos de viaje por FS; exige cuenta y permiso; conexiones a nómina heredadas; falta la lista de permisos | Inicial · Dueño |
| Estabilidad | Alto | El costo se calcula en 104 archivos, el libro se actualiza copiando y pegando sin control, la copia del Store Master está atrás y todo depende de una persona ⚠️ C-06 | Inicial · Dueño |
| Escalabilidad | Medio | 4.232 filas × 35 columnas, 14 consultas (3 en uso) y 60.332 fórmulas heredadas en `old router`; el proceso por FS es manual ⚠️ C-06 | Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🟠 Alta | **El costo por tienda se calcula en 104 archivos distintos y llega pegado como valor.** Cada `Routes` multiplica las millas por **0,725** (escrito en la fórmula), por las visitas al mes y lo divide entre las tiendas. No hay hoja de parámetros: 4,3 semanas, 3,75 y 7 días (Costco) viven en la consulta `CostFS`; 4,34524 en `Convertidor plan`; el Route Master usa 0,76 por milla. Cambiar una constante exige editar 104 archivos. | Dueño |
| R2 | 🟠 Alta | **Copiar y pegar sin ningún control.** Hoy coinciden **578 de las 579 rutas** con `Router Test`; la ruta `FSME001` tiene una fila de más y hay 17 filas con millas y 20 con costo distintos. Nadie avisa cuando el libro se queda atrás. | Dueño |
| R3 | 🟠 Alta | **Columnas heredadas del Route Master que ya no funcionan.** `#FS` vale `#N/A` en **1.437 filas** y `CLUSTER FS` está vacía en las 4.232. Ninguna consulta usa `#FS`. | Dueño |
| R4 | 🟠 Alta | **La copia del Store Master está atrás** (32 tiendas con otro FS, con marcadores `New_FS_…`; 34 con otro `Active`; 3 activas faltan) y se lee **por letra de columna** (13 columnas). | Dueño |
| R5 | 🟠 Alta | **92 tiendas activas sin ruta** (Walmart 40 · Sprouts 39 · Michaels 10 · Costco 3): 30 son de una FS nueva (carpeta con `Stores`, sin `Routes`); 2 no tienen FS. | Dueño |
| R6 | 🟠 Alta | **4 filas con tienda inactiva o inexistente** (RM, DM y FS en 0) y **5 rutas con tiendas de dos FS** (`FSPA009`, `FSTX039`, `FSTX042`, `FSTX061`, `FSCA051`). | Dueño |
| R7 | 🟡 Media | **`Start Time` es la hora de finalización de la visita** (intencional; 3.036 de 3.077 filas comparables), pero el encabezado dice "inicio" y FS, DM y RM lo leen para coordinar sus rutas. Renombrarlo exige cambiar también la consulta `CostFS`. | Dueño |
| R8 | 🟠 Alta | **`Router Test` es un archivo de pruebas que opera como producción:** su consulta lee todo el sitio de SharePoint, tiene 18 columnas escritas a mano y no limpia `Home Store` (11 variantes de la etiqueta). Hay 3 FS con `Routes` fechados en 2025. | Dueño |
| R9 | 🟠 Alta | **Hojas y consultas heredadas.** 9 de 11 hojas ocultas; solo 3 de 14 consultas alimentan algo en uso. Cuatro leen una tabla `RouteMaster` que ya no existe aquí, y `old router` pesa 60.332 fórmulas. El libro se construyó **duplicando el Route Master**, por eso están. Las que no se usan para nada se podrían borrar, pero el dueño quiere **revisarlas con detalle antes** (sin editar el archivo): de las 9 ocultas, **3 no tienen ningún lector** (`old router`, `MC`, `ST-RATE`), **3 forman una isla** sin lectores externos (`C2S`, `FS Cost`, `Dm Cost`) y **3 se usan** (`StoreMaster DSD`, `C2SFS`, `FS-CLUSTER`). Detalle y orden de borrado en el Anexo B del documento completo. | Dueño |
| R10 | 🟡 Media | **El vínculo a la copia local (`DSD Route Master copy Sep16.xlsx`) solo lo usa la hoja oculta `old router`.** El costo no depende de él: se pueden convertir esas 285 fórmulas en valores o dejarlo documentado, sin borrar la hoja. Esto cierra el pendiente del análisis del Route Master. | Dueño |
| R11 | 🟡 Media | **Dos significados de `Milleage`** (aquí *desde* la parada anterior; en el Route Master de mercaderistas, *hasta* la siguiente) y **costos repetidos en cada fila** de la ruta: sumar la columna cuenta cada gasto varias veces. | Dueño |
| R12 | 🟠 Alta | **Todo depende de una persona:** 356 de 357 versiones; el flujo no está escrito. La cuenta del planner la paga Falcon y la usan Jennifer Guarin, Jeronimo Sanchez y otras personas, así que el acceso no es el riesgo. | Dueño |
| R13 | 🟡 Media | **El libro conserva conexiones a nómina** (`Salary`, `Table2`) y hojas de costo por salario (`FS Cost`, `Dm Cost`) que son restos del Route Master. Aquí el costo del FS no usa salarios. | Dueño |
| R14 | 🟠 Alta | Contiene costos, presupuesto y datos de viaje por supervisor, y la lista de permisos no está revisada (Q-20) | Inicial |
| R15 | 🟡 Media | Si Last Visit y Visit FS leen este libro, un cambio de columnas los rompería sin aviso (Q-19) | Inicial |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Actualizar la copia del Store Master, corregir rutas y filas con error, y completar o retirar `#FS` y `CLUSTER FS` | Datos al día y sin errores | FSR-A05, FSR-A06, FSR-A07, FSR-A08 | Dueño |
| Corto plazo | Hoja `Parametros` con el costo calculado en el libro; convención de nombres y fechas; `Router Test` como archivo de producción; diccionario y registro de cambios | Un solo lugar para las constantes y trazabilidad | FSR-A10, FSR-A11, FSR-A12, FSR-A15, FSR-A16 | Dueño |
| Mediano plazo | Borrar por etapas las piezas heredadas, con copia previa, y quitar las conexiones a nómina | Libro más liviano y claro | FSR-A09, FSR-A20 | Dueño |
| Largo plazo | Cargar sin copiar y pegar, evaluar una base de datos y agregar validaciones y protección | Menos trabajo manual y datos validados | FSR-A22, FSR-A23, FSR-A24 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| FSR-A01 | Verificar accesos de Jennifer Guarin a los archivos | P0 | Dueño y suplente | Dueño | T-001 |
| FSR-A02 | Escribir y probar el procedimiento de alta, baja y cambio | P0 | Dueño | Dueño | T-003 |
| FSR-A03 | Quitar la dependencia de la copia local | P0 | Dueño | Dueño | T-005 |
| FSR-A04 | Búsquedas por nombre de columna | P0 | Dueño | Dueño | T-004 |
| FSR-A05 | Actualizar `StoreMaster DSD` | P0 | Dueño | Dueño | T-006 |
| FSR-A06 | `#FS` y `CLUSTER FS` | P0 | Dueño | Dueño | T-007 |
| FSR-A07 | 4 filas y 5 rutas con 2 FS | P0 | Dueño | Dueño | T-008 |
| FSR-A08 | Control de conteo contra `Router Test` y corregir `FSME001` | P0 | Dueño | Dueño | T-009 |
| FSR-A09 | Borrar las piezas heredadas por etapas (Anexo B), con copia previa | P0 | Dueño | Dueño | T-010 |
| FSR-A10 | Hoja `Parametros` y costo calculado en el libro | P1 | Dueño | Dueño | T-011 |
| FSR-A11 | Convención de nombres y fechas; `Home Store` | P1 | Dueño | Dueño | T-012 |
| FSR-A12 | `Router Test` como archivo de producción | P1 | Dueño | Dueño | T-013 |
| FSR-A13 | Regla del `ROUTE ID GLOBAL` | P1 | Dueño | Dueño | T-014 |
| FSR-A14 | Encabezado de `Start Time` (junto con `CostFS`) | P1 | Dueño | Dueño | T-015 |
| FSR-A15 | Diccionario | P1 | Dueño | Dueño | T-016 |
| FSR-A16 | Registro de cambios | P1 | Dueño | Dueño | T-017 |
| FSR-A17 | Convención de carpetas | P1 | Dueño | Dueño | T-018 |
| FSR-A18 | Cadena de costos de viaje | P1 | Dueño | Dueño | T-019 |
| FSR-A19 | Aviso sobre `Milleage` | P1 | Dueño | Dueño | T-020 |
| FSR-A20 | Quitar conexiones a nómina | P1 | Dueño | Dueño | T-021 |
| FSR-A21 | Rutas de una FS nueva y 62 tiendas | P1 | Dueño | Dueño | T-022 |
| FSR-A22 | Cargar sin copiar y pegar | P2 | Dueño | Dueño | T-023 |
| FSR-A23 | Evaluar base de datos | P2 | Dueño | Dueño | T-024 |
| FSR-A24 | Validaciones y protección | P2 | Dueño | Dueño | T-025 |
| FSR-A25 | Documentar el planner | P2 | Dueño | Dueño | T-026 |
| FSR-A26 | Audiencia de `Costs` (Q-17) | P2 | Dueño | Dueño | T-027 |
| FSR-A27 | Confirmar si Last Visit y Visit FS leen este libro y, si no, corregir el inventario | P1 | Dueño y PERFORMANCE | Inicial | C-03 |
| FSR-A28 | Revisar la lista de personas con acceso al libro y a la carpeta, y quién aprueba los accesos nuevos | P1 | Dueño e IT | Inicial | Q-20 |
| FSR-A29 | Hacer la revisión técnica con IT: costos y presupuesto por FS y conexiones a nómina | P1 | IT | Inicial | — |
| FSR-A30 | Guardar esta spec, las consultas de Power Query y las fórmulas del costo en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| FSR-A31 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-06 | `FFM` | Dueño (se resuelve con su tarea) | Dueño |
| Q-06b | fuente de la tienda base | Dueño (se resuelve con su tarea) | Dueño |
| Q-07 | `#FS`, `FS-CLUSTER` y `CLUSTER FS` | Dueño (se resuelve con su tarea) | Dueño |
| Q-08 | archivos `Total Costs`, `Travel Monthly Budget` y `Convertidor plan` | Dueño (se resuelve con su tarea) | Dueño |
| Q-09 | `Routes` de 2025 | Dueño (se resuelve con su tarea) | Dueño |
| Q-10 | `Visits x Month` 0,5 y 4 | Dueño (se resuelve con su tarea) | Dueño |
| Q-11 | tiendas sin ruta | Dueño (se resuelve con su tarea) | Dueño |
| Q-12 | conexiones a nómina | Dueño (se resuelve con su tarea) | Dueño |
| Q-13 | nombre de `Router Test` | Dueño (se resuelve con su tarea) | Dueño |
| Q-16 | constantes de costo distintas entre libros y unidad de `Promedio Daily Visit Cost` | Dueño (se resuelve con su tarea) | Dueño |
| Q-17 | audiencia del presupuesto por FS (`Costs`) | Dueño (se resuelve con su tarea) | Dueño |
| Q-18 | frecuencia y registro de las cotizaciones de viaje de la persona que cotiza los viajes | Dueño (se resuelve con su tarea) | Dueño |
| Q-19 | ¿Last Visit y Visit FS leen este libro, o solo el DSD Route Master? | Dueño y PERFORMANCE | Inicial |
| Q-20 | ¿Quiénes tienen acceso al libro y a la carpeta, y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Hojas visibles y ocultas | Inicial: 4 visibles y 7 ocultas. Dueño: 11 hojas, 9 ocultas | Lo del dueño | ✅ Resuelta a favor del dueño |
| C-02 | Tamaño | Inicial: ≈ 4.177 filas × 35 columnas. Dueño: 4.232 filas × 35 (versión 358.0) | Lo del dueño; el archivo cambió | ✅ Resuelta a favor del dueño |
| C-03 | Quién lo lee | Inicial (inventario): Last Visit y Visit FS. Dueño: el DSD Route Master (`C2S FS/MILES`); FS, DM y RM lo consultan | Lo del dueño; confirmar con PERFORMANCE (Q-19) | ❓ Por confirmar |
| C-04 | Frecuencia | Inicial: según la necesidad. Dueño: 357 versiones en 75 días | Cada cambio de rutas o de FS; casi diaria | ✅ Resuelta a favor del dueño |
| C-05 | Relación con Isolved y AFS | Inicial: sus campos sugieren relación con esos sistemas. Dueño: las conexiones a nómina son restos del Route Master; el costo del FS no usa salarios | Lo del dueño; retirar las conexiones (FSR-A20) | ✅ Resuelta a favor del dueño |
| C-06 | Nivel de riesgo | Inicial: estabilidad «Medio» y escalabilidad «Bajo». Dueño: costo en 104 archivos, copiar y pegar sin control, copia del Store Master atrás, 9 hojas ocultas y una sola persona | Estabilidad «Alto» y escalabilidad «Medio» | ❓ Por confirmar |
| C-07 | Cómo se alimenta | Inicial: por confirmar si es manual. Dueño: 14 columnas pegadas desde `Router Test`, 6 a mano y 13 búsquedas al Store Master | Lo del dueño | ✅ Resuelta a favor del dueño |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, inventario de consultas y fórmulas, calidad de datos, y la revisión de hojas y consultas heredadas con su orden de borrado) todavía no están integrados.
- La distribución de filas por DM y FS está en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/dsd-fs-route-master/spec.md`. [Inicial]
- Incluir el código de las consultas de Power Query de `Router Test` y las fórmulas del costo, sin datos de FS ni de tiendas. [Dueño · Inicial]
- Mantener en el mismo repositorio la hoja de parámetros del costo (0,725, semanas y días) y su historial de cambios. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Modelar rutas y pasos como tablas (ruta, paso, FS, tienda), con clave `ROUTE ID GLOBAL` más `stop`, y calcular el costo en SQL desde una tabla de parámetros (FSR-A10). [Dueño · Inicial]
2. Cargar los `Routes` con un proceso programado en lugar de copiar y pegar (FSR-A22). [Dueño]
3. Leer la jerarquía del Store Master por nombre de columna o desde la réplica SQL, no desde una copia (FSR-A04, FSR-A05). [Dueño · Inicial]
4. Exponer `C2SFS` como una vista con el nombre `C2S FS/MILES` para el DSD Route Master. [Dueño]
5. Retirar primero las piezas heredadas (FSR-A09) y migrar solo lo que se usa. [Dueño]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 3 | Dueño y suplente definidos; la suplente aprueba el costo y le faltan accesos |
| Operación documentada | 2 | Lista de verificación propuesta; el flujo no estaba escrito |
| Control de acceso | 3 | Cuenta y permiso; lectura para FS, DM y RM |
| Contrato de datos | 1 | Sin diccionario; encabezados engañosos; lectura por letra de columna |
| Calidad y validación | 2 | 578 de 579 rutas coinciden; `#N/A` en 1.437 filas |
| Automatización e integración | 2 | Consulta de Power Query, pero las columnas se pegan a mano |
| Trazabilidad de cambios | 1 | Solo versiones de SharePoint |
| Entornos y pruebas | 1 | `Router Test`, un archivo de pruebas, opera como producción |

**Nivel global: 2,0 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.

---

# Spec · Plan de visitas (Unify)

> **English version pending.** This document is currently available in Spanish only.

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m22 (inventario MIC) |
| Tipo | Base de datos: carpeta de libros de Excel mensuales (Labor Unif) y generador `plan1.xlsx` con Power Query |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos) y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Inicial]** análisis SDD inicial · **[Independiente]** análisis independiente · ⚠️ contradicción (ver «Información pendiente por confirmar») · ❓ por confirmar. Cuando el dueño y el análisis inicial difieren, vale lo del dueño.

## Resumen Ejecutivo

Plan mensual de ejecución de rutas: una fila por tienda activa y por día del mes, con ruta, orden de parada, horas de servicio, costo de servir, millas, tiempo de manejo, ventana horaria y RM → DM → FS. Como el Route Master y el Store Master solo guardan el estado de hoy, **cada Labor Unif es el único registro de cómo estaba el plan ese mes**. También se conoce como Plan Unify o «Labor Unif». [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Octubre | 77.188 filas · 2.411 tiendas · 31 días · 1.285 rutas · 60.024 h planeadas · 44.720 filas con visita (58 %) ⚠️ C-07 | Dueño |
| Clientes | Walmart 55.668 · Sprouts 15.724 · Costco 5.796 filas | Dueño |
| Costo | 53 tarifas por hora (17,51 a 56,50); `$ /dia` = horas × tarifa en el 100 % de octubre | Dueño |
| Libro mensual | 1 hoja (`Labor Report`), 25 columnas, 7,9 MB | Dueño |
| Generador | `plan1.xlsx`: 19,9 MB · 4 hojas (3 ocultas) · 12 consultas · 91 versiones | Dueño |
| Carpeta UNIFY | 8 archivos · 735 versiones guardadas · permisos propios | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Medio ⚠️ C-05 | Inicial, ajustado con el dueño |

**Hallazgos principales**

1. 🟠 **Septiembre tiene el Labor Day con la etiqueta de día cambiada:** 4.739 filas con el día de la semana intercambiado, un error que corrige el dueño; las 172 filas repetidas del 8 son intencionales. [Dueño]
2. 🟠 **Los ajustes parciales se pegan al final y pueden duplicar el plan:** en septiembre, 586 filas pegadas y 39 tienda–día con las filas viejas todavía con horas. [Dueño]
3. 🟠 **Las columnas cambian de un mes a otro** y *Last Visit* lee estos archivos. [Dueño] ⚠️ C-01
4. 🟠 **El plan regenerado hoy no es el plan pegado,** por eso el Unif es el único registro de cada mes. [Dueño]
5. 🟠 **Todo depende de dos personas** y de un procedimiento no escrito; además el alcance del query no es el que se quiere. [Dueño]

**Funciona bien:** una fila por tienda y fecha (Octubre sin repetidas ni etiquetas de día mal puestas), toda fila con horas tiene ruta y costo, `$ /dia` correcto en Octubre, jerarquía de 4 RM / 14 DM / 105 FS, y el generador lee las fuentes **por nombre de columna**. [Dueño]

**Contradicciones:** 7 detectadas; 5 resueltas a favor del dueño y 2 por confirmar.

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (UNI-A01, UNI-A02, UNI-A03, UNI-A04, UNI-A05, UNI-A06, UNI-A07, UNI-A21, UNI-A25) y las preguntas Q-05 y Q-13. El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Dar a PERFORMANCE un plan mensual de rutas con horas y costo, para comparar lo real contra lo planeado en el dashboard *Last Visit*, y conservar cómo estaba el plan cada mes.

- **Problema que resuelve:** el Route Master y el Store Master solo guardan el estado de hoy; sin los Labor Unif no hay registro del plan de cada mes. [Dueño]
- **Qué logra:** una fila por tienda y día con ruta, orden, horas, costo de servir, millas, manejo y ventana horaria. [Dueño]
- **Éxito:** un plan mensual con estructura fija, sin duplicados ni etiquetas cruzadas, que PERFORMANCE lee sin sorpresas (ver «Criterios de éxito»). [Dueño · Inicial]

## Alcance

**Incluye** [Dueño]: los libros mensuales (hoja `Labor Report`), el generador `plan1.xlsx`, el proceso mensual de generar, pegar y ajustar, y el contrato con PERFORMANCE.

**No incluye** [Dueño]: el Route Master, el Store Master y el FS Route Master (dependencias). No se revisó el Histórico hasta marzo ni el dashboard *Last Visit*.

**Futuro** [Dueño]: una foto mensual de los maestros (UNI-A18), generación automática (UNI-A19) y consolidar el Histórico (UNI-A20).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Responsables (el dueño y su suplente) | Generan y ajustan el plan; se respaldan entre sí | Cada mes | Dueño |
| PERFORMANCE | Usa los archivos para el dashboard *Last Visit* (real contra plan) | 7 meses | Dueño |
| Otras personas que guardan versiones | Según el dueño, solo visualizan o filtran; falta bloquearles la edición | 4 personas | Dueño |
| Visit FS y Costco Report ❓ | El inventario los lista como lectores; el dueño no los menciona (Q-13) | — | Inicial |

**Acceso**

- La carpeta UNIFY está en SharePoint › Sales Administration – Horas labor, con permisos propios; el generador está en otro sitio (Costo de Servir – Desviaciones › Herramienta Plan). [Dueño]
- Exige cuenta de la empresa y permiso. [Inicial]
- Para generar el plan, Excel necesita credenciales de SharePoint. [Dueño]
- ❓ Falta la lista de personas con acceso a la carpeta y su permiso, y bloquear la edición a quienes solo consultan (Q-14). [Inicial · Dueño]

## Dueño funcional

**Jeronimo Sanchez**, junto con su suplente: ambos generan y ajustan el plan y se respaldan entre sí. [Dueño] ⚠️ C-03

- Cada mes cambia las fechas, actualiza el generador, crea el libro del mes y pega el plan.
- Completa la tarifa por hora y hace los ajustes del mes.
- Corrige el error del `Weekday` de septiembre.
- Aprobó su análisis el 2026-10-21 (v1.2).

## Administrador técnico

**Jeronimo Sanchez**, administra la carpeta y el generador. [Inicial]

- Administra los libros en SharePoint y el código de Power Query de `plan1.xlsx`. [Dueño]
- ❓ Quién aprueba los accesos nuevos a la carpeta (Q-14).

## Suplente

**Jennifer Guarin.** Se respalda con el dueño: ambos generan y ajustan el plan. Falta verificar los accesos de ambos a los 3 libros de origen, a `plan1.xlsx` y a las tarifas. [Dueño]

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| Route Master, Store Master y FS Route Master | Poder leerlos desde el generador | ⬜ Por verificar (UNI-A01) |
| `plan1.xlsx` | Actualizarlo y copiar la hoja del plan | ⬜ Por verificar (UNI-A01) |
| Archivo de tarifas del mes | Leerlo para completar la tarifa | ⬜ Por verificar (UNI-A01) |
| Carpeta UNIFY | Crear y editar el libro del mes | ⬜ Por verificar (UNI-A01) |
| Procedimiento mensual y de ajustes | Seguirlo sin ayuda | ⬜ Pendiente (UNI-A03) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| DSD Route Master (`RouteMaster`) | Ruta, orden, duración, millas y manejo de cada tienda | Equipo del Route Master | Dueño |
| DSD Store Master (`StoreMaster`) | Tiendas activas y jerarquía (declara el tipo de unas 60 columnas por nombre) | Dueño | Dueño |
| DSD FS Route Master (`CostFS`) | Costo diario del FS (`C2S FS`) | Dueño | Dueño |
| `Rate para labor <mes>` | Tarifa por hora; la crean otra persona del equipo o la suplente, y se aplica con un cruce por distrito o estado | Dueño y suplente | Dueño |
| Ajustes a mano | Cierres de tiendas, rutas partidas y feriados durante el mes | Dueño y suplente | Dueño |

**Cómo se produce** [Dueño]

1. En `plan1.xlsx` se cambian `Start Date` y `End Date` (están dentro del código de Power Query).
2. Al actualizar, el generador lee en vivo los tres libros de origen y cruza cada tienda activa con cada fecha y con la ruta que le toca ese día de la semana.
3. Se copia la hoja `Plan STime (Unify)` y se pega en el libro nuevo del mes, en la carpeta UNIFY.
4. Se completan a mano la tarifa por hora y el costo diario, que el generador deja vacíos a propósito.
5. Durante el mes los cambios se hacen a mano en el libro del mes; si son muchos, se regenera en `plan1` y se pegan solo las filas editadas desde el día del cambio.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | Excel con Power Query y credenciales de SharePoint · SharePoint (carpeta UNIFY y Herramienta Plan) |
| Archivos | Los 3 libros de origen · el archivo de tarifas del mes · `plan1.xlsx` |
| Personas | El dueño y su suplente |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| PERFORMANCE | Lee los archivos para *Last Visit*; depende del nombre de la hoja, de los encabezados y de algunas columnas | PERFORMANCE |
| Visit FS y Costco Report ❓ | El inventario los lista como lectores (Q-13) | PERFORMANCE |

## Procesos operativos

[Dueño] Ciclo **mensual**: un libro por mes y ajustes durante el mes. Un mes se sigue editando semanas después de terminar (abril tiene versiones hasta el 14 de agosto). ⚠️ C-02

1. **Inicio de mes:** cambiar `Start Date` y `End Date`, actualizar `plan1.xlsx`, crear el libro del mes desde la plantilla y pegar la hoja `Plan STime (Unify)` (sin cambiar encabezados ni columnas).
2. **Tarifa:** completar `Pay Rate/ Hour` con el archivo del mes y verificar que `$ /dia` sea fórmula en todas las filas.
3. **Validar:** tiendas activas con fila, sin filas repetidas, `Weekday` = día de la fecha, `C2S FS` presente, sin filtros ni filas vacías.
4. **Ajustes:** registrar fecha, filas, motivo y autor; tienda cerrada de una sola manera; al regenerar, **anular las filas viejas antes de pegar las nuevas**.
5. **Feriados:** mover el plan cambiando la fecha, nunca la etiqueta del día; revisar que no queden filas dobles.
6. **Avisar:** a PERFORMANCE antes de cambiar columnas, hoja o encabezados, y de cada ajuste importante.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- El Unif del mes es el único registro del plan de ese mes: no se regenera un mes ya pegado.
- La visita del lunes movida y la del martes se registran las dos (las filas dobles del 8 son intencionales).
- Michaels, Walgreens y CVS quedan fuera a propósito: no tienen ruta de ejecución.
- Los feriados mueven el plan cambiando la fecha, nunca la etiqueta del día.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Fila del plan** | `Store` + `fecha` + `ROUTE` + `ORDER`. Un día sin visita = 0 horas y sin ruta (42 % de las filas). Costco puede tener 2 a 4 paradas el mismo día |
| **Horas Regulares /dia** | Horas de la visita = `Duration` del Route Master ÷ 60 |
| **Pay Rate / Hour y $ /dia** | Tarifa por hora (se completa a mano) y costo del día = horas × tarifa |
| **C2S / C2S FS** | Costo de servir de la parada (Route Master) y costo diario promedio del FS (FS Route Master) |
| **Window time** | `7am-12pm` si la parada empieza antes de las 12:00, `12pm-7pm` si no |
| **Tienda activa (para el plan)** | `Active` distinto de `N` y cliente Costco, ElSuper, Fiesta, Sprouts o Walmart (incluye `P`) ⚠️ |
| **Ajuste a mano / regeneración parcial** | Cambio directo en el libro del mes; o regenerar en `plan1` y pegar solo las filas editadas desde el día del cambio |
| **Histórico** | `Labor Unif Historico hasta Marzo 2026` (63 MB); desde Abril, un archivo por mes |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | El plan MUST tener una fila por tienda activa y por fecha, sin repetidas ni etiquetas de día mal puestas | Must Have | ⚠️ ✅ en octubre; septiembre con 4.739 filas de etiqueta cruzada (UNI-A05) | Dueño |
| FR-02 | Toda fila con horas MUST tener ruta y costo | Must Have | ✅ En octubre | Dueño |
| FR-03 | El alcance MUST ser Walmart, Sprouts y Costco con `Active = Y` | Must Have | ❌ El query usa `Active <> "N"` y 5 clientes (UNI-A14) | Dueño |
| FR-04 | La tarifa por hora MUST salir de un paso documentado | Must Have | ❌ Sin procedimiento (UNI-A08) | Dueño |
| FR-05 | La hoja, el orden y los encabezados MUST mantenerse entre meses | Must Have | ❌ Las columnas cambian de un mes a otro (UNI-A07) ⚠️ C-01 | Dueño · Inicial |
| FR-06 | Los ajustes MUST registrarse y las filas viejas anularse antes de pegar las nuevas | Must Have | ❌ 586 filas pegadas al final en septiembre (UNI-A09) | Dueño |
| FR-07 | La tienda cerrada MUST registrarse de una sola manera | Must Have | ❌ 543 tienda–día borrados y 3 tiendas con 0 horas (UNI-A05) | Dueño |
| FR-08 | El generador MUST tolerar que el Store Master cambie los nombres de columnas | Should Have | ❌ Declara el tipo de unas 60 por nombre (UNI-A12) | Dueño |
| FR-09 | PERFORMANCE MUST ser avisado antes de cambiar la hoja, el orden o los encabezados | Must Have | ❌ Sin contrato (UNI-A15) | Dueño |
| FR-10 | Los libros mensuales MUST abrirse sin filtros ni filas vacías | Should Have | ❌ Filtros en 5 de 7; ≈ 140.000 filas vacías (UNI-A06, UNI-A10) | Dueño |
| FR-11 | La suplente MUST poder generar y ajustar el plan | Must Have | ⚠️ Accesos por verificar (UNI-A01) | Dueño · Inicial |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Filas con la etiqueta del día cruzada en septiembre | 4.739 | 0 | Dueño |
| SC-02 | Archivos con filtros activos | 5 de 7 | 0 | Dueño |
| SC-03 | Filas de octubre con el costo diario del FS vacío | 1.674 | 0 | Dueño |
| SC-04 | Meses con la misma estructura de columnas | No (cambian entre meses) | Todos, con plantilla | Dueño |
| SC-05 | Personas que editan los libros | Varias guardan versiones | Solo el dueño y su suplente | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Tarifas por hora y costo por tienda y día; permisos propios; otras personas guardan versiones y falta bloquear la edición | Inicial · Dueño |
| Estabilidad | Alto | Todo depende de dos personas y de un procedimiento no escrito; el plan regenerado no coincide con el pegado; los ajustes se pegan sin registro ⚠️ C-05 | Inicial · Dueño |
| Escalabilidad | Medio | ≈ 77.000 filas por mes en un libro por mes; el histórico crece y hay ≈ 140.000 filas vacías con formato | Inicial · Dueño |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🟠 Alta | **Septiembre tiene el Labor Day con la etiqueta de día cambiada.** El plan del lunes 7 se movió al martes 8: **4.739 filas con el día de la semana intercambiado** (el 7 dice `Tuesday`, el 8 dice `Monday`) es un **error que corrige el dueño**. Las **172 tienda–ruta–parada repetidas el 8** (171 Costco, 1 Walmart; 459,8 h) son **intencionales**: la visita del lunes movida más la del martes. | Dueño |
| R2 | 🟠 Alta | **Los ajustes parciales se pegan al final y pueden duplicar el plan.** Septiembre: **586 filas pegadas al final** (52 tiendas, del 5 al 30); en **39 tienda–día** las filas viejas siguen con horas (43,3 h). No hay registro de los cambios. | Dueño |
| R3 | 🟠 Alta | **Las columnas cambian de un mes a otro.** Millas y tiempo de manejo existen desde Junio; `C2S FS` falta en Abril y Agosto y en el 99 % de Septiembre; la ventana horaria existe desde Agosto. *Last Visit* lee estos archivos. | Dueño |
| R4 | 🟠 Alta | **El plan regenerado hoy no es el plan pegado.** `plan1` (21-oct) trae 1.754 filas que el Unif de Octubre no tiene y viceversa 1.196, y el costo de servir es distinto en el 7,3 % de las filas que coinciden. Por eso no se regenera el mes, y por eso el Unif es el único registro del plan. No se puede separar ajuste manual de cambio de maestros. | Dueño |
| R5 | 🟠 Alta | **La tarifa por hora se llena en un paso aparte sin procedimiento.** Sale de `Rate para labor <mes>` (la crean otra persona del equipo o Jennifer Guarin; el de Octubre es del 2026-10-02) y se aplica con un cruce por distrito o estado. La descripción inicial no lo incluía. | Dueño |
| R6 | 🟠 Alta | **Las tiendas cerradas se registran de dos maneras.** En Octubre **32 tiendas tienen menos de 31 días** (543 tienda–día borrados) y 3 tiendas dejaron 29 filas con ruta y **0 horas**. Una tienda sin fila no es lo mismo que una con 0 horas. | Dueño |
| R7 | 🟠 Alta | **El generador se rompe si el Store Master renombra una columna** (declara el tipo de ~60 por nombre; agregar no rompe). | Dueño |
| R8 | 🟠 Alta | **El alcance del query no es el que se quiere.** Hoy usa `Active <> "N"` y clientes Costco, ElSuper, Fiesta, Sprouts, Walmart. **Decidido:** solo Walmart, Sprouts y Costco con `Active = Y`; Michaels, Walgreens y CVS quedan fuera a propósito (no tienen ruta de ejecución). Falta cambiar el query. | Dueño |
| R9 | 🟠 Alta | **Costo diario del FS vacío en 1.674 filas de Octubre** (957 con horas). | Dueño |
| R10 | 🟡 Media | **Nombres cruzados en `plan1.xlsx`:** la hoja visible `Plan STime (Unify)` la alimenta la consulta `Plan STime (test)`, y hay 3 hojas ocultas más. | Dueño |
| R11 | 🟡 Media | **Filtros dejados activos** en 5 de 7 archivos (Octubre muestra 31 de 77.188 filas) y **~140.000 filas vacías con formato** en Abril–Agosto. | Dueño |
| R12 | 🟡 Media | **`$ /dia` ≠ horas × tarifa** en Abril (2.085 filas), Mayo (3.377), Julio (2.446) y Junio (15); en Agosto, Septiembre y Octubre, 0. | Dueño |
| R13 | 🟠 Alta | **Todo depende de dos personas y de un procedimiento no escrito.** Además guardan versiones PERFORMANCE, otra persona y otra persona; según el dueño solo visualizan o filtran, y falta bloquearles la edición. | Dueño |
| R14 | 🟠 Alta | La carpeta concentra el historial laboral de todos los meses y su lista de permisos no está revisada (Q-14) | Inicial |
| R15 | 🟡 Media | Si Visit FS y Costco Report leen estos archivos, un cambio de columnas los rompe sin aviso (Q-13) | Inicial |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Corregir septiembre, cambiar el query al alcance definido, quitar los filtros y escribir el procedimiento mensual | Plan correcto y repetible | UNI-A03, UNI-A05, UNI-A06, UNI-A14 | Dueño |
| Corto plazo | Plantilla con estructura fija, tarifa documentada, registro de ajustes y contrato con PERFORMANCE | Menos sorpresas para *Last Visit* | UNI-A07, UNI-A08, UNI-A09, UNI-A15 | Dueño |
| Mediano plazo | Ordenar `plan1.xlsx`, hacer tolerante la consulta del Store Master y limpiar abril a agosto | Generador más estable | UNI-A10, UNI-A11, UNI-A12 | Dueño |
| Largo plazo | Foto mensual de los maestros, generación automática y Histórico consolidado; mover el plan a SQL | Plan reproducible y sin archivos mensuales | UNI-A18, UNI-A19, UNI-A20 | Dueño · Inicial |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| UNI-A01 | Accesos y lista de editores | P0 | Dueño | Dueño | T-001 |
| UNI-A02 | Publicar documento y diccionario | P0 | Dueño | Dueño | T-002 |
| UNI-A03 | Procedimiento mensual y de ajustes | P0 | Dueño | Dueño | T-003 |
| UNI-A04 | Hoja `Control` | P0 | Dueño | Dueño | T-004 |
| UNI-A05 | Corregir Septiembre y revisar cierres | P0 | Dueño | Dueño | T-005 |
| UNI-A06 | Quitar filtros | P0 | Dueño | Dueño | T-006 |
| UNI-A07 | Plantilla con estructura fija | P0 | Dueño | Dueño | T-007 |
| UNI-A08 | Tarifa por hora documentada/automatizada | P1 | Dueño | Dueño | T-008 |
| UNI-A09 | Registro de ajustes y regla de anular antes de pegar | P1 | Dueño | Dueño | T-009 |
| UNI-A10 | Limpiar Abril–Agosto | P1 | Dueño | Dueño | T-010 |
| UNI-A11 | Ordenar `plan1.xlsx` | P1 | Dueño | Dueño | T-011 |
| UNI-A12 | Consulta del Store Master tolerante y fechas en una celda | P1 | Dueño | Dueño | T-012 |
| UNI-A13 | Diccionario | P1 | Dueño | Dueño | T-013 |
| UNI-A14 | Alcance escrito | P1 | Dueño | Dueño | T-014 |
| UNI-A15 | Contrato con *Last Visit* | P1 | Dueño | Dueño | T-015 |
| UNI-A16 | Revisar editores | P1 | Dueño | Dueño | T-016 |
| UNI-A17 | Cierre de mes | P1 | Dueño | Dueño | T-017 |
| UNI-A18 | Foto mensual de los maestros | P2 | Dueño | Dueño | T-018 |
| UNI-A19 | Generación automática | P2 | Dueño | Dueño | T-019 |
| UNI-A20 | Consolidar el Histórico | P2 | Dueño | Dueño | T-020 |
| UNI-A21 | Cambiar el query del generador a Walmart, Sprouts y Costco con `Active = Y` | P0 | Dueño | Dueño | T-014 |
| UNI-A22 | Confirmar con PERFORMANCE si Visit FS y Costco Report leen estos archivos y corregir el inventario | P1 | Dueño y PERFORMANCE | Inicial | C-04 |
| UNI-A23 | Hacer la revisión técnica con IT: tarifas por hora y costo por tienda y día | P1 | IT | Inicial | — |
| UNI-A24 | Guardar esta spec, las consultas de `plan1.xlsx` y la plantilla del libro mensual en un repositorio privado de GitHub de Falcon | P1 | PM | Inicial (instructivo de GHT) | — |
| UNI-A25 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-06 | cierres de tienda (filas borradas o con 0 horas) | Dueño (se resuelve con su tarea) | Dueño |
| Q-07 | `C2S FS` faltante | Dueño (se resuelve con su tarea) | Dueño |
| Q-08 | valores de `Type` | Dueño (se resuelve con su tarea) | Dueño |
| Q-09 | filtros y filas vacías | Dueño (se resuelve con su tarea) | Dueño |
| Q-10 | hojas y consultas sin uso | Dueño (se resuelve con su tarea) | Dueño |
| Q-11 | quién edita los Unif (✅ solo visualizan o filtran) | Dueño (se resuelve con su tarea) | Dueño |
| Q-12 | cierre de mes e histórico | Dueño (se resuelve con su tarea) | Dueño |
| Q-13 | ¿Visit FS y Costco Report leen estos archivos, o solo Last Visit? | Dueño y PERFORMANCE | Inicial |
| Q-14 | ¿Quiénes tienen acceso a la carpeta UNIFY y quién aprueba los accesos nuevos? | Dueño e IT | Inicial |

## Información pendiente por confirmar

**Contradicciones entre el análisis inicial y la validación del dueño**

| # | Tema | Qué dice cada uno | Versión recomendada | Estado |
| --- | --- | --- | --- | --- |
| C-01 | Estructura entre meses | Inicial: un archivo por mes con la misma estructura. Dueño: las columnas cambian (millas y manejo desde junio; `C2S FS` falta en abril, agosto y casi todo septiembre; ventana horaria desde agosto) | Lo del dueño; plantilla con estructura fija (UNI-A07) | ✅ Resuelta a favor del dueño |
| C-02 | Frecuencia | Inicial: según la necesidad. Dueño: ciclo mensual, con ajustes durante el mes y ediciones semanas después | Mensual, con ajustes | ✅ Resuelta a favor del dueño |
| C-03 | Quién la mantiene | Inicial (inventario): creada por la suplente y administrada por el dueño. Dueño: ambos la generan y se respaldan entre sí | Los dos; dueño funcional: Jeronimo Sanchez, según el Excel del equipo | ✅ Resuelta a favor del dueño |
| C-04 | Quién la lee | Inicial: Last Visit, Visit FS y Costco Report. Dueño: PERFORMANCE, para Last Visit | Lo del dueño; confirmar los otros dos (Q-13) | ❓ Por confirmar |
| C-05 | Nivel de riesgo | Inicial: estabilidad «Medio». Dueño: el plan regenerado no coincide con el pegado, los ajustes se pegan sin registro y todo depende de dos personas | Estabilidad «Alto» | ❓ Por confirmar |
| C-06 | Qué es | Inicial: carpeta con un archivo por mes. Dueño: es un plan de rutas con costo, y «Labor» sugiere horas de mano de obra | Mantener el nombre del inventario y explicarlo en la descripción | ✅ Resuelta a favor del dueño |
| C-07 | Tamaño | Inicial: ≈ 74.206 filas por mes (septiembre). Dueño: 77.188 filas (octubre) | Cada mes cambia | ✅ Resuelta a favor del dueño |

**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, consultas, calidad de datos por mes y backlog) todavía no están integrados.
- El Histórico hasta marzo y el dashboard *Last Visit* no se han revisado.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/plan-de-visitas-unify/spec.md`. [Inicial]
- Incluir el código de las consultas de `plan1.xlsx` y la plantilla del libro mensual, sin datos de tiendas, tarifas ni personas. [Dueño · Inicial]
- Mantener el diccionario de las 25 columnas y su historial de cambios entre meses. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Inicial]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Inicial]

## Recomendaciones para migración a SQL

1. Una tabla del plan con clave `Store + fecha + ROUTE + ORDER` y una columna de mes, en lugar de un libro por mes. [Dueño · Inicial]
2. Guardar una foto mensual de los maestros (UNI-A18), porque hoy el Unif es el único registro de cada mes. [Dueño]
3. Generar el plan con un proceso automático (UNI-A19) y cargar el Histórico una sola vez (UNI-A20). [Dueño]
4. Guardar la tarifa por hora en una tabla por mes y aplicarla al cargar. [Dueño · Inicial]
5. Exponer una vista con el nombre de la hoja y los encabezados que hoy lee PERFORMANCE. [Inicial]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 3 | Dos personas que se respaldan; accesos por verificar |
| Operación documentada | 2 | Lista de verificación propuesta; el procedimiento no estaba escrito |
| Control de acceso | 2 | Permisos propios; varias personas guardan versiones |
| Contrato de datos | 1 | Las columnas cambian entre meses; sin diccionario ni contrato con PERFORMANCE |
| Calidad y validación | 2 | Octubre correcto; septiembre con errores; filas vacías y filtros |
| Automatización e integración | 2 | Generador con Power Query, pero el pegado y los ajustes son manuales |
| Trazabilidad de cambios | 1 | Los ajustes no se registran |
| Entornos y pruebas | 2 | El generador está separado de los libros mensuales |

**Nivel global: 2,0 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis completo del dueño y el análisis independiente.

---

# Spec · Stores Contact List

> **English version pending.** This document is currently available in Spanish only.

> Versión consolidada, en revisión. Es el único documento de especificación de esta herramienta: el mismo que se ve en el botón «Skill SDD» del inventario y que se descarga como Markdown. Una vez aprobada se guarda en el repositorio privado correspondiente. **Uso interno.**

| Campo | Valor |
| --- | --- |
| ID | m23 (inventario MIC) |
| Tipo | Base de datos: libro de Excel (maestro de contactos de las tiendas activas) |
| Versión | 1.0 |
| Estado | En revisión: faltan el análisis completo del dueño (anexos), el análisis inicial del equipo MIC y el análisis independiente |
| Fecha | 2026-10-23 |

**Origen de la información:** **[Dueño]** validada por el dueño de la herramienta · **[Independiente]** análisis independiente · ❓ por confirmar. Esta herramienta todavía no tiene análisis inicial del equipo MIC, por eso no hay contradicciones que resolver.

## Resumen Ejecutivo

Es el **maestro de contactos** de las tiendas activas. Cada fila de la hoja `Contact List` es una tienda con su dirección y, para su RM, su DM y su FS, el nombre, el correo y el teléfono. La hoja `People` guarda el correo y el teléfono de cada persona. Es pequeño (2.557 filas × 11 columnas y 122 personas), pero el **DSD Route Master lo lee** para tener el contacto de cada parada. [Dueño]

| Dato | Valor | Origen |
| --- | --- | --- |
| Tamaño | 2.557 tiendas × 11 columnas · 122 personas × 3 columnas | Dueño |
| Clientes | Walmart 1.785 · Sprouts 512 · Michaels 169 · Costco 91 | Dueño |
| Jerarquía | 4 RMs · 14 DMs · 105 FS | Dueño |
| Cobertura | 2.557 de 2.617 tiendas activas (97,7 %); faltan 60 en la versión 286.0 y quedan 4 Michaels en la 287.0 | Dueño |
| Concordancia con el Store Master | RM, DM y FS iguales en las 2.557 filas (100 %) | Dueño |
| Libro | 3 hojas (1 oculta) · 25.569 fórmulas · 2 vínculos externos · 27 hipervínculos | Dueño |
| Actividad | 285 versiones: dueño 206 · suplente 7 · otras 7 personas 72 | Dueño |
| Nivel de riesgo | Vulnerabilidad Medio · Estabilidad Alto · Escalabilidad Bajo | Dueño (nivel propuesto) |

**Hallazgos principales**

1. 🟠 **Alcance y tiendas que faltan:** el dueño definió solo Walmart, Sprouts, Michaels y Costco con `Active = Y`; en la versión 287.0 agregó las 28 Walmart y quedan 4 Michaels por agregar. [Dueño]
2. 🟠 **El contacto faltante se ve como `0`,** no como un error: las 10 fórmulas terminan en `XLOOKUP(…,0)` y el Route Master repite el patrón (479 de sus 3.664 filas con algún contacto en 0 en la versión 286.0). [Dueño]
3. 🟠 **Lectura por letra de columna en ambos sentidos:** si alguien inserta o mueve una columna, nada da error y se entregan otros datos. [Dueño]
4. 🟠 **Más personas guardan versiones** de las que se describieron; el dueño bloqueará las hojas para que los demás solo visualicen. [Dueño]
5. 🟠 **Todo depende de una persona** y de un procedimiento no escrito (72 % de las versiones). [Dueño]

**Funciona bien:** **Jerarquía:** RM, DM y FS coinciden con el Store Master vivo en las 2.557 filas; cada DM tiene un solo RM y cada FS un solo DM. **Tiendas:** ninguna repetida ni inactiva; Costco cubierto 91 de 91. **`People` limpia:** las 122 personas tienen puesto activo (nadie sobra), sin nombres, correos ni teléfonos repetidos, y todos los correos son del dominio de la empresa (salvo el `N/A`). **Direcciones:** las 2.557 tienen valor; 2.517 son idénticas a las del Store Master y 40 solo difieren en el cero inicial. [Dueño]

**Contradicciones:** ninguna (no hay análisis inicial con el que contrastar).

**Hallazgos independientes:** ninguno. Todavía no se ha recibido un análisis independiente.

**Recomendación:** aprobar esta versión como la Spec oficial, condicionada a cerrar las acciones P0 (SCL-A01, SCL-A02, SCL-A03, SCL-A04, SCL-A05, SCL-A06, SCL-A23). El resto se atiende desde el backlog.

## Objetivo de la herramienta

[Dueño] Tener en un solo libro el contacto (nombre, correo y teléfono) del RM, DM y FS de cada tienda activa, y que el DSD Route Master lo lea para mostrar el contacto de cada parada.

- **Problema que resuelve:** el Route Master y las personas de Execution Team y de HR (talento) necesitan saber a quién llamar en cada tienda. [Dueño]
- **Qué logra:** una fila por tienda con dirección y contactos, armada con fórmulas desde el Store Master, el Route Master y la hoja `People`. [Dueño]
- **Éxito:** todas las tiendas activas tienen fila y contactos completos, y ningún cambio de columnas rompe al Route Master (ver «Criterios de éxito»). [Dueño]

## Alcance

**Incluye** [Dueño]: el libro, el proceso que lo mantiene (alta de tiendas y mantenimiento de `People`) y los archivos que lo leen.

**No incluye** [Dueño]: el Store Master y el Route Master, que ya tienen su análisis y aquí son dependencias; Walgreens y CVS quedan fuera.

**Futuro** [Dueño]: una fuente corporativa de contactos (SCL-A17), un aviso automático de cambios de puesto (SCL-A18) y protección de columnas (SCL-A19).

## Usuarios

| Usuario | Cómo la usa | Volumen | Origen |
| --- | --- | --- | --- |
| Responsable (el dueño) | Es el único editor, según su descripción; mantiene `Contact List` y `People` | 206 de 285 versiones | Dueño |
| Suplente | Cubre al responsable | 7 versiones | Dueño |
| DSD Route Master (y sus dos copias) | Lee las columnas D, E, G, H, J y K de `Contact List`, por letra | — | Dueño |
| Execution Team y HR (talento) | Consultan los contactos | — | Dueño |
| Otras personas con versiones | Según el dueño, solo visualizaron o filtraron | 72 versiones | Dueño |

**Acceso**

- Está en SharePoint › Sales Administration › Consulta Route Master › Varios, con permisos propios; su lista no se pudo leer. [Dueño]
- El dueño bloqueará las hojas para que los demás solo visualicen. [Dueño]
- ❓ Falta la lista de editores y quién aprueba los accesos nuevos (SCL-A01). [Dueño]

## Dueño funcional

**Jeronimo Sanchez.** [Dueño]

- Es el único editor según su descripción: agrega las tiendas activas y mantiene la hoja `People`.
- Define el alcance de la lista (4 clientes, solo `Y`).
- Aprobó su análisis el 2026-10-21 (v1.3).

## Administrador técnico

**Jeronimo Sanchez.** [Dueño]

- Administra el libro en SharePoint y sus permisos propios.
- ❓ Quién aprueba los accesos nuevos (SCL-A01).

## Suplente

**Jennifer Guarin.** [Dueño] Tiene 7 versiones entre junio y agosto; falta verificar sus accesos al Store Master y al Route Master y escribir el procedimiento.

| Componente | Acceso que necesita | Estado |
| --- | --- | --- |
| `Stores Contact List.xlsx` | Editar el libro | ⬜ Por verificar (SCL-A01) |
| Store Master y Route Master | Leerlos desde las fórmulas | ⬜ Por verificar (SCL-A01) |
| Procedimiento escrito | Seguirlo sin ayuda | ⬜ Pendiente (SCL-A03) |

## Fuentes de datos

| Fuente | Qué aporta | Quién | Origen |
| --- | --- | --- | --- |
| DSD Store Master | Nombre del RM, DM y FS de cada tienda | Dueño | Dueño |
| Hoja `StoreMaster DSD` del DSD Route Master | Dirección de cada tienda | Dueño | Dueño |
| Hoja `People` | Correo y teléfono de cada persona | El dueño, a mano, desde Onboarding, los DM y RM y avisos por email | Dueño |
| Onboarding, DM y RM, IT | Teléfonos, avisos de cambios y creación de correos | Cada equipo | Dueño |

**Cómo se alimenta** [Dueño]

1. Solo `Store` se escribe a mano: cuando se activa una tienda en el Store Master, se copia al final de la tabla.
2. Las otras 10 columnas son `XLOOKUP`: el nombre sale del Store Master, la dirección del Route Master y el correo y teléfono de `People`.
3. `People` se mantiene a mano: se borra a quien se va, se agrega a quien llega y se actualizan correos y teléfonos según los avisos. Si IT aún no creó el correo, queda `N/A`.

## Dependencias

**Qué necesita para funcionar** [Dueño]

| Tipo | Elementos |
| --- | --- |
| Sistemas | SharePoint · Excel |
| Archivos | Store Master · DSD Route Master · hoja `People` |
| Personas | El dueño y su suplente · Onboarding y los avisos de DM y RM · IT |

**Quién depende de ella**

| Archivo o equipo | Qué toma | Dueño o responsable |
| --- | --- | --- |
| DSD Route Master y sus dos copias | Leen `Contact List` columnas D, E, G, H, J y K por su letra | Dueño del DSD Route Master |
| Execution Team y HR (talento) | Consultan los contactos | — |

## Procesos operativos

[Dueño] Cada vez que se activa una tienda, llega o se va una persona, o cambia un correo o teléfono.

1. **Tienda nueva:** confirmar en el Store Master que está activa y que tiene RM, DM y FS; copiar su `Store` al final de `Contact List`; confirmar que sus 10 columnas quedaron llenas.
2. **Persona nueva:** agregar a `People` con el nombre **exactamente como en el Store Master** ("Apellido, Nombre", sin espacios dobles), el teléfono en un solo formato y el correo; si IT aún no lo crea, escribir `N/A` y anotar la fecha para cerrarlo.
3. **Persona que se va:** borrarla de `People` después de que el Store Master ya no la use.
4. **Cambio de correo o teléfono:** actualizar `People` y anotar quién lo pidió y cuándo.
5. **Revisar:** sin `0`, sin celdas vacías en las 10 columnas y sin `N/A` pendientes.
6. **Avisar:** al dueño del Route Master antes de cambiar el orden o la letra de cualquier columna.


## Reglas de negocio

**Principios que gobiernan la herramienta** [Dueño]

- Solo entran tiendas de Walmart, Sprouts, Michaels y Costco con `Active = Y`; las `P` son tiendas por abrir y no entran todavía.
- La dirección sale del Route Master a propósito, porque su consulta la concatena y organiza.
- Los 40 códigos postales sin cero inicial se dejan así.
- Solo el dueño edita; los demás visualizan o filtran.

**Definiciones** [Dueño]

| Término | Definición |
| --- | --- |
| **Tienda activa** | Tienda del Store Master con `Active` = `Y` de Walmart, Sprouts, Michaels o Costco. `P` = tienda por abrir: no entra todavía (3 Sprouts en `P` se dejaron porque se activan la próxima semana) |
| **Store** | Identificador de la tienda en el Store Master (`119Sprouts`, `3501Walmart`). Única columna manual y llave de las búsquedas |
| **RM, DM, FS** | Regional Manager (4), District Manager (14) y Field Supervisor (105) de cada tienda, según el Store Master |
| **People** | Hoja con nombre, correo y teléfono de cada persona en un puesto de RM, DM o FS (122) |
| **`N/A` en el correo** | La persona ya está en el Store Master y se sabe su teléfono, pero IT aún no creó su correo (hoy 1 persona, 30 tiendas) |
| **`0` en un contacto** | Lo que devuelve la fórmula si no encuentra a la persona o la tienda; no es un dato |
| **Dirección** | `Store Address, City, State, Zip`, armada en la hoja `StoreMaster DSD` del Route Master |

## Requisitos funcionales consolidados

| ID | Requisito | Prioridad | Estado | Origen |
| --- | --- | --- | --- | --- |
| FR-01 | La lista MUST tener una fila por tienda de Walmart, Sprouts, Michaels y Costco con `Active = Y` | Must Have | ⚠️ Faltan 4 Michaels (SCL-A04) | Dueño |
| FR-02 | El RM, DM y FS de cada fila MUST coincidir con el Store Master | Must Have | ✅ 2.557 de 2.557 | Dueño |
| FR-03 | El contacto faltante MUST mostrarse con un texto claro, no con `0` | Must Have | ❌ (SCL-A07) | Dueño |
| FR-04 | Las búsquedas MUST hacerse por nombre de columna y debe existir la lista de columnas que lee el Route Master | Must Have | ❌ Lectura por letra en ambos sentidos (SCL-A08) | Dueño |
| FR-05 | `People` MUST tener nombres como en el Store Master y un formato único de teléfono | Should Have | ❌ 5 formatos; 36 teléfonos como texto (SCL-A10, SCL-A11) | Dueño |
| FR-06 | Solo el dueño MUST poder editar las hojas | Must Have | ⚠️ Más personas guardan versiones (SCL-A01) | Dueño |
| FR-07 | Se MUST avisar al dueño del Route Master antes de mover columnas | Must Have | ❌ (SCL-A15) | Dueño |
| FR-08 | El mantenimiento MUST seguir un procedimiento escrito y dejar registro de cambios | Should Have | ❌ (SCL-A03, SCL-A13) | Dueño |
| FR-09 | Una hoja `Control` MUST mostrar tiendas sin fila, contactos en `0` o `N/A` y personas sin puesto | Should Have | ❌ (SCL-A05) | Dueño |

**Criterios de éxito**

| ID | Criterio | Hoy | Meta | Origen |
| --- | --- | --- | --- | --- |
| SC-01 | Tiendas con `Active = Y` de los 4 clientes sin fila | 4 (Michaels) | 0 | Dueño |
| SC-02 | Filas del Route Master con algún contacto en 0 (versión 286.0) | 479 de 3.664 (30 tiendas) | 0 | Dueño |
| SC-03 | Tiendas con correo `N/A` | 30 (1 persona) | 0 al crear IT el correo | Dueño |
| SC-04 | Formatos de teléfono | 5 | 1 | Dueño |
| SC-05 | Personas que editan | Varias guardan versiones | El dueño y su suplente | Dueño |
| SC-06 | Concordancia de RM, DM y FS con el Store Master | 100 % | 100 % | Dueño |

## Riesgos

| Área | Nivel | Qué se observa | Origen |
| --- | --- | --- | --- |
| Vulnerabilidad | Medio | Nombres, correos y teléfonos de empleados; permisos propios con lista no leída; más personas guardan versiones | Dueño (nivel propuesto) |
| Estabilidad | Alto | Dos archivos se leen por letra de columna, el contacto faltante se ve como 0 y todo depende de una persona sin procedimiento | Dueño (nivel propuesto) |
| Escalabilidad | Bajo | 2.557 filas × 11 columnas y 122 personas | Dueño (nivel propuesto) |

**Hallazgos del dueño**

| # | Gravedad | Hallazgo | Origen |
| --- | --- | --- | --- |
| R1 | 🟠 Alta | **Alcance de la lista y tiendas que faltan.** El dueño definió: solo Walmart, Sprouts, Michaels y Costco, y solo `Active` = `Y` (las `P` son tiendas por abrir y no se ponen todavía). En la 286.0 faltaban 60 tiendas; con esa regla eran 32. **En la 287.0 el dueño agregó las 28 Walmart; quedan 4 Michaels en `Y`**, las 4 son `9876Michaels`, `9811Michaels`, `8387Michaels` y `8385Michaels`. Las 3 Sprouts en `P` (50, 58, 185) ya están en la lista y **se dejan** porque se activan la próxima semana. Walgreens y CVS (26) quedan fuera. | Dueño |
| R2 | 🟠 Alta | **El contacto faltante se ve como `0`, no como un error.** Las 10 fórmulas terminan en `XLOOKUP(…,0)` y el Route Master repite el patrón: con la 286.0 había **479 de sus 3.664 filas (30 tiendas)** con algún contacto en 0 (28 tiendas Walmart que no estaban en la lista, 1 que no existe y 1 por la celda vacía del hallazgo 7; ya corregidas en la 287.0), y 27 filas (24 tiendas) tienen `N/A` en el correo del FS. | Dueño |
| R3 | 🟠 Alta | **Lectura por letra de columna en ambos sentidos.** El Route Master lee `'Contact List'!D, E, G, H, J, K`; este libro lee el Store Master (`B`, `BC`, `U`, `V`) y el Route Master (`B`, `BY`). Si alguien inserta o mueve una columna, nada da error y se entregan otros datos. | Dueño |
| R4 | 🟠 Alta | **Más personas guardan versiones de las que se describieron** (el dueño dice que solo visualizaron o filtraron, y bloqueará las hojas). otra persona (41, 10 en los últimos 30 días), otra persona (18, todas desde 2026-09-29), otra persona, otra persona, otra persona y otra persona, además de Jennifer Guarin (7). El archivo tiene permisos propios y su lista no se pudo leer. | Dueño |
| R5 | 🟠 Alta | **40 códigos postales pierden el cero inicial** (`NJ, 8096` en lugar de `NJ, 08096`): el 100 % de las tiendas con código que empieza en 0. La dirección sale del Route Master a propósito (su consulta concatena y organiza la dirección completa), pero ahí el código postal se arma como número; en el Store Master está bien escrito. | Dueño |
| R6 | 🟠 Alta | **Dependencia cruzada entre dos archivos.** El Contact List lee la dirección del Route Master y el Route Master lee los contactos del Contact List. Como la dirección sale de la copia del Store Master del Route Master (2.592 tiendas), una tienda que aún no esté en esa copia saldría con dirección `0` aunque esté en la lista. | Dueño |
| R7 | 🟡 Media | **Un hipervínculo mal escrito y hipervínculos sueltos.** La celda vacía de la fila 114 (`Regional Email`) ✅ ya la corrigió el dueño (287.0); 27 hipervínculos `mailto:` puestos a mano (4 RM, 3 DM, 20 FS) conviven con 2.530 celdas sin él, y uno apunta a `falconfarm.com`. | Dueño |
| R8 | 🟡 Media | **Teléfonos en 5 formatos y 2 tipos.** En `People` 86 son números y 36 son texto; la lista entrega 6.774 sin formato, 424 con guiones, 397 con paréntesis, 56 con espacio y 20 con paréntesis pegado. | Dueño |
| R9 | 🟡 Media | **30 filas con correo `N/A`:** todas de un FS (IT aún no le crea el correo). El `N/A` se arrastra al Route Master. | Dueño |
| R10 | 🟡 Media | **Hoja oculta `Sheet1`** (2.533 filas y una tabla dinámica de 14 DMs): ninguna fórmula ni archivo revisado la lee; el dueño la usa a mano para sacar rápido los correos de los DM. No se borra; hay que documentarla. | Dueño |
| R11 | 🟡 Media | **Nombres y correos irregulares:** un nombre con espacio doble (`un FS`, igual en el Store Master) y 11 correos que no contienen nombre y apellido (apodos y apellidos compuestos); uno de ellos pertenece a otro nombre (por confirmar). | Dueño |
| R12 | 🟠 Alta | **Todo depende de una persona y de un procedimiento no escrito.** El dueño hizo el 72 % de las versiones; no hay lista de verificación ni registro de cuándo cambió cada contacto. | Dueño |

## Oportunidades de mejora

| Horizonte | Mejora | Beneficio | Acciones | Origen |
| --- | --- | --- | --- | --- |
| Inmediato | Agregar las 4 Michaels, bloquear las hojas, corregir el hipervínculo, escribir el procedimiento y crear la hoja `Control` | Lista completa y controlada | SCL-A01, SCL-A03, SCL-A04, SCL-A05, SCL-A06 | Dueño |
| Corto plazo | Cambiar el `0` por un texto claro, buscar por nombre de columna, leer la dirección del Store Master y unificar teléfonos | Menos errores silenciosos | SCL-A07, SCL-A08, SCL-A09, SCL-A10 | Dueño |
| Mediano plazo | Validaciones en `People`, diccionario, registro de cambios y revisión de `Sheet1` | Datos limpios y trazables | SCL-A11 a SCL-A16 | Dueño |
| Largo plazo | Evaluar una fuente corporativa de contactos, avisos automáticos y protección de columnas | Menos trabajo manual | SCL-A17, SCL-A18, SCL-A19 | Dueño |

## Backlog de acciones

Prioridad: P0 primero · P1 después · P2 al final. «Ref.» enlaza cada acción con la tarea del dueño (T-) o con la contradicción (C-) de la que viene.

| ID | Acción | Prioridad | Responsable | Origen | Ref. |
| --- | --- | --- | --- | --- | --- |
| SCL-A01 | Verificar accesos de Jennifer Guarin y la lista de editores | P0 | Dueño y suplente | Dueño | T-001 |
| SCL-A02 | Publicar el documento y el diccionario | P0 | Dueño | Dueño | T-002 |
| SCL-A03 | Procedimiento escrito | P0 | Dueño | Dueño | T-003 |
| SCL-A04 | Agregar las 4 Michaels en `Y` y escribir la regla (4 clientes, solo `Y`) | P0 | Dueño | Dueño | T-004 |
| SCL-A05 | Hoja `Control` | P0 | Dueño | Dueño | T-005 |
| SCL-A06 | Hipervínculo mal escrito (la fila 114 ya está corregida) | P0 | Dueño | Dueño | T-006 |
| SCL-A07 | Cambiar el `0` por un texto claro | P1 | Dueño | Dueño | T-008 |
| SCL-A08 | Búsquedas por nombre de columna y lista de columnas que lee el Route Master | P1 | Dueño | Dueño | T-009 |
| SCL-A09 | Leer la dirección del Store Master | P1 | Dueño | Dueño | T-010 |
| SCL-A10 | Formato único de teléfono | P1 | Dueño | Dueño | T-011 |
| SCL-A11 | Validaciones en `People` | P1 | Dueño | Dueño | T-012 |
| SCL-A12 | Diccionario | P1 | Dueño | Dueño | T-013 |
| SCL-A13 | Registro de cambios | P1 | Dueño | Dueño | T-014 |
| SCL-A14 | Revisar `Sheet1` | P1 | Dueño | Dueño | T-015 |
| SCL-A15 | Avisar a los dueños de los archivos que lo leen | P1 | Dueño | Dueño | T-016 |
| SCL-A16 | Revisar trimestralmente a los editores | P1 | Dueño | Dueño | T-017 |
| SCL-A17 | Evaluar una fuente corporativa de contactos | P2 | Dueño | Dueño | T-018 |
| SCL-A18 | Aviso automático de cambios de puesto | P2 | Dueño | Dueño | T-019 |
| SCL-A19 | Protección de columnas | P2 | Dueño | Dueño | T-020 |
| SCL-A20 | Hacer la revisión técnica con IT: nombres, correos y teléfonos de empleados | P1 | IT | Dueño (nivel propuesto) | — |
| SCL-A21 | Hacer el análisis inicial del equipo MIC de esta herramienta, para contrastarlo con el del dueño | P1 | Equipo MIC | — | — |
| SCL-A22 | Guardar esta spec en un repositorio privado de GitHub de Falcon | P1 | PM | Instructivo de GHT | — |
| SCL-A23 | Conseguir la firma del dueño y del administrador para aprobar la spec | P0 | Dueño y administrador | — | — |


## Preguntas abiertas

| ID | Pregunta | Responsable | Origen |
| --- | --- | --- | --- |
| Q-06 | hoja `Sheet1` (respondida) | Dueño (se resuelve con su tarea) | Dueño |
| Q-07 | hipervínculos | Dueño (se resuelve con su tarea) | Dueño |
| Q-08 | correos sin nombre y apellido | Dueño (se resuelve con su tarea) | Dueño |
| Q-09 | formato de teléfono | Dueño (se resuelve con su tarea) | Dueño |
| Q-10 | plazo del `N/A` | Dueño (se resuelve con su tarea) | Dueño |
| Q-11 | dónde se guardan los avisos de cambio | Dueño (se resuelve con su tarea) | Dueño |
| Q-12 | un RM que también figura como DM, y columnas BC/U/V frente a BM/BO/BS | Dueño (se resuelve con su tarea) | Dueño |

## Información pendiente por confirmar


**Por integrar y por medir**

- Los anexos del análisis completo del dueño (diccionario de columnas, fórmulas y vínculos, calidad de datos y backlog completo) todavía no están integrados.
- La distribución de tiendas por RM y DM está en el análisis completo del dueño.

**Análisis independiente:** pendiente de recibir. Cuando llegue, se contrastará con las contradicciones y los riesgos de esta spec.

## Recomendaciones para GitHub

- Guardar esta spec en un repositorio **privado** de la organización de Falcon, en `specs/stores-contact-list/spec.md`. [Dueño]
- Describir en el repositorio las columnas que lee el DSD Route Master (D, E, G, H, J y K), sin correos ni teléfonos de personas. [Dueño]
- Proteger la rama principal: la spec solo cambia con un pull request aprobado por el dueño (CODEOWNERS). [Dueño]
- Mantener un `CHANGELOG.md` con cada versión de la spec. [Dueño]

## Recomendaciones para migración a SQL

1. Una tabla de contactos de tienda con clave `Store` y una tabla de personas (`People`) con puesto, correo y teléfono. [Dueño]
2. Que el Route Master lea una vista con los nombres de columna actuales y no por letra (SCL-A08). [Dueño]
3. Poblar la tabla desde el Store Master en SQL (una sola fuente de tiendas, jerarquía y dirección). [Dueño]
4. Mostrar el contacto faltante como un valor nulo con una regla de calidad, no como `0` (SCL-A07). [Dueño]

## Evaluación de madurez SDD

Escala: 1 inicial · 2 documentado · 3 controlado · 4 gestionado · 5 optimizado.

| Dimensión | Nivel | Evidencia |
| --- | --- | --- |
| Especificación escrita | 3 | Spec completa; no existía descripción ni diccionario |
| Responsables | 2 | Dueño y suplente definidos; la suplente tiene pocos accesos |
| Operación documentada | 2 | Lista de verificación propuesta; procedimiento no escrito |
| Control de acceso | 2 | Permisos propios; más personas guardan versiones |
| Contrato de datos | 1 | Lectura por letra de columna; sin diccionario |
| Calidad y validación | 2 | Concordancia del 100 % con el Store Master; `0` y `N/A` sin control |
| Automatización e integración | 3 | Casi todo son fórmulas; solo `Store` y `People` son manuales |
| Trazabilidad de cambios | 1 | Sin registro de cuándo cambió cada contacto |
| Entornos y pruebas | 2 | Hay copias del Route Master que también lo leen |

**Nivel global: 2,0 de 5 (documentado, todavía no controlado).** Al cerrar las acciones P0 y P1 llega al nivel 3 (controlado).

**Versión final recomendada:** aprobar esta spec como la oficial, con las condiciones del Resumen Ejecutivo, y actualizarla al recibir el análisis inicial del equipo MIC, el análisis completo del dueño y el análisis independiente.

---

# SDD · FIT

## Summary
It asks for an account and an Admin’s approval; it updates live. Tasks to do: 7.

## 1. Project principles

**Starting point**
- Vulnerability (Medium): It asks for an account and an Admin’s approval and the session expires by itself, but free-text reports name store employees and the Admin sees full emails; the database access rules are still to be confirmed
- Stability (Medium): Its creator is also its administrator, with no backup; it depends on Vercel, Supabase, email and an AI assistant; backup to be confirmed
- Scalability (Low): About 2,551 stores and 106 historical cases: low volume today; plan limits still to be confirmed

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | Partial | It asks for email and password and an Admin’s approval; it remains to confirm that sign-up requires a company email. |
| 2 | Data in a company place | To confirm | The data lives in Supabase and the application on Vercel; it remains to confirm who owns those accounts and that they belong to the company. |
| 3 | Up-to-date information | Done | It updates live (“Live from FIT”) and the Dashboard shows the cases instantly. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record; today its creator is also its administrator. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 14 items remain to close. |

## 2. What is needed

### People's needs

- **US-001** (Partial): That only people with a company account get in — It asks for an account and an Admin’s approval; the company email remains to be confirmed.
- **US-002A** (Done): That it updates by itself and shows when — It updates live.
- **US-002B** (To confirm): That it is confirmed whether it fails and a notice is sent — It remains to confirm whether there is a notice when the database or email fails.
- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-F1** (To do): That the people who report or appear in reports have their data protected — Free texts name store employees and the Admin sees full emails: what is written, who sees it and how long it is kept still have to be defined.
- **US-F2** (To do): That cases and photos are not lost if something fails — The backup of the database and attachments, and who owns the Supabase and Vercel accounts, still have to be confirmed.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FIT-FR-1 | Account sign-up requires a company email. | To confirm |
| FIT-FR-2 | The database row-level access rules are active and reviewed. | To confirm |
| FIT-FR-3 | Only the roles that need it see the full emails of users and contacts. | To do |
| FIT-FR-4 | Free-text reports do not include employee names, and how long they are kept is defined. | To do |
| FIT-FR-5 | The database and attachments have a backup, with a defined retention date. | To do |
| FIT-FR-6 | The Vercel and Supabase accounts belong to the company and there is a second administrator. | To do |
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| FIT-SC-1 | An email that does not belong to the company cannot activate an account. | Try to sign up with a non-company email: it must be rejected. | To confirm |
| FIT-SC-2 | After a failure the information of the cases and their attachments can be recovered. | Restore the backup in a test and open a case with its attachments. | To do |
| FIT-SC-3 | New reports do not include employee names. | Review a sample of one month of reports. | To do |
| SC-003 | FIT has a registered backup within 30 days. | Its record shows the backup. | To do |
| SC-006 | The pending lines of FIT’s record drop from 14 to fewer than 5. | The pending items of its record drop to zero or almost (today 14). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| How do people get into FIT? | With email and password. Every new account stays pending until an Admin approves it and assigns a role; the session closes by itself after 10 minutes without activity. |
| What data does it keep? | Cases with free text, category, reason, status, dates and goals; photos and attachments; stores by customer with their management chain; users with their role; contacts and email rules. |
| Where is it hosted and where does it keep the data? | The application is on Vercel; the accounts, cases and rules are in Supabase, and it updates live. |
| Can the data be exported? | No export button was seen; there is only import (stores in Excel or CSV and an initial catalog). |
| What does the AI assistant do? | It helps classify the reports; its default name is “FITTI”. |

### To answer

- Verify whether sign-up requires a company email (Falcon Farms) or accepts any email.
- How many accounts are approved per role and who approves the new ones.
- Who owns the Supabase account, and which plan and region it is on.
- Backup of the database and the attachments, and how long cases are kept.
- Where the stores Excel comes from and who maintains it.
- Which AI provider the assistant uses, what data of the report it sends and whether a person validates its classification.
- Owner of the Vercel accounts and of the code repository, and the plan contracted.
- Whether the company will have its own domain; today it is a vercel.app subdomain.
- How often new versions are published and who publishes them.
- Whether the database has row-level access rules (RLS) active and reviewed.
- Who sees the photos and attachments and where they are stored.
- Retention and deletion policy for cases with personal data.
- Recovery plan if Supabase, Vercel or email fails.
- Expected volume of cases and attachments, and the limits of the Supabase and Vercel plans.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| FIT is analysed separately | With the same structure as the other tools, but outside the general analysis of the 17. | It is an application with its own database; the general analysis is limited to dashboards, forms and Excel databases. |
| Personal data first | Review first the free text of the reports and the emails the Admin sees. | It is what most exposes people. |

### Phases that apply

- Phase 1: Secure access to dashboards
- Phase 2: Reliable and visible refresh
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Free-text reports name store employees and describe situations with them. | Ask that names are not written, define how long they are kept and who sees them. |
| One person creates and administers FIT, and the Vercel and Supabase accounts may depend on that person. | Note the backup and move the accounts to the company with a second administrator. |
| Without a confirmed backup, a Supabase failure could lose cases and photos. | Confirm the backup and test a restore. |
| Sign-up may accept emails that do not belong to the company. | Require a company email and keep the Admin’s approval. |
| It is a prototype already in use: a change can affect daily work. | Test changes before publishing and note who publishes them. |

## 5. Tasks

- [ ] FIT-T1: Review FIT’s free-text reports for privacy, ask that they do not include employee names and define how long they are kept (To do · First)
  - Done when: There is a written rule about what is written in reports and for how long they are kept.
- [ ] FIT-T2: Confirm who owns the Vercel and Supabase accounts, move them to the company and register a second administrator (To do · First)
  - Done when: The accounts belong to the company and there are two administrators.
- [ ] FIT-T3: Confirm the backup of the database and attachments, and test a restore (To do · First)
  - Done when: There is a dated backup and a successful test restore.
- [ ] FIT-T4: Require a company email at sign-up and review the database access rules (To do · Next)
  - Done when: A non-company email cannot activate an account and the access rules are reviewed.
- [ ] FIT-T5: Limit who sees the full emails of users and contacts (To do · Next)
  - Done when: Only the roles that need it see the full emails.
- [ ] FIT-T6: Confirm which provider the AI assistant uses and what report data it sends (To do · Next)
  - Done when: The provider and the data sent to it are noted.
- [ ] FIT-T7: Note FIT’s backup in the record and close the pending documentation items (To do · Last)
  - Done when: The record shows the backup and its pending items drop to zero or almost.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “FIT” (FIT-T1, FIT-T2, FIT-T3, FIT-T4, FIT-T5, FIT-T6, FIT-T7) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: FIT-T1, FIT-T2, FIT-T3 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: try a non-company email at sign-up and test a backup restore | Tool owner | First two weeks |
| 4 | Note the backup in the record and close the 14 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---
