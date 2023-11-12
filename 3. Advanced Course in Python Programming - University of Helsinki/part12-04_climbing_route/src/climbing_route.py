class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

#Returns a new list of routes, sorted by length from longest to shortest.
def sort_by_length(routes: list):
    def order_by_length(route: ClimbingRoute):
        return route.length
        
    return sorted(routes, key=order_by_length, reverse=True)

#Returns a new list of routes, sorted by difficulty, i.e. grade, from hardest to easiest then by lenght if the grades are the same.
def sort_by_difficulty(routes: list):
    def order_by_grade(route: ClimbingRoute):
        return (route.grade, route.length)
                
    return sorted(routes, key=order_by_grade, reverse=True)