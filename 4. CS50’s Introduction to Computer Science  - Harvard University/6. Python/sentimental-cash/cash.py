def main():
    # Prompt the user for the change owed, calculate and print the number of coins.
    change_owned = get_cents()
    quarters = calculate_quarters(change_owned)
    dimes = calculate_dimes(change_owned - (quarters*0.25))
    nickels = calculate_nickels(change_owned - (quarters*0.25) - (dimes*0.10))
    pennies = calculate_pennies(change_owned - (quarters*0.25) - (dimes*0.10) - (nickels*0.05))
    print(quarters + dimes + nickels + pennies)


def get_cents():
    # Prompt the user for the change owed until a positive number is given.
    while True:
        try:
            change = float(input("Change owed: "))
            if change > 0:
                return change
        except (TypeError, ValueError):
            pass


def calculate_quarters(change_owned):
    # Calculates and returns as an int, how many quarters a customer should be given if they’re owed some number of cents.
    return int(round(change_owned, 2) / 0.25)


def calculate_dimes(change_owned):
    # Calculates and returns as an int, how many dimes a customer should be given if they’re owed some number of cents.
    return int(round(change_owned, 2) / 0.10)


def calculate_nickels(change_owned):
    # Calculates and returns as an int, how many nickels a customer should be given if they’re owed some number of cents.
    return int(round(change_owned, 2) / 0.05)


def calculate_pennies(change_owned):
    # Calculates and returns as an int, how many pennies a customer should be given if they’re owed some number of cents.
    return int(round(change_owned, 2) / 0.01)


if __name__ == "__main__":
    main()