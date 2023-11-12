# Item class which is used to create items of different kinds.
class Item:
    # Constructor which takes the name and weight of an item as an argument.
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    # Returns the name of the item.        
    def name(self):
        return self.__name

    # Returns the weight of the item.
    def weight(self):
        return self.__weight

# Suitcase for packing items into a suitcase. It also has a maximum combined weight for the items stored within.
class Suitcase:
    # Constructor which takes the maximum weight as an argument.
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    # Returns a string in the format "x items (y kg)".    
    def __str__(self):
        current_weight = self.weight()
        num_items = len(self.__items)
        if num_items == 1:
            return f"{num_items} item ({current_weight} kg)"
        return f"{num_items} items ({current_weight} kg)"

    # Adds the item given as an argument to the suitcase.
    def add_item(self, new_item: Item):
        current_weight = self.weight()       
        if new_item.weight() + current_weight <= self.__max_weight:
            self.__items.append(new_item)

    # Prints out all the items stored in the suitcase.
    def print_items(self):
        for item in self.__items:
            print(item)

    # Returns an integer number representing the combined weight of all the items stored in the suitcase.
    def weight(self):
        current_weight = 0
        if self.__items:
            for item in self.__items:
                current_weight += item.weight()
        return current_weight

    # Returns the Item which is the heaviest.        
    def heaviest_item(self):
        if self.__items:
            heaviest = None
            kgs = 0
            for item in self.__items:
                if item.weight() > kgs:
                    heaviest = item
                    kgs = item.weight()
            return heaviest
        return None
        
class CargoHold:
    # Constructor which takes the maximum weight as an argument.
    def __init__(self, cargo_max_weight: int):
        self.__cargo_max_weight = cargo_max_weight
        self.__cargo_items = []

    # Returns a string in the format "x suitcases, space for y kg".
    def __str__(self):
        current_weight = self.cargo_weight()
        num_items = len(self.__cargo_items)
        space = self.__cargo_max_weight - current_weight
        if num_items == 1:
            return f"{num_items} suitcase, space for {space} kg"
        return f"{num_items} suitcases, space for {space} kg"

    # Adds the suitcase given as an argument to the cargo hold.
    def add_suitcase(self, new_suitcase: Suitcase):
        current_weight = self.cargo_weight()       
        if new_suitcase.weight() + current_weight <= self.__cargo_max_weight:
            self.__cargo_items.append(new_suitcase)

    # Returns the cargo weight.            
    def cargo_weight(self):
        current_weight = 0
        if self.__cargo_items:
            for suitcase in self.__cargo_items:
                current_weight += suitcase.weight()
        return current_weight

    # Prints out all the items in all the suitcases within the cargo hold.
    def print_items(self):
        for suitcase in self.__cargo_items:
            suitcase.print_items()