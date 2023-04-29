# Create your Game class logic in here.

from phrasehunter.phrase import Phrase

import random

import re

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
            ======================= PHRASE HUNTER! =======================
                  
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
        Phrase.display(Phrase,Phrase(self.active_phrase).guessed_letter)

    def get_guess(self):
        while True:
            attempt = input("Guess a letter:  ").lower()
            if re.match(r'^[a-zA-Z]$', attempt):
                if attempt in self.guesses:
                    print('You already type this letter. Try again!')
                    return self.get_guess()
                elif attempt not in self.guesses:
                    self.guesses.append(attempt)
                    return attempt
                return self.get_guess()
            else:
                print('Error: Please enter a single letter')
                return self.get_guess()
        
    def game_over(self):
        print('''
              ========== Game over! ==========
              ''')
        continue_game = str(input('Do you want to play again? y/n  ')).lower()
        if continue_game == 'y':
            game = Game()
            game.start()
        else:
            print('Thank you for play the game!')
        
            
    def start(self):
        # calls the method
        self.welcome()
        self.get_random_phrase()
        
        phrase_list = Phrase(self.active_phrase).phrase
        guesses_list = Phrase(self.active_phrase).guessed_letter
        
        attempt = self.get_guess()
        
        # create a game loop
        game_running = True
        while game_running:
            if Phrase(self.active_phrase).check_letter(attempt):
                print('You got a letter')
                for x in range(len(phrase_list)):
                    if attempt == phrase_list[x]:
                        guesses_list[x] = attempt                
                if Phrase(self.active_phrase).check_complete(guesses_list):
                    Phrase.display(Phrase, guesses_list)
                    print('Congratulations! You won!')
                    return game_running == False
                else:
                    Phrase.display(Phrase, guesses_list)
                    attempt = self.get_guess()
            else:
                self.missed += 1
                if self.missed >= 5:
                    self.game_over()
                    return game_running == False
                else:
                    print(f'You have {5-(self.missed)} out of 5 lives remaining! Try Again')
                    attempt = self.get_guess()

if __name__ == '__main__':
    game = Game()
    game.start()