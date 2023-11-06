"""
Prompts the user for a level, n. If the user does not input a positive integer, the program prompts again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
from random import randint

#Prompts the user for a level, n. If the user does not input a positive integer, prompt again.
while True:
    try:
        n = int(input("Level: "))
        break
    except ValueError:
        pass

while True:
    try:
        #Randomly generates an integer between 1 and n, inclusive.
        randomnum = randint(1, n)
        #Prompts the user to guess that integer.
        guess = int(input("Guess: "))
    #If the guess is not a positive integer, the program prompts the user again.
    except ValueError:
        pass
    else:
        #If the guess is smaller than that integer, the program output "Too small!" and prompt the user again.
        if guess < randomnum:
            print("Too Small!")
        #If the guess is larger than that integer, the program output "Too large!" and prompt the user again.
        elif guess > randomnum:
            print("Too Large!")
        #If the guess is the same as that integer, the program should output "Just right!" and exit.
        elif guess == randomnum:
            print("Just right!")
            break


