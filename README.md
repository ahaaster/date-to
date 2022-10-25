# Date Converter

### Convert from any date to another with just a single function

```date_to``` will make your naive dates timezone aware and uniformly convert. No more boilerplate and headaches of trying to keep track of your dates and their (lack) of timezones

All output dates are converted to UTC and rounded to second precision.

## Installation
```
pip install date_to
```

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

### Accepted Inputs

```python
from datetime import datetime

accepted_object_inputs = int | str | datetime.date
accepted_string_inputs = [
    "str", "string", "text",
    "int", "timestamp", "epoch", "unix", "float",
    "datetime.date", "datetime", "date",
]
```
