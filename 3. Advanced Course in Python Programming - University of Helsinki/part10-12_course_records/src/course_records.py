# Interactive application for keeping track of a person's studies.

# Course class for course details with course name, grade and credits attributes.
class Course:
    def __init__(self, course: str, grade: int, credits: int):
        self._course = course
        self._grade = grade
        self._credits = credits

    def course(self):
        return self._course
        
    def grade(self):
        return self._grade
        
    def credits(self):
        return self._credits
        
    def add_grade(self, grade: str):
        if grade > self._grade:
            self._grade = grade

# CourseRecords class for handling various courses.        
class CourseRecords:
    def __init__(self):
        self.__courses = {}

    def add_course(self, course: str, grade: int, credits: int):
        if not course in self.__courses:
            self.__courses[course] = None
            self.__courses[course] = Course(course, grade, credits)
        elif self.__courses[course].grade() < grade:
            self.__courses[course].add_grade(grade)
        
    def get_entry(self, course: str):
        if not course in self.__courses:
            return None
        return self.__courses[course].course(), self.__courses[course].grade(), self.__courses[course].credits()

    def statistics(self):
        grades = []
        total_grades = 0
        total_credits = 0
        num_courses = len(self.__courses)
        for key, course in self.__courses.items():
            grade = course.grade()
            credit = course.credits()
            grades.append(grade)
            total_grades += grade
            total_credits += credit
        mean = total_grades / num_courses
        mean_str = f"{mean:.1f}" if mean % 1 != 0 else f"{int(mean)}"
        
        print(f"{num_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_str}")
        print("grade distribution")
        for i in range(5, 0, -1):
            print(f"{i}: {'x' * grades.count(i)}")
        
    def all_entries(self):
        return self.__courses

# CourseApplication class for handling data entry and searching.
class CourseApplication:
    def __init__(self):
        self.__database = CourseRecords()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__database.add_course(course, grade, credits)

    def search(self):
        course = input("course: ")
        if self.__database.get_entry(course) != None:
            dcourse, dgrade, dcredits = self.__database.get_entry(course)
            print(f"{dcourse} ({dcredits} cr) grade {dgrade}")
        else:
            print("no entry for this course")
                
    def statistics(self):
        self.__database.statistics() 
            
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.statistics()

application = CourseApplication()
application.execute()