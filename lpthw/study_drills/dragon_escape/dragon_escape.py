from sys import exit
# Dragon Escape

# Dragons
baby_dragons = ['Baby Green Dragon', 'Baby Blue Dragon', 'Baby Black Dragon']
dragons = ['Green Dragon', 'Blue Dragon' 'Black Dragon']

# Baby Weaponry
baby_weaponry = ['1.Stick', '2.Dagger', '3.Dodge']

alive = True
dead = False

# Defines a function called user_choice() which takes user input and returns it
# to them.
def user_choice():
    choice = raw_input("> ")
    return choice


# Defines a function called baby_dragon_dungeon(), Where all the baby dragon
# commands form.
def baby_dragon_dungeon():
    print "You creep through the dungeon slowly and something lurks in the midst"
    baby_green_dragon()
    baby_blue_dragon()


# Defines a function baby_weapons(), which prints out all the weaponry that a
# user can choose from
def baby_weapons():
    for weaponry in baby_weaponry:
        print "Weaponry:%s" % weaponry

def baby_riddle():
    print "You approach the Baby Blue Dragon, the dragon asks you a question!"
    print "I am bluer then then the sea, at time i can get darker then sight of",
    print "The sun going down. What am i ?"

def baby_green_dragon():
    print "You see a Baby Green Dragon"
    baby_weapons()
    choice = user_choice()

    if "1" in choice:
        print "The Baby Green Dragon breaks your stick and licks you to death"
        exit(0)
    elif "2" in choice:
        print "You slay the Baby Green Dragon"

    elif "3" in choice:
        print "You dodge the Baby Green Dragon slip over a rock and crack your head"
        exit(0)
    else:
        print "That choice isnt valid"


def baby_blue_dragon():
    print "You see a Baby Blue Dragon"
    baby_riddle()
    choice = user_choice()
    if "sky" in choice:
        print "You shall Pass!"
    else:
        print "He blows a small flame but ends up killing you upon touching the skin"
    exit(0)
def start():
    while True:
        baby_dragon_dungeon()

start()
