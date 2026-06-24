import pandas as pd
import base64

from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

print("Starting Fake Mail Generator")

# Authentication
creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

gmail_service = build(
    "gmail",
    "v1",
    credentials=creds
)

# Read candidates
df = pd.read_excel("candidates.xlsx")

print(f"Found {len(df)} candidates")

sent_count = 0

# Send emails
for _, row in df.iterrows():

    candidate_name = str(row["Full_Name"])
    candidate_email = str(row["Email"])
    position = str(row["Position"])
    region = str(row["Region"])
    experience = str(row["Experience_Years"])
    education = str(row["Education"])
    skills = str(row["Skills"])

    subject = f"Application for {position}"

    body = f"""
Candidate Name: {candidate_name}

Email: {candidate_email}

Position: {position}

Region: {region}

Experience: {experience}

Education: {education}

Skills: {skills}

I would like to apply for this position.

Regards,
{candidate_name}
"""

    message = MIMEText(body)

    message["to"] = "litalbiu4@gmail.com"
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    gmail_service.users().messages().send(
        userId="me",
        body={"raw": raw_message}
    ).execute()

    sent_count += 1

    print(f"Sent {sent_count}: {candidate_name}")

print("\n========================")
print("PROCESS COMPLETED")
print("========================")
print(f"Emails Sent: {sent_count}")