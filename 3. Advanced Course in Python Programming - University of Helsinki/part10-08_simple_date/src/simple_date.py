# Implementing a class to handle dates assuming that each month has 30 days 
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    # Allows user to check if two dates are equal, returns True if the dates are the same otherwise returns False.        
    def __eq__(self, other: "SimpleDate"):
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        return False

    # Allows user to check if two dates are not equal, returns True if the dates are not equal otherwise returns False.
    def __ne__(self, other: "SimpleDate"):
        if self.day != other.day or self.month != other.month or self.year != other.year:
            return True
        return False

    # Allows user to check if a date comes before another date(less than), returns True if that is the case otherwise returns False.
    def __lt__(self, other: "SimpleDate"):
        if self.year < other.year or (self.year == other.year and self.month < other.month) or (self.year == other.year and self.month == other.month and self.day < other.day) :
            return True
        return False

    # Allows user to check if a date comes after another date(greater than), returns True if that is the case otherwise returns False.        
    def __gt__(self, other: "SimpleDate"):
        if self.year > other.year or (self.year == other.year and self.month > other.month) or (self.year == other.year and self.month == other.month and self.day > other.day) :
            return True
        return False

    # Allows user to add a given number of days to a SimpleDate object, returns a new SimpleDate object.
    def __add__(self, days: int):
        day = self.day + days
        month = self.month
        year = self.year
        if day > 30:
            month = month + (day // 30)
            day = day % 30
        if month > 12:
            year = year + (month // 12)
            month = month % 12
        return SimpleDate(day, month, year)

    # Allows user to find out the difference in days between two SimpleDate objects.
    def __sub__(self, other: "SimpleDate"):
        self_AD_in_days = (self.year * 12 * 30) + (self.month * 30) + self.day
        other_AD_in_days = (other.year * 12 * 30) + (other.month * 30) + other.day
        return abs(self_AD_in_days - other_AD_in_days)