# PDplayerClass.py
# -*- coding: utf-8 *-*
# by: aMigod666(KyleJRoux)
#import PDmenu
#import time

debug = True

class Player(object):
    _playerCount = 0
    _playerList = [None]
    _playerScores = dict()

    def  __init__(self, name=''):
        Player._playerCount += 1
        if not (name == ''):
            self._name = name
        else:
            self._name = 'Player #{0}'.format(Player._playerCount)
        self.playerNumber = Player._playerCount
        Player._playerList.append(self._name)
        Player._playerScores[self._name] = 0

        if (debug):
            print '{0} has joined the game and is player #{1}'.format(self._name, Player._playerCount)

    def __str__(self):
            return str(self._name)

def main():
    kyle = Player('Kyle')




if __name__ == "__main__":
    main()
