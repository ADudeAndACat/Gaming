from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

def convert_time(time_str):
    """
    Convert a time string in "HH:MM" format to different timezones.
    Returns a dictionary of timezone conversions.
    """
    try:
        # Parse the input time
        hour, minute = map(int, time_str.split(':'))
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError("Invalid time format")

        # Get current date and combine with input time
        current = datetime.now()
        input_time = datetime.combine(current.date(), datetime.strptime(time_str, "%H:%M").time())
        
        # Get current timezone
        local_tz = datetime.now().astimezone().tzinfo
        input_time = input_time.replace(tzinfo=local_tz)

        # List of major timezones to convert to
        major_timezones = [
            "US/Central",          # Central Time
            "US/Eastern",          # Eastern Time
            "Europe/London",       # UK
            "Europe/Sofia",        # Bulgaria
            "UTC"                  # UTC
        ]

        # Convert to each timezone
        conversions = {}
        for tz_name in major_timezones:
            tz = ZoneInfo(tz_name)
            converted_time = input_time.astimezone(tz)
            conversions[tz_name] = converted_time.strftime("%H:%M")

        return conversions

    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def show_times(time_str):
    """
    Display the time conversions in a formatted way.
    """
    result = convert_time(time_str)
    if isinstance(result, str):  # Error occurred
        print(result)
        return

    print(f"\nTime Conversions for {time_str}")
    print("-" * 32)
    for tz, time in result.items():
        # Format timezone name for better readability
        tz_display = tz.replace("_", " ").split("/")[-1]
        print(f"{tz_display:<15} : {time}")

if __name__ == "__main__":
    # Example usage
    time_input = input("Enter time in 24-hour format (HH:MM): ")
    show_times(time_input)
