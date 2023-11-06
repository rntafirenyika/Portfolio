# Asks the user for an integer number. If the number is divisible by three, prints out Fizz.
# If the number is divisible by five, prints out Buzz.
# If the number is divisible by both three and five, prints out FizzBuzz.

num = int(input("Number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")