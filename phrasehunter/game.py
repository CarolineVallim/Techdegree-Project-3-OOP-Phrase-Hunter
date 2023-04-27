# Create your Game class logic in here.

from phrase import Phrase

import random

# Create a class
class Game:
    def __init__(self):
        self.missed = 0
        self.phrase = ["Dream big start small", 
                        "Change begins within you", 
                        "Take risks embrace growth", 
                        "Create your own path", 
                        "Chase your own dreams"]
        self.active_phrase = []
        self.guesses = []
    
    def welcome(self):
         print('''
            PHRASE HUNTER!
                  
            Instructions:
            - The program will random choose a phrase that contains 4 words
            - The first tip is the phrase with all the letters
            - The program will prompt you to guess the letter
            - If it's right, the program will show you the phrase update
            - If it's wrong, you need to try again
            - The user win when guess all the letters
                  
            Rules:
            - The game is over when the user has guessed incorrectly five times
            ''')

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrase)
        print(self.active_phrase)
        Phrase.display(Phrase(self.active_phrase))
        
                        
    def get_guess(self):
        try:
            attempt = input("Guess a letter:  ").lower()
            if attempt in self.guesses:
                print('You already type this letter')
                return game.get_guess
            elif attempt not in self.guesses:
                self.guesses.append(attempt)
        except ValueError as err:
            print('Ops')
            return game.get_guess
        
        
        
        #if attempt in Phrase.self.phrase:
        #    for index, letter in enumerate(self.phrase):
        #        if letter == attempt:
        #            Phrase.guessed_letter[index] = letter
        
    def game_over(self):
        print('Game over')
    
    def start(self):
        self.welcome()
        self.get_random_phrase()
        game_running = True
        while game_running:
            attempt = self.get_guess()
            if self.active_phrase.check_letter(attempt):
                print('Nice work. The phrase has this letter!')
                for index, letter in enumerate(self.phrase):
                    if letter == attempt:
                        Phrase.guessed_letter[index] = letter
            else:
                self.missed += 1
                while self.missed < 5:
                    self.get_guess
                else:
                    self.game_over()

    
        #increments the number of missed by one if the guess is incorrect
        #if attempt not in self.phrase:
        #    self.missed.append(attempt)
            

if __name__ == '__main__':
    game = Game()
    game.start()