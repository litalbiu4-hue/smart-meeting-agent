import pandas as pd

from datetime import datetime, timedelta

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/calendar"
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

pending_count = 0

# =====================================
# START TIME
# =====================================

tomorrow = datetime.now() + timedelta(days=1)

start_time = tomorrow.replace(
    hour=9,
    minute=0,
    second=0,
    microsecond=0
)

saved_rows = []

event_links = []

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

    end_time = start_time + timedelta(
        minutes=30
    )

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

    start_time = end_time

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