
import string

class theBigBoard(object):
    
    def __init__(self, puzzle):
        self.specialCharacters = [" ", "-", ",", "'", "!"]
        self.puzzleString = puzzle.string
        self.puzzleStringU = self.puzzleString.upper()
        self.category = puzzle.category
        self.guessedLetters = []
        self.vowelsInPuzzle = True
         
    def guessALetter(self, letter):
        """ letter should always be upper case """
        exiter = False
        if letter in self.guessedLetters:
            print "Already guessed this letter"
        else:
            if letter in self.puzzleStringU:
                count = 0
                for c in self.puzzleStringU:
                    if c == letter:
                        count += 1                
                exiter = count
            self.guessedLetters.append(letter)
        self.vowelsInPuzzle = False
        for vowel in ['A', 'E', 'I', 'O', 'U']:
            if (vowel in self.puzzleStringU) and not (vowel in self.guessedLetters):
                self.vowelsInPuzzle = True
        return exiter
        
    def guessThePuzzle(self, guess):
        if guess.upper() == self.puzzleStringU:
            return True
        else:
            return False    
        
    def printPuzzle(self):
        displayString = "* * * * * * *\n* PUZZLE: * *  "
        for c in self.puzzleString:
            if c in self.specialCharacters:
                displayString += " " + c
            elif c.upper() in [x.upper() for x in self.guessedLetters]:
                displayString += " " + c 
            else:
                displayString += " _"
        displayString += "\n* * * * * * *"
        displayString += "\n* CATEGORY: *   " + self.category + "\n* * * * * * *\n"
        if not self.vowelsInPuzzle:
            displayString += " ((NO MORE VOWELS)) \n"
        print displayString
        
    def printAvailableConsonants(self):
        outS = "Available consonants to choose: "
        for i in string.uppercase:
            if (i in self.guessedLetters) or (i in ['A', 'E', 'I', 'O', 'U']):
                outS += "_"
            else:
                outS += i
        print outS
        
    def printAvailableVowels(self):
        outS = "Available vowels to choose: "
        for i in string.uppercase:
            if (not i in self.guessedLetters) and (i in ['A', 'E', 'I', 'O', 'U']):
                outS += i
            else:
                outS += "_"
        print outS                

