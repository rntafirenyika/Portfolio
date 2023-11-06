#Asks the user for their date of birth, and then prints out how old the user was on the eve of the new millennium.

from datetime import datetime
 
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
 
millennium_eve = datetime(1999,  12, 31)
dob = datetime(year, month, day)
 
difference = millennium_eve - dob
 
if difference.days > 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")