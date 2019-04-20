# Names of math symbols
# + plus
# - minus
# / slash
# * asterisk
# % percent
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal

print("I will now count my chickens:")

# Division results in float, result of 25 + 5.0 is float 30.0. Casted to the least restrictive data type (I think)
print("Hens", 25 + 30 / 6)

# Modulo does not take precedence over multiplication. 25 * 3 -> 75 is performed first. Then 75 % 4 -> 3 is performed.
# The result remains in integer precision.
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")
# Modulo and division take precedence. Division results in float so result of the entire expression is float.
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Arithmetic operations take precedence over conditional operations. I.e. the addition and subtraction are performed
# before the comparison for less-than
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("Oh, that's why it's False.")

# Nothing to say here
print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Output:
# I will now count my chickens:
# Hens 30.0
# Roosters 97
# Now I will count the eggs:
# 6.75
# Is it true that 3 + 2 < 5 - 7?
# False
# What is 3 + 2? 5
# What is 5 - 7? -2
# Oh, that's why it's False.
# How about some more.
# Is it greater? True
# Is it greater or equal? True
# Is it less or equal? False


# 1. Above each line, use the # to write a comment to yourself explaining what the line does.
#
# Done. Had to Google for docs about floating point conversion in division. Learned about operator precedence through
# deduction.


# 2. Remember in Exercise 0 when you started python3.6? Start python3.6 this way again and, using the math operators,
# use Python as a calculator.
#
# I definitely skipped Exercise 0 because I prefer to use an IDE. Sorry, Zed...


# 3. Find something you need to calculate and write a new .py file that does it.
#


# 4. Rewrite ex3.py to use floating point numbers so it's more accurate. 20.0 is floating point.
#
# I'll just add another one here that casts everything to float to print out 97.0
print(100.0 - 25 * 3 % 4)
