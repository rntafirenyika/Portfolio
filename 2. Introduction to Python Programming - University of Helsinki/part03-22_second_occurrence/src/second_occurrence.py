# Finds the second occurrence of a substring.

word = input("Please type in a string: ")
chars = input("Please type in a substring: ")
chars_len = len(chars)
count = 0
count_index = 0

while True:
    index = word.find(chars)
    if index != -1:
        count += 1
        count_index += index + chars_len
        word = word[index+chars_len:]
    if index == -1:
        print("The substring does not occur twice in the string.")
        break
    if count == 2:
        print(f"The second occurrence of the substring is at index {count_index-chars_len}.")
        break