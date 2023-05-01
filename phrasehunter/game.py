from phrasehunter.phrase import Phrase

import random

import re


class Game:
    def __init__(self):
        self.missed = 0
        self.phrase = [Phrase("Dream big start small"), 
                       Phrase("Change begins within you"), 
                       Phrase("Take risks embrace growth"), 
                       Phrase("Create your own path"), 
                       Phrase("Chase your own dreams")]
        self.active_phrase = []
        self.guesses = []
    
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
        self.active_phrase.display(self.active_phrase.matched_guess)

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
        phrase_list = self.active_phrase.phrase
        guesses_list = self.active_phrase.matched_guess
        
        attempt = self.get_guess()
        
        game_running = True
        while game_running:
        
            # If matched letter.
            if self.active_phrase.check_letter(attempt):
                print('You got a letter')
                # Create a loop for update the guesses_list with the matched letter.
                for x in range(len(phrase_list)):
                    if attempt == phrase_list[x]:
                        guesses_list[x] = attempt
                if self.active_phrase.check_complete(guesses_list):
                    self.active_phrase.display(guesses_list)
                    print('Congratulations! You won!')
                    self.game_over()
                    return game_running == False
                else:
                    self.active_phrase.display(guesses_list)
                    attempt = self.get_guess()
            
            # Not matched letter.
            else:
                self.missed += 1
                if self.missed >= 5:
                    print('''
                    ========== Game over! ==========
                    ''')
                    self.game_over()
                    return game_running == False
                else:
                    print(f'You have {5-(self.missed)} out of 5 lives remaining! Try Again')
                    attempt = self.get_guess()
