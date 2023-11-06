"""
Prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value,
formatted to one decimal place.
"""

def main():
    """
    It is assumed that the user's input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:
    x is an integer
    y is +, -, *, or /
    z is an integer
    For instance, if the user inputs 1 + 1, the program outputs 2.0. It is assumed that, if y is /, then z will not be 0.
    """

    #Prompting for user's input, interpretting the arithmetic expression and printing the answer.
    expression = input("Expression: \n")
    answerform = float("{:.1f}".format(answer(expression)))
    print(answerform)


def answer(expression):
    #Math interpreter for the user's arithmetic expression.
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "/":
        return float(x / z)
    elif y == "*":
        return float(x * z)
    else:
        return "That is not a correct math sign."


main()

