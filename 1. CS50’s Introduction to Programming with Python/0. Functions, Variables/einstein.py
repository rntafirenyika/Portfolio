"""
Prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer.
It is assumed that the user will input an integer.
"""
#Prompt user for mass in kilograms
m = int(input("Please enter mass in Kilograms. \n"))
e = m * (300000000 ** 2)
print(e)