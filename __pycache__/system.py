from datetime import datetime
import platform

try:
    import psutil
except ImportError:
    psutil = None


def get_time():
    """Return current time."""
    return datetime.now().strftime("%I:%M %p")


def get_date():
    """Return today's date."""
    return datetime.now().strftime("%A, %d %B %Y")


def battery_status():
    """
    Returns a human-readable battery status.
    Requires: pip install psutil
    """
    if psutil is None:
        return "Battery information is unavailable. Install psutil."

    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information is not available on this device."

    percent = battery.percent
    charging = battery.power_plugged

    if charging:
        return f"Battery is {percent}% and charging."
    else:
        return f"Battery is {percent}% and not charging."


def system_info():
    """Basic operating system information."""
    return (
        f"System: {platform.system()}\n"
        f"Release: {platform.release()}\n"
        f"Machine: {platform.machine()}\n"
        f"Processor: {platform.processor()}"
    )
