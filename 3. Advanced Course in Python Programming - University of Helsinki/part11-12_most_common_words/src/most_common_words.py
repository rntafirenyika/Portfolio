import string

# Function to remove punctuation from a string
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Takes a filename and an integer value for a lower limit as its arguments.
# Returns a dictionary containing the occurrences of the words which appear at least the number of times specified in the lower_limit parameter.
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        words = [word for line in file for word in remove_punctuation(line).split()]
    return {i: words.count(i) for i in words if words.count(i) >= lower_limit}
