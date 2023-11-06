#Asks the user for four numbers, then prints out the sum and the mean of the numbers.
sum = 0
sum += int(input("Number 1: "))
sum += int(input("Number 2: "))
sum += int(input("Number 3: "))
sum += int(input("Number 4: "))
mean = sum / 4
print(f"The sum of the numbers is {sum} and the mean is {mean}")