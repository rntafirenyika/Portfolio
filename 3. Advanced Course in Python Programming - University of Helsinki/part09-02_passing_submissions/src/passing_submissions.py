# Exam submission class with examinee and points attributes.
class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f'ExamSubmission (examinee: {self.examinee}, points: {self.points})'

#Takes a list of exam submissions and an integer number representing the lowest passing grade as its arguments.
#Returns a new list, which contains only the passed submissions from the original list.        
def passed(submissions: list, lowest_passing: int):
    results = []
    for submission in submissions:
        if submission.points >= lowest_passing:
            results.append(submission)
    return results
    
if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)