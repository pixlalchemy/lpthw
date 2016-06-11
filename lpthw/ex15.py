# Imports argument variable from system module
from sys import argv
# Unpacks the variables passed from the command line into their own variables
script, filename = argv
# opens the file stored in filename and stores it in txt
txt = open(filename)
# Print's a string "Here's your file %r:" and takes the name of the file stored
# in filename and formats it into the string
print "Here's your file %r:" % filename
# reads the file and prints it as a string
print txt.read()
# Prints the string "Type the filename again:"
print "Type the filename again:"
# Get's the filename again from the user and stores it in file_again
file_again = raw_input("> ")
# Opens the file stored in file again and stores it in txt_again
txt_again = open(file_again)
# reads the file and prints it as a string again
print txt_again.read()
# Close the file
txt.close()
txt_again.close()
