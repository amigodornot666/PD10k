# PDstart.py
# by: aMigod666(KyleJRoux)
import PDplayerClass
import PDmenu

player = list()
# DEBUG
debug = True

def add_player():
    global player
    player.append(PDplayerClass.Player(raw_input('Please enter your name: '))),
    if (debug):
        print 'added another player'

def start_single_game():
    add_player()
    print 'time to play {0}'.format(player[0])

def ask_to_continue():
    answer = str(raw_input('Would you like to add another player?(y or n)\t')),
    if (answer == ('y',)):
        PDmenu.s_flush()
        start_multi_game()
    else:
        print 'starting game with ',
        for players in range(len(player)):
            print player[players],
            print ', ',
        
            

def start_multi_game():
    add_player()
    ask_to_continue()

if __name__ == "__main__":
    start_multi_game()
