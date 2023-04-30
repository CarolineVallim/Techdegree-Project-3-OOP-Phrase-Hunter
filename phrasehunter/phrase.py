class Phrase:     
    def __init__(self, phrase):
        self.phrase = list(phrase.lower())
        
        self.matched_guess = []
        
        # Create a loop to build the list with underscore of the corresponding phrase.
        for item in self.phrase:
            if item == ' ':
                self.matched_guess.append(' ')
            else:
                self.matched_guess.append('_')
    
    def display(self, list):
        print(' '.join(list))
        
    # Checks if the attempt by the user matches a letter in the phrase.
    def check_letter(self, letter):
        return letter in self.phrase
    
    # Checks if the whole phrase has been guessed.
    def check_complete(self, list):
        return self.phrase == list
