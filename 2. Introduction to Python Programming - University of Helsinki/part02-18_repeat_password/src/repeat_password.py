# Asks the user for a password.
# Keeps on asking until the user types the first password again correctly.

pwd1 = input("Password: ")
while True:
    pwd2 = input("Repeat password: ")
    if pwd1 == pwd2:
        print("User account created!")
        break
    print("They do not match!")