from datetime import date

from googleapiclient.discovery import build

from src.get_credentials import get_credentials

CALENDAR_ID = "c_f58feee0d9e6431c68333c9340043eeea6484f4dfa17d948dff46d1dc7c2493b@group.calendar.google.com"


def create_event(summary: str, date: date) -> dict:
    service = build("calendar", "v3", credentials=get_credentials())

    event = {
        "summary": summary,
        "start": {
            "date": date.isoformat(),
            "timeZone": "Europe/Madrid",
        },
        "end": {
            "date": date.isoformat(),
            "timeZone": "Europe/Madrid",
        },
    }

    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return event
