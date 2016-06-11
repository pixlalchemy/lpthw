from sys import argv

script, first_name, last_name = argv

print "Script Name: %s" % script
print "First Name: %s" % first_name
print "Last Name: %s" % last_name

prompt = '>'
print "%s %s What's your programming language of choice? " % (first_name,
                                                              last_name)
language = raw_input(prompt)

print "so you're a %s enthusiast" % (language)



