def main():
    # Prompting the user for the card number until only numbers are entered.
    while True:
        cardnum = input("Number: ")
        if cardnum.isnumeric() == True:
            break
    length_validity = check_length(cardnum)
    luhn_algo_check = check_luhn(cardnum)

    # Checking the the card number prefix and length validity then printing out the issuer.
    if int(cardnum[:1]) == 4 and length_validity == True and luhn_algo_check == True:
        print("VISA")
    elif int(cardnum[:2]) in [34, 37] and length_validity == True and luhn_algo_check == True:
        print("AMEX")
    elif int(cardnum[:2]) in [51, 52, 53, 54, 55] and length_validity == True and luhn_algo_check == True:
        print("MASTERCARD")
    else:
        print("INVALID")


def check_length(cardnum):
    # Checking if the length of the card number is valid.
    if len(cardnum) in [13, 15, 16]:
        return True
    else:
        return False


def check_luhn(cardnum):
    # Checking if Luhn's Algorithm holds.
    reverse_cardnum = cardnum[::-1]
    every_other_digit = reverse_cardnum[1::2]

    """ Multiplying every other digit by 2, starting with the card number's second-to-last digit,
    and then add those products' digits together."""
    every_other_digit = list(every_other_digit)
    mutiplied_digits = list("".join([str(int(i)*2) for i in every_other_digit]))
    sum_mutiplied_digits = sum([int(i) for i in mutiplied_digits])

    # Sum of the digits that weren't mutiplied by 2.
    remaining_digits = reverse_cardnum[0::2]
    sum_remaining_digits = sum([int(i) for i in remaining_digits])

    # Adding the two sums and checking if divisible by 10 without a remainder.
    if (sum_remaining_digits + sum_mutiplied_digits) % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()