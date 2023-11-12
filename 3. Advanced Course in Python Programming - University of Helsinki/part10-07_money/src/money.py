#Overloading operators
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{(self.__euros + (self.__cents/100)):.2f} eur"

    # Allows the use of == comparison operator on Money objects.        
    def __eq__(self, another):
        if self.__euros == another.__euros and self.__cents == another.__cents:
            return True
        return False

    # Allows the use of < (less than) comparison operator on Money objects.
    def __lt__(self, another):
        if (self.__euros + (self.__cents/100)) < (another.__euros + (another.__cents/100)):
            return True
        return False

    # Allows the use of > (greater than) comparison operator on Money objects.        
    def __gt__(self, another):
        if (self.__euros + (self.__cents/100)) > (another.__euros + (another.__cents/100)):
            return True
        return False

    # Allows the use the != (not equal to) comparison operator on Money objects.        
    def __ne__(self, another):
        if (self.__euros + (self.__cents/100)) != (another.__euros + (another.__cents/100)):
            return True
        return False

    # Allows the use of + (addition) comparison operator on Money objects.
    def __add__(self, another):
        euros = self.__euros + another.__euros
        cents = self.__cents + another.__cents
        if cents >= 100:
            euros += 1
            cents = cents - 100
        return Money(euros, cents)

    # Allows the use of - (subtraction) comparison operator on Money objects.        
    def __sub__(self, another):
        euros = self.__euros - another.__euros
        cents = self.__cents - another.__cents
        if cents < 0:
            euros -= 1
            cents = cents + 100
        if euros < 0:
            raise ValueError("A negative result is not allowed")
        return Money(euros, cents)