import base64
import json
from datetime import datetime

import anthropic
import pandas as pd

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

# =====================================
# ANTHROPIC CLIENT
# =====================================

ANTHROPIC_API_KEY = "YOUR_API_KEY_HERE"

anthropic_client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY
)

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
# EXTRACT CANDIDATE INFO USING CLAUDE
# =====================================

def extract_candidate_info(email_body, email_subject):

    prompt = f"""You are a recruitment assistant.
Analyze the following job application email and extract candidate information.

Email Subject: {email_subject}

Email Body:
{email_body}

Extract the following information and return ONLY a JSON object with these exact fields:
- candidate_name: full name of the candidate
- candidate_email: email address of the candidate
- position: job position applied for
- region: geographic region or location mentioned
- experience: number of years of experience (number only, e.g. "5")
- education: highest education level (BA, MA, PhD, or Other)
- skills: comma-separated list of technical skills mentioned

If any field cannot be found, use an empty string "".

Return ONLY the JSON object, no other text."""

    try:

        message = anthropic_client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_text = message.content[0].text.strip()

        response_text = response_text.replace(
            "```json", ""
        ).replace(
            "```", ""
        ).strip()

        candidate_data = json.loads(response_text)

        return candidate_data

    except Exception as e:

        print(f"Claude extraction error: {e}")

        return None


# =====================================
# MARK EMAIL AS READ
# =====================================

def mark_as_read(message_id):

    try:

        gmail_service.users().messages().modify(
            userId="me",
            id=message_id,
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

    except Exception as e:

        print(f"Error marking email as read: {e}")


# =====================================
# GET UNREAD EMAILS ONLY
# =====================================

results = []

messages = gmail_service.users().messages().list(
    userId="me",
    maxResults=50,
    q="is:unread"
).execute()

message_list = messages.get("messages", [])

print(f"Unread messages found : {len(message_list)}")
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
    # SKIP NON-APPLICATION EMAILS
    # =====================================

    application_keywords = [
        "application",
        "applying",
        "position",
        "candidate",
        "resume",
        "cv",
        "job",
        "interest",
        "opening"
    ]

    subject_lower = subject.lower()
    body_lower = body.lower()

    is_application = any(
        keyword in subject_lower or keyword in body_lower
        for keyword in application_keywords
    )

    if not is_application:
        mark_as_read(item["id"])
        continue

    if not body.strip():
        mark_as_read(item["id"])
        continue

    # =====================================
    # EXTRACT USING CLAUDE
    # =====================================

    print(f"Analyzing email: {subject[:50]}...")

    candidate_data = extract_candidate_info(
        body,
        subject
    )

    if candidate_data is None:
        continue

    candidate_name = str(
        candidate_data.get("candidate_name", "")
    ).strip()

    candidate_email = str(
        candidate_data.get("candidate_email", "")
    ).strip()

    position = str(
        candidate_data.get("position", "")
    ).strip()

    region = str(
        candidate_data.get("region", "")
    ).strip()

    experience = str(
        candidate_data.get("experience", "")
    ).strip()

    education = str(
        candidate_data.get("education", "")
    ).strip()

    skills = str(
        candidate_data.get("skills", "")
    ).strip()

    if candidate_name == "":
        mark_as_read(item["id"])
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
    # MARK EMAIL AS READ
    # =====================================

    mark_as_read(item["id"])
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
