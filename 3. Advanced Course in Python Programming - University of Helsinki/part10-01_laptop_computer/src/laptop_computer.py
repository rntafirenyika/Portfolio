#class named LaptopComputer which inherits the class Computer.

# Computer class which has the attributes model and speed.
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

# Inherits the class Computer, take a third argument, weight.    
class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        super().__init__(model, speed)
        self.__weight = weight
        
    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.__weight} kg"