from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Takes a list of course attempts as its argument.
# Sums up the total number of study credits covered by the courses.
def sum_of_all_credits(attempts: list):
    return reduce(lambda sum, x: sum + x.credits, attempts, 0)

# Takes a list of course attempts as its argument.
# Sums up the credits for the course attempts with grade 1 or above.  
def sum_of_passed_credits(attempts: list):
    return reduce(lambda sum, x: sum + x.credits, filter(lambda x: x.grade > 1, attempts), 0)

# Takes a list of course attempts as its argument.
# Calculates the average grade for the course attempts with grade 1 or above.
def average(attempts: list):
    passed = list(filter(lambda x: x.grade > 1, attempts))
    return reduce(lambda sum, x: sum + x.grade, passed, 0) / len(passed)