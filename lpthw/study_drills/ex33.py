
numbers = []

def loop(num, increment):
    i = 0
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


print "How many times do you want the loop to run? "
num = int(raw_input('> '))
print "How much do you want it to increment by? "
increment = int(raw_input('> '))

loop(num, increment)

print "The numbers: "

for for_num in range(0, num):
    for_num += 3
    print for_num

for num in numbers:
    print num

