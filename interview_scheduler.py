import pandas as pd

from datetime import datetime, timedelta

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]

print("Interview Scheduler Started\n")

# Connect to Google Calendar

creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

calendar_service = build(
    "calendar",
    "v3",
    credentials=creds
)

# Read candidate file

df = pd.read_excel("gmail_candidates.xlsx")

# Select candidates with Score >= 80

interview_candidates = df[df["Score"] >= 80].copy()

print(f"Candidates selected for interview: {len(interview_candidates)}")

# Tomorrow at 09:00

tomorrow = datetime.now() + timedelta(days=1)

start_time = tomorrow.replace(
    hour=9,
    minute=0,
    second=0,
    microsecond=0
)

event_links = []

for index, row in interview_candidates.iterrows():

    end_time = start_time + timedelta(minutes=30)

    event = {
        "summary": f"Interview - {row['Candidate_Name']}",
        "description":
            f"Position: {row['Position']}\n"
            f"Score: {row['Score']}",

        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Asia/Jerusalem"
        },

        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Asia/Jerusalem"
        }
    }

    created_event = calendar_service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    event_links.append(created_event["htmlLink"])

    print(
        f"Interview created for "
        f"{row['Candidate_Name']}"
    )

    start_time = end_time

interview_candidates["Calendar_Event"] = event_links

interview_candidates.to_excel(
    "interview_candidates.xlsx",
    index=False
)

print("\n========================")
print("PROCESS COMPLETED")
print("========================")
print(
    f"Interviews Created: {len(interview_candidates)}"
)
print("interview_candidates.xlsx created")