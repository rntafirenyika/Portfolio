# Takes one string and two integers as arguments.
# Returns True if the two characters at the indexes specified are the same.
# Otherwise, and especially if either of the indexes falls outside the scope of the string, returns False.
def same_chars(text, ind1, ind2):
    if ind1 + 1 > len(text) or ind2 + 1 > len(text):
        return False
    elif text[ind1] == text[ind2]:
        return True
    else:
        return False

# test function
if __name__ == "__main__":
    print(same_chars("programmer", 6, 7))