
import random

class puzzle(object):
    
    def __init__(self, string, category):
        self.string = string
        self.category = category
        
class puzzleList(object):
    
    def __init__(self):
        
        self.puzzles = []
        
        self.puzzles.append(puzzle('Gibson Scott Lee','Proper Name'))
        self.puzzles.append(puzzle('Daxton Foster Lee','Proper Name'))
        self.puzzles.append(puzzle('Edwin Scott Lee','Proper Name'))
        self.puzzles.append(puzzle('Caitlin Marie Lee','Proper Name'))
        
        self.puzzles.append(puzzle('Alphabet Blocks', 'Fun and Games'))
        self.puzzles.append(puzzle('Hot Wheels Cars', 'Fun and Games'))
        
        self.puzzles.append(puzzle('Thomas the Train', 'Characters'))
        self.puzzles.append(puzzle('Sid the Science Kid', 'Characters'))
        self.puzzles.append(puzzle('Cat in the Hat', 'Characters'))
        self.puzzles.append(puzzle('Super Why!', 'Characters'))
        self.puzzles.append(puzzle('Nick, Sally, and The Cat', 'Characters'))
        self.puzzles.append(puzzle('The Man with the Yellow Hat', 'Characters'))
        self.puzzles.append(puzzle('Caillou and Gilbert', 'Characters'))
                
        self.puzzles.append(puzzle('Vacuum Cleaner', 'Around the House'))
        self.puzzles.append(puzzle('Garage Door', 'Around the House'))
        self.puzzles.append(puzzle('Orange Patio Chairs', 'Around the House'))
        self.puzzles.append(puzzle('Blue Picnic Table', 'Around the House'))
        self.puzzles.append(puzzle('Pictures of Two Boys', 'Around the House'))
        
        self.puzzles.append(puzzle('Watching Great Shows', 'What are you doing?'))
        self.puzzles.append(puzzle('Helping Mommy Cook', 'What are you doing?'))
        self.puzzles.append(puzzle('Having Rest Time', 'What are you doing?'))
        self.puzzles.append(puzzle('Playing Wheel Of Fortune', 'What are you doing?'))
        
        self.puzzles.append(puzzle('Cats and Dogs', 'Living Things'))
        self.puzzles.append(puzzle('Beavers and Ducks', 'Living Things'))
        self.puzzles.append(puzzle('Happy Kitties', 'Living Things'))
        self.puzzles.append(puzzle('Soft Kitties', 'Living Things'))
                
        
        self.bonusPuzzles = []
        
        self.bonusPuzzles.append(puzzle('Playing Cars', 'What are you doing?'))
        self.bonusPuzzles.append(puzzle('Resting in Bed', 'What are you doing?'))
        self.bonusPuzzles.append(puzzle('Making Arts and Crafts', 'What are you doing?'))
        
        
    def newPuzzle(self):
        return self.puzzles[int(random.random() * len(self.puzzles))]

    def getBonusPuzzle(self):
        return self.bonusPuzzles[int(random.random() * len(self.bonusPuzzles))]
