"""
Lists are ordered collection of objects
Random access
pop: remove and return element from end of list

"""


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Split the string by spaces and return in a list
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    # Remove and return item from the end of more_stuff
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # Add item to the end of stuff list
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")


print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # get last element of the list
print(stuff.pop())  # remove and return last element of list
print(' '.join(stuff))
print('#'.join(stuff[3:5]))  # slice, get elements [3, 5) == [3, 4] and join them with a #
