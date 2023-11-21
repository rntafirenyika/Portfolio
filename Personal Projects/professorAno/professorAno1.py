from random import randint
from gtts import gTTS
import pygame
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols


def main():

    name = get_name()
    symbol = get_symbol()
    level = get_level()

    score = 0
    questionNumber = 0

    language = "en"

    gtts.tokenizer.symbols.SUB_PAIRS.append(("-", "minus"))
    gtts.tokenizer.symbols.SUB_PAIRS.append(("+", "plus"))
    gtts.tokenizer.symbols.SUB_PAIRS.append(("/", "divided by"))
    gtts.tokenizer.symbols.SUB_PAIRS.append(("*", "times"))

    for i in range(10):
        x, y = generate_integer(level)
        tries = 0
        questionNumber += 1
        while True:
            try:
                #Prompts the user to solve each math problem formatted as "X + Y ="
                print(f"{x} {symbol} {y} = ", end="")
                question = (f"{x} {symbol} {y} = ")
                question = pre_processors.word_sub(question)
                myobj = gTTS(text=question, lang=language, slow=False, tld="co.uk")
                myobj.save(f"{questionNumber}.mp3")
                pygame.mixer.init()
                pygame.mixer.music.load(f"{questionNumber}.mp3")
                pygame.mixer.music.play()
                UserAnswer = int(input(""))
                if symbol == "+":
                    CorrectAnswer = x + y
                elif symbol == "-":
                    CorrectAnswer = x - y
                elif symbol == "*":
                    CorrectAnswer = x * y
                else:
                    CorrectAnswer = x / y
                if UserAnswer == CorrectAnswer :
                    compliment = f"That is correct, well done {name}!"
                    myobj = gTTS(text=compliment, lang=language, slow=False, tld="co.uk")
                    myobj.save("compliment.mp3")
                    pygame.mixer.init()
                    pygame.mixer.music.load("compliment.mp3")
                    pygame.mixer.music.play()
                    pygame.time.wait(3000)
                    score += 1
                    break
                #If an answer is not correct (or not even a number), the program prompts the user again, allowing the user up to three tries in total.
                elif UserAnswer != CorrectAnswer and tries != 2 :
                    notCorrect = f"That is not correct {name}, try again!"
                    myobj = gTTS(text=notCorrect, lang=language, slow=False, tld="co.uk")
                    myobj.save("notCorrect.mp3")
                    pygame.mixer.init()
                    pygame.mixer.music.load("notCorrect.mp3")
                    pygame.mixer.music.play()
                    pygame.time.wait(3000)
                    tries += 1
                    raise ValueError
                #After the third trial, the program outputs the correct answer.
                else :
                    print(f"{x} {symbol} {y} = {CorrectAnswer}")
                    answer = (f"That is not correct again, the correct answer for {x} {symbol} {y} = {CorrectAnswer}")
                    answer = pre_processors.word_sub(answer)
                    myobj = gTTS(text=answer, lang=language, slow=False, tld="co.uk")
                    myobj.save("answer.mp3")
                    pygame.mixer.init()
                    pygame.mixer.music.load("answer.mp3")
                    pygame.mixer.music.play()
                    pygame.time.wait(6000)
                    break
            except ValueError:
                pass

    #The program finally output the user’s score, a number out of 10.
    print(f"Your Score is {score} out of 10.")
    finalScore = (f"Your Score is {score} out of 10, excellent work {name}")
    myobj = gTTS(text=finalScore, lang=language, slow=False, tld="co.uk")
    myobj.save("finalScore.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("finalScore.mp3")
    pygame.mixer.music.play()
    pygame.time.wait(7000)



def get_level():
#Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program prompts again
    while True:
        try:
            l = int(input("Level: "))
            if l == 1 or l == 2 or l == 3:
                return l
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


def get_name():
#Prompts the user for a name, if the user does not input anything, the program prompts again
    while True:
        n = input("Name: ").title()
        if len(n) > 0 :
            return n
        else:
            pass


def get_symbol():
#Prompts the user for a math symbol, the program prompts again if the input is invalid.
    while True:
        s = input("Symbol: ")
        if s in ["+", "-", "*" , "/"] :
            return s
        else:
            pass

if __name__ == "__main__":
    main()