"""
Usage examples for cnholidays
"""

from datetime import date, datetime
from .core import ChineseCalendar, is_holiday, is_workday, get_holiday_name

def basic_usage_examples():
    """Basic usage examples"""
    # Using convenience functions
    print("=== Convenience Function Examples ===")
    
    # Check if a date is a holiday
    print(f"Is 2025-01-01 a holiday? {is_holiday('2025-01-01')}")
    print(f"Holiday name for 2025-01-01: {get_holiday_name('2025-01-01')}")
    
    # Check if a date is a workday
    print(f"Is 2025-01-01 a workday? {is_workday('2025-01-01')}")
    print(f"Is 2025-04-27 a workday? {is_workday('2025-04-27')}")  # Adjusted weekend
    print(f"Is 2025-04-26 a workday? {is_workday('2025-04-26')}")  # Regular weekend
    
    # Using different date parameter types
    today = date.today()
    now = datetime.now()
    print(f"Is today a holiday? {is_holiday(today)}")
    print(f"Is now a workday? {is_workday(now)}")

def chinese_calendar_examples():
    """ChineseCalendar class usage examples"""
    print("\n=== ChineseCalendar Class Examples ===")
    
    # Create an instance
    cal = ChineseCalendar(years=[2025, 2026])
    
    # Get all holidays
    holidays_2025 = cal.get_holidays(2025)
    print(f"2025 has {len(holidays_2025)} official holidays")
    for d, name in list(holidays_2025.items())[:3]:
        print(f"  - {d.strftime('%Y-%m-%d')}: {name}")
    
    # Get all workdays
    workdays_2025 = cal.get_workdays(2025)
    print(f"2025 has {len(workdays_2025)} workdays")
    
    # Get workday adjustments
    workday_adjustments = cal.get_workday_adjustments(2025)
    print(f"2025 has {len(workday_adjustments)} workday adjustments:")
    for d in workday_adjustments:
        print(f"  - {d.strftime('%Y-%m-%d')}")
    
    # Add custom workday adjustment
    cal.add_workday_adjustment('2025-12-20')
    print(f"After adding a custom adjustment, is 2025-12-20 a workday? {cal.is_workday('2025-12-20')}")

def custom_calendar_example():
    """Custom adjustment calendar example"""
    print("\n=== Custom Adjustment Calendar Example ===")
    
    # Define custom workday adjustments
    custom_adjustments = {
        2025: [
            date(2025, 12, 20),  # Custom adjustment
            date(2025, 12, 21),  # Custom adjustment
        ]
    }
    
    # Create custom calendar
    custom_cal = ChineseCalendar(workday_adjustments=custom_adjustments)
    
    # Check custom adjustment dates
    print(f"Using custom calendar, is 2025-12-20 a workday? {custom_cal.is_workday('2025-12-20')}")
    print(f"Using custom calendar, is 2025-12-21 a workday? {custom_cal.is_workday('2025-12-21')}")


if __name__ == "__main__":
    basic_usage_examples()
    chinese_calendar_examples()
    custom_calendar_example() 