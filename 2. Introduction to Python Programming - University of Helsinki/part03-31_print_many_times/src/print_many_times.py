# Takes a string and an integer as arguments.
# The integer argument specifies how many times the string argument should be printed out.
def print_many_times(text, times):
    for i in range(times):
        print(text)
# test function
if __name__ == "__main__":
    print_many_times("python", 5)