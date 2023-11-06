# Any student whose any task was handed in over 3 hours later than their exam start time is labelled a cheater.

import csv
from datetime import datetime, timedelta

def cheaters():
    start_times = []
    end_times = []
    cheaters = []
    with open("start_times.csv") as my_file, open("submissions.csv") as sub:
        for line in csv.reader(my_file, delimiter=";"):
            start_times.append(line)
        for line in csv.reader(sub, delimiter=";"):
            end_times.append(line)
    for student in start_times:
        for times in end_times:
            if student[0] == times[0]:
                time_diff = (datetime.strptime(times[3], "%H:%M") - datetime.strptime(student[1], "%H:%M")).total_seconds() / 3600
                if time_diff > 3 and student[0] not in cheaters:
                    cheaters.append(student[0])
    return cheaters