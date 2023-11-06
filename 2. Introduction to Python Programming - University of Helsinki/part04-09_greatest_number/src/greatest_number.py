# Takes three arguments, returns the greatest in value of the three.
def greatest_number(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z and y >= x:
        return y
    elif z >= x and z >= y:
        return z

# test function
if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)