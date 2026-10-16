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
