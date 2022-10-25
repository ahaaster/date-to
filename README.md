# Date Converter

A handy date parser and converter that handles timestamps, strings, and datetime.date.

### Convert from any date to another with a single function!

Date converter will make your naive dates timezone aware and uniformly convert them to UTC for your convenience!

## Basic Use

```python
from date_to import date_to

some_date = "2001-09-11 17:20 EDT"

date_to(some_date, str)
date_to(some_date, int)
date_to(some_date, "datetime")

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
    "str", "string",
    "int", "timestamp", "epoch", "unix", "float",
    "datetime.date", "datetime", "date",
]
```
