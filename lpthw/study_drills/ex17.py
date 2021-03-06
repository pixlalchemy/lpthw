# imports argument variable from sys
from sys import argv
# imports exists from os.path
from os.path import exists
# Takes the arguments entered from the command line,
# and stores them in their own variables
script, from_file, to_file = argv
# Prints the string "Copying from %s to %s" and takes the values stored
# in from_file and to file and formats it into the string.
print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
# opens the file stored in the from_file and stores it in the in_file
in_file = open(from_file)
# Stores the read file and stores it in the indata variable
indata = in_file.read()
print """
The input file is %d bytes long.
Does the output file exist? %r
""" % (len(indata), exists(to_file))
# Opens the file stored in the to_file in write mode and stores it in the out
# file
out_file = open(to_file, 'w')
# writes the read file stored in indata in the out_file
out_file.write(indata)

print "Alright, all done."
# Closes the files
out_file.close()
in_file.close()
