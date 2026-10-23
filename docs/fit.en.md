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
