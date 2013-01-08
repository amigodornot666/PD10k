# PDroll.py
# by: aMigod666(KyleJRoux)
import random

class Dice(object):
    Value = {'One' : 100, 'Two' : 20, 'Three' : 30, 'Four' : 40, 'Five' : 50, 'Six' : 60}
    Face = {1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six'}
    
    def __init__(self, face=0):
        if not(face == 0):
            self.face = Dice.Face[face]
        else:
            # default to roll random number
            self.face = Dice.Face[random.choice(1, 7)]
        self.value = Dice.Value[self.face]
        
    def __str__(self):
        return 'A_{0},\nWith a single value of {1},\nBut that dosent mean thats your score!'.format(self.face, self.value)
        
    def get_face(self):
        return self.face
        
    def print_face(self):
        print self.get_face()
        
    def get_value(self):
        return self.value
    
    def print_value(self):
        print self.get_value()
        
         
def Roll(object):
    def __init__(self, dieNum=6):
        self.askToHold = False
        self.rollScore = 0
        self.dice = list()
        for die in range(dieNum):
            self.dice.append(Dice())
        
    def __str__(self):
        if not(self.askToHold):
            return 'You rolled {0}, {1}, {2}, {3}, {4}, {5}'.format(self.dice[0].face, self.dice[1].face, self.dice[2].face, self.dice[3].face, self.dice[4].face, self.dice[5].face)
        else:
            pass
    
    def get_roll_score(self):
        for i in self.dice:
            self.rollScore += Dice.Value[i.face]
        return self.rollScore
        
    def print_roll_score(self):
        self.get_roll_score()
        print self.rollScore
    
def main():
    roll = Roll(6)
    print roll
    
main()        


