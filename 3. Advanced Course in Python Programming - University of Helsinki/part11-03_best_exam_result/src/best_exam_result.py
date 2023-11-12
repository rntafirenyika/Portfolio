class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')

# Takes a list of ExamResult objects as its argument.
# Returns a new list containing only the best result from each ExamResult object.
def best_results(results: list):
    return [max([result.grade1, result.grade2, result.grade3]) for result in results]
