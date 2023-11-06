#Reads a JSON file in the above format, and prints the contents in an easy to read format.

import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    students = json.loads(data)

    for student in students:
        if student['hobbies']:
            print(f"{student['name']} {student['age']} years (", end ="")
            for hobby in student['hobbies']:
                if hobby == student['hobbies'][-1]:
                    print(f"{hobby})")
                else:
                    print(f"{hobby}, ", end="")
        else:
            print(f"{student['name']} {student['age']} years ()")