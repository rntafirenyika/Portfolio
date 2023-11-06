# Adds a new student to the database.
def add_student(students: dict, name: str):
    students[name] = []

# Prints out a summary based on all the information stored in the database.
def print_student(students: dict, name: str):
    if name not in students:
            print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")
        courses = students[name]
        if courses == []:
            print(" no completed courses")
        else:
            number = len(courses)
            print(f" {number} completed courses:")
            grades = 0
            for course in courses:
                print(f"  {course[0]} {course[1]}")
                grades += course[1]
            average = grades / number
            print(f" average grade {average}")

# Adds a completed course to the information of a specific student in the database.
# The course data is a tuple consisting of the name of the course and the grade.        
def add_course(students: dict, name: str, course):
    #Ignore courses with grade 0
    if course[1] != 0:
        courses = students[name]
        c_title = []
        for s_course in courses:
            c_title.append(s_course[0])
        if course[0] not in c_title:
            students[name].append(course)
        else:
            for existing_course in courses:
                # if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.
                if existing_course[0] == course[0] and existing_course[1] < course[1]:
                    students[name].remove(existing_course)
                    students[name].append(course)

# Summary based on all the information stored in the database.
def summary(students: dict):
    most_courses = 0
    most_student = ""
    best_ave = 0
    best_student = ""
    for student in students:
        course_count = len(students[student])
        if  course_count > most_courses:
            most_courses = course_count
            most_student = student
        grades = 0
        for course in students[student]:
            grades += course[1]
        average = grades / course_count
        if  average > best_ave:
            best_ave = average
            best_student = student
            
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses} {most_student}")
    print(f"best average grade {best_ave} {best_student}")
