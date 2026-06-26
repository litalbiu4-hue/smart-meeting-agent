import re
import base64
from datetime import datetime

import pandas as pd

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

print("=" * 60)
print("SMART RECRUITMENT AGENT")
print("=" * 60)
print("Recruitment Agent Started...\n")

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
# GET EMAILS
# =====================================

results = []

messages = gmail_service.users().messages().list(
    userId="me",
    maxResults=50
).execute()

message_list = messages.get("messages", [])

print(f"Messages downloaded : {len(message_list)}")
print("-" * 60)

candidate_counter = 1
processed_counter = 0

# =====================================
# PROCESS EMAILS
# =====================================

for item in message_list:

    msg = gmail_service.users().messages().get(
        userId="me",
        id=item["id"],
        format="full"
    ).execute()

    payload = msg.get("payload", {})
    headers = payload.get("headers", [])

    subject = ""

    for h in headers:

        if h["name"] == "Subject":

            subject = h["value"]

    body = ""

    if "parts" in payload:

        for part in payload["parts"]:

            if part.get("mimeType") == "text/plain":

                data = part["body"].get("data")

                if data:

                    body = base64.urlsafe_b64decode(
                        data
                    ).decode(
                        "utf-8",
                        errors="ignore"
                    )

    else:

        data = payload.get(
            "body",
            {}
        ).get(
            "data"
        )

        if data:

            body = base64.urlsafe_b64decode(
                data
            ).decode(
                "utf-8",
                errors="ignore"
            )

    # =====================================
    # EXTRACT FIELDS
    # =====================================

    def extract(pattern):

        match = re.search(
            pattern,
            body,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

        return ""

    candidate_name = extract(
        r"Candidate Name:\s*(.*)"
    )

    candidate_email = extract(
        r"Email:\s*(.*)"
    )

    position = extract(
        r"Position:\s*(.*)"
    )

    region = extract(
        r"Region:\s*(.*)"
    )

    experience = extract(
        r"Experience:\s*(.*)"
    )

    education = extract(
        r"Education:\s*(.*)"
    )

    skills = extract(
        r"Skills:\s*(.*)"
    )

    if candidate_name == "":
        continue

    processed_counter += 1

    print(f"Processing Candidate #{processed_counter}")
    print(f"Name  : {candidate_name}")
    print(f"Email : {candidate_email}")

    # =====================================
    # SCORE
    # =====================================

    score = 0

    try:

        exp = float(experience)

    except:

        exp = 0

    if exp >= 8:
        score += 60

    elif exp >= 5:
        score += 50

    elif exp >= 3:
        score += 30

    else:
        score += 10

    if education.upper() == "MA":
        score += 30

    elif education.upper() == "BA":
        score += 20

    skills_lower = skills.lower()

    if "python" in skills_lower:
        score += 10

    if "power bi" in skills_lower:
        score += 10

    if "excel" in skills_lower:
        score += 5

    if score >= 80:
        status = "High Priority"

    elif score >= 60:
        status = "Interview"

    else:
        status = "Review"

    candidate_id = f"CAND-{candidate_counter:04d}"
    candidate_counter += 1

    interview_date = ""
    interview_time = ""

    calendar_status = "Pending"
    invitation_status = "Pending"

    print(f"Score : {score}")
    print(f"Status: {status}")
    print("-" * 60)
    results.append({

        "Candidate_ID": candidate_id,

        "Candidate_Name": candidate_name,

        "Email": candidate_email,

        "Position": position,

        "Region": region,

        "Experience": experience,

        "Education": education,

        "Skills": skills,

        "Score": score,

        "Status": status,

        "Interview_Date": interview_date,

        "Interview_Time": interview_time,

        "Calendar_Status": calendar_status,

        "Invitation_Status": invitation_status

    })

# =====================================
# EMAIL SCAN COMPLETED
# =====================================

print("\nEmail scan completed.")
print(f"Processed Candidates : {processed_counter}")
print("-" * 60)

# =====================================
# CREATE DATAFRAME
# =====================================

df = pd.DataFrame(results)

# =====================================
# REMOVE DUPLICATES
# =====================================

before_duplicates = len(df)

df = df.drop_duplicates(
    subset="Email",
    keep="first"
)

duplicates_removed = before_duplicates - len(df)

# =====================================
# SORT RESULTS
# =====================================

df = df.sort_values(
    by="Score",
    ascending=False
).reset_index(drop=True)

print(f"Duplicate Emails Removed : {duplicates_removed}")
print(f"Final Candidates         : {len(df)}")
print("-" * 60)

# =====================================
# SAVE EXCEL
# =====================================

df.to_excel(
    "gmail_candidates.xlsx",
    index=False
)

# =====================================
# PREPARE SUMMARY STATISTICS
# =====================================

high_priority = len(
    df[df["Status"] == "High Priority"]
)

interview = len(
    df[df["Status"] == "Interview"]
)

review = len(
    df[df["Status"] == "Review"]
)
# =====================================
# CREATE SUMMARY FILE
# =====================================

with open(
    "gmail_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("=" * 50 + "\n")
    f.write("SMART RECRUITMENT AGENT SUMMARY\n")
    f.write("=" * 50 + "\n\n")

    f.write(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    )

    f.write(
        f"Candidates Found : {len(df)}\n"
    )

    f.write(
        f"Duplicate Emails Removed : {duplicates_removed}\n"
    )

    if len(df) > 0:

        f.write(
            f"Highest Score : {df['Score'].max()}\n"
        )

        f.write(
            f"Average Score : {df['Score'].mean():.1f}\n\n"
        )

    else:

        f.write("Highest Score : 0\n")
        f.write("Average Score : 0\n\n")

    f.write("STATUS SUMMARY\n")
    f.write("------------------------------\n")

    f.write(
        f"High Priority : {high_priority}\n"
    )

    f.write(
        f"Interview     : {interview}\n"
    )

    f.write(
        f"Review        : {review}\n\n"
    )

    f.write("FILES CREATED\n")
    f.write("------------------------------\n")

    f.write("gmail_candidates.xlsx\n")
    f.write("gmail_summary.txt\n")

# =====================================
# FINAL CONSOLE OUTPUT
# =====================================

print()

print("=" * 60)
print("SMART RECRUITMENT AGENT COMPLETED")
print("=" * 60)

print(f"Messages Read            : {len(message_list)}")
print(f"Candidates Processed     : {processed_counter}")
print(f"Duplicate Emails Removed : {duplicates_removed}")
print(f"Final Candidates         : {len(df)}")

print("-" * 60)

print(f"High Priority : {high_priority}")
print(f"Interview     : {interview}")
print(f"Review        : {review}")

print("-" * 60)

print("Generated Files")

print("✓ gmail_candidates.xlsx")
print("✓ gmail_summary.txt")

print("=" * 60)
print("Recruitment Agent Finished Successfully")
print("=" * 60)