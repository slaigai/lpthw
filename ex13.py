# In pycharm, make sure to use the terminal to run this exercise

# Import argv from the sys module
from sys import argv
# read the WYSS section for how to run this
# E.g. python ex13.py 1 2 3
script, first, second, third = argv # argv is the "argument variable". This line unpacks argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# If not enough command line args were passed in, unpack errors out with a ValueError: not enough values to unpack

# Note that command line arguments come as strings. To convert them, use something like int(input())

# Note that "run" in pycharm calls the script without any command line arguments (besides the script name)
