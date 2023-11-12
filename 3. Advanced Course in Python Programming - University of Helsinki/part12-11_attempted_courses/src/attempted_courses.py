class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Takes a list of CourseAttempt objects as its argument.
# Returns a new list with the names of the students who have attempted the course using map function.
def names_of_students(attempts: list):
    return list(map(lambda attempt: attempt.student_name, attempts))

# Takes a list of CourseAttempt objects as its argument. 
# Returns a new list containing the names of the courses on the original list in alphabetical order.
def course_names(attempts: list):
    return list(sorted(set(map(lambda attempt: attempt.course_name, attempts))))