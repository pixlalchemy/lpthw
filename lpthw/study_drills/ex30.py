people = 30
cars = 40
buses = 15

# if cars > (greater than people): prints out the string "We should take the
# cars."
if cars > people:
    print "We should take the cars."
# else if cars < (less than people): prints out the string "We should not take
# the cars."
elif cars < people:
    print "We should not take the cars."
# else prints out a string "We can't decide."
else:
    print "We can't decide."
# if buses > (greater than cars): prints out the string "That's to many buses."
if buses > cars:
    print "That's to many buses."
# else if buses < (less than cars): prints out the string "Maybe we could take
# the buses."
elif buses < cars:
    print "Maybe we could take the buses."
# else: prints out the string "We still can't decide."
else:
    print "We still can't decide."
# if people > buses(greater than people): prints out the string "Alright, let's
# just take the buses."
if people > buses:
    print "Alright, let's just take the buses."
# else: prints out the string "Fine, let's stay home then."
else:
    print "Fine, let's stay home then."
