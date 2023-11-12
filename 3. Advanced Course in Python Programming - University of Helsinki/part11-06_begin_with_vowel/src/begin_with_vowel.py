# Takes a list of strings as its argument.
# Using list comprehension, create and return a new list, containing only those words from the original list which begin with a vowel.
def begin_with_vowel(words: list):
    return [i for i in words if i[0].lower() in ['a', 'e', 'i', 'o', 'u']]
