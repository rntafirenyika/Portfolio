# class for statistics on numbers entered
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    # Adds a new number to the statistical record.
    def add_number(self, number:int):
        self.count += 1
        self.numbers += number

    # Returns the count of how many numbers have been added.
    def count_numbers(self):
        return self.count

    # Returns the sum of the numbers added (if no numbers have been added, returns 0).        
    def get_sum(self):
        return self.numbers

    # Returns the mean of the numbers added (if no numbers have been added, returns 0).        
    def average(self):
        if self.numbers == 0:
            return 0
        else:
            return self.numbers / self.count


stats = NumberStats()
evens = NumberStats()
odds = NumberStats()

# Prompt user for input.
print("Please type in integer numbers:")
while True:
        number = int(input())
        if number == -1:
            break
        if number % 2 == 0:
            evens.add_number(number)
        else:
            odds.add_number(number)
        stats.add_number(number)

# Print statistics.        
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", evens.get_sum())
print("Sum of odd numbers:", odds.get_sum())