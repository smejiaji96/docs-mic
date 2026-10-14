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
