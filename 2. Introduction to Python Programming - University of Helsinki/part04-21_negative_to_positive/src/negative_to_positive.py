# Asks the user for a positive integer N.
# Prints out all numbers between -N and N inclusive, but leaves out the number 0.

num = int(input('Please type in a positive integer:\n'))

for i in range(-num, num+1):
    if i != 0:
        print(i)