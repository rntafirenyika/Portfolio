# Returns the factorials of the numbers 1 to n in a dictionary.
# The number is the key, and the factorial of that number is the value mapped to it.

def calc_fact(n: int):
    if n == 1:
        return 1
    return n * calc_fact(n-1)

def factorials(n: int):
    facts = {}
    for i in range(1, n+1):
        facts[i] = calc_fact(i)
    return facts