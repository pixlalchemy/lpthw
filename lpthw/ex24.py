# Prints a string
print "Let's practice everything."
# Prints a string with some escape characters \', to escape the single quotes,
# \\ to escape the backslash, \n for the new and \t for the tabs
print 'You\'d need to know \'bout escapes with \\ that do \n newline and \t tabs.'

# stores a string in poem which includes a couple of escape characters \t for
# tabs, \n for new line.
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\twhere there is none.
"""
# Prints "--------"
print "----------------"
# Prints the string stored in poem
print poem
# Prints "--------"
print "----------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
# Defines a function called secret_formula(started) that takes an argument
def secret_formula(started):
    # Stores the final value of started * 500 in jelly_beans
    jelly_beans = started * 500
    # Stores the final value of jelly_beans / 1000 in jars
    jars = jelly_beans / 1000
    # Stores the final value jars / 100 in crates
    crates = jars / 100
    # Returns the values to use later in your script
    return jelly_beans, jars, crates

# Stores 10000 in start_point
start_point = 10000
# Takes the returned value in the secret_formula(start_point)
# and stores them in their own individual variables
beans, jars, crates = secret_formula(start_point)
# Prints the string "With a starting point of: %d" and takes the value stored in
# start point and formats it into the string
print "With a starting point of: %d" % start_point
# Prints the string "We'd have %d beans, %d jars, and %d crates."
# Takes the values stored in beans, jars, and crates and formats it into the
# string
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# Takes the value stored in start_point and divides it by 10
start_point = start_point / 10
# Prints the string "We can also do that this way:"
print "We can also do that this way:"
# Prints the string "We'd have %d beans. %d jars, and %d crates."
# Takes the returned values from secret_formula and formats it into the string
print "we'd have %d beans. %d jars, and %d crates." % secret_formula(start_point)

