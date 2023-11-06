# Get course data from Helsinki University and summarise.

import urllib.request
import json

def retrieve_all():
    active_courses = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    for course in courses:
        if course["enabled"]:
            active_courses.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))
    return active_courses

def retrieve_course(course_name: str):    
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    course_data = json.loads(my_request.read())

    summary = {}

    max_students = 0
    total_hours = 0
    sum_students = 0
    exercise_total = 0
    for week, data in course_data.items():
        total_hours += data['hour_total']
        sum_students += data['students']
        exercise_total += data['exercise_total']
        if data['students'] > max_students:
            max_students = data['students']

    summary['weeks'] = len(course_data)
    summary['students'] = max_students
    summary ['hours'] = total_hours
    summary['hours_average'] = total_hours // max_students
    summary['exercises'] = exercise_total
    summary['exercises_average'] = exercise_total // max_students

    return summary