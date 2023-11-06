#Asks the user for the names of the files, process the files and print out a grade for each student.

# Calculate exercise points
def get_exercise_points(points: int) -> int:
    i = (points / 40 * 100)
    if i == 100:
        return 10
    elif i >= 90:
        return 9
    elif i >= 80:
        return 8
    elif i >= 70:
        return 7
    elif i >= 60:
        return 6
    elif i >= 50:
        return 5
    elif i >= 40:
        return 4
    elif i >= 30:
        return 3
    elif i >= 20:
        return 2
    elif i >= 10:
        return 1
    else:
        return 0

# Converts points to grades
def grading(points: int) -> int:
    if points >= 28:
            return 5
    elif points >= 24:
            return 4
    elif points >= 21:
            return 3
    elif points >= 18:
            return 2
    elif points >= 15:
            return 1
    elif points <= 14:
            return 0

# Prompt user for the information.
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

# Reads data from the student_info file
info = {}    
with open(student_info) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        info[parts[0].strip()] = f"{parts[1].strip()} {parts[2].strip()}"

# Reads data from the exercise_data file       
exercises = {}
with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0].strip()] = []
        for grade in parts[1:]:
            exercises[parts[0].strip()].append(int(grade))       

# Reads data from the exam_data file
exams = {}
with open(exam_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[parts[0].strip()] = []
        for points in parts[1:]:
            exams[parts[0].strip()].append(int(points))

# Prints out the processed info.
for id, name in info.items():
    if id in exercises:
        total_points = get_exercise_points(sum(exercises[id])) + sum(exams[id])
        print(f"{name} {grading(total_points)}")
    else:
        print(f"{name} 0")