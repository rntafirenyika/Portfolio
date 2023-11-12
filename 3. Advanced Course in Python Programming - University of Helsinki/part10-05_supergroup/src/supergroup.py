#class with protected attributes

# class definition for a SuperHero.
class SuperHero:
    # Constructor which takes the name and superpowers of the super hero as arguments.
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup:
    # Constructor which takes the name and location of the group as arguments, in that order.
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []

    # Getter method for the name attribute.
    @property
    def name(self):
        return self._name

    # Getter method for the location attributes.
    @property
    def location(self):
        return self._location

    # Adds a new member to the group.
    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    # Prints out information about the group and its members.
    def print_group(self):
        print(f"{self._name}, {self._location}")
        print("Members:")
        for member in self._members:
            print(member)