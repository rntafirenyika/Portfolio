#Implementation of Person and Room classes. Can add any number of persons to a room, and search for and remove the shortest person in the room.
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

# Room class with a list of persons as an attribute.     
class Room:
    def __init__(self):
        self.persons = []
        self.total = 0

    # Adds the person given as an argument to the room.        
    def add(self, person: Person):
        self.persons.append(person)
        self.total += person.height

    # Returns True or False depending on whether the room is empty.        
    def is_empty(self):
        return len(self.persons) == 0

    # Prints out the contents of the list of persons in the room.        
    def print_contents(self):
        if not self.is_empty():
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.total} cm")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")

    # Returns the shortest person in the room it is called on.
    def shortest(self):
        if not self.is_empty():
            shortest_person = self.persons[0]
            shortest_height = self.persons[0].height
            for person in self.persons:
                if person.height < shortest_height:
                    shortest_person = person
                    shortest_height = person.height
            return shortest_person
        return None

    # Removes the shortest Person object from the room and return the reference to the object.    
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.total -= shortest_person.height
            self.persons.remove(shortest_person)
        return shortest_person