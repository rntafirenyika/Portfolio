class Pet:
    # Pet class constructor
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

# Creates and return a new object of type Pet, as defined in the class Pet.        
def new_pet(name: str, species: str, year_of_birth: int):
    newpet = Pet(name, species, year_of_birth)
    return newpet