"""
Utility functions for handling time conversions.
"""


def time_to_minutes(time_value):
    """
    Convert HH:MM:SS into total minutes.

    Example:
        00:31:00 -> 31
        01:45:00 -> 105
    """

    hours = time_value.hour
    minutes = time_value.minute

    total_minutes = (hours * 60) + minutes

    return total_minutes