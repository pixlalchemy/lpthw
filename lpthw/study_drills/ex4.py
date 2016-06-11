# assigns 100 to cars
cars = 100
# assigns 4 to space_in_a_car
space_in_a_car = 4
# assigns 30 to drovers
drivers = 30
# assigns 90 to passengers
passengers = 90
# takes the total of cars subtracted from drivers and assigns it
# to cars_not_driven
cars_not_driven = cars - drivers
# cars_driven is assigned the total stored in drivers
cars_driven = drivers
# carpool_capacity is assigned the total of cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car is assigned the total of passengers divided by
# cars driven
average_passengers_per_car = passengers / cars_driven

# prints the string "There are" and the value stored in cars,
# and "cars available"
print "There are", cars, "cars available."
# prints the string "There are only" and the value stored in drivers,
# "drivers available."
print "There are only", drivers, "drivers available."
# prints the string "There will be", and the value stored in cars_not_driven
# "empty cars today."
print "There wil be", cars_not_driven, "empty cars today."
# prints the string "We can transport", and the value stored in carpool_capacity
# "people today."
print "We can transport", carpool_capacity, "people today."
# prints the string "We have", and the value stored in passengers,
# "to carpool today."
print "We have", passengers, "to carpool today."
# prints the string "We need to put about", and the value stored in
# average_passengers_per_car, "in each car."
print "We need to put about", average_passengers_per_car, "in each car."
