# Modules, classes, and objects

# Modules are like dictionaries
# Python file with functions or variables in it
# Import the file
# Access functions or variables in the module with the dot operator and the name of the function or variable


# Classes are like modules
# Groups functions and data, accessed with dot operator
# Can be used to create many instances of the class, unlike modules that have one instance.


# Object instantiation
# 1. Look for class definition
# 2. Create empty object with methods defined in class definition
# 3. Looks for "magic" function __init__(self), this is the constructor
# 4. __init__(self) gets the argument self, which is the empty object created in 2. Set variables in the empty object
# 5. The initialized object instance is returned (not from init but from whatever Python calls)


# First class example
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there!"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()




