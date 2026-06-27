import pandas as pd

from datetime import datetime, timedelta, timezone

from email.mime.text import MIMEText
import base64

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send"
]

print("Interview Scheduler Started\n")

# =====================================
# CONNECT TO GOOGLE CALENDAR
# =====================================

creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

calendar_service = build(
    "calendar",
    "v3",
    credentials=creds
)

gmail_service = build(
    "gmail",
    "v1",
    credentials=creds
)

# =====================================
# READ CANDIDATE FILE
# =====================================

df = pd.read_excel("gmail_candidates.xlsx")

# =====================================
# CREATE NEW COLUMNS IF NEEDED
# =====================================

required_columns = [
    "Interview_Date",
    "Interview_Time",
    "Calendar_Status",
    "Calendar_Event"
]

for col in required_columns:

    if col not in df.columns:
        df[col] = ""

    # Prevent pandas dtype errors
    df[col] = (
        df[col]
        .fillna("")
        .astype(str)
    )

# =====================================
# SELECT CANDIDATES
# KEEP ORIGINAL LOGIC
# =====================================

interview_candidates = df[
    df["Score"] >= 80
].copy()

print(
    f"Candidates selected for interview: "
    f"{len(interview_candidates)}"
)

# =====================================
# SUMMARY COUNTERS
# =====================================

total_candidates = len(df)

eligible_candidates = len(interview_candidates)

created_count = 0

skipped_count = 0

conflict_count = 0

pending_count = 0

# =====================================
# START TIME
# AT LEAST 7 DAYS FROM NOW
# SKIP FRIDAY (4) AND SATURDAY (5)
# =====================================

next_week = datetime.now() + timedelta(days=7)

next_week = next_week.replace(
    hour=9,
    minute=0,
    second=0,
    microsecond=0
)

while next_week.weekday() in (4, 5):
    next_week += timedelta(days=1)

start_time = next_week

# TEMP DEBUG - REMOVE AFTER TESTING
print(f"First interview slot: {start_time.strftime('%Y-%m-%d %H:%M %A')}")

saved_rows = []

event_links = []

# =====================================
# SKIP WEEKENDS FUNCTION
# =====================================

def next_working_slot(current_time):

    next_slot = current_time + timedelta(minutes=30)

    if next_slot.hour >= 17:

        next_slot = next_slot.replace(
            hour=9,
            minute=0,
            second=0,
            microsecond=0
        ) + timedelta(days=1)

    while next_slot.weekday() in (4, 5):
        next_slot += timedelta(days=1)

    return next_slot


# =====================================
# CHECK CALENDAR AVAILABILITY
# =====================================

def is_time_slot_available(start, end):

    tz_israel = timezone(timedelta(hours=3))

    start_aware = start.astimezone(tz_israel)
    end_aware = end.astimezone(tz_israel)

    time_min = start_aware.isoformat()
    time_max = end_aware.isoformat()

    events_result = calendar_service.events().list(
        calendarId="primary",
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    return len(events) == 0


# =====================================
# SEND CONFLICT EMAIL
# =====================================

def send_conflict_email(candidate_name, candidate_email, position):

    subject = "Interview Scheduling Update"

    body = f"""Hello {candidate_name},

Thank you for your application for the {position} position.

Unfortunately, we were unable to schedule your interview
at the requested time due to a calendar conflict.

Our HR team will contact you shortly to arrange
an alternative interview time.

We apologize for any inconvenience.

HR Department
"""

    message = MIMEText(body)

    message["To"] = candidate_email

    message["Subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    try:

        gmail_service.users().messages().send(
            userId="me",
            body={"raw": raw_message}
        ).execute()

        print(
            f"Conflict email sent to "
            f"{candidate_name}"
        )

    except Exception as e:

        print(
            f"Error sending conflict email "
            f"to {candidate_name}"
        )

        print(e)
# =====================================
# CREATE INTERVIEWS
# =====================================

for index, row in interview_candidates.iterrows():

    status = str(
        row.get(
            "Calendar_Status",
            ""
        )
    ).strip().lower()

    if status == "scheduled":

        skipped_count += 1

        print(
            f"Skipping "
            f"{row['Candidate_Name']} "
            f"(already scheduled)"
        )

        saved_rows.append(row)

        event_links.append(
            row.get(
                "Calendar_Event",
                ""
            )
        )

        continue

    if status == "conflict":

        conflict_count += 1

        print(
            f"Skipping "
            f"{row['Candidate_Name']} "
            f"(conflict already recorded)"
        )

        saved_rows.append(row)

        event_links.append("")

        continue

    end_time = start_time + timedelta(
        minutes=30
    )

    # =====================================
    # CHECK AVAILABILITY
    # =====================================

    slot_available = is_time_slot_available(
        start_time,
        end_time
    )

    if not slot_available:

        conflict_count += 1

        candidate_name = str(
            row.get("Candidate_Name", "")
        )

        candidate_email = str(
            row.get("Email", "")
        )

        position = str(
            row.get("Position", "")
        )

        print(
            f"Calendar conflict for "
            f"{candidate_name} "
            f"at {start_time.strftime('%Y-%m-%d %H:%M')}"
        )

        send_conflict_email(
            candidate_name,
            candidate_email,
            position
        )

        df.at[index, "Calendar_Status"] = "Conflict"
        df.at[index, "Interview_Date"] = ""
        df.at[index, "Interview_Time"] = ""
        df.at[index, "Calendar_Event"] = ""

        row["Calendar_Status"] = "Conflict"
        row["Interview_Date"] = ""
        row["Interview_Time"] = ""
        row["Calendar_Event"] = ""

        saved_rows.append(row)

        event_links.append("")

        start_time = next_working_slot(start_time)

        continue

    event = {

        "summary":
            f"Interview - {row['Candidate_Name']}",

        "description":
            f"Position: {row['Position']}\n"
            f"Score: {row['Score']}",

        "start": {

            "dateTime":
                start_time.isoformat(),

            "timeZone":
                "Asia/Jerusalem"

        },

        "end": {

            "dateTime":
                end_time.isoformat(),

            "timeZone":
                "Asia/Jerusalem"

        }

    }

    created_event = calendar_service.events().insert(

        calendarId="primary",

        body=event

    ).execute()

    created_count += 1

    event_link = created_event["htmlLink"]

    interview_date = start_time.strftime(
        "%Y-%m-%d"
    )

    interview_time = start_time.strftime(
        "%H:%M"
    )

    # =====================================
    # UPDATE ORIGINAL DATAFRAME
    # =====================================

    df.at[index, "Interview_Date"] = interview_date

    df.at[index, "Interview_Time"] = interview_time

    df.at[index, "Calendar_Status"] = "Scheduled"

    df.at[index, "Calendar_Event"] = event_link

    # =====================================
    # UPDATE COPY FOR OUTPUT FILE
    # =====================================

    row["Interview_Date"] = interview_date

    row["Interview_Time"] = interview_time

    row["Calendar_Status"] = "Scheduled"

    row["Calendar_Event"] = event_link

    saved_rows.append(row)

    event_links.append(event_link)

    print(
        f"Interview created for "
        f"{row['Candidate_Name']}"
    )

    start_time = next_working_slot(start_time)

# =====================================
# BUILD INTERVIEW FILE
# =====================================

if len(saved_rows) > 0:

    interview_candidates = pd.DataFrame(
        saved_rows
    )

    interview_candidates = interview_candidates.sort_values(
        by="Score",
        ascending=False
    )

else:

    interview_candidates = pd.DataFrame(
        columns=df.columns
    )

# =====================================
# SAVE INTERVIEW FILE
# =====================================

interview_candidates.to_excel(
    "interview_candidates.xlsx",
    index=False
)

# =====================================
# SAVE UPDATED GMAIL CANDIDATES
# =====================================

df.to_excel(
    "gmail_candidates.xlsx",
    index=False
)

# =====================================
# CALCULATE SUMMARY
# =====================================

pending_count = (
    eligible_candidates
    - created_count
    - skipped_count
    - conflict_count
)

# =====================================
# PRINT SUMMARY
# =====================================

print("\n========================")
print("PROCESS COMPLETED")
print("========================")

print(
    f"Total Candidates: "
    f"{total_candidates}"
)

print(
    f"Eligible Candidates: "
    f"{eligible_candidates}"
)

print(
    f"Interviews Created: "
    f"{created_count}"
)

print(
    f"Skipped Candidates: "
    f"{skipped_count}"
)

print(
    f"Calendar Conflicts: "
    f"{conflict_count}"
)

print(
    f"Pending Candidates: "
    f"{pending_count}"
)

print()

print("Files Created / Updated")

print(
    "- gmail_candidates.xlsx"
)

print(
    "- interview_candidates.xlsx"
)
