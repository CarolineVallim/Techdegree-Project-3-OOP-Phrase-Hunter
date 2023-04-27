# Create your Phrase class logic here.

class Phrase:
    # create a initializer        
    def __init__(self, phrase):
        self.phrase = list(phrase.lower())
        print(self.phrase)
        
        self.guessed_letter = []
        for item in self.phrase:
            if item == ' ':
                self.guessed_letter.append(' ')
            else:
                self.guessed_letter.append('_')
        print(self.guessed_letter)
    
    # display(): print the output the phrase
    def display(self):
        print(' '.join(self.guessed_letter))
        
    # check_letter(): checks to see if the letter selected by the user matches a letter in the phrase.
    def check_letter(self, letter):
        return letter in self.phrase
        
    # check_complete(): checks to see if the whole phrase has been guessed.
    def check_complete(self):
        while '_' in self.guessed_letter:
            return self.check_letter()
            

if __name__ == '__main__':
    phrase = Phrase('A casa é nova')
    phrase.display()