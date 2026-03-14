from .auth import get_calendar_service
from datetime import datetime

def get_events():

    service = get_calendar_service()

    now = datetime.utcnow().isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    results = []

    for event in events:
        start = event['start'].get('dateTime')
        results.append(f"{event['summary']} at {start}")

    return results