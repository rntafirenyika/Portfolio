# Returns the final exam points received by the students, in a dictionary format.
# If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
# If the submission was made over 3 hours after the start time, the submission is ignored.

import csv
from datetime import datetime, timedelta

def final_points():
    start_times = {}
    end_times = []
    subs = {}
    results = {}
    with open("start_times.csv") as my_file, open("submissions.csv") as sub:
        for line in csv.reader(my_file, delimiter=";"):
            start_times[line[0]] = line[1]
            subs[line[0]] = {}
        for line in csv.reader(sub, delimiter=";"):
            end_times.append(line)
            
    for times in end_times:
        if times[0] in start_times:
            time_diff = (datetime.strptime(times[3], "%H:%M") - datetime.strptime(start_times[times[0]], "%H:%M")).total_seconds() / 3600
            if time_diff < 3:
                if int(times[1]) not in subs[times[0]]:
                    subs[times[0]][int(times[1])] = int(times[2])
                elif int(times[1]) in subs[times[0]] and subs[times[0]][int(times[1])] < int(times[2]):
                    subs[times[0]][int(times[1])] = int(times[2])
                    
    for student, points in subs.items():
        results[student] = sum(points.values())
    
    return results