# Takes a list of strings as its argument.
# The function finds and returns the longest string in the list.
def longest(strings: list):
    longest = 0
    lstring = ""
    for i in range(len(strings)):
        if len(strings[i]) > longest:
            lstring = strings[i]
            longest = len(strings[i])
    return lstring
    
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))