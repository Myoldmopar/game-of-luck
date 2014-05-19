
import os
import sys
from support import getAkey, splashMessage, getAline, getKeyOrExit
import string

class player(object):
    
    def __init__(self, name):
        self.name = name
        self.moneyThisRound = 0
        self.moneyOverall = 0
        
    def startNewRound(self):
        self.moneyThisRound = 0

    def gotConsonant(self, amount):
        self.moneyThisRound += amount
        
    def boughtVowel(self, amount):
        self.moneyThisRound -= amount
        
    def wentBankrupt(self):
        self.moneyThisRound = 0
        
    def winner(self, houseMinimum):
        if self.moneyThisRound <= houseMinimum:
            self.moneyThisRound = houseMinimum
        self.moneyOverall += self.moneyThisRound
        
    def printPlayer(self, current):
        emptyPrefix =       "               "
        if current:
            prefix =        "* CURRENT:  *  "
            hangingPrefix = "* * * * * * *  "
        else:
            prefix =        emptyPrefix
            hangingPrefix = emptyPrefix
        print hangingPrefix + ("Player: %s\n" + prefix + "   Money This Round: $%5i\n" + hangingPrefix + "   Total Money:      $%5i") % (self.name, self.moneyThisRound, self.moneyOverall)

    def printPlayerTotal(self):
        print ("Player: %s\n" + "    " + "   Total Money:      $%5i") % (self.name, self.moneyOverall)

class playerList(object):
    
    def __init__(self):
        
        self.players = []
        
        while True:
            self.printHeader()
        
            print "Enter # players (1, 2, or 3)... (or press ESCAPE to quit)"
            key = getAkey()
            if key == '\033':
                sys.exit(0)
            try:
                numPlayers = int(key)
                if not numPlayers in [1,2,3]:
                    print "Invalid # players entered"
                    continue
                for i in range(numPlayers):
                    self.printHeader()
		    name = ""
		    while True:
	                    name = getAline("Enter name for Player # %i: " % (i+1))
			    if name.strip() == "":
				print "Blank name not valid, try again"
                                continue
			    else:
				break
                    self.players.append(player(name))
                break
            except:
                print "Invalid # players entered, press any key to try again (or press ESCAPE to quit)"
                if getAkey() == '\033':
                    sys.exit(0)
                continue
            
    def getFirstPlayer(self):
        self.curPlayerNum = -1
        return self.getNextPlayer()
        
    def getNextPlayer(self):
        self.curPlayerNum += 1
        if self.curPlayerNum == len(self.players):
            self.curPlayerNum = 0
        return self.players[self.curPlayerNum]
        
    def newRound(self):
        for player in self.players:
            player.startNewRound()
        
    def printHeader(self):
        splashMessage('Players')
        
    def printPlayers(self):
        playerNum = -1
        print "------------------------------------------"
        for player in self.players:
            playerNum += 1
            player.printPlayer(self.curPlayerNum == playerNum)
            print "------------------------------------------"

    def endOfGameSummary(self):
        splashMessage("Results!")
        print ""
        for player in self.players:
            player.printPlayerTotal()
        getKeyOrExit()
        
    def getWinner(self):
        # first determine maximum money
        winningMoney = 0
        for player in self.players:
            winningMoney = max(winningMoney, player.moneyOverall)
            
        # now count how many players have that much
        numWinners = 0
        for player in self.players:
            if player.moneyOverall == winningMoney:
                numWinners += 1
        
        # if only one, return it; if more than one, we need a tiebreaker
        if numWinners == 1:
            for player in self.players:
                if player.moneyOverall == winningMoney:
                    return player

