# Imports argument variable from system module
from sys import argv
# Unpacks the arguments passed from the command line and inserts them into
# their own variables
script, filename = argv
# Prints the string "We're going to erase %r." % filename
# and takes the string stored in filename and formats it into the string
print "We're going to erase %r." % filename
# Prints the string "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit CTRL-C (^C)."
# Prints the string "If you do want that, hit RETURN."
print "If you do want that, hit RETURN."
# Asks the user for input
raw_input("?")
# Prints the string "Opening the file..."
print "Opening the file..."
# Opens the file stored in the variable filename in write mode and stores it
# in the target variable
target = open(filename, 'w')
# Prints the string "Truncating the file. Goodbye!"
print "Truncating the file. Goodbye!"
# Empties the file stored in the variable target
target.truncate()
# Prints the string "Now I'm going to ask you for three lines."
print "Now I'm going to ask you for three lines."
# Gets user input and stores it in the variable line1
line1 = raw_input("line 1: ")
# Gets user input and stores it in the variable line2
line2 = raw_input("line 2: ")
# Gets user input and stores it in the variable line3
line3 = raw_input("line 3: ")
# Prints the string "I'm going to write these to the file"
print "I'm going to write these to the file."
# Writes the string stored in line1 to the file stored in target
target.write(line1)
# Writes a new line to the file stored in target
target.write("\n")
# Writes the string stored in line2 to the file stored in target
target.write(line2)
# Writes a new line to the file stored in target
target.write("\n")
# Writes the string stored in line3 to the file stored in target
target.write(line3)
# Writes a new line to the file stored in target
target.write("\n")

print "And finally we close it."
target.close()
