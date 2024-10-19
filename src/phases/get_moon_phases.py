from datetime import date, datetime
from zoneinfo import ZoneInfo

import ephem


def get_next_moon_phases() -> dict[str, date]:
    """
    Returns the dates of the next major moon phases from the current datetime in Madrid timezone.

    Returns:
        dict: A dictionary with moon phases as keys and their corresponding date objects.
    """
    # Define the moon phases and their corresponding ephem methods
    phases = {
        "🌑": ephem.next_new_moon,
        "🌓": ephem.next_first_quarter_moon,
        "🌕": ephem.next_full_moon,
        "🌗": ephem.next_last_quarter_moon,
    }

    # Get the current datetime in Madrid timezone
    madrid_tz = ZoneInfo("Europe/Madrid")
    now = datetime.now(madrid_tz)

    moon_phases_dates = {}

    for phase, phase_method in phases.items():
        # Find the next occurrence of the phase using the specific method
        phase_date = phase_method(ephem.Date(now))
        phase_datetime = ephem.localtime(phase_date)

        # Convert to date object (year, month, day only)
        phase_date = date(phase_datetime.year, phase_datetime.month, phase_datetime.day)

        moon_phases_dates[phase] = phase_date

    return moon_phases_dates
