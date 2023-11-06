#Asks for the hourly wage, hours worked, and the day of the week. Prints out the daily wages.

rate = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")

if day.lower() == "sunday":
    wages = rate * hours * 2
else:
    wages = rate * hours

print(f"Daily wages: {wages} euros")