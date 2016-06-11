# x stores the string "There are %d types of people." and the
# number 10 is formatted into the string
x = "There are %d types of people." % 10
# stores the string "binary" into binary
binary = "binary"
# stores don't in do_not
do_not = "don't"
# y stores the string "Those who know %s and those who %s."
# and the string 'binary' and "don't" is formatted into the string
y = "Those who know %s and those who %s." % (binary, do_not)
# prints the string stored in x
print x
# prints the string stored in y
print y
# prints the string "i said: %r. " and takes the value stored in x
# and formats it into the string
print "I said: %r. " % x
# prints the string "i also said: '%s'." % y" and takes the value stored in y
# and formats it into the string
print "I also said: '%s'." % y
# stores the value of False in hilarious
hilarious = False
# stores the string "Isn't that joke so funny?! %r" in joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"
# prints the string stored in joke evaluation and takes the value of hilarious
# and formats it into the string
print joke_evaluation % hilarious

# stores the string "This is the left side of..." in w
w = "This is the left side of..."
# stores the string "a string with a right side." in e
e = "a string with a right side."
#prints the added strings stored in w and e together
print w + e
