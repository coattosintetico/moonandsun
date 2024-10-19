from datetime import datetime

from googleapiclient.discovery import build

from ..get_credentials import get_credentials

CALENDAR_ID = "c_f58feee0d9e6431c68333c9340043eeea6484f4dfa17d948dff46d1dc7c2493b@group.calendar.google.com"


def create_event(summary: str, start_time: datetime, end_time: datetime) -> dict:
    service = build("calendar", "v3", credentials=get_credentials())

    event = {
        "summary": summary,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Europe/Madrid",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Europe/Madrid",
        },
    }

    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return event
