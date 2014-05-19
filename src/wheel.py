
import random
import sys

tileType_money     = -1
tileName_money     = "Money"
tileType_loseATurn = -2
tileName_loseATurn = "Lose A Turn"
tileType_bankrupt  = -3
tileName_bankrupt  = "Bankrupt"
class tile(object):
    
    def __init__(self, typeOf, value=0):
        self.tileTypeOf = typeOf
        self.value = value
    
    def nameFromInt(self, typeOf):
        if typeOf == tileType_money:
            return tileName_money
        elif typeOf == tileType_loseATurn:
            return tileName_loseATurn
        elif typeOf == tileType_bankrupt:
            return tileName_bankrupt
        else:
            print "Invalid tile typeOf integer in tile.nameFromInt"
            sys.exit(1)
    
    def intFromName(self, name):
        if name == tileName_money:
            return tileType_money
        elif name == tileName_loseATurn:
            return tileType_loseATurn
        elif name == tileName_bankrupt:
            return tileType_bankrupt
        else:
            print "Invalid tile name in tile.intFromName"
            sys.exit(1)

class wheel(object):
    
    def __init__(self):
        self.tiles = []
        self.tiles.extend( [tile(tileType_money, 50)]   * 1 )
        self.tiles.extend( [tile(tileType_money, 100)]  * 2 )
        self.tiles.extend( [tile(tileType_money, 150)]  * 3 )
        self.tiles.extend( [tile(tileType_money, 200)]  * 5 )
        self.tiles.extend( [tile(tileType_money, 250)]  * 6 )
        self.tiles.extend( [tile(tileType_money, 300)]  * 7 )
        self.tiles.extend( [tile(tileType_money, 400)]  * 8 )
        self.tiles.extend( [tile(tileType_money, 500)]  * 7 )
        self.tiles.extend( [tile(tileType_money, 750)]  * 4 )
        self.tiles.extend( [tile(tileType_money, 1000)] * 2 )
        self.tiles.extend( [tile(tileType_loseATurn)]   * 3 )
        self.tiles.extend( [tile(tileType_bankrupt)]    * 2 )
        
        self.bonusTiles = []
        self.bonusTiles.extend([ 5000]  * 1)
        self.bonusTiles.extend([10000]  * 2)
        self.bonusTiles.extend([15000]  * 3)
        self.bonusTiles.extend([25000]  * 2)
        self.bonusTiles.extend([50000]  * 1)
                
    def spin(self):
        return self.tiles[int(random.random() * len(self.tiles))]

    def bonusRoundTile(self):
        return self.bonusTiles[int(random.random() * len(self.bonusTiles))]
