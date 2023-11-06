#Asks the user for the names of two files, reads the files, and then prints out the total number of exercises completed by each student.
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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
        exercises[parts[0]] = []
        for grade in parts[1:]:
            exercises[parts[0].strip()].append(int(grade))       


for id, name in info.items():
    if id in exercises:
        num_exercises = sum(exercises[id])
        print(f"{name} {num_exercises}")
    else:
        print(f"{name} 0")