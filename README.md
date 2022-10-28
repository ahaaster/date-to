# date_to - A light-weight date converter

[![https://img.shields.io/pypi/v/date_to?label=version](https://img.shields.io/pypi/v/date_to?label=version)](https://pypi.org/project/date_to/)

### Convert any date to another with just one friendly function

```date_to()``` will convert your dates between datetime objects, unix timestamps, and strings. No more boilerplate and headaches of trying to keep track of your dates and their (lack) of timezones.

```date_to()``` utilises the dateparser library for string parsing, enabling [many kinds of string representations](url="https://dateparser.readthedocs.io/en/latest/index.html#features") of time to be converted into machine interpretable dates.

All output dates are rounded to second precision.
Default conversion is to the UTC timezone. 
As of now, timezone conversion is only supported from ```str``` to ```str | datetime.date```. Further conversion support is planned.


## Installation
The ```date_to``` library is available on [PyPi]("https://pypi.org/project/date_to/") and easily installed using pip:
```
pip install date_to
```

## Basic Use

```python
from date_to import date_to

some_date = "2001-09-11 17:20 EDT"

a = date_to(some_date)
b = date_to(some_date, "date")
c = date_to(some_date, int)
d = date_to(some_date, str, timezone="JST")

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
```

**Output:**

```
2001-09-11 21:20:00+00:00 <class 'datetime.datetime'> 
2001-09-11 21:20:00+00:00 <class 'datetime.datetime'> 
1000243200 <class 'int'> 
2001-09-12 06:20:00+09:00 <class 'str'> 
```

### Accepted Inputs

```python
from datetime import date

accepted_object_inputs = str | date | int | float
accepted_string_inputs = {
    str: ["str", "string", "text"],
    date: ["datetime.date", "datetime", "date", "dt", "dt.date"],
    int: ["int", "timestamp", "epoch", "unix", "float"],
}
```
#### Parse Settings
If you wish to change the string parse conversion behaviour you can add a ```dict``` of keyword arguments to the function's ```parser_settings=``` optional keyword argument. Please refer to the [dateparser documentation](url="https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.parse") for possible settings.
```python
DEFAULT_SETTINGS = {
    "TIMEZONE": "UTC",
    "PREFER_DAY_OF_MONTH": "first",
    "RETURN_AS_TIMEZONE_AWARE": True,
}
```
