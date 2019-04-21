# For loops and lists!

# Use lists to store the stuff from the for loops
# Lists are a container of things that are organized in order from first to last
# Make lists with square brackets around items
# Lists are not the same things as arrays because of how they're implemented in python

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count{number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was {i}")


# Study Drills

# 1. range function returns a range object


# 2. Cant replace the for loop because range returns an object. I wanted a list


# 3. index(of_value), count(of_value), etc.

# 2D lists
# [[1, 2, 3], [4, 5, 6]]
