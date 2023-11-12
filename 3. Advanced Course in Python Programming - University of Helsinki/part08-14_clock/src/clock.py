class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    # Returns a string representation of the state of the stopwatch.
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    # Sets new values for the hours and the minutes, and sets the seconds to zero.
    def set(self, hours: int, minutes: int):
        self.seconds = 0
        self.minutes = minutes
        self.hours = hours

    # Adds one second to the stopwatch. The maximum value for both seconds and minutes is 59.
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
