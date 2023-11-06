# Asks the user to type in a limit.
# Calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user.

limit = int(input("Upper limit: "))
runsum = 0
total = 0

while total < limit:
    runsum += 1
    total += runsum

print(f"{total}")