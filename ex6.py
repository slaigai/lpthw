# Either double-quotes or single-quotes signify a string literal.
# Strings can contain any number of variables (i.e. within an "f-string")
# the .format() method is another way to format strings

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Puts the format args into the curly braces in order
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# When using + operator to concatenate strings, no space is added. When using print with a comma to separate args to
# the print function, the args are joined with a space by default
print(w + e)

# 1. Go through this program and write a comment above each line explaining it.
#
# Done.


# 2. Find all the places where a string is put inside a string. There are four places.
#
# 2 in the following line
# y = f"Those who know {binary} and those who {do_not}."
#
# 1 in each of the following lines (2 total)
# print(f"I said: {x}")
# print(f"I also said: '{y}'")


# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
#
# Does appending a string with print(w + e) count as putting e into w at the end?


# 4. Explain why adding the two strings w and e with + makes a longer string.
#
# String concatenation
