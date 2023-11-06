# Takes two strings as arguments.
# Returns True if the strings are anagrams of each other.
# Two words are anagrams if they contain exactly the same characters.

def anagrams(text1: str, text2: str) -> bool:
    return sorted(text1) == sorted(text2)

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False