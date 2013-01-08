# learnPy4-ch27.py
# first python file written on macbook!
class User(object):
    __counter = 0

    @staticmethod
    def increment_counter():
        User.__counter += 1
        
    def __init__(self, name=''):
        self.inc = False
        if not (name == ''):
            self.__name = name
        else:
            self.increment_counter()
            self.inc = True
            self.__name = 'User ' + str(User.__counter)

        if not (self.inc):
            self.increment_counter()
    
    def __str__(self):
        return 'Hi im %s' % (self.__name)

    def change_name(self, newName=None):
        if not (newName == None):
            print ('"Hmm I think ill change my name to {0}" said {1}.'.format(newName, self.__name))
            self.__name = newName
        else:
            raise ValueError("Must give a name in a string!")
        

def main():
    ron = User('Ron')
    hank = User('Hank')
    shelly = User()
    print hank
    print ron
    print shelly

    shelly.change_name('shelly')
    print shelly


    hank.change_name('Tom')
    print hank
if __name__ == "__main__":
    main()
