# Prompt marks from user.
def get_marks():
    points = []
    exercises = []
    while True:
        marks = input("Exam points and exercises completed: ")
        if marks == "":
            break
        marks = marks.split()
        points.append(int(marks[0]))
        exercises.append(int(marks[1]))
    return points, exercises
    
# Convert exercises completed into exercise points
def exercise_points(mylist: list) -> list:
    exercise_points = []
    for i in mylist:
        if i == 100:
            exercise_points.append(10)
        elif i >= 90:
            exercise_points.append(9)
        elif i >= 80:
            exercise_points.append(8)
        elif i >= 70:
            exercise_points.append(7)
        elif i >= 60:
            exercise_points.append(6)
        elif i >= 50:
            exercise_points.append(5)
        elif i >= 40:
            exercise_points.append(4)
        elif i >= 30:
            exercise_points.append(3)
        elif i >= 20:
            exercise_points.append(2)
        elif i >= 10:
            exercise_points.append(1)
        else:
            exercise_points.append(0)
    return exercise_points

# Grade the exam points + exercise points. 
def grade(exam_points: list, exercise_points: list) -> list:
    grades = []
    for i in range(len(exam_points)):
        if exam_points[i] < 10:
            grades.append(0)
        elif (exam_points[i] + exercise_points[i]) >= 28:
            grades.append(5)
        elif (exam_points[i] + exercise_points[i]) >= 24:
            grades.append(4)
        elif (exam_points[i] + exercise_points[i]) >= 21:
            grades.append(3)
        elif (exam_points[i] + exercise_points[i]) >= 18:
            grades.append(2)
        elif (exam_points[i] + exercise_points[i]) >= 15:
            grades.append(1)
        elif (exam_points[i] + exercise_points[i]) <= 14:
            grades.append(0)
    return grades

# Prints out grade statistics for a university course.
def statistics():
    exam_pts, exercises = get_marks()
    exercise_pts = exercise_points(exercises)
    grades = grade(exam_pts, exercise_pts)
    total_points = []
    for i in range(len(exam_pts)):
        total_points.append(exam_pts[i] + exercise_pts[i])
    num_failed = grades.count(0)
    if num_failed != 0:
        passed = (len(grades) - num_failed) / len(grades) * 100
    else:
        passed = 100.0
    symbol = "*"
    print("Statistics:")
    print(f"Points average: {(sum(total_points)/len(exam_pts)):.1f}")
    print(f"Pass percentage: {passed:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"  {i}: {symbol * grades.count(i)}")
            
   
statistics()