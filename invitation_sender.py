import base64

import pandas as pd

from datetime import datetime

from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

print("Invitation Sender Started\n")

# =====================================
# AUTHENTICATION
# =====================================

creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

gmail_service = build(
    "gmail",
    "v1",
    credentials=creds
)

# =====================================
# READ EXCEL
# =====================================

df = pd.read_excel(
    "gmail_candidates.xlsx"
)

# =====================================
# CREATE REQUIRED COLUMNS
# =====================================

required_columns = [
    "Invitation_Status",
    "Invitation_Sent_Date"
]

for col in required_columns:

    if col not in df.columns:

        df[col] = ""

    df[col] = (
        df[col]
        .fillna("")
        .astype(str)
    )

# =====================================
# SUMMARY COUNTERS
# =====================================

total_candidates = len(df)

sent_count = 0

skipped_count = 0

error_count = 0

# =====================================
# SEND INVITATIONS
# =====================================

for index, row in df.iterrows():

    calendar_status = str(
        row.get(
            "Calendar_Status",
            ""
        )
    ).strip()

    invitation_status = str(
        row.get(
            "Invitation_Status",
            ""
        )
    ).strip()

    candidate_name = str(
        row.get(
            "Candidate_Name",
            ""
        )
    )

    candidate_email = str(
        row.get(
            "Email",
            ""
        )
    )

    position = str(
        row.get(
            "Position",
            ""
        )
    )

    interview_date = str(
        row.get(
            "Interview_Date",
            ""
        )
    )

    interview_time = str(
        row.get(
            "Interview_Time",
            ""
        )
    )

    # =====================================
    # ONLY SCHEDULED CANDIDATES
    # =====================================

    if calendar_status != "Scheduled":

        continue

    # =====================================
    # PREVENT DUPLICATE EMAILS
    # =====================================

    if invitation_status == "Sent":

        skipped_count += 1

        print(
            f"Skipping invitation for "
            f"{candidate_name}"
        )

        continue

    subject = "Interview Invitation"

    body = f"""Hello {candidate_name},

Congratulations.

Your interview has been scheduled.

Position: {position}

Interview Date:
{interview_date}

Interview Time:
{interview_time}

Please arrive 10 minutes before the interview.

Good luck.

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

            body={
                "raw": raw_message
            }

        ).execute()

        sent_count += 1

        df.at[
            index,
            "Invitation_Status"
        ] = "Sent"

        df.at[
            index,
            "Invitation_Sent_Date"
        ] = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

        print(
            f"Invitation sent to "
            f"{candidate_name}"
        )

    except Exception as e:

        error_count += 1

        print(
            f"Error sending invitation "
            f"to {candidate_name}"
        )

        print(e)

# =====================================
# SAVE UPDATED EXCEL
# =====================================

df.to_excel(
    "gmail_candidates.xlsx",
    index=False
)

# =====================================
# PRINT SUMMARY
# =====================================

print()

print("========================")
print("Invitation Sender Completed")
print("========================")

print(
    f"Total Candidates: "
    f"{total_candidates}"
)

print(
    f"Invitations Sent: "
    f"{sent_count}"
)
print(
    f"Skipped Invitations: "
    f"{skipped_count}"
)

print(
    f"Errors: "
    f"{error_count}"
)

print()

print("Updated File")

print(
    "- gmail_candidates.xlsx"
)

print()

print("Invitation Sender Finished Successfully")
