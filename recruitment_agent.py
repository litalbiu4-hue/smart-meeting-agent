import re
import pandas as pd
import base64

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

print("Recruitment Agent Started")

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

print(f"Found {len(message_list)} messages")

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

    results.append({

        "Candidate_Name": candidate_name,
        "Email": candidate_email,
        "Position": position,
        "Region": region,
        "Experience": experience,
        "Education": education,
        "Skills": skills,
        "Score": score,
        "Status": status

    })

# =====================================
# SAVE RESULTS
# =====================================

df = pd.DataFrame(results)

df = df.sort_values(
    by="Score",
    ascending=False
)

df.to_excel(
    "gmail_candidates.xlsx",
    index=False
)

with open(
    "gmail_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        f"Candidates Found: {len(df)}\n"
    )

    f.write(
        f"Highest Score: {df['Score'].max()}\n"
    )

    f.write(
        f"Average Score: {df['Score'].mean():.1f}\n"
    )

print("\n====================")
print("PROCESS COMPLETED")
print("====================")

print(
    f"Candidates Found: {len(df)}"
)

print(
    "Created:"
)

print(
    "gmail_candidates.xlsx"
)

print(
    "gmail_summary.txt"
)