# Real property class with methods which allow for comparison between available properties.
class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    # Returns True if the RealProperty object itself is bigger than the one it is compared to.
    def bigger(self, compared_to: "RealProperty"):
        return self.square_metres > compared_to.square_metres

    # Returns the difference in price between the RealProperty object itself and the one it is compared to.        
    def price_difference(self, compared_to: "RealProperty"):
        return abs((self.square_metres * self.price_per_sqm) - (compared_to.square_metres * compared_to.price_per_sqm))

    # Returns True if the RealProperty object itself is more expensive that the one it is compared to.
    def more_expensive(self, compared_to: "RealProperty"):
        return (self.square_metres * self.price_per_sqm) > (compared_to.square_metres * compared_to.price_per_sqm)
        
