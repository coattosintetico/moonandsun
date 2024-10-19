from .create_event import create_event
from .get_moon_phases import get_next_moon_phases


def main():
    # 1. get the dates for the next moon phases
    phases = get_next_moon_phases()

    # 2. create an event for each moon phase
    for phase, date in phases.items():
        create_event(phase, date)
        print(f"Created event: {phase} on {date}")


if __name__ == "__main__":
    main()
