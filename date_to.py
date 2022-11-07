"""One friendly python function for parsing and converting to and between datetime.datetime, int, and string objects"""
__version__ = "1.2.1"

import math
import datetime as dt
from dateparser import parse
from dateparser.timezone_parser import pop_tz_offset_from_string as tz_parse


DateTypes = str | int | float | dt.datetime | dt.date
ACCEPTED_STRINGS = {
    "str": ["str", "string", "text", ],
    "date": ["datetime.datetime", "datetime", "date", "dt", "dt.datetime", "dt.date", ],
    "int": ["int", "timestamp", "epoch", "unix", "float", ],
}

TIMESTAMP_DIGITS = 10
DEFAULT_SETTINGS = {
    "TO_TIMEZONE": "UTC",
    "PREFER_DAY_OF_MONTH": "first",
    "RETURN_AS_TIMEZONE_AWARE": True,
}


def date_to(your_date: DateTypes, /, end_type: DateTypes = dt.datetime,  
            timezone: str = None, *, parser_settings: dict = None,
            ) -> DateTypes:
    """
    :param your_date: Requires to be either int, float, str, or datetime.date
    :param end_type: The type you want the date to be converted into
    :param timezone: Three letter abbreviation (case insensitive) of desired output timezone. Default is "UTC"
    :param parser_settings: dict of keyword arguments for overriding default dateparser.parse() settings
    :return: converted time to specified Type[end_type] rounded to seconds
    """
    
    end_type = _validate_end_type(end_type)
    settings = _parse_settings(timezone, parser_settings)
    if isinstance(your_date, (int, float)):
        your_date = _round_timestamp_to_seconds(your_date)


    if end_type == dt.datetime:
        if isinstance(your_date, str):
            return _str_to_datetime(your_date, settings)
        return _to_datetime(your_date, timezone)

    elif end_type == int:
        if isinstance(your_date, str):
            return _string_date_to_timestamp(your_date, settings)
        elif isinstance(your_date, dt.datetime):
            return _date_time_to_timestamp(your_date)

    elif end_type == str:
        if isinstance(your_date, str):
            # This operation completes a possibly incomplete query_string to seconds
            your_date = _str_to_datetime(your_date, settings)
        elif isinstance(your_date, (int, float)):
            your_date = _to_datetime(your_date, timezone)
        return your_date.isoformat()

    return your_date

# =====================================

def _str_to_datetime(_str_date: str, settings: dict) -> dt.datetime:
    _datetime = parse(_str_date, settings=settings)
    if not _datetime:
        raise DateInputError(f"Input string could not be parsed! Input: {_str_date}")
    else:
        return _datetime


def _to_datetime(_time: DateTypes, timezone: str = None) -> dt.datetime:
    if not isinstance(_time, (int, float)):
        _time = _date_time_to_timestamp(_time)
    
    _tz = tz_parse(f"dummy text {timezone}") if timezone else dt.timezone.utc
    return dt.datetime.fromtimestamp(_time, tz=_tz)


def _date_time_to_timestamp(_date_time: dt.date) -> int:
    # Fix for issue: 
    # https://stackoverflow.com/questions/60736569/timestamp-subtraction-must-have-the-same-timezones-or-no-timezones-but-they-are
    _date_time = _date_time.astimezone(dt.timezone.utc)
    unix_start = dt.datetime.fromtimestamp(0, tz=dt.timezone.utc)
    return int((_date_time - unix_start).total_seconds())


def _string_date_to_timestamp(_date_string: str, settings: dict) -> int:
    date_time = _str_to_datetime(_date_string, settings)
    return _date_time_to_timestamp(date_time)

# =====================================

def _validate_end_type(end_type):
    
    if end_type == float:
        end_type = int
    elif end_type == dt.date:
        end_type = dt.datetime
    
    if isinstance(end_type, str):
        if end_type.lower() in ACCEPTED_STRINGS["str"]:
            end_type = str
        elif end_type.lower() in ACCEPTED_STRINGS["date"]:
            end_type = dt.datetime
        elif end_type.lower() in ACCEPTED_STRINGS["int"]:
            end_type = int
        else:
            raise KeyError(f"Invalid input string: {end_type=}"
                           f"Accepted string representations are: {ACCEPTED_STRINGS}")
            
    elif end_type != str and end_type != int and end_type != dt.datetime:
        raise TypeError(f"Invalid input {end_type=} given. \n"
                        f"The only date input types allowed are {DateTypes} either as an object or in string representation.")

    return end_type


def _parse_settings(timezone: str = None, parser_settings: dict = None) -> dict:
        settings = parser_settings if parser_settings else DEFAULT_SETTINGS
        if timezone:
            settings["TO_TIMEZONE"] = timezone.upper()
        return settings


def _round_timestamp_to_seconds(_timestamp: int | float) -> int:
    if _timestamp < 0:
        raise DateInputError(f"Input timestamp {_timestamp} is invalid (negative number)")
    
    stamp_digits = TIMESTAMP_DIGITS
    num_length = int(math.log10(_timestamp)) + 1
    if num_length > stamp_digits:
        decimal = num_length - stamp_digits
        _timestamp //= 10**decimal
    return int(_timestamp)

# =====================================
class DateInputError(Exception):
    pass

