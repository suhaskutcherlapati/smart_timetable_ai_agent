from .auth import get_calendar_service

def create_event(summary, start_time, end_time):

    service = get_calendar_service()

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata'
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata'
        }
    }

    event = service.events().insert(
        calendarId='primary',
        body=event
    ).execute()

    return event.get('htmlLink')