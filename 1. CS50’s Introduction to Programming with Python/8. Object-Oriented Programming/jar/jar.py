"""
Implementation of a class called Jar in which to store cookies.
Methods included in the class are __init__, __str__, deposit, withdraw, capacity and size.
"""

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if n + self.size > self.capacity :
            raise ValueError("Deposit will exceed capacity")
        else:
            self.size += n
        return self.size


    def withdraw(self, n):
        if self.size - n < 0 :
            raise ValueError("Withdrawal exceeds available cookies")
        else:
            self.size -= n
        return self.size


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != int or capacity < 0:
            raise ValueError("Capacity not valid")
        self._capacity = capacity


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        self._size = size




jar = Jar()
