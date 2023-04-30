from phrasehunter.phrase import Phrase

import random

import re


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
        self.Phrase = 0
    
    def welcome(self):
         print('''
            ======================= PHRASE HUNTER! =======================
            
            GAME RULES:
            - Goal: Guess the phrase that contains 4 words.
            - Every turn you can type a single letter.
            - The game is over when you make 5 wrong guesses.
            ''')

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrase)
        self.Phrase = Phrase(self.active_phrase)
        # Create and store an Phrase Instance Attributes.
        self.Phrase.display(self.Phrase.matched_guess)

    # Get the user input and check possible errors.
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
        self.welcome()
        self.get_random_phrase()
        
        # Create a variable to store Phrase instance attributes. 
        phrase_list = self.Phrase.phrase
        guesses_list = self.Phrase.matched_guess
        
        attempt = self.get_guess()
        
        game_running = True
        while game_running:
        
            # If matched letter.
            if self.Phrase.check_letter(attempt):
                print('You got a letter')
                # Create a loop for update the guesses_list with the matched letter.
                for x in range(len(phrase_list)):
                    if attempt == phrase_list[x]:
                        guesses_list[x] = attempt
                if self.Phrase.check_complete(guesses_list):
                    self.Phrase.display(guesses_list)
                    print('Congratulations! You won!')
                    return game_running == False
                else:
                    self.Phrase.display(guesses_list)
                    attempt = self.get_guess()
            
            # Not matched letter.
            else:
                self.missed += 1
                if self.missed >= 5:
                    self.game_over()
                    return game_running == False
                else:
                    print(f'You have {5-(self.missed)} out of 5 lives remaining! Try Again')
                    attempt = self.get_guess()

