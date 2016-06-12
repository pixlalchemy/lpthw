# Defines a function name cheese and crackers,
# Which accept arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints the string "You have %d cheese!" and takes the value
    # stored in cheese_count and formats it into the string
    print "You have %d cheese!" % cheese_count
    # Prints the string "You have %d boxes of crackers!" and takes value
    # stored in boxes_of_crackers and formats it into the string
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Prints the string, "Man That's enough for a party"
    print "Man that's enough for a party"
    # Prints the string "Get a blanket." and created a new line with the \n
    # escape
    print "Get a blanket.\n"

# Prints the string "We can just give the function numbers directly:"
print "We can just give the function numbers directly:"
# Passes the arguments into the function
cheese_and_crackers(20, 30)


# Prints the string "Or, we can use variables from our script:"
print "OR, we can use variables from our script:"
# Stores 10 into the variable amount_of_cheese
amount_of_cheese = 10
# Stores 50 into the variable amount_of_crackers
amount_of_crackers = 50
# Passes the arguments into the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Prints the string "We can even do math inside too:"
print "We can even do math inside too:"
# Adds 10 + 20, and 5 + 6 and passes them into the arguments
cheese_and_crackers(10 + 20, 5 + 6)

# Prints the string "And we can combine the two, Variables and math:"
print "And we can combine the two, Variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def greeting(greet):
    print greet


greeting("Hello World")
hello_world = "Hello World"


greeting(hello_world)


hello = "%s " % ("Hello World")
greeting(hello)
greeting(hello * 2)
greeting(hello + hello)

