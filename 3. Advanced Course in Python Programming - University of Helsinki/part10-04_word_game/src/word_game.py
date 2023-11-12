# classes for different word games inheriting the class WordGame
import random

#The winner is determined randomly in this "basic" version of the game.
class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie
                
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

#Whoever types in the longest word on each round wins.
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2

#Whoever has squeezed more vowels into their word wins the round.
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ['a', 'e', 'i', 'o', 'u']
        p1 = 0
        for letter in player1_word:
            if letter in vowels:
                p1 += 1
        p2 = 0
        for letter in player2_word:
            if letter in vowels:
                p2 += 1
        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2

#Allows you to play a game of rock paper scissors.
# rock beats scissors (the rock can break the scissors but the scissors can't cut the rock)
# paper beats rock (the paper can cover the rock)
# scissors beats paper (the scissors can cut the paper)

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    # If the input from either player is invalid, they lose the round.
    # If both players type in something else than rock, paper or scissors, the result is a tie.        
    def round_winner(self, player1_word: str, player2_word: str):
        valid = ['rock', 'paper', 'scissors']
        if player1_word in valid and player2_word not in valid:
            return 1
        elif player2_word in valid and player1_word not in valid:
            return 2
        elif player1_word == 'rock' and player2_word == 'scissors':
            return 1
        elif player2_word == 'rock' and player1_word == 'scissors':
            return 2
        elif player1_word == 'paper' and player2_word == 'rock':
            return 1
        elif player2_word == 'paper' and player1_word == 'rock':
            return 2
        elif player1_word == 'scissors' and player2_word == 'paper':
            return 1
        elif player2_word == 'scissors' and player1_word == 'paper':
            return 2

