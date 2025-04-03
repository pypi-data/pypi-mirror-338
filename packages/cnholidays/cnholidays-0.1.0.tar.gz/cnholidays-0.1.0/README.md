# cnholidays

Chinese holiday and workday determination library, supporting legal holiday and workday adjustment detection.

[![PyPI version](https://badge.fury.io/py/cnholidays.svg)](https://badge.fury.io/py/cnholidays)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- Determine if a specific date is a Chinese legal holiday
- Determine if a specific date is a workday (including regular workdays and adjusted workdays)
- Support for custom workday adjustment schedules
- Get all holidays and workdays for a specified year
- Built-in 2025 adjustment schedule
- Support for various date input formats (string, date object, datetime object)

## Installation

```bash
pip install cnholidays
```

## Quick Start

```python
from datetime import date
from cnholidays import is_holiday, is_workday, get_holiday_name

# Check if today is a holiday
print(f"Is today a holiday? {is_holiday(date.today())}")

# Check if a specific date is a workday
print(f"Is 2025-01-01 a workday? {is_workday('2025-01-01')}")  # New Year's Day, not a workday
print(f"Is 2025-01-26 a workday? {is_workday('2025-01-26')}")  # Spring Festival adjustment, is a workday

# Get holiday name
print(f"What holiday is 2025-01-01? {get_holiday_name('2025-01-01')}")
```

## Detailed Usage

### Convenience Functions

```python
from cnholidays import is_holiday, is_workday, get_holiday_name, get_holidays, get_workdays

# Check if a date is a holiday
is_holiday('2025-01-01')  # True, New Year's Day
is_holiday('2025-01-02')  # False, regular workday

# Check if a date is a workday
is_workday('2025-01-01')  # False, New Year's Day is not a workday
is_workday('2025-01-02')  # True, regular workday
is_workday('2025-01-04')  # False, regular weekend is not a workday
is_workday('2025-01-26')  # True, adjusted workday

# Get holiday name
get_holiday_name('2025-01-01')  # "New Year's Day"
get_holiday_name('2025-01-02')  # None, not a holiday

# Get all holidays for a specific year
holidays_2025 = get_holidays(2025)  # {date(2025, 1, 1): "New Year's Day", ...}

# Get all workdays for a specific year
workdays_2025 = get_workdays(2025)  # {date(2025, 1, 2), date(2025, 1, 3), ...}
```

### Using ChineseCalendar Class

```python
from datetime import date
from cnholidays import ChineseCalendar

# Create an instance, optionally specify years
cal = ChineseCalendar(years=[2025, 2026])

# Check dates
cal.is_holiday('2025-01-01')  # True
cal.is_workday('2025-01-26')  # True, adjusted workday

# Get all holidays
holidays = cal.get_holidays(2025)
print(f"2025 has {len(holidays)} legal holidays")

# Get all workdays
workdays = cal.get_workdays(2025)
print(f"2025 has {len(workdays)} workdays")

# Get workday adjustments
adjustments = cal.get_workday_adjustments(2025)
print(f"2025 has {len(adjustments)} adjusted workdays")
```

### Custom Adjustment Schedules

```python
from datetime import date
from cnholidays import ChineseCalendar

# Define custom workday adjustments
custom_adjustments = {
    2025: [
        date(2025, 12, 20),  # Custom weekend adjustment to workday
        date(2025, 12, 21),  # Custom weekend adjustment to workday
    ]
}

# Create calendar with custom adjustment schedule
cal = ChineseCalendar(workday_adjustments=custom_adjustments)

# Check custom adjustment dates
print(f"Is 2025-12-20 a workday? {cal.is_workday('2025-12-20')}")  # True

# Dynamically add adjustment
cal.add_workday_adjustment('2025-12-27')
print(f"Is 2025-12-27 a workday? {cal.is_workday('2025-12-27')}")  # True
```

## Preset Data

cnholidays includes built-in adjustment data for 2025:

- January 26, 2025 (Spring Festival adjustment)
- February 28, 2025 (Spring Festival adjustment)
- April 27, 2025 (Labor Day adjustment)
- September 28, 2025 (Mid-Autumn Festival adjustment)
- October 11, 2025 (Mid-Autumn Festival and National Day adjustment)

## Background

Chinese workday scheduling has some special characteristics:

1. Legal holidays are not workdays
2. Monday to Friday are generally workdays (unless they are legal holidays)
3. Saturday and Sunday are generally not workdays
4. But some weekends are adjusted to be workdays (usually to create extended holiday periods)

This library considers these special cases and can accurately determine if a date is a workday.

## License

MIT

## Change Log

### 0.1.0
- Initial release
- Support for Chinese legal holidays and workday adjustments
- Built-in 2025 adjustment schedule 