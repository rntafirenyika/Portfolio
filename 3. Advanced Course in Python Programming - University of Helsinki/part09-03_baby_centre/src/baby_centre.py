# Person class with name, age, height and weight attributes.
class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

# A BabyCentre object performs various actions on a Person object, for example, weigh or feed the person.
class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        self.number_of_weigh_ins += 1
        return person.weight
        
    def feed(self, person: Person):
        person.weight += 1
        
    def weigh_ins(self):
        return self.number_of_weigh_ins
