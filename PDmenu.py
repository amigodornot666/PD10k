# PDmenu.py
# -*- coding: utf-8 *-*
# by:aMigod666(KyleJRoux)
import sys
import time
import PDplayerClass
import PDstart


def add_footer():
    print ret_footer()


def ret_footer(num=0):
    FOOTER = '\n\n\n'
    if not(num == 0):
        for i in range(num):
            print FOOTER
    else:
        return FOOTER

# options
OPT1 = '1) Single Player Game'
OPT2 = '2) Multi-Player Game'
OPT3 = '3) Options'
OPT4 = '4) Game Rules'
OPT5 = '5) Exit'

# screens for menus
MAIN_MENU = '''

                        %s

                        %s

                        %s

                        %s

                        %s

                        ''' % (OPT1, OPT2, OPT3, OPT4, OPT5)

WELCOME_MENU = '''

                    10Kpy
                A dice Game!!!!!
                10,000 like never
                      before!!!


            READY TO PLAY?!?!
'''

RULES1 = ('''



            RULES OF 10,000

        To play 10,000, roll 6 dice
        and check if you would like
        to "keep" any. You have to
        "keep" somthing to score.



        ''' + ret_footer())

RULES2 = '''

        If you keep nothing on the
        first roll you lose your
        turn. If you keep any dice
        you can keep the points they
        add up to, if you already have
        1000 points banked, if not you
        must keep rolling until you
        reach 1000 points. After that
        you can "stay" and keep your
        points on any future roll
        until the game ends.

        '''
RULES3 = '''

            SCORE LIST:


            STRAIT(1,2,3,4,5,6)
            1000

            DOUBLES(xx,yy,zz)
            1000

            THREE OF A KIND(xxx)[2-6]
            100 * Dice Face
            IE - 3,3,3 = 300


        '''

RULES4 = '''




            FOUR OF A KIND(xxxx)
            (100 * Dice Face) * 2
            IE - 5,5,5,5 = 1000

            FIVE OF A KIND
            (100 * Dice Face) * 2 ) * 2
            IE 2,2,2,2,2 = 800

            SIX OF A KIND
            (100 * Dice Face) * 2) * 2) * 2
            IE 4,4,4,4,4,4 = 3200


         '''

RULES5 = ('''


            ONE'S & FIVE'S
            FIVE'S  = 50 each

            ONE's 1-2 = 100 each
                  3 = 1000
                  4 = 2000
                  5 = 4000
                  6 = 8000




          ''' + ret_footer())

def s_flush():
    for i in range(20):
        print '\n'


def welcome_menu():
    print WELCOME_MENU
    add_footer()
    time.sleep(3)

def main_menu():
    choice = str(raw_input(MAIN_MENU))
    s_flush()
    print 'You picked {0}'.format(choice)
    time.sleep(2)
    s_flush()
    option_picker(int(choice))

def start_menu():
    welcome_menu()
    main_menu()


def display_rules():
    s_flush()
    print RULES1
    raw_input('press enter to continue')
    s_flush()
    print RULES2
    raw_input('press enter to continue')
    s_flush()
    print RULES3
    raw_input('press enter to continue')
    s_flush()
    print RULES4
    raw_input('press enter to continue')
    s_flush()
    print RULES5
    raw_input('press enter to continue')
    s_flush()
    main_menu()
    #for rule in [RULES1, RULES2, RULES3, RULES4, RULES5]:
    #    print rule
    #        add_footer()
    #        raw_input('Press enter to continue')
    #        s_flush()
    #        main_menu()


def option_picker(choice=0):
    if not(choice == 0):
        if int(choice) == 1:
            # option one
            PDstart.start_single_game()
        elif int(choice) == 2:
            #option two
            PDstart.start_multi_game()
        elif int(choice) == 3:
            # option 3 ironicly "options"
            print 'This is a temporeary options menu'
            add_footer()
            raw_input('press enter to return to main menu')
            main_menu()
        elif int(choice) == 4:
            # option 4
            display_rules()
        elif int(choice) == 5:
            print 'exiting'
            time.sleep(3)
        else:
            raise ValueError('Bad value')
    else:
        raise ValueError('Please enter a number')


def main():
    main_menu()


if __name__ == "__main__":
    main()
