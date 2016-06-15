# Imports argument variables from sys module
from sys import argv
# Takes the arguments entered from the command line and passes them into
# their own variables
script, input_file = argv

# Defines a function called print_all(f): which accepts a argument
def print_all(f):
    # Prints out the file that's been passed through the function
    print f.read()
    # Defines a function called rewind(f): which accepts a argument
def rewind(f):
    # Starts back at the beginning of the file
    f.seek(0)

# Defines a function called print_a_line(line_count, f): which accepts
# arguments
def print_a_line(line_count, f):
    # Print's out the line count, and the line that was read in the file
    print line_count, f.readline()

# Opens the file in read mode
current_file = open(input_file)

# Prints the string "First let's print the whole file:\n(new line)"
print "First let's print the whole file:\n"

# Calls the functions print_all(current_file) and passes the argument
# current_file into it
print_all(current_file)

# Print's the string "Now let's rewind, kind of like a tape."
print "Now let's rewind, kind of like a tape."
# Calls the rewind function and passes the argument of current file
rewind(current_file)
# Prints the string "Let's print three lines:"
print "Let's print three lines:"


# Stores the value of 1 in current_line
current_line = 1
# Calls the function print_a_line(current_line, current_file)
# and passes it the arguments current_line, and current_file
print_a_line(current_line, current_file)


# Adds 1 to the value already stored in current line
current_line += 1
# Calls the function print_a_line(current_line, current_file)
# and passes it the arguments current_line, and current_file
print_a_line(current_line, current_file)

# Adds 1 to the value already stored in current line
current_line += 1
# Calls the function print_a_line(current_line, current_file)
# and passes it the arguments current_line, and current_file
print_a_line(current_line, current_file)
