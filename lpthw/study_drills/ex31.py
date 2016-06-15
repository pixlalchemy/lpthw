print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good Job!"
    else:
        print "Well, doing %s is probably better, Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good Job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good Job!"

elif door == "3":
    print "You enter a room with a sleeping dragon."
    print "1. Run away."
    print "2. Grab the sword to the left of your footer and slay the dragon."
    print "3. Hide."

    slay = raw_input("> ")

    if slay == "1":
        print "The dragon roars and yells coward, flys infront of you and eats your head"
    elif slay == "2":
        print "You slay the dragon!"
    elif slay == "3":
        print "The dragon finds you hiding behind the column and claws you to death"
    else:
        print "Wrong answer the flames from the dragon roast you"
else:
    print "You stumble around and fall on a knife and die. Good Job!"
