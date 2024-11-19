"""Utility functions for time management in the digital clock."""
import time


def get_current_time():
    """
    Returns the current time formatted for a 12-hour clock.

    :return: A tuple of strings (hours, minutes, seconds).
    """
    current_time = time.localtime()
    hours = str(current_time.tm_hour % 12)
    if hours == "0":
        hours = "12"  # 12-hour clocks show 12:00 instead of 00:00.
    minutes = str(current_time.tm_min)
    seconds = str(current_time.tm_sec)
    return hours, minutes, seconds
