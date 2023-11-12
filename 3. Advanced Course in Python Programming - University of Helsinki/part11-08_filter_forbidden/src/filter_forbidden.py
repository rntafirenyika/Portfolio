# Takes two strings as its arguments.
# Returns a new version of the first string that does not contain any characters from the second string.
def filter_forbidden(string: str, forbidden: str):
    return "".join([i if i not in forbidden else '' for i in string ])