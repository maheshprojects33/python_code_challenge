"""
Shiritori Game
This challenge is an English twist on the Japanese word game Shiritori. The basic premise is to follow two rules:
    1. First character of next word must match last character of previous word.
    2. The word must not have already been said.
"""

from random import choice
import enchant
import string


class ShiritoriGame:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.current_player = ""
        self.DICTIONARY = enchant.Dict("en_US")
        self.GUESSED_WORD = []
        self.LAST_LETTER = ''
        self.LIFE_PLAYER1 = 3
        self.LIFE_PLAYER2 = 3
        self.CORRECT_ANSWER = ['Nice', "Great", "Bravo", "WellDone", "Perfect"]

    def get_player_name(self):
        players = [self.player1, self.player2]
        for i in range(2):
            while True:
                name = input(f"Enter Player {i + 1} name: ").strip().upper()
                if not name:
                    print(f"Player {i + 1} name cannot be blank. Please try again.")
                elif name == players[1 - i]:
                    print("Both players cannot have the same name. Please try again.")
                else:
                    players[i] = name
                    break
        self.player1, self.player2 = players

    def start_game(self):
        self.GUESSED_WORD = [choice(string.ascii_lowercase)]
        self.LAST_LETTER = self.GUESSED_WORD[-1].upper()
        self.get_player_name()
        self.current_player = self.player1
        print(f"Game started! {self.current_player} goes first.")

        while True:
            guess = self.get_guess_word()
            valid_guess = self.is_valid(guess)
            if valid_guess:
                print(f'\t{choice(self.CORRECT_ANSWER)}! You Entered A Correct Word "{self.current_player}"')
                print(f"Switching Player's Turn. . . .")
                self.switch_players()
            else:
                if self.current_player == self.player1:
                    self.get_winner(self.LIFE_PLAYER1)
                else:
                    self.get_winner(self.LIFE_PLAYER2)
                print("Please Try Again. Use Your Remaining Life Wisely")

    def get_guess_word(self):
        print(f'"{self.current_player}" You Have '
              f'"{self.LIFE_PLAYER1 if self.current_player == self.player1 else self.LIFE_PLAYER2}" Life Remaining')
        guess = input(f"Enter a Word Starts With {self.LAST_LETTER}: ").title()
        while True:
            if guess.isalnum():
                return guess
            else:
                return " "

    def wrong_answer(self, player):
        if player == self.player1:
            self.LIFE_PLAYER1 -= 1
        else:
            self.LIFE_PLAYER2 -= 1

    def is_valid(self, guess):
        if self.DICTIONARY.check(guess):
            if len(guess) > 2:
                if guess[0] == self.LAST_LETTER and guess not in self.GUESSED_WORD:
                    self.GUESSED_WORD.append(guess)
                    self.LAST_LETTER = guess[-1].upper()
                    return True
                else:
                    print(f"The Word Should Start With Letter {self.LAST_LETTER} and Had Not Guessed Earlier")
                    self.wrong_answer(self.current_player)
            else:
                print("The word should be greater than 2 characters")
                self.wrong_answer(self.current_player)
        else:
            print(f'The word "{guess}" is not a valid word')
            self.wrong_answer(self.current_player)
        return False

    def get_winner(self, life):
        if self.LIFE_PLAYER1 < 0:
            print(f"{self.player2} Wins The Game")
            self.restart_game()
        if self.LIFE_PLAYER2 < 0:
            print(f"{self.player1} Wins The Game")
            self.restart_game()
        print(f'!!! {self.current_player} lost 1 life !!!')
        return life

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def restart_game(self):
        while True:
            restart = input("Do You Want to Play Again (y/n): ").lower()
            if restart == 'y':
                self.GUESSED_WORD[1:] = []
                self.LIFE_PLAYER1 = 3
                self.LIFE_PLAYER2 = 3
                self.start_game()
            elif restart == 'n':
                exit()
            else:
                print("Invalid Selection!!! Try Again")


if __name__ == "__main__":
    game = ShiritoriGame()
    # Start the game
    game.start_game()