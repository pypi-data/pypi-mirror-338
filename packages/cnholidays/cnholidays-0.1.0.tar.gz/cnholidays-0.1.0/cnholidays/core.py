"""
Core functionality implementation for cnholidays
"""

import holidays
from datetime import datetime, date, timedelta
from typing import Dict, List, Union, Optional, Set, Tuple


# Predefined workday adjustments (weekends that are designated as working days)
DEFAULT_WORKDAY_ADJUSTMENTS = {
    # 2025
    2025: [
        date(2025, 1, 26),  # Spring Festival adjustment
        date(2025, 2, 28),  # Spring Festival adjustment
        date(2025, 4, 27),  # Labor Day adjustment
        date(2025, 9, 28),  # Mid-Autumn Festival adjustment
        date(2025, 10, 11), # Mid-Autumn Festival and National Day adjustment
    ],
    # You can add other years' adjustment schedules here
}


class ChineseCalendar:
    """Chinese calendar class, providing holiday and workday determination"""
    
    def __init__(self, years: Union[int, List[int]] = None, workday_adjustments: Dict[int, List[date]] = None):
        """
        Initialize Chinese calendar
        
        Parameters:
            years: Year or list of years. Defaults to current year
            workday_adjustments: Dictionary of workday adjustments in format {year: [list of dates]}
        """
        if years is None:
            years = datetime.now().year
            
        self.years = [years] if isinstance(years, int) else years
        
        # Merge default and user-provided workday adjustments
        self.workday_adjustments = dict(DEFAULT_WORKDAY_ADJUSTMENTS)
        if workday_adjustments:
            for year, dates in workday_adjustments.items():
                if year in self.workday_adjustments:
                    self.workday_adjustments[year].extend(dates)
                else:
                    self.workday_adjustments[year] = dates
        
        # Use the CN class from holidays library to get official holidays
        self.cn_holidays = holidays.CN(years=self.years)
    
    def is_holiday(self, day: Union[date, datetime, str]) -> bool:
        """
        Determine if the specified date is an official holiday
        
        Parameters:
            day: Date to check, can be a date object, datetime object, or 'YYYY-MM-DD' string
            
        Returns:
            True if the date is an official holiday, False otherwise
        """
        if isinstance(day, str):
            day = datetime.strptime(day, "%Y-%m-%d").date()
        elif isinstance(day, datetime):
            day = day.date()
            
        return day in self.cn_holidays
    
    def is_workday(self, day: Union[date, datetime, str]) -> bool:
        """
        Determine if the specified date is a workday (defined as Mon-Fri that are not holidays, 
        or weekends that are adjusted to be workdays)
        
        Parameters:
            day: Date to check, can be a date object, datetime object, or 'YYYY-MM-DD' string
            
        Returns:
            True if the date is a workday, False otherwise
        """
        if isinstance(day, str):
            day = datetime.strptime(day, "%Y-%m-%d").date()
        elif isinstance(day, datetime):
            day = day.date()
            
        # If it's an official holiday, it's not a workday
        if self.is_holiday(day):
            return False
        
        # If it's a weekend (Sat=5, Sun=6)
        if day.weekday() >= 5:
            # Check if it's in the workday adjustments list
            year = day.year
            return year in self.workday_adjustments and day in self.workday_adjustments[year]
        
        # Mon-Fri that are not holidays are workdays
        return True
    
    def get_holiday_name(self, day: Union[date, datetime, str]) -> Optional[str]:
        """
        Get the name of the holiday for the specified date
        
        Parameters:
            day: Date to check, can be a date object, datetime object, or 'YYYY-MM-DD' string
            
        Returns:
            The name of the holiday if the date is a holiday, None otherwise
        """
        if isinstance(day, str):
            day = datetime.strptime(day, "%Y-%m-%d").date()
        elif isinstance(day, datetime):
            day = day.date()
            
        return self.cn_holidays.get(day)
    
    def get_holidays(self, year: int = None) -> Dict[date, str]:
        """
        Get all official holidays for the specified year
        
        Parameters:
            year: Year to get holidays for. Defaults to current year
            
        Returns:
            Dictionary of holidays in format {date: holiday name}
        """
        if year is None:
            year = datetime.now().year
            
        return {k: v for k, v in self.cn_holidays.items() if k.year == year}
    
    def get_workdays(self, year: int = None) -> Set[date]:
        """
        Get all workdays for the specified year
        
        Parameters:
            year: Year to get workdays for. Defaults to current year
            
        Returns:
            Set of workdays
        """
        if year is None:
            year = datetime.now().year
            
        # Calculate all dates in the year
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        delta = (end_date - start_date).days + 1
        
        all_days = [start_date + timedelta(days=i) for i in range(delta)]
        return {d for d in all_days if self.is_workday(d)}
    
    def get_workday_adjustments(self, year: int = None) -> List[date]:
        """
        Get the list of workday adjustments for the specified year
        
        Parameters:
            year: Year to get workday adjustments for. Defaults to current year
            
        Returns:
            List of workday adjustment dates
        """
        if year is None:
            year = datetime.now().year
            
        return self.workday_adjustments.get(year, [])
    
    def add_workday_adjustment(self, day: Union[date, datetime, str]) -> None:
        """
        Add a workday adjustment
        
        Parameters:
            day: Date to add, can be a date object, datetime object, or 'YYYY-MM-DD' string
        """
        if isinstance(day, str):
            day = datetime.strptime(day, "%Y-%m-%d").date()
        elif isinstance(day, datetime):
            day = day.date()
            
        year = day.year
        if year not in self.workday_adjustments:
            self.workday_adjustments[year] = []
            
        if day not in self.workday_adjustments[year]:
            self.workday_adjustments[year].append(day)


# Create a default instance for convenience functions
_default_calendar = ChineseCalendar()

# Convenience functions using the default calendar instance
def is_holiday(day: Union[date, datetime, str]) -> bool:
    """Determine if the specified date is an official holiday"""
    return _default_calendar.is_holiday(day)

def is_workday(day: Union[date, datetime, str]) -> bool:
    """Determine if the specified date is a workday"""
    return _default_calendar.is_workday(day)

def get_holiday_name(day: Union[date, datetime, str]) -> Optional[str]:
    """Get the name of the holiday for the specified date"""
    return _default_calendar.get_holiday_name(day)

def get_holidays(year: int = None) -> Dict[date, str]:
    """Get all official holidays for the specified year"""
    return _default_calendar.get_holidays(year)

def get_workdays(year: int = None) -> Set[date]:
    """Get all workdays for the specified year"""
    return _default_calendar.get_workdays(year)

def get_workday_adjustments(year: int = None) -> List[date]:
    """Get the list of workday adjustments for the specified year"""
    return _default_calendar.get_workday_adjustments(year) 