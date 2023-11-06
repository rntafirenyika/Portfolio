"""
Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program prompts again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. Operations other than addition (+) are not supported.
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program outputs EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program outputs the correct answer.
The program ultimately output the user’s score: the number of correct answers out of 10.
"""
from random import randint

def main():

    level = get_level()

    score = 0

    for i in range(10):
        x, y = generate_integer(level)
        tries = 0
        while True:
            try:
                #Prompts the user to solve each math problem formatted as "X + Y ="
                print(f"{x} + {y} = ", end="")
                UserAnswer = int(input(""))
                CorrectAnswer = x + y
                if UserAnswer == CorrectAnswer :
                    score += 1
                    break
                #If an answer is not correct (or not even a number), the program outputs "EEE" and prompt the user again, allowing the user up to three tries in total.
                elif UserAnswer != CorrectAnswer and tries != 2 :
                    tries += 1
                    print("EEE")
                    raise ValueError
                #After the third trial, the program outputs the correct answer.
                else :
                    print("EEE")
                    print(f"{x} + {y} = ", CorrectAnswer)
                    break
            except ValueError:
                pass

    #The program finally output the user’s score, a number out of 10.
    print(f"Score: {score}")



def get_level():
#Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program prompts again
    while True:
        try:
            n = int(input("Level: "))
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                pass
        except ValueError:
            pass



def generate_integer(level):
    #Randomly generates ten (10) math problems wherein each of X and Y is a non-negative integer with (level) digits.
    if level == 1 :
        x = randint(0, 9)
        y = randint(0, 9)
    elif level == 2 :
        x = randint(10, 99)
        y = randint(10, 99)
    elif level == 3 :
        x = randint(100, 999)
        y = randint(100, 999)
    return x, y




if __name__ == "__main__":
    main()