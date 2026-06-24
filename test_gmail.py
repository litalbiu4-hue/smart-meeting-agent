from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/calendar"
]

creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

service = build("gmail", "v1", credentials=creds)

profile = service.users().getProfile(userId="me").execute()

print("Connected!")
print("Email:", profile["emailAddress"])
print("Messages:", profile["messagesTotal"])