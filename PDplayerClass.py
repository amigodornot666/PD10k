# PDplayerClass.py // Player class file for pyDice10k
# by: aMigod666(KyleJRoux)
import random
import PDrollClass
import PDmenu

class Player(object):
    '''Players interact with the game while keeping track of individual 
    Users data(per instance), and keeps track of the current player as
    well as the number of players(at the class level)
	
    class attrs  - _playerList, _playerCounter, _firstNumberList

    instance attrs - _name, _playerNumber, _firstNum, _diceToRoll,
    _diceToHold, _isRolling, _gameScore, _rollScore

    class methods - get_player_count, {get,set}_first_player, add_a_player

    instance methods - roll_dice(dieNum), {get,set}_{roll,game}_score,
    print_roll, {get,set}_held_dice'''
    #CLASS DATA
    _playerList = list()
    _playerCounter = 0
    _firstNumberList = dict()
    # CONSTRUCTOR
    def __init__(self):
        Player._playerCounter += 1
        self._playerNumber = Player._playerCounter
        self._name = raw_input('\n\n\nPlease enter name of player {0}: '.format(self._playerNumber))
        print 'Welcome {0}'.format(self._name)
        Player._playerList.append(self._name)
        self._firstNum = random.choice(range(1, 101))
        Player._firstNumberList[self._name] = self._firstNum
        self._diceHolding = list()
        self._diceRolling = list()
        self._isRolling = False
        self._rollScore = 0
        self._gameScore = 0
        self._tempScore = 0

    def __str__(self):
        return 'Player #{0}: {1}'.format(self._playerNumber, self._name)	

    
    #CLASS METHODS
    @staticmethod
    def get_player_count():
        return Player._playerCounter
    @staticmethod
    def print_player_count():
        print Player.get_player_count()
    @staticmethod
    def get_first_player():
        #code to sort Player._firstNumberList and find biggest
        pass
    @staticmethod
    def set_first_player():
        # code to set isPlaying to True for highest _firstNum
		pass
    @staticmethod
    def add_player(objRef):
        # code to add a player with a method
        objRef = Player()

    #INSTANCE METHODS
    def roll_dice(self, dieNum=6):
        self.diceRolling = self.roll(dieNum)


    def print_roll(self):
        self.roll_dice()
        for die in range(len(self.diceRolling)):
            print self.diceRolling[die],
            print ' ',
	
    def roll(self, num=6):
        tmpRoll = list()	
        for i in range(num):
            tmpRoll.append(random.choice(range(1, 7)))
        return tmpRoll			

    def set_held_dice(self):
        pass	

    def get_held_dice(self):
        pass	

    def set_roll_score(self):
        pass	

    def get_roll_score(self):
        pass	

    def set_game_score(self):
        pass	

    def get_game_score(self):
        pass	

		

def main():
    #P1 = 'Kyle'
    #Player.add_player(P1)
    #P1.print_roll()
    x = Player()
    print 'roll one'

    x.print_roll()
    
    print 'roll two'

    x.print_roll()

    print 'roll three'
    
    y = x.roll()	
    print y
    print type(y)

    print x



if __name__ == "__main__":
    main()


 
