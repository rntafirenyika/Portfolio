# Generator returns new prime numbers, one by one in sequence, from 2 onwards.
def prime_numbers():
    number = 2
    while True:
        factors = 0
        for i in range(1, number + 1):
            if number % i == 0:
                factors += 1
        if factors == 2: 
            yield number
        number += 1