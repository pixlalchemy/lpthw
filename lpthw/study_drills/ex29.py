people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled out!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

if people != dogs:
    print "People are not dogs."

if people == dogs and cats > dogs:
    print "We need more people and more dogs =("

if dogs == 20 and not(dogs > cats):
    print "Sorry their are not enough dogs"

