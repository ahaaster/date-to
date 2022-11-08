# date_to - The easy date converter

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/date_to?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/ahaaster/date-to?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/date-to?style=for-the-badge)

![Tests](https://github.com/ahaaster/date-to/actions/workflows/tests.yml/badge.svg)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/ahaaster/date-to/dateparser)

## Convert any date to another with just one friendly function

```date_to()``` will convert your dates between datetime objects, unix timestamps, and strings. No more boilerplate and headaches of trying to keep track of your dates and their (lack) of timezones.

```date_to()``` utilises the dateparser library for string parsing, enabling [many kinds of string representations](https://dateparser.readthedocs.io/en/latest/index.html#features) of time to be converted into machine interpretable dates.
All output dates are rounded to second precision.

Default timezone conversion is to UTC. If you wish to convert your date to another timezone, simply provide the abbreviation of your desired timezone for the optional ```timezone=``` keyword argument.

## Installation

The ```date_to``` library is available on [PyPi](https://pypi.org/project/date_to/) and easily installed using pip:

```bash
pip install date_to
```

## Basic Use

```python
from date_to import date_to

some_date = "2001-09-11 17:20 EDT"

a = date_to(some_date)
b = date_to(some_date, "date")
c = date_to(some_date, str, timezone="JST")
d = date_to(some_date, to_type=int)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
```

**Output:**

```text
2001-09-11 21:20:00+00:00 <class 'datetime.datetime'>
2001-09-11 21:20:00+00:00 <class 'datetime.datetime'>
2001-09-12T06:20:00+09:00 <class 'str'>
1000243200 <class 'int'>
```

### Accepted ```to_type``` Inputs

```python
import datetime as dt

accepted_object_inputs = str | int | float | dt.datetime | dt.date
accepted_string_inputs = {
    "str": ["str", "string", "text", ],
    "int": ["int", "timestamp", "epoch", "unix", "float", ],
    "date": ["datetime.datetime", "datetime", "date", "dt", "dt.datetime", "dt.date", ],
}
```

#### Parse Settings

If you wish to change the string parse conversion behaviour you can add a ```dict``` of keyword arguments to the function's ```parser_settings=``` optional keyword argument. Please refer to the [dateparser documentation](https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.parse) for possible settings.

```python
DEFAULT_SETTINGS = {
    "TIMEZONE": "UTC",
    "PREFER_DAY_OF_MONTH": "first",
    "RETURN_AS_TIMEZONE_AWARE": True,
}
```
