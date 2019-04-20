# This exercise illustrates the usage of "f-strings" or formatter string literals. This was introduced in Python 3.6.
#
# Must start the string with f, use curly braces {} with a variable name inside
# e.g. f"Hello {somevar}"

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")

# Study Drills


# 1. Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere,
# not just where you used = to set them.
#
# I think I'll pass. I get the point.


# 2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in
# the measurements. Work out the math in Python.
height_cm = my_height * 2.54
weight_kg = my_weight * 2.205
print(f"Height in cm is {height_cm}.")
print(f"Weight in kg is {weight_kg}.")


# Notes

# Floating point numbers can be rounded using the round() function
rounded_weight_kg = round(weight_kg)
print(f"Rounded weight in kg is {rounded_weight_kg}.")
