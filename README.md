# Smart Recruitment Agent

### AI-Powered Recruitment Automation System

---

## Overview

**Smart Recruitment Agent** is an end-to-end recruitment automation system developed in Python as part of the **Applied Artificial Intelligence** course at **Bar-Ilan University**.

The system automates the complete recruitment process, beginning with candidate application generation and ending with interview scheduling, Google Calendar integration, automated invitation emails, and Excel report generation.

The project demonstrates how multiple independent software modules can work together to automate a real-world Human Resources (HR) recruitment workflow using Google APIs, workflow automation, and intelligent decision-making.

---

## Project Objectives

The primary objectives of this project are:

* Automate candidate processing.
* Reduce manual HR workload.
* Evaluate and rank candidates automatically.
* Schedule interviews using Google Calendar.
* Detect calendar conflicts before scheduling.
* Send conflict notification emails automatically.
* Schedule interviews at least 7 days in advance.
* Skip weekends when scheduling interviews.
* Send interview invitations automatically via Gmail.
* Generate recruitment reports in Excel format.
* Demonstrate a complete AI-assisted recruitment workflow.
* Showcase modular software architecture and API integration.

---

## Main Features

The system provides the following capabilities:

* Gmail API Integration
* Google Calendar API Integration
* Automatic Candidate Evaluation
* Intelligent Candidate Ranking
* Interview Scheduling
* Calendar Conflict Detection
* Conflict Notification Emails
* Weekend-Aware Interview Scheduling
* 7-Day Advance Scheduling
* Automatic Email Invitations
* Excel Report Generation
* Duplicate Detection and Prevention
* Error Handling and Validation
* Modular Architecture
* Interactive Main Menu
* End-to-End Workflow Automation

---

## System Workflow

```text
                   Demo Mode
                       │
                       ▼
           Fake Mail Generator
                       │
                       ▼
                 Gmail Inbox
                       │
                       ▼
            Recruitment Agent
                       │
                       ▼
             Candidate Ranking
                       │
                       ▼
           Interview Scheduler
           (Conflict Detection)
                       │
                       ▼
            Google Calendar
                       │
                       ▼
           Invitation Sender
                       │
                       ▼
              Excel Reports
```

---

## Project Architecture

The project follows a modular architecture where every module has a single responsibility.

```text
                    main.py
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ▼                ▼                ▼
fake_mail_generator.py recruitment_agent.py
                               │
                               ▼
                  interview_scheduler.py
                  (Calendar Conflict Detection)
                               │
                               ▼
                  invitation_sender.py
                  (Dual Excel Sync)
```

Each module can run independently or as part of the complete workflow managed by **main.py**.

---

## Technologies Used

### Programming Language

* Python 3.13

### Google Services

* Gmail API
* Google Calendar API
* Google OAuth 2.0

### Python Libraries

* Pandas
* OpenPyXL
* Google API Python Client
* Google Authentication Libraries

### Development Tools

* Git
* GitHub
* Microsoft Excel
* Visual Studio Code
* PowerShell

---

## Key Project Capabilities

The Smart Recruitment Agent demonstrates:

* Workflow Automation
* API Integration
* Data Processing
* Business Rule Evaluation
* Automated Decision Making
* Calendar Management
* Calendar Conflict Detection
* Conflict Notification Emails
* Weekend-Aware Scheduling
* Email Automation
* Authentication with OAuth 2.0
* Excel Reporting
* Error Handling
* Duplicate Prevention
* Modular Software Design
* ---
## Project Structure

```text
SmartRecruitmentAgent/
│
├── main.py
├── fake_mail_generator.py
├── recruitment_agent.py
├── interview_scheduler.py
├── invitation_sender.py
├── create_token.py
├── requirements.txt
├── candidates.xlsx
├── credentials.json
├── token.json
│
├── docs/
├── screenshots/
├── skill/
│
├── gmail_candidates.xlsx          (Generated Automatically)
├── interview_candidates.xlsx      (Generated Automatically)
├── gmail_summary.txt              (Generated Automatically)
│
└── README.md
```

---

## Repository Contents

The repository contains:

| File / Folder            | Description                                       |
| ------------------------ | ------------------------------------------------- |
| `main.py`                | Main workflow manager                             |
| `fake_mail_generator.py` | Generates demonstration job applications          |
| `recruitment_agent.py`   | Reads Gmail applications and evaluates candidates |
| `interview_scheduler.py` | Schedules interviews with conflict detection      |
| `invitation_sender.py`   | Sends interview invitation emails                 |
| `create_token.py`        | Creates the Google OAuth token                    |
| `requirements.txt`       | Python dependencies                               |
| `docs/`                  | Project documentation                             |
| `screenshots/`           | Project screenshots                               |
| `skill/`                 | AI skills and supporting files                    |
| `README.md`              | Project documentation                             |

Generated output files are created automatically during execution.

---

## System Requirements

The project was developed and tested using:

| Component           | Version       |
| ------------------- | ------------- |
| Python              | 3.13          |
| Operating System    | Windows 11    |
| Gmail API           | v1            |
| Google Calendar API | v3            |
| Microsoft Excel     | Microsoft 365 |

---

## Required Python Packages

Install all required packages using:

```bash
pip install -r requirements.txt
```

Main packages:

* pandas
* openpyxl
* google-api-python-client
* google-auth
* google-auth-oauthlib
* google-auth-httplib2

---

## Google API Configuration

The project uses Google's OAuth 2.0 authentication.

Required files:

* `credentials.json`
* `token.json`

These files must be located in the project root directory.

Authentication is shared between:

* Gmail API
* Google Calendar API

This allows the system to access Gmail messages and manage Google Calendar events using the same authenticated account.

---

## Required Project Files

Before running the application, verify that the following files exist:

```text
main.py
fake_mail_generator.py
recruitment_agent.py
interview_scheduler.py
invitation_sender.py
candidates.xlsx
credentials.json
token.json
requirements.txt
```

The application validates the required files before executing any workflow.

---

## Installation

### Step 1 – Clone the Repository

```bash
git clone <repository-url>
```

---

### Step 2 – Navigate to the Project Folder

```bash
cd SmartRecruitmentAgent
```

---

### Step 3 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4 – Configure Google APIs

Place the following files inside the project folder:

* credentials.json
* token.json

---

### Step 5 – Run the Application

```bash
python main.py
```

After launching the application, the Smart Recruitment Agent main menu will appear.

---

## Running the Project

Launch the application using:

```bash
python main.py
```

The application opens an interactive console menu that allows the user to execute each module independently or run the complete recruitment workflow.

---

## Main Menu

```text
==================================================
SMART RECRUITMENT AGENT
==================================================

1. Generate Fake Applications (Demo)

2. Process Gmail Applications

3. Schedule Interviews

4. Send Interview Invitations

5. Run Recruitment Workflow

6. Project Information

7. Exit
```

---

## Menu Options

### Option 1 – Generate Fake Applications (Demo)

This option generates realistic job application emails for demonstration purposes.

The generated emails are automatically sent to the configured Gmail account and simulate real candidates applying for various positions.

**Executed Module**

```text
fake_mail_generator.py
```

---

### Option 2 – Process Gmail Applications

This option scans the Gmail inbox and processes candidate applications.

The Recruitment Agent performs the following tasks:

* Downloads candidate emails.
* Extracts candidate information.
* Calculates recruitment scores.
* Classifies candidates.
* Removes duplicate email addresses.
* Generates recruitment reports.

**Generated Files**

* gmail_candidates.xlsx
* gmail_summary.txt

**Executed Module**

```text
recruitment_agent.py
```

---

### Option 3 – Schedule Interviews

Candidates classified as **High Priority** are automatically selected for interviews.

The Interview Scheduler:

* Checks calendar availability before scheduling.
* Detects and handles calendar conflicts automatically.
* Sends conflict notification emails to affected candidates.
* Schedules interviews at least 7 days in advance.
* Skips Friday and Saturday when scheduling.
* Creates interview events in Google Calendar.
* Assigns interview dates and times.
* Updates the recruitment Excel report.
* Prevents duplicate interview scheduling.

**Generated Files**

* gmail_candidates.xlsx (updated)
* interview_candidates.xlsx

**Executed Module**

```text
interview_scheduler.py
```

---

### Option 4 – Send Interview Invitations

After interviews are scheduled, invitation emails are automatically sent to the selected candidates.

The Invitation Sender performs the following tasks:

* Reads interview details from the recruitment report.
* Sends personalized interview invitation emails using Gmail API.
* Updates the invitation status.
* Records the invitation date and time.
* Prevents duplicate invitation emails.
* Syncs invitation status to both Excel reports.

**Updated Files**

* gmail_candidates.xlsx
* interview_candidates.xlsx

**Executed Module**

```text
invitation_sender.py
```

---

### Option 5 – Run Recruitment Workflow

This option executes the entire recruitment workflow automatically.

Workflow execution order:

```text
Recruitment Agent
        │
        ▼
Interview Scheduler
(Calendar Conflict Detection)
        │
        ▼
Invitation Sender
(Dual Excel Sync)
```

The Demo module is intentionally excluded from this workflow.

Its purpose is only to generate demonstration data when needed.

During execution the system:

* Validates all required files.
* Executes each module sequentially.
* Stops immediately if a critical error occurs.
* Displays a success message after each completed step.
* Prints a final workflow summary.

---

### Option 6 – Project Information

Displays general project information, including:

* Project Name
* Current Version
* Project Description
* Workflow Overview
* Technologies Used

This option does not execute any module.

---

### Option 7 – Exit

Safely terminates the application.

The program closes gracefully after displaying a confirmation message.
---

## Workflow Execution

The complete recruitment workflow consists of three main stages.

### Stage 1 – Candidate Processing

The Recruitment Agent reads candidate applications from Gmail, evaluates each candidate according to predefined business rules, calculates a recruitment score, classifies the candidate, and generates the initial Excel reports.

---

### Stage 2 – Interview Scheduling

Candidates classified as **High Priority** are automatically selected.

Interview Scheduler:

* Checks calendar availability before scheduling.
* Detects calendar conflicts automatically.
* Sends conflict notification emails to affected candidates.
* Schedules interviews at least 7 days in advance.
* Skips Friday and Saturday when scheduling.
* Creates Google Calendar events for available slots.
* Updates the recruitment report with interview details.

Interview details recorded:

* Interview Date
* Interview Time
* Calendar Status
* Calendar Event ID

Duplicate interview creation is automatically prevented.

---

### Stage 3 – Invitation Delivery

Invitation Sender sends interview invitation emails only to candidates who:

* Have a scheduled interview.
* Have not already received an invitation.

After successful delivery the system updates:

* Invitation Status
* Invitation Sent Date

Both `gmail_candidates.xlsx` and `interview_candidates.xlsx` are synced automatically.

Duplicate invitations are automatically prevented.

---

## Design Principles

The Smart Recruitment Agent was designed according to the following software engineering principles:

* Modular Architecture
* Separation of Responsibilities
* Automation
* Reusability
* Error Isolation
* Data Validation
* Duplicate Prevention
* Workflow Management

Each module performs a single responsibility and communicates through shared project files.

---

## Main Project Modules

The project consists of five independent Python modules managed by **main.py**.

### fake_mail_generator.py

This module is responsible for generating realistic job application emails for demonstration purposes.

**Main Responsibilities**

* Generate sample candidate information.
* Create realistic recruitment emails.
* Send emails using Gmail API.
* Simulate incoming job applications.

**Input**

* candidates.xlsx

**Output**

* Gmail Inbox

---

### recruitment_agent.py

This module processes all candidate applications received through Gmail.

**Main Responsibilities**

* Connect to Gmail API.
* Download candidate emails.
* Extract candidate information.
* Calculate recruitment scores.
* Apply business rules.
* Classify candidates.
* Remove duplicate email addresses.
* Generate recruitment reports.

**Generated Files**

* gmail_candidates.xlsx
* gmail_summary.txt

---

### interview_scheduler.py

Automatically schedules interviews for eligible candidates with full calendar conflict detection.

**Main Responsibilities**

* Read recruitment results.
* Select High Priority candidates.
* Check calendar availability before scheduling.
* Detect and handle calendar conflicts.
* Send conflict notification emails to affected candidates.
* Schedule interviews at least 7 days in advance.
* Skip Friday and Saturday when scheduling.
* Create Google Calendar events.
* Assign interview dates and times.
* Update recruitment reports.
* Prevent duplicate interviews.

**Generated Files**

* interview_candidates.xlsx
* Updated gmail_candidates.xlsx

---

### invitation_sender.py

Sends interview invitation emails to scheduled candidates.

**Main Responsibilities**

* Read scheduled interview information.
* Send interview invitations.
* Update invitation status.
* Record invitation sending date.
* Prevent duplicate invitation emails.
* Sync invitation status to both Excel reports.

**Updated Files**

* gmail_candidates.xlsx
* interview_candidates.xlsx

---

### main.py

The central workflow manager of the project.

**Main Responsibilities**

* Display the interactive menu.
* Validate required project files.
* Execute project modules.
* Handle execution errors.
* Execute the complete recruitment workflow.
* Manage user interaction.

---

## Generated Output Files

During execution the system automatically creates several output files.

### gmail_candidates.xlsx

The primary recruitment report.

Contains:

* Candidate ID
* Candidate Name
* Email
* Position
* Recruitment Score
* Recruitment Status
* Interview Date
* Interview Time
* Calendar Status
* Calendar Event
* Invitation Status
* Invitation Sent Date

---

### interview_candidates.xlsx

Contains only candidates selected for interviews.

Information includes:

* Candidate Name
* Position
* Interview Date
* Interview Time
* Calendar Status
* Invitation Status
* Invitation Sent Date

---

### gmail_summary.txt

Provides a summary of each recruitment cycle.

Includes:

* Total Candidates
* Duplicate Emails Removed
* Highest Score
* Average Score
* High Priority Candidates
* Interview Candidates
* Review Candidates
* ---

## Error Handling

The project includes comprehensive exception handling.

Handled situations include:

* Missing required files.
* Gmail API connection errors.
* Google Calendar API failures.
* Authentication errors.
* Missing permissions.
* Keyboard interruption.
* Unexpected runtime exceptions.

Whenever an unexpected error occurs, the workflow stops safely to prevent inconsistent data.

---

## Duplicate Prevention

The system includes several duplicate prevention mechanisms.

### Candidate Processing

Duplicate candidate email addresses are automatically removed before report generation.

---

### Interview Scheduling

Before creating a Google Calendar event, the system:

* Checks calendar availability for the requested time slot.
* Verifies whether the candidate already has a scheduled interview.
* Sends a conflict notification email if the slot is unavailable.

If an interview already exists, the candidate is skipped.

---

### Invitation Delivery

Before sending an invitation email, the system verifies:

* Calendar Status
* Invitation Status

If an invitation has already been sent, no additional invitation is generated.

---

## Calendar Conflict Detection

The Interview Scheduler includes a full calendar conflict detection mechanism.

### How It Works

Before creating each interview event, the system:

1. Calculates the proposed interview time slot.
2. Queries Google Calendar for existing events in that time slot.
3. If the slot is available — creates the interview event.
4. If the slot is occupied — sends a conflict notification email to the candidate.

### Conflict Notification Email

When a conflict is detected, the system automatically sends a notification email to the affected candidate informing them that the interview could not be scheduled at the requested time and that the HR team will contact them to arrange an alternative.

### Weekend-Aware Scheduling

The system automatically skips Friday and Saturday when scheduling interviews.

If the next available slot falls on a weekend, the scheduler advances to the following Sunday.

### 7-Day Advance Scheduling

All interviews are scheduled at least 7 days in advance from the date the workflow is executed.

---

## Validation

Before executing any workflow, the system validates:

* Required project files.
* Authentication files.
* Project modules.
* Input files.

Only after successful validation does the workflow continue.

---

## Testing

The project was tested using multiple execution scenarios.

Completed tests include:

* Gmail API connectivity.
* Google Calendar connectivity.
* Fake candidate generation.
* Candidate processing.
* Candidate evaluation.
* Candidate ranking.
* Excel report generation.
* Interview scheduling.
* Calendar conflict detection.
* Conflict notification email delivery.
* Weekend skip logic.
* 7-day advance scheduling.
* Invitation email delivery.
* Duplicate interview prevention.
* Duplicate invitation prevention.
* Complete workflow execution through Main v2.

All modules were tested independently and as part of the complete integrated workflow.

---

## Project Highlights

The Smart Recruitment Agent project demonstrates the integration of multiple technologies into a complete recruitment automation platform.

Key project highlights include:

* End-to-end recruitment workflow automation.
* Gmail API integration for processing applications.
* Google Calendar API integration for interview scheduling.
* Calendar conflict detection and automatic handling.
* Conflict notification emails sent automatically.
* Weekend-aware interview scheduling.
* 7-day advance scheduling enforcement.
* Automated interview invitation emails.
* Excel-based recruitment reporting with dual file sync.
* Interactive workflow management.
* Duplicate detection and prevention.
* Modular software architecture.
* Comprehensive error handling.
* Google OAuth 2.0 authentication.

---

## Skills Demonstrated

### Technical Skills

* Python Programming
* Object-Oriented Programming (OOP)
* Workflow Automation
* REST API Integration
* Gmail API
* Google Calendar API
* OAuth 2.0 Authentication
* Excel Data Processing
* Pandas
* OpenPyXL
* Error Handling
* File Management
* Git & GitHub
* Software Documentation

### Professional Skills

* Problem Solving
* Process Automation
* Business Process Analysis
* System Integration
* Software Testing
* Debugging
* Technical Documentation
* Workflow Design
* Project Planning
* ---

## Error Handling

The project includes comprehensive exception handling.

Handled situations include:

* Missing required files.
* Gmail API connection errors.
* Google Calendar API failures.
* Authentication errors.
* Missing permissions.
* Keyboard interruption.
* Unexpected runtime exceptions.

Whenever an unexpected error occurs, the workflow stops safely to prevent inconsistent data.

---

## Duplicate Prevention

The system includes several duplicate prevention mechanisms.

### Candidate Processing

Duplicate candidate email addresses are automatically removed before report generation.

---

### Interview Scheduling

Before creating a Google Calendar event, the system:

* Checks calendar availability for the requested time slot.
* Verifies whether the candidate already has a scheduled interview.
* Sends a conflict notification email if the slot is unavailable.

If an interview already exists, the candidate is skipped.

---

### Invitation Delivery

Before sending an invitation email, the system verifies:

* Calendar Status
* Invitation Status

If an invitation has already been sent, no additional invitation is generated.

---

## Calendar Conflict Detection

The Interview Scheduler includes a full calendar conflict detection mechanism.

### How It Works

Before creating each interview event, the system:

1. Calculates the proposed interview time slot.
2. Queries Google Calendar for existing events in that time slot.
3. If the slot is available — creates the interview event.
4. If the slot is occupied — sends a conflict notification email to the candidate.

### Conflict Notification Email

When a conflict is detected, the system automatically sends a notification email to the affected candidate informing them that the interview could not be scheduled at the requested time and that the HR team will contact them to arrange an alternative.

### Weekend-Aware Scheduling

The system automatically skips Friday and Saturday when scheduling interviews.

If the next available slot falls on a weekend, the scheduler advances to the following Sunday.

### 7-Day Advance Scheduling

All interviews are scheduled at least 7 days in advance from the date the workflow is executed.

---

## Validation

Before executing any workflow, the system validates:

* Required project files.
* Authentication files.
* Project modules.
* Input files.

Only after successful validation does the workflow continue.

---

## Testing

The project was tested using multiple execution scenarios.

Completed tests include:

* Gmail API connectivity.
* Google Calendar connectivity.
* Fake candidate generation.
* Candidate processing.
* Candidate evaluation.
* Candidate ranking.
* Excel report generation.
* Interview scheduling.
* Calendar conflict detection.
* Conflict notification email delivery.
* Weekend skip logic.
* 7-day advance scheduling.
* Invitation email delivery.
* Duplicate interview prevention.
* Duplicate invitation prevention.
* Complete workflow execution through Main v2.

All modules were tested independently and as part of the complete integrated workflow.

---

## Project Highlights

The Smart Recruitment Agent project demonstrates the integration of multiple technologies into a complete recruitment automation platform.

Key project highlights include:

* End-to-end recruitment workflow automation.
* Gmail API integration for processing applications.
* Google Calendar API integration for interview scheduling.
* Calendar conflict detection and automatic handling.
* Conflict notification emails sent automatically.
* Weekend-aware interview scheduling.
* 7-day advance scheduling enforcement.
* Automated interview invitation emails.
* Excel-based recruitment reporting with dual file sync.
* Interactive workflow management.
* Duplicate detection and prevention.
* Modular software architecture.
* Comprehensive error handling.
* Google OAuth 2.0 authentication.

---

## Skills Demonstrated

### Technical Skills

* Python Programming
* Object-Oriented Programming (OOP)
* Workflow Automation
* REST API Integration
* Gmail API
* Google Calendar API
* OAuth 2.0 Authentication
* Excel Data Processing
* Pandas
* OpenPyXL
* Error Handling
* File Management
* Git & GitHub
* Software Documentation

### Professional Skills

* Problem Solving
* Process Automation
* Business Process Analysis
* System Integration
* Software Testing
* Debugging
* Technical Documentation
* Workflow Design
* Project Planning
