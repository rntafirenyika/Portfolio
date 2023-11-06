# Takes a string argument, returns a new string, which is the same as the original but with all vowels removed.
def no_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        text = text.replace(i, "")
    return text
