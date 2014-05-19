#!/usr/bin/env python

# todo:
#  handle ties
#  show how much they won and current total in the Great Job page
#  show # letters, etc. (result of guess) in a separate splash screen
#  make easier entry of puzzle characters such as ! ... or just eliminate them
#
# I ended up with money
# gibs and I traded turns, gibs solved, I got money?


# import local source
import wheel
import puzzles
import bigBoard
import player
from support import getAkey, getKeyOrExit, splashMessage, getAline

# import python distribution source
import sys
import os
import re

class wheelOfFortune(object):

    def __init__(self):
        # setup some constants here
        self.gameName = "GIBSON'S WHEEL!"
        self.vowelCost = 250
        self.houseMinimum = 1000
        self.numRegularRounds = 3
        # setup some regex's for use as needed
        self.re_alpha = re.compile('[A-Za-z]')
        self.re_vowel = re.compile('[AEIOUaeiou]')
        self.re_num   = re.compile('[0-9]')
        # start gameplay with a splash screen
        self.printWelcome()
        # instantiate the wheel, puzzle list, and players (not the board, re-instantiate it each round)
        self.wheel = wheel.wheel()
        self.puzzles = puzzles.puzzleList()
        self.players = player.playerList()
        # play a game
        self.playGame()
        # maybe like "Thanks for playing!"
        self.endGame()
        
    def playGame(self):
        # continue playing rounds indefinitely
        for i in range(self.numRegularRounds):
            self.playRound(i+1)
        # give a summary of player amounts
        self.players.endOfGameSummary()
        # play bonus round
        self.playBonusRound()
                 
    def endGame(self):
        print "Thanks for playing!"     
         
    def playRound(self, roundNum):
        
        # at the beginning of each round, select a puzzle and instantiate the big board
        self.curPuzzle = self.puzzles.newPuzzle()
        self.board = bigBoard.theBigBoard(self.curPuzzle)
        self.players.newRound()
        self.player = self.players.getFirstPlayer()
        
        while True:
            
            self.printHeader(roundNum)
            self.board.printPuzzle()
            self.players.printPlayers()
            self.printRoundMenu()
            ch = getAkey().upper()
            if ch == " ":
                newTile = self.wheel.spin()
                if newTile.tileTypeOf == wheel.tileType_money:
                    print "You spin the wheel and get...\n "
                    splashMessage('$ %i' % newTile.value, True)
                    thisLetter = self.getAconsonant()
                    if thisLetter == None:
                        self.players.getNextPlayer()
                        getKeyOrExit()
                        continue
                    count = self.board.guessALetter(thisLetter)
                    if count:
                        print "Great! Number of %s's found: %i" % (thisLetter , count)
                        self.player.gotConsonant(newTile.value*count)
                    else:
                        print "No %s's found...next player" % (thisLetter)
                        self.player = self.players.getNextPlayer()
                else:
                    splashMessage(newTile.nameFromInt(newTile.tileTypeOf))
                    if newTile.tileTypeOf == wheel.tileType_bankrupt:
                        self.player.wentBankrupt()
                    self.player = self.players.getNextPlayer()
                getKeyOrExit()
            elif ch == "S":
                guess = getAline("You'd like to try to solve...type the answer...")
                success = self.board.guessThePuzzle(guess)
                if success:
                    splashMessage('Great Job!')
                    self.player.winner(self.houseMinimum)
                    getKeyOrExit()
                    return True
                else:
                    print "Not quite, next player...press any key"
                    self.players.getNextPlayer()
                    getKeyOrExit()
            elif ch == "V":
                if self.player.moneyThisRound < self.vowelCost:
                    print "Don't have enough money to buy a vowel!"
                    self.players.getNextPlayer()
                else:
                    thisLetter = self.getAvowel()
                    if thisLetter == None:
                        self.players.getNextPlayer()
                        getKeyOrExit()
                        continue
                    count = self.board.guessALetter(thisLetter)
                    self.player.boughtVowel(self.vowelCost)
                    if count:
                        print "Great! Number of %s's found: %i" % (thisLetter , count)
                    else:
                        print "No %s's found...next player" % (thisLetter)
                        self.player = self.players.getNextPlayer()
                getKeyOrExit()
            elif ch == "N":
                print "Are you sure to want to skip this round? (y/n)"
                if getAkey() in ["y", "Y"]:
                    return True
            elif ch == '\033':
                sys.exit(0)
            else:
                pass 
        
    def playBonusRound(self):
        splashMessage("BONUS ROUND!")
        
        # select winner
        self.player = self.players.getWinner()
        
        print "Press any key for the bonus round, %s!" % self.player.name
        getKeyOrExit(True)
        
        self.curPuzzle = self.puzzles.getBonusPuzzle()
        self.board = bigBoard.theBigBoard(self.curPuzzle)
        self.board.guessedLetters = ['R', 'S', 'T', 'L', 'N', 'E']
        self.players.newRound()
        self.player = self.players.getWinner()
        
        consonantsFound = 0
        while consonantsFound < 3:
            splashMessage("BONUS ROUND!")
            self.board.printPuzzle()
            self.player.printPlayer(True)
            print ""
            self.board.printAvailableConsonants()
            print "\nGive me a consonant! (Press ESCAPE to exit)"
            ch = getKeyOrExit(True).upper()
            if ch == None:
                continue
            else:
                if self.isAconsonant(ch):
                    if ch in self.board.guessedLetters:
                        continue
                    self.board.guessedLetters.append(ch)
                    consonantsFound += 1
                else:
                    continue
                
        vowelsFound = 0
        while vowelsFound < 1:
            splashMessage("BONUS ROUND!")
            self.board.printPuzzle()
            self.player.printPlayer(True)
            print ""
            self.board.printAvailableVowels()
            print "\nGive me a vowel! (Press ESCAPE to exit)"
            ch = getKeyOrExit(True).upper()
            if ch == None:
                continue
            else:
                if self.isAvowel(ch):
                    if ch in self.board.guessedLetters:
                        continue
                    self.board.guessedLetters.append(ch)
                    vowelsFound += 1               
                else:
                    continue
                    
        bonusAmount = self.wheel.bonusRoundTile()
        splashMessage("BONUS ROUND!")
        self.board.printPuzzle()
        self.player.printPlayer(True)
        print ""
        guess = getAline("Solve the puzzle...type the answer...")
        success = self.board.guessThePuzzle(guess)
        if success:
            self.player.moneyOverall += bonusAmount
            splashMessage("Wonderful!")
            print "\nBonus prize was $%i" % bonusAmount
        else:
            splashMessage("Oops, not quite!")
            print "\nPuzzle answer was...\n"
            print "  " + self.board.puzzleString
            
        print "\n%s wins $%i!" % (self.player.name, self.player.moneyOverall)
        print "Press any key to end game"
        getAkey()
        
    def isAconsonant(self, ch):
        if self.re_alpha.match(ch) and not self.re_vowel.match(ch):
            return True
        else:
            return None
            
    def isAvowel(self, ch):
        if self.re_vowel.match(ch):
            return True
        else:
            return None
        
    def getAconsonant(self):
        self.board.printAvailableConsonants()
        print "\nGuess a letter! (Press ESCAPE to exit)"
        ch = getKeyOrExit(True).upper()
        print "    ...You guessed '%s'\n" % ch
        if self.re_alpha.match(ch):
            if self.re_vowel.match(ch):
                print "Sorry, you have to *buy* vowels! Next Player..."
            else:
                return ch
        elif self.re_num.match(ch):
            print "Don't press numbers, just letters! Next Player..."
        else:
            print "You must press a letter! Next Player..."
        return None
            
    def getAvowel(self):
        self.board.printAvailableVowels()
        print "\nGuess a vowel! (Press ESCAPE to exit)"
        ch = getKeyOrExit(True).upper()
        print "    ...You guessed '%s'\n" % ch
        if self.re_alpha.match(ch):
            if self.re_vowel.match(ch):
                return ch
            else:
                print "Sorry, you have to *spin the wheel* for consanants! Next Player..."
        elif self.re_num.match(ch):
            print "Don't press numbers, just letters! Next Player..."
        else:
            print "You must press a letter! Next Player..."
        return None
        
    def printWelcome(self):
        splashMessage(self.gameName)
        print "Welcome, press any key to start, but press ESCAPE to quit!"
        getKeyOrExit(True)
        
    def printHeader(self, roundNum):
        splashMessage("ROUND " + str(roundNum))
                
    def printRoundMenu(self):
        print """
       * * * * * * * * * * * * * * *
        Press:
         [space bar] to spin
         [v] to buy a vowel for $%i
         [s] to solve
         [n] to skip this round
         [ESC] to quit
       * * * * * * * * * * * * * * *
            """ % self.vowelCost
        
wheelOfFortune()

