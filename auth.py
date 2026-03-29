import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_calendar_service():
    creds = None

    # project root folder
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    credentials_path = os.path.join(BASE_DIR, "credentials.json")
    token_path = os.path.join(BASE_DIR, "token.json")

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path):
                raise FileNotFoundError(
                    f"credentials.json not found. Put it here: {credentials_path}"
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path,
                SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(token_path, "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    return service
