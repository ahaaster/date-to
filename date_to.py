"""A handy python function to parse and convert to and between datetime.datetime, int, and string objects"""
__version__ = "1.0b1"

import math
import datetime
from dateparser import parse


DateTypes = str | int | float | datetime.date
TIMESTAMP_DIGITS = 10
DEFAULT_SETTINGS = {
    "TIMEZONE": "UTC",
    "PREFER_DAY_OF_MONTH": "first",
    "RETURN_AS_TIMEZONE_AWARE": True,
}
ACCEPTED_STRINGS = {
    "str": ["str", "string", "text",],
    "date": ["datetime.date", "datetime", "date",],
    "int": ["int", "timestamp", "epoch", "unix", "float",],
}


def date_to(your_date: DateTypes, /, end_type: DateTypes, *, parser_settings: dict = None) -> DateTypes:
    """
    :param your_date: Requires to be either int, float, str, or datetime.date
    :param end_type: The type you want the date to be converted into
    :return: converted time to specified Type[end_type] rounded to seconds and always in UTC
    """

    if isinstance(end_type, str):
        if end_type.lower() in ACCEPTED_STRINGS["int"]:
            end_type = int
        elif end_type.lower() in ACCEPTED_STRINGS["date"]:
            end_type = datetime.date
        elif end_type.lower() in ACCEPTED_STRINGS["str"]:
            end_type = str
        else:
            raise TypeError(
                f"The only date input types allowed are {DateTypes} either as an object or in stringform.\n"
                f"Other accepted string representations of these types are: {ACCEPTED_STRINGS}"
            )

    # TODO: Add behaviour for float end_type support
    if not your_date:
        return your_date
    elif isinstance(your_date, int):
        your_date = _round_timestamp_to_seconds(your_date)

    if end_type == datetime.date:
        your_date = _to_datetime(your_date, parser_settings)

    elif end_type == int:
        if isinstance(your_date, str):
            your_date = _string_date_to_timestamp(your_date, parser_settings)
        elif isinstance(your_date, datetime.date):
            your_date = _date_time_to_timestamp(your_date)
        elif isinstance(your_date, float):
            your_date = int(your_date)

    elif end_type == str:
        if isinstance(your_date, str):
            # This operation completes a possibly incomplete query_string to seconds
            your_date = _to_datetime(your_date, parser_settings)
        elif isinstance(your_date, (int, float)):
            your_date = _to_datetime(your_date)
        your_date = your_date.isoformat()

    return your_date


def _to_datetime(_time: DateTypes, parser_settings: dict = None) -> datetime.date:
    if not isinstance(_time, (int, float)):
        if isinstance(_time, str):
            settings = parser_settings if parser_settings else DEFAULT_SETTINGS
            _time = parse(_time, settings=settings)
            
        _time = _date_time_to_timestamp(_time)

    return datetime.datetime.fromtimestamp(_time, tz=datetime.timezone.utc)


def _round_timestamp_to_seconds(_timestamp: int) -> int:  # Assumes positive number
    stamp_digits = TIMESTAMP_DIGITS
    num_length = int(math.log10(_timestamp)) + 1
    if num_length > stamp_digits:
        decimal = num_length - stamp_digits
        _timestamp //= 10**decimal
    return _timestamp


def _date_time_to_timestamp(_date_time) -> int:
    # pd.to_datetime uses pytz, can result in conflict
    # we're overriding the timezone class to avoid any conflict
    # Issue:https://stackoverflow.com/questions/60736569/timestamp-subtraction-must-have-the-same-timezones-or-no-timezones-but-they-are
    # TODO: test if this overriding causes non-UTC timezones to get borked
    _date_time = _date_time.replace(tzinfo=datetime.timezone.utc)
    unix_start = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return int((_date_time - unix_start).total_seconds())


def _string_date_to_timestamp(_date_string: str, parser_settings: dict = None) -> int:
    date_time = _to_datetime(_date_string, parser_settings)
    return _date_time_to_timestamp(date_time)
