# MIC tool inventory · Full report (English)

General analysis, summary and the analysis of each of the 17 tools. Version 1.14. It contains no people names, emails, phone numbers, rates or links; it is internal information.

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
18. SDD · Incident Reporting Route
19. SDD · Walmart Audit
20. SDD · Time Correction
21. SDD · DSD Store Master
22. SDD · DSD Route Master
23. SDD · DSD FS Route Master
24. SDD · Plan de visitas (Unify)

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
- The 5 applications are outside this version.
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
- The 5 applications (Tallie, AFS Console, Staffing Request, F.I.T. and Portal).
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
| Incident Reporting Route | Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1. | 1 |
| Walmart Audit | Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1. | 1 |
| Time Correction | Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1. | 1 |
| DSD Store Master | It asks for a company account and permission; it is updated as needed. Tasks to do: 1. | 1 |
| DSD Route Master | It asks for a company account and permission; it is updated as needed. Tasks to do: 1. | 1 |
| DSD FS Route Master | It asks for a company account and permission; it is updated as needed. Tasks to do: 1. | 1 |
| Plan de visitas (Unify) | It asks for a company account and permission; it is updated as needed. Tasks to do: 1. | 1 |

---

# SDD · Sprouts Execution Report

## Summary
Its link is public (anyone with the link opens it); it is updated by hand (last: week 40). Tasks to do: 5.

## 1. Project principles

**Starting point**
- Vulnerability (Alto): Public with no sign-in; shows staff names and auditor remarks
- Stability (Medio): Refreshed manually; last: week 40
- Scalability (Bajo): 2 MB model; grows every week

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
- Vulnerability (Alto): Public with no sign-in; shows staff names and auditor remarks
- Stability (Medio): Refreshed manually (last: October 5)
- Scalability (Bajo): 2 MB model

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
- Vulnerability (Alto): Public with no sign-in; shows customer sales and inventory; 1 hidden page
- Stability (Medio): Scheduled refresh; last: October 12, 2026; a page showing zeros
- Scalability (Medio): 44 MB model with 16 tables and about 148 slicers

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
- Vulnerability (Alto): Public with no sign-in; shows names and free-text comments; 3 hidden pages
- Stability (Bajo): Scheduled refresh; last: October 12, 2026
- Scalability (Bajo): 5 MB model

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
- Vulnerability (Bajo): It is entered only through the Portal; only people with access to the Portal can get in (according to the inventory owner)
- Stability (Bajo): Scheduled refresh; last: October 7, 2026 (according to the active report in the Portal)
- Scalability (Bajo): 12 MB model (according to the previous public link)

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
- Vulnerability (Alto): Public with no sign-in; shows staff names, hours and turnover; 5 hidden pages
- Stability (Bajo): Refresh scheduled several times a day; 5 hidden pages and duplicates
- Scalability (Medio): 331 MB model with 34 tables of mixed topics; the largest

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
- Vulnerability (Alto): Public with no sign-in; shows compliance and hours per supervisor
- Stability (Bajo): Daily scheduled refresh
- Scalability (Bajo): 8 MB model

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
- Vulnerability (Alto): Public with no sign-in; shows sales, targets and store comments; 3 hidden pages
- Stability (Medio): It updates by itself (last: October 11, 2026); the date and time of the last update are not shown in the report
- Scalability (Medio): DirectQuery (queries the live source); 30 MB model with 23 tables

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
- Vulnerability (Medio): Public link: anyone who has it can open it and respond; collects screenshots and names
- Stability (Medio): The administrator receives and updates it; response destination to confirm

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
- Vulnerability (Medio): Public link: anyone who has it can open it and respond; collects name and employee ID
- Stability (Medio): The administrator receives and updates it; response destination to confirm

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

# SDD · Incident Reporting Route

## Summary
Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medio): Public link: anyone who has it can open it and respond; collects names and justifications
- Stability (Medio): The administrator receives and updates it; response destination to confirm

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

- [ ] T-006: Limit “Incident Reporting Route” to company accounts and define where its responses are stored (To do · First)
  - Done when: An outside account cannot respond and the form has a response destination.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Incident Reporting Route” (T-006) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-006 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: try to respond from a non-company account | Tool owner | First week |
| 4 | Note the backup in the record and close the 4 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Walmart Audit

## Summary
Anyone with the link can respond; it is filled in when the event happens. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medio): Public link: anyone who has it can open it and respond; collects supervisor names; feeds the Walmart Audit dashboard
- Stability (Medio): The administrator receives and updates it; response destination to confirm; changing its questions may break the dashboard

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
- Vulnerability (Medio): Public link: anyone who has it can open it and respond; collects supervisor names
- Stability (Medio): The administrator receives and updates it; response destination to confirm

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

# SDD · DSD Store Master

## Summary
It asks for a company account and permission; it is updated as needed. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medio): Contains store addresses and phone numbers; requires a company account and permission; the permission list still needs review
- Stability (Alto): Lives in a personal OneDrive: if its owner leaves, access is lost; no update date
- Scalability (Medio): About 21,358 rows and 82 columns on one sheet

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | Done | It asks for a company account and permission. |
| 2 | Data in a company place | To do | It is in a personal OneDrive. |
| 3 | Up-to-date information | To do | It is updated as needed; who updates it and when still has to be noted. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 3 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-004** (To do): That the data is in a safe, tidy place — It still has to be moved to a server, who updates it noted and permissions reviewed.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-013 | The system MUST keep every master database in a company-controlled place, never in a personal account, with reviewed permissions. Moving them to a server is suggested, for security. Moving it to a server is suggested. | To do |
| FR-014 | The system SHOULD keep a single master list of stores and retire the copies. | Partial |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-004 | No master file remains in a personal account. | The file is in a company place, not in a personal account. | To do |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 3). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| How often are the Excel files updated? | As needed. |
| Could the Excel databases be migrated to a server? | Yes, as a suggestion for security. |

### To answer

- List of people with access to the file and their permission (read or edit).
- Whether it is fed by other systems or captured by hand.
- Permissions and who can share it.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Master databases | Move the 4 Excel databases to a server (suggested), with a single master list of stores | Improves security compared with Excel files and avoids different figures across reports. |

### Phases that apply

- Phase 4: Tidy databases
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Moving the Excel databases to a server interrupts whoever uses them today | Move one database at a time, warn beforehand and keep the original file until the result is validated. |

## 5. Tasks

- [ ] T-005: Move “DSD Store Master” to the server as the single store master, take it out of the personal OneDrive, review permissions and note who updates it and when (To do · Next)
  - Done when: It is on the server, shows its last update and who has access, and nothing remains in personal accounts.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “DSD Store Master” (T-005) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-005 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: confirm who has access and that nothing remains in personal accounts | Tool owner | First week |
| 4 | Note the backup in the record and close the 3 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · DSD Route Master

## Summary
It asks for a company account and permission; it is updated as needed. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medio): Contains rates, costs and staff contacts; requires a company account and permission; the permission list still needs review
- Stability (Medio): Hidden sheets and a copy of the store master that may drift out of sync
- Scalability (Bajo): About 3,658 route rows across 10 sheets

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | Done | It asks for a company account and permission. |
| 2 | Data in a company place | Partial | It is on a team site; the permissions still have to be reviewed and the copy of the store master removed. |
| 3 | Up-to-date information | To do | It is updated as needed; who updates it and when still has to be noted. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 3 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-004** (To do): That the data is in a safe, tidy place — It still has to be moved to a server, who updates it noted and permissions reviewed.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-013 | The system MUST keep every master database in a company-controlled place, never in a personal account, with reviewed permissions. Moving them to a server is suggested, for security. Moving it to a server is suggested. | Partial |
| FR-014 | The system SHOULD keep a single master list of stores and retire the copies. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-004 | No master file remains in a personal account. | The file is in a company place, not in a personal account. | Partial |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 3). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| How often are the Excel files updated? | As needed. |
| Could the Excel databases be migrated to a server? | Yes, as a suggestion for security. |

### To answer

- List of people with access to the file and their permission (read or edit).
- Whether it is fed by other systems or captured by hand.
- File permissions and version control.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Master databases | Move the 4 Excel databases to a server (suggested), with a single master list of stores | Improves security compared with Excel files and avoids different figures across reports. |

### Phases that apply

- Phase 4: Tidy databases
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Moving the Excel databases to a server interrupts whoever uses them today | Move one database at a time, warn beforehand and keep the original file until the result is validated. |

## 5. Tasks

- [ ] T-005: Move “DSD Route Master” to the server using the single master (and removing the copy), review permissions and note who updates it and when (To do · Next)
  - Done when: It is on the server, shows its last update and who has access, and nothing remains in personal accounts.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “DSD Route Master” (T-005) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-005 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: confirm who has access and that nothing remains in personal accounts | Tool owner | First week |
| 4 | Note the backup in the record and close the 3 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · DSD FS Route Master

## Summary
It asks for a company account and permission; it is updated as needed. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medio): Contains costs, budget and travel data per supervisor; requires a company account and permission; the permission list still needs review
- Stability (Medio): Copy of the store master and a hidden previous version
- Scalability (Bajo): About 4,177 rows across 11 sheets

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | Done | It asks for a company account and permission. |
| 2 | Data in a company place | Partial | It is on a team site; the permissions still have to be reviewed and the copy of the store master removed. |
| 3 | Up-to-date information | To do | It is updated as needed; who updates it and when still has to be noted. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 3 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-004** (To do): That the data is in a safe, tidy place — It still has to be moved to a server, who updates it noted and permissions reviewed.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-013 | The system MUST keep every master database in a company-controlled place, never in a personal account, with reviewed permissions. Moving them to a server is suggested, for security. Moving it to a server is suggested. | Partial |
| FR-014 | The system SHOULD keep a single master list of stores and retire the copies. | To do |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-004 | No master file remains in a personal account. | The file is in a company place, not in a personal account. | Partial |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 3). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| How often are the Excel files updated? | As needed. |
| Could the Excel databases be migrated to a server? | Yes, as a suggestion for security. |

### To answer

- List of people with access to the file and their permission (read or edit).
- Whether it is fed by other systems or captured by hand.
- Permissions and version control.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Master databases | Move the 4 Excel databases to a server (suggested), with a single master list of stores | Improves security compared with Excel files and avoids different figures across reports. |

### Phases that apply

- Phase 4: Tidy databases
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Moving the Excel databases to a server interrupts whoever uses them today | Move one database at a time, warn beforehand and keep the original file until the result is validated. |

## 5. Tasks

- [ ] T-005: Move “DSD FS Route Master” to the server using the single master (and removing the copy), review permissions and note who updates it and when (To do · Next)
  - Done when: It is on the server, shows its last update and who has access, and nothing remains in personal accounts.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “DSD FS Route Master” (T-005) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-005 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: confirm who has access and that nothing remains in personal accounts | Tool owner | First week |
| 4 | Note the backup in the record and close the 3 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---

# SDD · Plan de visitas (Unify)

## Summary
It asks for a company account and permission; it is updated as needed. Tasks to do: 1.

## 1. Project principles

**Starting point**
- Vulnerability (Medio): Contains hourly rates and cost per store and day; requires a company account and permission; the permission list still needs review
- Stability (Medio): One file per month: depends on it being created every month
- Scalability (Medio): About 74,000 rows per month; the history grows

| # | Principle | Status | How this tool stands |
|---|---|---|---|
| 1 | Sign in with the company account | Done | It asks for a company account and permission. |
| 2 | Data in a company place | Partial | It is on a team site; the permissions still have to be reviewed and the monthly files consolidated. |
| 3 | Up-to-date information | To do | It is updated as needed; who updates it and when still has to be noted. |
| 4 | Owners — Owner | Done | Owner: its creator, already recorded. |
| 4 | Owners — Backup | To do | Backup: still has to be noted in the record. |
| 5 | Document and change in an orderly way | Partial | It has its documentation record; 3 pending items remain to be closed. |

## 2. What is needed

### People's needs

- **US-003A** (Done): That it has its owner recorded — Its owner is its creator, already recorded.
- **US-003B** (To do): That it has a backup recorded — The backup still has to be noted in the record.
- **US-004** (To do): That the data is in a safe, tidy place — It still has to be moved to a server, who updates it noted and permissions reviewed.

### What must be met

| ID | Requirement | Status |
|---|---|---|
| FR-010 | Every tool MUST have a backup recorded, who is a person. | To do |
| FR-011 | The system MUST keep the 7-area documentation per tool. | Partial |
| FR-013 | The system MUST keep every master database in a company-controlled place, never in a personal account, with reviewed permissions. Moving them to a server is suggested, for security. Moving it to a server is suggested. | Partial |
| FR-014 | The system SHOULD keep a single master list of stores and retire the copies. | Not applicable |

### How we will know it worked

| ID | Criterion | How to measure it here | Status |
|---|---|---|---|
| SC-003 | 100% of the 17 tools have a registered backup within 30 days (the owner, its creator, is already recorded). | Its record shows the backup. | To do |
| SC-004 | No master file remains in a personal account. | The file is in a company place, not in a personal account. | Partial |
| SC-006 | The pending documentation lines drop from 32 to fewer than 10. | The pending items of its record drop to zero or almost (today 3). | Partial |

## 3. Questions and answers

### Already answered

| Question | Answer |
|---|---|
| Which links ask for sign-in today? | No dashboard (except Cost to Serve, through the Portal) and no form: anyone who has the link can open them. The Excel databases, on SharePoint, require a company account and permission. |
| How often are the Excel files updated? | As needed. |
| Could the Excel databases be migrated to a server? | Yes, as a suggestion for security. |

### To answer

- List of people with access to the file and their permission (read or edit).
- Whether it is fed by other systems or captured by hand.
- Folder permissions: it concentrates the labor history of all months.

## 4. Plan: how it is done

### Decisions about tools

| Area | What is chosen | Why |
|---|---|---|
| Master databases | Move the 4 Excel databases to a server (suggested), with a single master list of stores | Improves security compared with Excel files and avoids different figures across reports. |

### Phases that apply

- Phase 4: Tidy databases
- Phase 3: Owner and backup per tool
- Final phase: Close

### Risks and how to avoid them

| Risk | How to avoid it |
|---|---|
| Moving the Excel databases to a server interrupts whoever uses them today | Move one database at a time, warn beforehand and keep the original file until the result is validated. |

## 5. Tasks

- [ ] T-005: Move “Plan de visitas (Unify)” to the server in a single table, review permissions and note who updates it and when (To do · Next)
  - Done when: It is on the server, shows its last update and who has access, and nothing remains in personal accounts.

## 6. Action plan

| # | What is done | Who | When |
|---|---|---|---|
| 1 | Load the tasks of “Plan de visitas (Unify)” (T-005) into the work list | Inventory owner | Day one |
| 2 | Do the most important first: T-005 | Tool owner (its creator), with the backup | First week |
| 3 | Check the result: confirm who has access and that nothing remains in personal accounts | Tool owner | First week |
| 4 | Note the backup in the record and close the 3 pending documentation items | Tool owner | First two weeks |
| 5 | Every week, mark the progress in the work list | Inventory owner | Every week |

---
