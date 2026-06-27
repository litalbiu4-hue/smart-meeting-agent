# Product Requirements Document (PRD)

## Project Name

**Smart Recruitment Agent – AI-Powered Recruitment Automation System**

---

## Project Purpose

The Smart Recruitment Agent is an end-to-end recruitment automation system developed to streamline and automate the candidate recruitment process.

The system simulates candidate applications, processes incoming Gmail messages using Claude LLM for free-text analysis, evaluates applicants according to predefined business rules, schedules interviews in Google Calendar with conflict detection, sends interview invitation emails, and generates recruitment reports.

The project demonstrates workflow automation through the integration of multiple Google services, Claude AI, and Python-based business logic.

---

## Business Problem

Recruitment teams spend a significant amount of time performing repetitive administrative tasks such as:

* Reading candidate applications.
* Evaluating applicant qualifications.
* Ranking candidates.
* Scheduling interviews.
* Sending interview invitations.
* Maintaining recruitment reports.

Manual processing increases workload, introduces delays, and may result in inconsistent decision-making.

The Smart Recruitment Agent automates these repetitive tasks using AI-powered free-text analysis, allowing recruiters to focus on candidate selection rather than administrative work.

---

## Project Objectives

The system aims to:

* Generate demonstration candidate applications in natural free-text format.
* Read Gmail applications automatically.
* Extract candidate information using Claude LLM from free-text emails.
* Evaluate and rank candidates.
* Classify recruitment status.
* Schedule interviews automatically.
* Check calendar availability before scheduling.
* Detect calendar conflicts before scheduling interviews.
* Send automatic conflict notification emails to affected candidates.
* Schedule interviews at least 7 days in advance.
* Skip weekends (Friday and Saturday) when scheduling.
* Create Google Calendar interview events.
* Send interview invitation emails automatically.
* Generate Excel recruitment reports.
* Sync invitation status to both Excel reports.
* Prevent duplicate interviews.
* Prevent duplicate invitation emails.
* Execute the complete recruitment workflow through a single application.

---

## Functional Requirements

The system shall:

### Candidate Management

* Generate candidate applications in natural free-text format.
* Read Gmail messages.
* Read only unread emails.
* Mark emails as read after processing.
* Extract candidate information using Claude LLM.
* Calculate recruitment scores.
* Classify candidates into recruitment categories.

---

### Interview Management

* Select High Priority candidates.
* Check calendar availability before scheduling.
* Detect and handle calendar conflicts.
* Send conflict notification emails to affected candidates.
* Schedule interviews at least 7 days in advance.
* Skip Friday and Saturday when scheduling.
* Schedule interviews automatically.
* Create Google Calendar events.
* Record interview information.
* Prevent duplicate interview scheduling.

---

### Invitation Management

* Send interview invitation emails.
* Update invitation status.
* Record invitation dates.
* Prevent duplicate invitations.
* Sync invitation status to both Excel reports.

---

### Reporting

Generate:

* gmail_candidates.xlsx
* interview_candidates.xlsx
* gmail_summary.txt

---

### Workflow Management

The system shall provide:

* Interactive main menu.
* Individual module execution.
* Complete workflow execution.
* Required file validation.
* Runtime error handling.
* ---

## Inputs

* Candidate database (Excel)
* Gmail inbox messages (unread only)
* Google Calendar
* Google OAuth authentication
* Anthropic Claude API

---

## Outputs

The system generates:

* Candidate ranking report
* Interview report
* Recruitment summary
* Google Calendar events
* Interview invitation emails
* Conflict notification emails
* Excel recruitment reports

---

## Technologies

* Python 3.13
* Gmail API
* Google Calendar API
* Google OAuth 2.0
* Claude AI (Anthropic)
* Claude API (claude-haiku-4-5-20251001)
* Pandas
* OpenPyXL
* Google API Python Client
* GitHub

---

## Success Criteria

The project is considered successful when it can:

* Authenticate successfully with Google APIs.
* Authenticate successfully with Anthropic Claude API.
* Process Gmail applications automatically.
* Read only unread emails and mark them as read after processing.
* Extract candidate information from free-text emails using Claude LLM.
* Evaluate and classify candidates.
* Generate recruitment reports.
* Check calendar availability before scheduling interviews.
* Detect calendar conflicts automatically.
* Send conflict notification emails to affected candidates.
* Schedule interviews at least 7 days in advance.
* Skip weekends when scheduling interviews.
* Schedule interviews automatically.
* Create Google Calendar events.
* Send interview invitations automatically.
* Sync invitation status across both Excel reports.
* Prevent duplicate interview scheduling.
* Prevent duplicate invitation emails.
* Execute the complete workflow successfully through the Main application.

---

## Final Deliverables

The completed project includes:

* Recruitment Agent with Claude LLM Integration
* Fake Mail Generator with Natural Free-Text Templates
* Interview Scheduler with Calendar Conflict Detection
* Invitation Sender with Dual Excel Sync
* Main Workflow Manager
* Gmail Integration
* Google Calendar Integration
* Claude AI Integration
* Calendar Conflict Detection
* Conflict Notification Emails
* Weekend-Aware Scheduling
* 7-Day Advance Scheduling
* Excel Reporting
* Complete Project Documentation
* ---

## Project Status

**Status:** ✅ Completed

The Smart Recruitment Agent project has been fully implemented, tested, documented, and published.

The final solution provides a complete recruitment automation workflow from candidate application generation through interview invitation delivery, including:

* Claude LLM free-text email analysis
* Calendar conflict detection
* Automatic conflict notifications
* Weekend-aware scheduling
* Synchronized Excel reporting
* Unread email processing with automatic read marking

---
