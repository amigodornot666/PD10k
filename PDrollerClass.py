# PDrollerClass.py
import random

class Dice(object):
    def __init__(self, rolled=True):
	    self.faces = range(1, 7)
	    self.rolled = rolled

    def __str__(self):
        if (self.rolled):
		    return str(random.choice(self.faces))
        else:
            return str(self.faces)
    def make_roll(self):
        return random.choice(self.faces)
    def roll(self):
        print self.make_roll()


class Roller(object):
    def __init__(self, num=6):
        self.dieNum = num
        self.dies = list()
        for i in range(self.dieNum):
            self.dies.append(Dice())
    def roll(self):
        for i in self.dies:
            print i, 
            print '',

if __name__ == "__main__":
    aRoll = Roller()
    for i in range(1, 7):
        print 'Roll %d - ' % (i),		
        aRoll.roll()	
        print
        #print

				
	    
