from sys import argv

script, filename = argv

# Opens the file stored in filename and stores it in target
target = open(filename)
# Reads the file stored in target
print target.read()
# Closes the file stored in target
target.close()
