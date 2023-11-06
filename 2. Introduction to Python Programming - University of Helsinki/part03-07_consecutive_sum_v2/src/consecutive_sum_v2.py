# Asks the user to type in a limit.
# Calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user.
# Prints out the calculation performed.

limit = int(input("Upper limit: "))
runsum = 0
total = 0
strtotal = []
cons = ""

while total < limit:
    runsum += 1
    total += runsum
    strtotal.append(runsum)

for i in strtotal:
    if i == strtotal[-1]:
        cons += str(i)
    else:
        cons += str(i) + " + "
print(f"The consecutive sum: {cons} = {total}")