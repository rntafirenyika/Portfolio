# Asks for the names of the input files. Output is written to the files. The user will only see a message confirming this.

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

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_data = input("Course information: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_data = "course1.txt"


info = {}    
with open(student_info) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        info[parts[0].strip()] = f"{parts[1].strip()} {parts[2].strip()}"
        
exercises = {}
with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0].strip()] = []
        for grade in parts[1:]:
            exercises[parts[0].strip()].append(int(grade))       

exams = {}
with open(exam_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exams[parts[0].strip()] = []
        for points in parts[1:]:
            exams[parts[0].strip()].append(int(points))

header = []
with open(course_data) as cfile, open("results.txt", "w") as rtxt, open("results.csv", "w") as rcsv:
    for row in cfile:
        header.append(row.strip().split(":"))
    rtxt.write(f"{header[0][1].strip()}, {header[1][1].strip()} credits\n")

    rtxt.write("======================================\n")

    rtxt.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")

    for id, name in info.items():
        if id in exercises:
            es_points = get_exercise_points(sum(exercises[id]))
            em_points = sum(exams[id])
            total_points = es_points + em_points
            rtxt.write(f"{name:30}{sum(exercises[id]):<10}{es_points:<10}{em_points:<10}{total_points:<10}{grading(total_points):<10}\n")
            rcsv.write(f"{id};{name};{grading(total_points)}\n")
        else:
            rxtx.write(f"{name} 0\n")
