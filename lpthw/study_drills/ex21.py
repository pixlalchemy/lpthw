def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVINDING %d / %d" % (a, b)
    return a / b

def receipt(item, gst):
    print "Gst:", item * gst
    return item + item * gst

# Receipt
total = receipt(9.99, 0.05)

print total

print "Let's do some math with just functions!"


age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age:%d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 5))))
formula = subtract(height, add(age, multiply(iq, divide(weight, 10))))

print "That becomes: ", what, "Can you do it by hand?"
print "formula becomes: ", formula, "Can you do it by hand?"
