# PDrollerClass.py
import random

class Dice(object):
    Value = {'One' : 100, 'Two' : 20, 'Three' : 30, 'Four' : 40, 'Five' : 50, 'Six' : 60}
    Face = {1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six'}
    counts = {'One' : 0, 'Two' : 0, 'Three' : 0, 'Four' : 0, 'Five' : 0, 'Six' : 0}

    def __init__(self, rolled=True):
            self.faces = range(1, 7)
            self.rolled = rolled

    def __str__(self):
        if (self.rolled):
                    return str(self.current_value())
        else:
            return str(self.faces)

    def current_value(self):
        self.currentValue = random.choice(self.faces)
        Dice.counts[Dice.Face[self.currentValue]] += 1

    def make_roll(self):
        return Dice.Face[random.choice(self.faces)]

    def roll(self):
        return self.make_roll(),

    def get_face(self):
        return self.face

    def print_face(self):
        print self.get_face()

    def get_value(self):
        return self.value

    def print_value(self):
        print self.get_value()


class Roller(object):
    def __init__(self, num=6):
        self.dieNum = num
        self.dies = list()
        for i in range(self.dieNum):
            self.dies.append(Dice())
        self.numCounts = dict()

    def roll(self):
        self.dieList = []
        for i in self.dies:
            self.dieList.append(i.roll())
        for i in range(len(self.dieList)):
            print str(self.dieList[i]) ,
            print '',

    def get_face_counts(self):
        #for i in range(1, 7):
        #    self.numCounts[Dice.Face[i]] = Dice.counts[Dice.Face[i]]
        pass

    def print_face_counts(self):
        #self.get_face_counts()
        #for i in self.numCounts:
        #    print '{0} {1}'.format(i, self.numCSounts[i])
        print Dice.counts



if __name__ == "__main__":
    aRoll = Roller()
    for i in range(1, 7):
        print 'Roll %d - ' % (i)
        aRoll.roll(),
        print
        aRoll.print_face_counts()
        #print

    print 'now another roll'
    aRoll.roll()
    aRoll.dies[1].current_value()
    print aRoll.dies[1].currentValue

