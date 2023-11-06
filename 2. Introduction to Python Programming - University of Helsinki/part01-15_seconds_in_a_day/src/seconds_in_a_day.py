#Asks the user for a number of days, then prints out the number of seconds in the amount of days given.
days = int(input("How many days? "))
print(f"Seconds in that many days: {days * 24 * 60 * 60}")