from datetime import date, datetime

import pytz
from astral import LocationInfo
from astral.sun import sun


def get_sunrise_sunset(input_date: date) -> tuple[datetime, datetime]:
    """
    Retrieves the sunrise and sunset times for Madrid on the specified date.

    Args:
        input_date (date): The date for which to retrieve sunrise and sunset times.

    Returns:
        tuple: A tuple containing sunrise and sunset as datetime objects in Madrid's timezone.
    """
    # Define the location for Madrid
    madrid = LocationInfo("Madrid", "Spain")

    # Get Madrid's timezone
    tz = pytz.timezone(madrid.timezone)

    # Create a datetime object at midnight for the input date in Madrid's timezone
    date = tz.localize(datetime.combine(input_date, datetime.min.time()))

    # Calculate sunrise and sunset times
    s = sun(madrid.observer, date=date, tzinfo=tz)
    sunrise = s["sunrise"]
    sunset = s["sunset"]

    return (sunrise, sunset)
