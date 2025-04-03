"""
cnholidays - Chinese holiday and workday determination library

This library provides functionality for determining Chinese holidays and adjusted workdays, 
with support for custom adjustment schedules.
"""

__version__ = '0.1.0'

from .core import (
    ChineseCalendar,
    is_holiday,
    is_workday,
    get_holidays,
    get_workdays,
    get_holiday_name
)

__all__ = [
    'ChineseCalendar',
    'is_holiday',
    'is_workday',
    'get_holidays',
    'get_workdays',
    'get_holiday_name'
] 