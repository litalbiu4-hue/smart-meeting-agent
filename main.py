"""
=========================================================
SMART RECRUITMENT AGENT
Main v2 - Final Submission
=========================================================

This file manages the project workflow only.

It does NOT contain any business logic.

Modules:
- fake_mail_generator.py
- recruitment_agent.py
- interview_scheduler.py
- invitation_sender.py
"""

import os
import sys
import subprocess

# =========================================================
# PROJECT CONFIGURATION
# =========================================================

PROJECT_NAME = "Smart Recruitment Agent"
VERSION = "2.0"

REQUIRED_FILES = [
    "candidates.xlsx",
    "token.json",
    "fake_mail_generator.py",
    "recruitment_agent.py",
    "interview_scheduler.py",
    "invitation_sender.py"
]

# =========================================================
# UTILITIES
# =========================================================


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress ENTER to continue...")


def print_header():

    clear_screen()

    print("=" * 60)
    print("SMART RECRUITMENT AGENT")
    print("=" * 60)
    print(f"Version : {VERSION}")
    print()


def check_required_files():

    print("\nChecking required files...\n")

    missing = []

    for file_name in REQUIRED_FILES:

        if os.path.exists(file_name):
            print(f"✓ {file_name}")

        else:
            print(f"✗ {file_name}")
            missing.append(file_name)

    if missing:

        print("\nERROR")
        print("-" * 40)
        print("The following required files are missing:\n")

        for file_name in missing:
            print(f"- {file_name}")

        print("\nProgram cannot continue.\n")

        raise FileNotFoundError(
            "Missing required project files."
        )

    print("\nAll required files were found.\n")


# =========================================================
# MODULE EXECUTION
# =========================================================

def run_module(script_name):

    print(f"\nRunning {script_name}...\n")

    subprocess.run(
        [sys.executable, script_name],
        check=True
    )

    print("\n✓ Step completed successfully\n")
    # =========================================================
# MENU ACTIONS
# =========================================================

def generate_fake_applications():

    print_header()

    check_required_files()

    print("DEMO MODE")
    print("-" * 40)

    run_module("fake_mail_generator.py")

    pause()


def process_gmail():

    print_header()

    check_required_files()

    run_module("recruitment_agent.py")

    pause()


def schedule_interviews():

    print_header()

    check_required_files()

    run_module("interview_scheduler.py")

    pause()


def send_invitations():

    print_header()

    check_required_files()

    run_module("invitation_sender.py")

    pause()


# =========================================================
# FULL WORKFLOW
# =========================================================

def run_workflow():

    print_header()

    check_required_files()

    print("Starting Recruitment Workflow...\n")

    workflow = [
        "recruitment_agent.py",
        "interview_scheduler.py",
        "invitation_sender.py"
    ]

    for script in workflow:

        run_module(script)

    print("\n" + "=" * 42)
    print("WORKFLOW COMPLETED SUCCESSFULLY")
    print("=" * 42)

    pause()


# =========================================================
# PROJECT INFORMATION
# =========================================================

def project_information():

    print_header()

    print("Project Name")
    print("------------")
    print(PROJECT_NAME)

    print("\nVersion")
    print("-------")
    print(VERSION)

    print("\nProject Description")
    print("-------------------")
    print(
        "AI-based recruitment automation system "
        "that processes candidate applications using "
        "Claude LLM for free-text analysis, "
        "schedules interviews with calendar conflict "
        "detection and sends interview invitations."
    )

    print("\nWorkflow Overview")
    print("-----------------")
    print("1. Process Gmail Applications")
    print("2. Schedule Interviews")
    print("3. Send Interview Invitations")

    print("\nDemo Mode")
    print("---------")
    print(
        "Generate Fake Applications is available "
        "for demonstration purposes only and is "
        "not part of the main recruitment workflow."
    )

    print("\nTechnologies Used")
    print("-----------------")
    print("- Python")
    print("- Gmail API")
    print("- Google Calendar API")
    print("- Claude AI (Anthropic)")
    print("- Claude API")
    print("- Pandas")
    print("- Excel")
    print("- subprocess")
    print("- OAuth2 Authentication")

    pause()
    # =========================================================
# MAIN MENU
# =========================================================

def main():

    while True:

        try:

            print_header()

            print("1. Generate Fake Applications (Demo)")
            print("2. Process Gmail Applications")
            print("3. Schedule Interviews")
            print("4. Send Interview Invitations")
            print("5. Run Recruitment Workflow")
            print("6. Project Information")
            print("7. Exit")

            choice = input("\nSelect an option (1-7): ").strip()

            if choice == "1":

                generate_fake_applications()

            elif choice == "2":

                process_gmail()

            elif choice == "3":

                schedule_interviews()

            elif choice == "4":

                send_invitations()

            elif choice == "5":

                run_workflow()

            elif choice == "6":

                project_information()

            elif choice == "7":

                print("\nThank you for using")
                print(PROJECT_NAME)
                print("Goodbye!\n")
                break

            else:

                print("\nInvalid option.")
                pause()

        except FileNotFoundError as error:

            print("\nERROR")
            print("-" * 40)
            print(error)
            pause()

        except subprocess.CalledProcessError as error:

            print("\nWORKFLOW STOPPED")
            print("-" * 40)
            print("A module returned an error.")
            print(error)
            pause()

        except KeyboardInterrupt:

            print("\n\nOperation cancelled by user.")
            break

        except Exception as error:

            print("\nUNEXPECTED ERROR")
            print("-" * 40)
            print(error)
            pause()


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    main()

# =========================================================
# ===== END OF FILE =====
# =========================================================
