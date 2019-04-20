# Number of available cars
cars = 100
# Space in each car (i.e. number of seats/spots in a car, including the driver)
space_in_car = 4.0
# Number of available drivers
drivers = 30
# Number of available passengers
passengers = 90
# Number of unoccupied cars (because there isn't a driver for the car)
cars_not_driven = cars - drivers
# Number of cars with drivers (i.e. cars that can be occupied because there is an available driver). Assumes 1 driver
# per car (i.e. drivers cannot be passengers)
cars_driven = drivers
# Total number of seats available
carpool_capacity = cars_driven * space_in_car
# Average number of passengers in a car (including the driver)
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# Study Drills

# Explain this error in your own words and use line numbers to explain why
#
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
#
# Explanation:
# The variable 'car_pool_capacity' had not been declared before line 8 of ex4.py. The interpreter did not know what to
# do and raised a NameError.


# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
#
# Nope. carpool_capacity would have been 120 instead of 120.0


# 2. Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of
# just 4 so that it is floating point.
#
# Okay.

# 3. Write comments above each of the variable assignments.
#
# Fine...


# 4. Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names
# (cars_driven, passengers).
#
# = symbol is the assignment operator


# 5. Remember that _ is an underscore character.
#
# Okay.


# 6. Try running python3.6 from the Terminal as a calculator like you did before, and use variable names to do your
# calculations. Popular variable names are also i, x, and j.
#
# Using more informative variable names would be better. Even 'num' would be better than 'x' in my opinion (but to each
# their own).
