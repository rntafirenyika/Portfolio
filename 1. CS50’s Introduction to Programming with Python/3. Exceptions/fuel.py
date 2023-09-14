"""
Prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If 1% or less remains, output E instead to indicate that the tank is essentially empty. If 99% or more remains, output F instead to indicate that the tank is essentially full.
Catch any exceptions like ValueError or ZeroDivisionError.
"""
def main():
    fra = input("Fraction: ")
    p = convert(fra)
    print(gauge(p))


def convert(fraction):
    while True:
        try :
            x,y = fraction.split("/")
            z = round(int(x) / int(y) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if z > 100 :
                pass
            else:
                break
    return z


def gauge(percentage):
    if percentage <= 1 :
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()