from sys import exit

# Defines a function called gold room
def gold_room():
    # Prints a string "This room is full of gold. How much do you take"
    print "This room is full of gold. How much do you take?"
    # Asks user for input and stores the value entered in next
    next = raw_input("> ")
    # Check if the "0" is in next or "1" is in next:
    if "0" in next or "1" in next:
        # Changes next into an integer and stores it in the variable how much
        how_much = int(next)
    # If "0" or "1" is not in next this else block runs
    else:
        # Calls the function dead() and prints the string "Man, learn to type
        # a number
        dead("Man, learn to type a number")
    # if how_much < (less than 50) this block runs
    if how_much < 50:
        # Prints the string "Nice, you're not greedy, you win!"
        print "Nice, you're not greedy, you win!"
        # Calls the exit 0 function
        exit(0)
    # if how_much is not less than 50 this block runs
    else:
        # Calls the function dead() and prints the string "You greedy bastard"
        dead("You greedy bastard")
# Defines a function called bear room
def bear_room():
    # Prints the string "There is a bear here."
    print "There is a bear here."
    # Prints the string "The bear has a bunch of honey."
    print "The bear has a bunch of honey."
    # Prints the string "The fat bear is infront of another door."
    print "The fat bear is infront of another door."
    # Prints the string "How are you going to move the bear?"
    print "How are you going to move the bear?"
    # stores False in bear_moved
    bear_moved = False
    # This block runs while True
    while True:
        # Takes the user input and stores it in next
        next = raw_input("> ")
        # if next == "take honey" this block runs
        if next == "take honey":
            # Calls the function dead() and prints the string "The bear looks at
            # you then slaps your face face off."
            dead("The bear looks at you then slaps your face off.")
        # elif next == "taunt bear: and not bear_moved this block runs
        elif next == "taunt bear" and not bear_moved:
            # Prints the string "The bear has moved from the door. You can go
            # through it now"
            print "The bear has moved from the door. You can go through it now"
            # Stores true in bear_moved
            bear_moved = True
        # elif next == "open door" and bear_moved: this block runs
        elif next == "open door" and bear_moved:
            # calls the function gold_room()
            gold_room()
        # else this block runs if none of the values are equal to "take honey",
        # "taunt bear", and "open door"
        else:
            # Prints the string "I got no idea what that means."
            print "I got no idea what that means."

# Defines a function called cthulhu_room()
def cthulhu_room():
    # Prints a string "Here you see the great evil Cthulhu."
    print "Here you see the great evil Cthulhu."
    # Prints a string "He, it, what ever stares at you and you go insane."
    print "He, it, whatever stares at you and you go insane."
    # Prints a string "Do you flee for your or eat your head?"
    print "Do you flee for your life or eat your head?"
    # Gets user input and stores it in next
    next = raw_input("> ")
    # if "flee" is in next this block runs
    if "flee" in next:
        # Calls the start() function
        start()
    # elif "head" is in next this block runs
    elif "head" in next:
        # Calls the dead() function prints "Well that was tasty!"
        dead("Well that was tasty!")
    # If none of the values in next are "flee", and "head" this block runs
    else:
        # Calls the cthulhu_room() function
        cthulhu_room()

# Defines a function called dead(why) which accepts an argument
def dead(why):
    # Prints the value stored in why, and the string "Good job!"
    print why, "Good job!"
    # Calls the exit(0) function
    exit(0)

# Defines a function called start()
def start():
    # Prints a string "You are in a dark room."
    print "You are in a dark room."
    # Prints a string "There is a door to your right and left."
    print "There is a door to your right and left."
    # Prints a string "Which one do you take?"
    print "Which one do you take?"
    # gets user input and stores it in next
    next = raw_input("> ")
    # if next == (equal to) "left" this block runs
    if next == "left":
        # Calls the function bear_room()
        bear_room()
    # elif next == (equal to) "right" this block runs
    elif next == "right":
        # Calls this function cthulhu_room()
        cthulhu_room()
    # if next is not (equal to) "right" or "left" this block runs
    else:
        # Calls the function dead() and prints the string "You stumble around
        # the room until you starve."
        dead("You stumble around the room until you starve.")

# Calls the start function
start()


