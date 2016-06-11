print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)


print "What's your name?",
name = raw_input()
print "Favourite programming language?",
language = raw_input()
print "Hobby?",
hobby = raw_input()

print """ So your name is %s, \n you take fascination in %s.
 Your hobby consists of %s
""" % (name, language, hobby)
