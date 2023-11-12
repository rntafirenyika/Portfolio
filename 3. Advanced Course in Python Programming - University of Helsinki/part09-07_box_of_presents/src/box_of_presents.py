# Present class which can be used to represent different kinds of presents.
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

# Box class to add presents to the box, and the box keeps track of the combined weight of the presents within.
class Box:
    def __init__(self):
        self.presents = []

    # Adds the present given as an argument to the box.        
    def add_present(self, present: Present):
        self.presents.append(present)

    # Returns the combined weight of the presents in the box.        
    def total_weight(self):
        box_weight = 0
        for present in self.presents:
            box_weight += present.weight
        return box_weight