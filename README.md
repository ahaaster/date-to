# date_to - A light-weight, handy date converter

[![https://img.shields.io/pypi/v/date_to?label=version](https://img.shields.io/pypi/v/date_to?label=version)](https://pypi.org/project/date_to/)

### Convert any date to another with just one friendly function

```date_to()``` will convert your dates between datetime objects, unix timestamps, and strings. No more boilerplate and headaches of trying to keep track of your dates and their (lack) of timezones.

```date_to``` utilises the dateparser library for string parsing, enabling [many kinds of string representations](url="https://dateparser.readthedocs.io/en/latest/index.html#features") of time to be converted into machine interpretable dates.

All output dates are rounded to second precision.
Default conversion is to the UTC timezone. 

If you wish to change this conversion behaviour you can add a dict of keyword arguments to the function's ```parser_settings=``` optional keyword argument. Please refer to the [dateparser documentation](url="https://dateparser.readthedocs.io/en/latest/dateparser.html#dateparser.parse") for possible settings

## Basic Use

```python
from date_to import date_to

some_date = "2001-09-11 17:20 EDT"

a = date_to(some_date, str)
b = date_to(some_date, int)
c = date_to(some_date, "datetime")

print(type(a), a)
print(type(b), b)
print(type(c), c)
```

**Output:**

```
<class 'str'> "2001-09-11T21:20:00+00:00"
<class 'int'> 1000243200
<class 'datetime.datetime'> 2001-09-11 21:20:00+00:00
```

## Installation
The ```date_to``` library is available on [PyPi]("https://pypi.org/project/date_to/") and easily installed using pip:
```
pip install date_to
```

### Accepted Inputs

```python
from datetime import datetime

accepted_object_inputs = int | str | datetime.date
accepted_string_inputs = {
    "str": ["str", "string", "text",],
    "date": ["date", "datetime.date", "datetime",],
    "int": ["int", "timestamp", "epoch", "unix", "float",],
}
```
