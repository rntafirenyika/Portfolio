# Takes three dictionary objects as its arguments.
# Calculates the average of the three results for each contestant, and returns the contestant whose average result was the smallest.

import math

def smallest_average(person1: dict, person2: dict, person3: dict):
    results = [person1, person2, person3]
    s_average = positive_infinity = math.inf
    smallest = 0
    for result in results:
        total = 0
        for i in range(1,4):
            total += result[f"result{i}"]
        average = total / 3
        if average < s_average:
           s_average = average
           smallest = result
    return smallest
