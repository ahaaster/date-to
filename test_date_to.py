import pytest
import datetime as dt
from date_to import date_to, DateInputError


LOCAL_STR = "2001-09-11 17:20:52 EDT"
TIME_STR = "2001-09-11T21:20:52+00:00"
TIME_INT = 1000243252
TIME_DATE = dt.datetime(2001, 9, 11, 21, 20, 52, tzinfo=dt.timezone.utc)


@pytest.mark.parametrize("input_date, input_type, expected", [
    (LOCAL_STR, str, TIME_STR),
    (LOCAL_STR, int, TIME_INT),
    (LOCAL_STR, dt.datetime, TIME_DATE),
    
    (TIME_INT, "str", TIME_STR),
    (TIME_INT, "int", TIME_INT),
    (TIME_INT, "dt", TIME_DATE),
    
    (TIME_DATE, "text", TIME_STR),
    (TIME_DATE, "timestamp", TIME_INT),
    (TIME_DATE, "date", TIME_DATE),
    
    (LOCAL_STR, float, TIME_INT),
    (TIME_INT+0.2, "unix", TIME_INT),
    (TIME_INT*10**3, "epoch", TIME_INT),
    (TIME_INT, dt.date, TIME_DATE)
])
def test_basic_input_output(input_date, input_type, expected):
    assert date_to(input_date, input_type) == expected


@pytest.mark.parametrize("input_date, input_type, tz, expected", [
    (LOCAL_STR, str, "JST", "2001-09-12T06:20:52+09:00"),
    (TIME_STR, str, "JST", "2001-09-12T06:20:52+09:00"),
])
def test_timezone_conversion(input_date, input_type, tz, expected):
    assert date_to(input_date, input_type, tz) == expected


def test_invalid_str_endtype():
    with pytest.raises(KeyError):
        date_to(LOCAL_STR, "Not a valid datetype")


def test_invalid_endtype():
    with pytest.raises(TypeError):
        date_to(LOCAL_STR, dict)


def test_invalid_int_input():
    with pytest.raises(DateInputError):
        date_to(-1, int)

        
def test_invalid_str_input():
    with pytest.raises(DateInputError):
        date_to("not an actual date")