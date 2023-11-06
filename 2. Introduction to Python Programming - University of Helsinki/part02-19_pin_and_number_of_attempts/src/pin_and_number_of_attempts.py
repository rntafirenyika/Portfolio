# Keeps asking the user for a PIN code until they type in the correct one, which is 4321.

attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1

    if code == "4321":
        break

    print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")