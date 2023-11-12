# Class for a car with make and top speed attributes.
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# Takes a list of Car objects as its argument.
# Returns the make of the fastest car, assuming there will always be a single car with the highest top speed.        
def fastest_car(cars: list):
    fastest_make = ""
    fastest_speed = 0
    for car in cars:
        if car.top_speed > fastest_speed:
            fastest_speed = car.top_speed
            fastest_make = car.make
    return fastest_make
    
if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))