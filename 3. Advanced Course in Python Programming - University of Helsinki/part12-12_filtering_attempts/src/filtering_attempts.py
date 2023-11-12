class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Takes a list of CourseAttempt objects as its argument.
# Returns a new list of CourseAttempt objects, including only those items from the original list whose grade is at least 1.
def accepted(attempts: list):
    return filter(lambda x: x.grade >= 1, attempts)

# Takes a list of CourseAttempt objects and an integer as its arguments.
# Returns a new list containing only those CourseAttempt objects from the original list whose grade matches the second argument.    
def attempts_with_grade(attempts: list, grade: int):
    return filter(lambda x: x.grade == grade, attempts)

# Takes a list of CourseAttempt objects and a course name as its arguments.
# Returns an alphabetically ordered list of names of those students who passed the course.
def passed_students(attempts: list, course: str):
    return sorted(map(lambda x: x.student_name, filter(lambda x: x.grade > 0 and x.course_name == course, attempts)))