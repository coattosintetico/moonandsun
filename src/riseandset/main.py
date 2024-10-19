import sys
from datetime import datetime, timedelta

from .create_event import create_event
from .get_sunrise_and_sunset import get_sunrise_sunset

EVENT_DURATION_MINUTES = 15
SUNRISE_EVENT_SUMMARY = "rise"
SUNSET_EVENT_SUMMARY = "set"


def main():
    # 1. Ask for start and end dates as user input
    start_date_str = input("start date (YYYY-MM-DD): ")
    end_date_str = input("  end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # 2. get the sunrise and sunset for each date
    current_date = start_date
    while current_date <= end_date:
        sunrise, sunset = get_sunrise_sunset(current_date)

        # 3. create an event for each sunrise and sunset
        sunrise_end = sunrise + timedelta(minutes=EVENT_DURATION_MINUTES)
        sunset_end = sunset + timedelta(minutes=EVENT_DURATION_MINUTES)

        sunrise_event = create_event(SUNRISE_EVENT_SUMMARY, sunrise, sunrise_end)
        print(f"Created event: {sunrise_event['summary']} - Start: {sunrise_event['start']['dateTime']}")

        sunset_event = create_event(SUNSET_EVENT_SUMMARY, sunset, sunset_end)
        print(f"Created event: {sunset_event['summary']} - Start: {sunset_event['start']['dateTime']}")


        current_date += timedelta(days=1)


if __name__ == "__main__":
    main()
