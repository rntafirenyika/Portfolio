# Takes a string argument and returns True if the string is a palindrome.
# Palindromes are words which are spelled exactly the same backwards and forwards.
def palindromes(text: str) -> bool:
    reverse = ""
    for i in range(len(text) - 1, -1, -1):
        reverse += text[i]
    return text == reverse

# Asks the user to type in words until they type in a palindrome.
while True:    
    word = input("Please type in a palindrome: \n")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
