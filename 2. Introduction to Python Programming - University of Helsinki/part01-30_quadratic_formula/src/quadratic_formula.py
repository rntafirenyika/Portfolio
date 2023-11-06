# Program for solving a quadratic equation of the form ax²+bx+c. Asks for values a, b and c.

from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

x1 = (-b + sqrt((b**2)-4*a*c))/(2*a)
x2 = (-b - sqrt((b**2)-4*a*c))/(2*a)

print(f"The roots are {x1} and {x2}")