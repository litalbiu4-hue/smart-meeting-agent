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
                               │
                               ▼
                  invitation_sender.py
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
* Email Automation
* Authentication with OAuth 2.0
* Excel Reporting
* Error Handling
* Duplicate Prevention
* Modular Software Design

---
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
| `interview_scheduler.py` | Schedules interviews using Google Calendar        |
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

**Updated File**

* gmail_candidates.xlsx

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
        │
        ▼
Invitation Sender
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

Interview Scheduler creates Google Calendar events and updates the recruitment report with:

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

Automatically schedules interviews for eligible candidates.

**Main Responsibilities**

* Read recruitment results.
* Select High Priority candidates.
* Create Google Calendar events.
* Assign interview dates.
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

**Updated File**

* gmail_candidates.xlsx

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

---

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

Before creating a Google Calendar event, the system verifies whether the candidate already has a scheduled interview.

If an interview already exists, the candidate is skipped.

---

### Invitation Delivery

Before sending an invitation email, the system verifies:

* Calendar Status
* Invitation Status

If an invitation has already been sent, no additional invitation is generated.

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
* Automated interview invitation emails.
* Excel-based recruitment reporting.
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

---

## Future Improvements

Possible future enhancements include:

* AI-based CV parsing using Large Language Models (LLMs).
* Automatic interview reminders.
* SMS and WhatsApp notifications.
* Candidate self-service interview rescheduling.
* Integration with LinkedIn API.
* Multi-user authentication.
* HR management dashboard.
* Machine Learning candidate ranking.
* Cloud deployment using Docker and Azure or AWS.
* Integration with additional HR systems.

---

## Project Status

**Status:** ✅ Completed

The Smart Recruitment Agent project has been fully implemented, tested, and validated.

The final version successfully supports:

* Candidate application generation.
* Gmail application processing.
* Automatic candidate evaluation.
* Candidate ranking.
* Google Calendar interview scheduling.
* Automatic interview invitation emails.
* Excel report generation.
* Duplicate prevention.
* Complete workflow automation.

All project modules were tested both independently and as part of the integrated workflow.

---

## Repository Contents

The repository includes:

* Python source code
* Project documentation
* Installation requirements
* Project screenshots
* Supporting documentation
* Skills folder

Output files are generated automatically during execution.

---

## Screenshots

The following screenshots are recommended for the GitHub repository:

* Main Menu
* Gmail Inbox
* Candidate Processing
* Google Calendar Interview Schedule
* Interview Invitation Email
* Excel Reports
* Workflow Execution

Store all screenshots inside the **screenshots** folder.

---

## Author

**Lital Edani**

Bar-Ilan University

M.Sc. Supply Chain Management

Course: Applied Artificial Intelligence

2026

---

## Acknowledgments

Special thanks to the course instructors for their guidance throughout the project.

This project also utilizes Google's official Gmail API and Google Calendar API for workflow automation.

---

## License

This project was developed exclusively for academic purposes as part of the Applied Artificial Intelligence course.

Commercial use is not permitted without the author's written permission.

---

## Conclusion

Smart Recruitment Agent demonstrates how modern software engineering practices, workflow automation, and cloud-based APIs can be combined to build a complete recruitment management system.

The project integrates Gmail, Google Calendar, Excel reporting, and modular Python applications into a single automated workflow, providing a realistic example of intelligent recruitment automation.

---

**End of README**

© 2026 Lital Edani. All Rights Reserved.
