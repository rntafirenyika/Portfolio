# Asks for the amount of points received and then prints out the grade attained according to the table.

p = int(input("How many points [0-100]: "))

if p > 100 or p < 0:
    print("Grade: impossible!")
elif p >= 90:
    print("Grade: 5")
elif p >= 80:
    print("Grade: 4")
elif p >= 70:
    print("Grade: 3")
elif p >= 60:
    print("Grade: 2")
elif p >= 50:
    print("Grade: 1")
elif p < 50:
    print("Grade: fail")