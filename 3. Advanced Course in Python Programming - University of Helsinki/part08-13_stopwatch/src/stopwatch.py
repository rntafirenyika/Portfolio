class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.count = 0

    # Returns a string representation of the state of the stopwatch
    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"

    # Adds one second to the stopwatch.
    def tick(self):
        self.count += 1
        if self.count == 3600:
            self.count = 0
        self.minutes = self.count // 60 
        self.seconds = self.count % 60
