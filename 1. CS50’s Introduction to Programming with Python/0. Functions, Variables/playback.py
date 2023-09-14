"""
Prompts the user for input and then outputs that same input, replacing each space with ...(i.e., three periods)
"""
#Prompt user for words
spokenwords = input("Please enter your words. \n").replace(" ", "...")
#Display delayed words
print(spokenwords)