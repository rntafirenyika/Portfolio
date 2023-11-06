#Program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a specific period of time.

from datetime import datetime, timedelta
 
filename  = input("Filename: ")
sdate =   datetime.strptime(input("Starting date: "), "%d.%m.%Y")
days = int(input("How many days: "))
edate = sdate + timedelta(days=days-1)
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
minutes = []
data = []
for i in range(days):
    day = sdate + timedelta(days=i)
    screentime = input(f"Screen time {day.strftime('%d.%m.%Y')}: ")
    minutes += [int(m) for m in screentime.split()]
    data.append(f"{day.strftime('%d.%m.%Y')}: {screentime. replace(' ', '/')}")
 
total = sum(minutes )
average = total / days
 
with open(filename, "w") as file:
    file.write(f"Time period: {sdate.strftime('%d.%m.%Y')}-{edate.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {average}\n")
    for d in data:
        file.write(f"{d}\n")