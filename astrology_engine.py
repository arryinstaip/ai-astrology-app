print("HELLO FROM ASTROLOGY_ENGINE")
"""
Astrology Calculation Engine
----------------------------
This module handles all astrological calculations including:
- Western Zodiac signs
- Chinese Zodiac animals
- Element associations
- Lucky numbers, colors, days, etc.
"""

from datetime import datetime
from dateutil import parser
import random


class AstrologyEngine:
    """
    Main class for performing astrological calculations.
    All methods are designed to be deterministic based on birth data.
    """
    
    def __init__(self):
        """Initialize the astrology engine with reference data."""
        
        # Western Zodiac signs with date ranges
        self.zodiac_signs = [
            {'name': 'Capricorn', 'symbol': '♑', 'start': (12, 22), 'end': (1, 19), 'element': 'Earth'},
            {'name': 'Aquarius', 'symbol': '♒', 'start': (1, 20), 'end': (2, 18), 'element': 'Air'},
            {'name': 'Pisces', 'symbol': '♓', 'start': (2, 19), 'end': (3, 20), 'element': 'Water'},
            {'name': 'Aries', 'symbol': '♈', 'start': (3, 21), 'end': (4, 19), 'element': 'Fire'},
            {'name': 'Taurus', 'symbol': '♉', 'start': (4, 20), 'end': (5, 20), 'element': 'Earth'},
            {'name': 'Gemini', 'symbol': '♊', 'start': (5, 21), 'end': (6, 20), 'element': 'Air'},
            {'name': 'Cancer', 'symbol': '♋', 'start': (6, 21), 'end': (7, 22), 'element': 'Water'},
            {'name': 'Leo', 'symbol': '♌', 'start': (7, 23), 'end': (8, 22), 'element': 'Fire'},
            {'name': 'Virgo', 'symbol': '♍', 'start': (8, 23), 'end': (9, 22), 'element': 'Earth'},
            {'name': 'Libra', 'symbol': '♎', 'start': (9, 23), 'end': (10, 22), 'element': 'Air'},
            {'name': 'Scorpio', 'symbol': '♏', 'start': (10, 23), 'end': (11, 21), 'element': 'Water'},
            {'name': 'Sagittarius', 'symbol': '♐', 'start': (11, 22), 'end': (12, 21), 'element': 'Fire'}
        ]
        
        # Chinese Zodiac animals (12-year cycle starting from 1900 = Rat)
        self.chinese_zodiac = [
            {'name': 'Rat', 'symbol': '🐀', 'element': 'Water'},
            {'name': 'Ox', 'symbol': '🐂', 'element': 'Earth'},
            {'name': 'Tiger', 'symbol': '🐅', 'element': 'Wood'},
            {'name': 'Rabbit', 'symbol': '🐇', 'element': 'Wood'},
            {'name': 'Dragon', 'symbol': '🐉', 'element': 'Earth'},
            {'name': 'Snake', 'symbol': '🐍', 'element': 'Fire'},
            {'name': 'Horse', 'symbol': '🐎', 'element': 'Fire'},
            {'name': 'Goat', 'symbol': '🐐', 'element': 'Earth'},
            {'name': 'Monkey', 'symbol': '🐒', 'element': 'Metal'},
            {'name': 'Rooster', 'symbol': '🐓', 'element': 'Metal'},
            {'name': 'Dog', 'symbol': '🐕', 'element': 'Earth'},
            {'name': 'Pig', 'symbol': '🐖', 'element': 'Water'}
        ]
        
        # Element associations
        self.elements = {
            'Fire': {'colors': ['Red', 'Orange', 'Gold'], 'direction': 'South', 'season': 'Summer'},
            'Earth': {'colors': ['Brown', 'Green', 'Yellow'], 'direction': 'Center', 'season': 'Late Summer'},
            'Air': {'colors': ['White', 'Light Blue', 'Silver'], 'direction': 'East', 'season': 'Spring'},
            'Water': {'colors': ['Blue', 'Black', 'Purple'], 'direction': 'North', 'season': 'Winter'}
        }
        
        # Lucky gemstones by zodiac sign
        self.gemstones = {
            'Aries': 'Diamond',
            'Taurus': 'Emerald',
            'Gemini': 'Pearl',
            'Cancer': 'Ruby',
            'Leo': 'Peridot',
            'Virgo': 'Sapphire',
            'Libra': 'Opal',
            'Scorpio': 'Topaz',
            'Sagittarius': 'Turquoise',
            'Capricorn': 'Garnet',
            'Aquarius': 'Amethyst',
            'Pisces': 'Aquamarine'
        }
        
        # Lucky days by zodiac sign
        self.lucky_days = {
            'Aries': 'Tuesday',
            'Taurus': 'Friday',
            'Gemini': 'Wednesday',
            'Cancer': 'Monday',
            'Leo': 'Sunday',
            'Virgo': 'Wednesday',
            'Libra': 'Friday',
            'Scorpio': 'Tuesday',
            'Sagittarius': 'Thursday',
            'Capricorn': 'Saturday',
            'Aquarius': 'Saturday',
            'Pisces': 'Thursday'
        }
    
    def calculate_astrology(self, user_data: dict) -> dict:
        """
        Main method to calculate all astrological data.
        
        Args:
            user_data: Dictionary containing user's birth information
            
        Returns:
            Dictionary with all calculated astrological data
        """
        # Parse the date of birth
        dob = parser.parse(user_data['date_of_birth'])
        
        # Calculate Western Zodiac
        zodiac = self._get_zodiac_sign(dob.month, dob.day)
        
        # Calculate Chinese Zodiac
        chinese = self._get_chinese_zodiac(dob.year)
        
        # Get element data
        element_data = self.elements.get(zodiac['element'], {})
        
        # Calculate lucky number based on birth date (numerology-inspired)
        lucky_number = self._calculate_lucky_number(dob)
        
        # Compile all astrology data
        astrology_data = {
            'zodiac_sign': zodiac['name'],
            'zodiac_symbol': zodiac['symbol'],
            'element': zodiac['element'],
            'chinese_zodiac': chinese['name'],
            'chinese_symbol': chinese['symbol'],
            'chinese_element': chinese['element'],
            'lucky_number': lucky_number,
            'lucky_color': element_data.get('colors', ['Gold'])[0],
            'lucky_day': self.lucky_days.get(zodiac['name'], 'Sunday'),
            'lucky_gemstone': self.gemstones.get(zodiac['name'], 'Quartz'),
            'lucky_direction': element_data.get('direction', 'North'),
            'birth_season': self._get_season(dob.month),
            'life_path_number': self._calculate_life_path(dob),
            'birth_day_meaning': self._get_day_meaning(dob.weekday())
        }
        
        return astrology_data
    
    def _get_zodiac_sign(self, month: int, day: int) -> dict:
        """
        Determine the Western Zodiac sign based on month and day.
        
        Args:
            month: Birth month (1-12)
            day: Birth day (1-31)
            
        Returns:
            Dictionary with zodiac sign details
        """
        for sign in self.zodiac_signs:
            start_month, start_day = sign['start']
            end_month, end_day = sign['end']
            
            # Handle Capricorn which spans December-January
            if start_month > end_month:
                if (month == start_month and day >= start_day) or \
                   (month == end_month and day <= end_day):
                    return sign
            else:
                if (month == start_month and day >= start_day) or \
                   (month == end_month and day <= end_day) or \
                   (start_month < month < end_month):
                    return sign
        
        # Default fallback (should never reach here)
        return self.zodiac_signs[0]
    
    def _get_chinese_zodiac(self, year: int) -> dict:
        """
        Calculate the Chinese Zodiac animal based on birth year.
        
        Args:
            year: Birth year
            
        Returns:
            Dictionary with Chinese zodiac details
        """
        # Chinese zodiac cycles every 12 years, starting from 1900 (Rat year)
        index = (year - 1900) % 12
        return self.chinese_zodiac[index]
    
    def _calculate_lucky_number(self, dob: datetime) -> int:
        """
        Calculate a lucky number using numerology principles.
        Adds all digits of the birth date until reaching a single digit.
        
        Args:
            dob: Date of birth as datetime object
            
        Returns:
            Lucky number (1-9)
        """
        # Combine all digits from the date
        date_string = dob.strftime('%Y%m%d')
        total = sum(int(digit) for digit in date_string)
        
        # Reduce to single digit
        while total > 9:
            total = sum(int(digit) for digit in str(total))
        
        return total
    
    def _calculate_life_path(self, dob: datetime) -> int:
        """
        Calculate the Life Path Number (a key numerology concept).
        
        Args:
            dob: Date of birth
            
        Returns:
            Life path number (1-9, or master numbers 11, 22, 33)
        """
        # Sum each component separately first
        year_sum = sum(int(d) for d in str(dob.year))
        month_sum = sum(int(d) for d in str(dob.month))
        day_sum = sum(int(d) for d in str(dob.day))
        
        # Reduce each to single digit (keeping master numbers)
        def reduce(n):
            while n > 9 and n not in [11, 22, 33]:
                n = sum(int(d) for d in str(n))
            return n
        
        total = reduce(year_sum) + reduce(month_sum) + reduce(day_sum)
        return reduce(total)
    
    def _get_season(self, month: int) -> str:
        """Determine the birth season (Northern Hemisphere)."""
        if month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Autumn'
        else:
            return 'Winter'
    
    def _get_day_meaning(self, weekday: int) -> str:
        """Get the traditional meaning of the birth day."""
        meanings = {
            0: "Monday's child is fair of face",
            1: "Tuesday's child is full of grace",
            2: "Wednesday's child is full of woe",
            3: "Thursday's child has far to go",
            4: "Friday's child is loving and giving",
            5: "Saturday's child works hard for a living",
            6: "Sunday's child is bonny and blithe"
        }
        return meanings.get(weekday, "A day of great potential")
