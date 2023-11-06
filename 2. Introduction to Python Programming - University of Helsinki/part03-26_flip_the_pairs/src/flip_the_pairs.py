# Asks the user to type in a number, prints out all the positive integer values from 1 up to the number.

num = int(input("Please type in a number: "))
output = []

for i in range(num):
    output.append(str(i+1))

i = 0
while i < len(output):
    if (i+1) > len(output) - 1:
        pass
    else:
        print(output[i+1])
    print(output[i])
    i += 2