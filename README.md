# Date Converter
A handy date parser and converter that handles timestamps, strings, and datetime.date.

### Convert from any date to another with a single function!
Date converter will make your naive dates timezone aware and uniformly convert them to UTC for your convenience!

## Basic Use

``` { .python capture }
from date-converter import date_to

some_date = "2022-03-01 14:00"

d = date_to(some_date, int)

print(f"The converted date to unix timestamps is now: {d}")
```
