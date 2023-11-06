# asks the user to type in a number.
# Prints out the positive integers between 1 and the number itself, alternating between the two ends of the range.

num = int(input("Please type in a number: "))
output = []

for i in range(num):
    output.append(str(i+1))
size = len(output)

i = 1
if size % 2 != 0:
    loop_size = (size // 2) + 1
else:
    loop_size = size // 2
while i <= loop_size:
    if output[i-1] == output[size - i]:
        print(output[i-1])
    else:
        print(output[i-1])
        print(output[size - i])
    i += 1