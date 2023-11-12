# Car class with two private, encapsulated variables.
class Car:
    def __init__(self):
        self.__fuel = 0
        self.__odometer = 0

    # Returns a string representation of the car.
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km,\npetrol remaining {self.__fuel} litres"

    # Which fills up the tank.    
    def fill_up(self):
        self.__fuel = 60

    # Drives the car for the distance indicated, or for however long the petrol in the tank allows.
    def drive(self, km:int):
        if self.__fuel >= km:
            self.__odometer += km
            self.__fuel -= km
        else:
            self.__odometer += self.__fuel
            self.__fuel -= self.__fuel