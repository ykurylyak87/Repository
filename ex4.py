# -*- coding: utf-8 -*-
# Змінні

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "We have", cars, "cars"
print "And only", drivers, "drivers that came to work today"
print "So", cars_not_driven, "cars are empty"
print "We can carry today", carpool_capacity, "persons"
print "Today we need to carry", passengers, "persons"
print "In every car there will be near", average_passengers_per_car, "persons"

