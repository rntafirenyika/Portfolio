"""
Tip calculator
"""

def main():
    """
    Calculates a tip after a meal based on a percentage of how much the meal cost.
    """
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Accepts a string as input (formatted as $##.##, wherein each # is a decimal digit),
    removes the leading $,
    and return the amount as a float. For instance, given $50.00 as input, it returns 50.0.
    """
    d = d.replace("$", "")
    return float(d)


def percent_to_float(p):
    """
     accept a str as input (formatted as ##%, wherein each # is a decimal digit),
     removes the trailing %,
     and return the percentage as a float. For instance, given 15% as input, it returns 0.15.
    """
    p = p.replace("%", "")
    return float(p) / 100


main()