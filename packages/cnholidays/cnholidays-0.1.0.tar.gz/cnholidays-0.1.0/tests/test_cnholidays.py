"""
Unit tests for cnholidays
"""

import unittest
from datetime import date
from cnholidays import ChineseCalendar, is_holiday, is_workday


class TestCNHolidays(unittest.TestCase):
    """Test basic functionality of cnholidays library"""
    
    def test_basic_functions(self):
        """Test convenience functions"""
        # Test holidays
        self.assertTrue(is_holiday("2025-01-01"))  # New Year's Day
        self.assertTrue(is_holiday(date(2025, 5, 1)))  # Labor Day
        
        # Test workdays
        self.assertFalse(is_workday("2025-01-01"))  # New Year's Day is not a workday
        self.assertTrue(is_workday("2025-01-02"))   # Regular workday
        self.assertFalse(is_workday("2025-01-04"))  # Regular weekend is not a workday
        self.assertTrue(is_workday("2025-01-26"))   # Adjusted weekend workday
    
    def test_chinese_calendar(self):
        """Test ChineseCalendar class"""
        cal = ChineseCalendar(years=2025)
        
        # Test holidays
        self.assertTrue(cal.is_holiday("2025-01-01"))  # New Year's Day
        self.assertFalse(cal.is_holiday("2025-01-02"))  # Regular workday
        
        # Test workdays
        self.assertTrue(cal.is_workday("2025-01-02"))  # Regular workday
        self.assertFalse(cal.is_workday("2025-01-01"))  # New Year's Day is not a workday
        self.assertFalse(cal.is_workday("2025-01-05"))  # Sunday without adjustment
        self.assertTrue(cal.is_workday("2025-01-26"))   # Sunday with adjustment
        
        # Test holiday names
        self.assertEqual(cal.get_holiday_name("2025-01-01"), "New Year's Day")
        self.assertIsNone(cal.get_holiday_name("2025-01-02"))
        
        # Test getting all holidays
        holidays = cal.get_holidays(2025)
        self.assertGreater(len(holidays), 0)
        self.assertIn(date(2025, 1, 1), holidays)
        
        # Test getting all workdays
        workdays = cal.get_workdays(2025)
        self.assertGreater(len(workdays), 200)  # A year has more than 200 workdays
        self.assertIn(date(2025, 1, 2), workdays)
        self.assertIn(date(2025, 1, 26), workdays)  # Adjusted workday
        self.assertNotIn(date(2025, 1, 1), workdays)  # New Year's Day is not a workday
        
        # Test workday adjustments
        adjustments = cal.get_workday_adjustments(2025)
        self.assertEqual(len(adjustments), 5)  # 2025 has 5 adjusted workdays
        self.assertIn(date(2025, 1, 26), adjustments)
    
    def test_custom_adjustments(self):
        """Test custom workday adjustments"""
        custom_adjustments = {
            2025: [
                date(2025, 12, 20),  # Custom adjustment
                date(2025, 12, 21),  # Custom adjustment
            ]
        }
        
        cal = ChineseCalendar(workday_adjustments=custom_adjustments)
        
        # Test custom adjustment dates
        self.assertTrue(cal.is_workday("2025-12-20"))  # Custom adjusted Saturday
        self.assertTrue(cal.is_workday("2025-12-21"))  # Custom adjusted Sunday
        self.assertTrue(cal.is_workday("2025-01-26"))  # Default adjustment still works
        
        # Test adding workday adjustment
        cal.add_workday_adjustment("2025-12-27")
        self.assertTrue(cal.is_workday("2025-12-27"))
        adjustments = cal.get_workday_adjustments(2025)
        self.assertIn(date(2025, 12, 27), adjustments)


if __name__ == "__main__":
    unittest.main() 