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
        Phrase(self.active_phrase).display()
        
                        
    def get_guess(self):
        try:
            attempt = input("Guess a letter:  ").lower()
            if attempt in self.guesses:
                print('You already type this letter')
                return self.get_guess()
            elif attempt not in self.guesses:
                self.guesses.append(attempt)
                return self.get_guess()
            return self.get_guess()
        except ValueError as err:
            print('Ops')
            return self.get_guess()
        
        
    def game_over(self):
        print('Game over')
            
    def start(self):
        # calls the method
        self.welcome()
        self.get_random_phrase()
        # create a game loop
        game_running = True
        while game_running:
        # calls the get_guess
            attempt = self.get_guess()
            if Phrase(self.active_phrase).check_letter(attempt):
                print('You got a letter')
                
                # increments the number of missed
            else:
                self.missed += 1
                print('Sorry! Try again.')
                if self.missed == 5:
                    self.game_over()
                    game_running = False
                elif Phrase(self.active_phrase).check_complete(self.guesses):
                    print('Congratulations! You won!')
                    self.game_over()
                    game_running = False
        # Update game state
        # Render graphics
                            
        # calls game_over method
        self.game_over()

if __name__ == '__main__':
    game = Game()
    game.start()