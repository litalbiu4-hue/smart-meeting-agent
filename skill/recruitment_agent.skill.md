# Recruitment Agent Skill

## Name
Recruitment Agent

---

## Purpose
The Recruitment Agent is responsible for automatically processing candidate applications received through Gmail.
It evaluates candidates according to predefined business rules, calculates recruitment scores, classifies applicants, removes duplicate candidates, and generates recruitment reports that are used by the remaining modules of the Smart Recruitment Agent system.

---

## Responsibilities
The Recruitment Agent performs the following tasks:

* Connect to Gmail using Google OAuth 2.0.
* Read candidate application emails.
* Extract candidate information.
* Calculate recruitment scores.
* Classify candidates.
* Remove duplicate applications.
* Generate Excel recruitment reports.
* Generate recruitment summary reports.

---

## Inputs

* Gmail inbox messages
* Candidate application emails
* Candidate database (Excel)

---

## Processing Steps

1. Authenticate with Gmail API.
2. Read unread candidate emails.
3. Extract candidate information.
4. Validate candidate data.
5. Calculate recruitment scores.
6. Classify recruitment status.
7. Remove duplicate candidates.
8. Generate recruitment reports.

---

## Outputs

The Recruitment Agent generates:

* gmail_candidates.xlsx
* gmail_summary.txt

These files are later used by:

* Interview Scheduler (with Calendar Conflict Detection)
* Invitation Sender (with Dual Excel Sync)
* Main Workflow

---

## Technologies

* Python 3.13
* Gmail API
* Google OAuth 2.0
* Pandas
* OpenPyXL

---

## Success Criteria

The module is considered successful when it:

* Authenticates successfully with Gmail.
* Reads candidate applications.
* Processes all candidates.
* Calculates recruitment scores.
* Classifies candidates correctly.
* Removes duplicate candidates.
* Generates Excel recruitment reports.

---

## Integration

The Recruitment Agent is fully integrated with:

* Interview Scheduler (with Calendar Conflict Detection and Weekend-Aware Scheduling)
* Invitation Sender (with Dual Excel Sync)
* Main Workflow Manager

It represents the first processing stage of the complete recruitment workflow.

---

## Future Enhancements

Potential future improvements include:

* AI-powered CV parsing.
* Machine Learning candidate evaluation.
* LinkedIn API integration.
* Power BI recruitment dashboard.
* Candidate recommendation engine.
* Cloud deployment.

---

## Status

**Status:** ✅ Completed

The Recruitment Agent has been fully implemented, tested, documented, and integrated into the Smart Recruitment Agent recruitment workflow.
