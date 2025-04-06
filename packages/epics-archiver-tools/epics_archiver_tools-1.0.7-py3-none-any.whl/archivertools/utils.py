"""Utility functions for timezone conversion in the EPICS archiver tools.

This module provides functions for converting datetime objects between UTC and PST timezones,
which is essential for proper interaction with the EPICS archiver.

Author: Andrea Pollastro - apollastro@lbl.gov
Date: 04/19/2023
Python version: 3.10.8
"""
from datetime import datetime
import pytz

def to_UTC(datetime_obj: datetime, tznaive: bool) -> datetime:
    """Convert a datetime object to UTC timezone.

    This function handles timezone conversion to UTC, with special handling for naive
    datetime objects (assumed to be in US/Pacific timezone).

    Args:
        datetime_obj (datetime): The datetime object to convert. If naive (no timezone
            information), it will be treated as US/Pacific time without affecting the
            actual timestamp.
        tznaive (bool): If True, returns a naive datetime object (without timezone
            information). If False, returns a timezone-aware datetime object.

    Returns:
        datetime: The input datetime converted to UTC timezone.

    Example:
        >>> from datetime import datetime
        >>> dt = datetime(2023, 4, 25, 12, 0)  # Naive datetime
        >>> utc_dt = to_UTC(dt, tznaive=False)  # Returns timezone-aware UTC datetime
    """
    if datetime_obj.tzinfo is None:
        datetime_obj.replace(tzinfo=pytz.timezone('US/Pacific'))
    datetime_obj = datetime_obj.astimezone(pytz.utc)
    if tznaive:
        datetime_obj = datetime_obj.replace(tzinfo=None)

    return datetime_obj

def to_PST(datetime_obj: datetime, tznaive: bool) -> datetime:
    """Convert a datetime object to US/Pacific timezone.

    This function handles timezone conversion to US/Pacific time, with special handling
    for naive datetime objects (assumed to be in UTC timezone).

    Args:
        datetime_obj (datetime): The datetime object to convert. If naive (no timezone
            information), it will be treated as UTC time without affecting the actual
            timestamp.
        tznaive (bool): If True, returns a naive datetime object (without timezone
            information). If False, returns a timezone-aware datetime object.

    Returns:
        datetime: The input datetime converted to US/Pacific timezone.

    Example:
        >>> from datetime import datetime
        >>> dt = datetime(2023, 4, 25, 12, 0)  # Naive datetime
        >>> pst_dt = to_PST(dt, tznaive=False)  # Returns timezone-aware PST datetime
    """
    if datetime_obj.tzinfo is None:
        datetime_obj.replace(tzinfo=pytz.utc)
    datetime_obj = datetime_obj.astimezone(pytz.timezone('US/Pacific'))
    if tznaive:
        datetime_obj = datetime_obj.replace(tzinfo=None)

    return datetime_obj