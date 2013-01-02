# PDplayerClass.py
# second mac OS python file.
# aMigod666(KyleJRoux)
import PDuserClass

class Player(PDuserClass.User):
    __rollHistory = dict()
    playerNameList  = list([None])
    playerNameDict = {None : 0}

    def __init__(self, name=' '):
        #super(Player, self).__init__(name)
        PDuserClass.User.__init__(self)
        self.__name = name
        Player.playerNameList.append(self.__name)
        Player.playerNameDict[Player.playerNameList[Player.counter]] = Player.counter


    def __str__(self):
        return 'Hi my name is {0},\nIm the first ever Player!!'.format(self.name)


def main():
    john = PDuserClass.User('john')
    ron = PDuserClass.User('Ron')
    kate = PDuserClass.User()

    for user in [john, ron, kate]:
        print user

    print 'now players'

    kyle = Player('Kyle Roux')
    print kyle

if __name__ == "__main__":
    main()
