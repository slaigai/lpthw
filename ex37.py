# General Notes
"""
# >>> [] == []
# True
# >>> [] is []
# False
# >>> {} == {}
# True
# >>> {} is {}
# False

An empty list or dictionary is equal to another empty one. But they are not identical objects as they are located
separately in memory. This is because list and dictionary are mutable (value can be changed).


# >>> '' == ''
# True
# >>> '' is ''
# True
# >>> () == ()
# True
# >>> () is ()
# True

Unlike list and dictionary, string and tuple are immutable (value cannot be altered once defined). Hence,
two equal string or tuple are identical as well. They refer to the same memory location.

"""


# Notes on python keywords

"""
Dependencies

as: create alias (import module as alias, with object as alias)

from: import only a specified section from a module

import: import modules into the current namespace

"""


"""
Logical Operators

and: logical and

or: logical or

not: logical not

"""


"""
Blocks and structures

class: defines a class

def: define a function

lambda: create anonymous function

pass: this block is empty. "null statement", nothing happens when it is executed. Used as a placeholder

"""


"""
Exceptions

assert: ensure condition is true or raise error

except: "catch" statement in try...except blocks

raise: "throw" an exception (error)

finally: exception or not, do this block no matter what

"""


"""
Flow control

break: exit loop

continue: start at top of loop immediately (don't process the rest of the loop)

if: if condition is True, execute

elif: if previous if or elif condition(s) False and this elif condition is true, execute this. Otherwise, 
do not execute this block.

else: executes if no previous if or elif conditions are True

for: loop over an iterable object (e.g. list, tuple, string)

return: exit function and return a value. If no value is returned, None is returned automatically

while: execute block until condition is false or break is encountered

with: wrap code block in context manager. Context manager is a class that implements __enter__ and __exit__ methods. 
Ensures that __exit__ is called at the end of the block. Similar to a try...finally block.

yield: used like a return statement but returns a generator instead of a value. Generator is an iterator that 
generates one item at a time. Low memory cost, compute values as needed

"""


"""
Object methods

del: delete reference to object. NOTE everything is a reference in python. This is deleting a variable

global: declare global variable (not needed to read variable value)

in: test if a sequence (e.g. list, tuple, string) contains a value. Returns True if value present, otherwise returns 
False

is: tests if two variables refer to the same object, whereas == tests that two variables have the same value. 
Remember, everything is a reference.

print: print this object (usually strings and other printable objects that are converted to strings)

"""


"""
Misc

exec(): executes string or code object as python code

"""


"""
Data types

True: true boolean

False: false boolean

None: null, nothing, no value

bytes: stores bytes of objects (text, PNG, file, etc.)

strings: stores textual information

numbers: stores integers

floats: stores decimals

lists: stores a list of things (don't need to be the same type)

dicts: key-value mapping of things

"""


"""
Escape characters

\\: backslash

\': single quote

\": double quote

\a: bell (sound)

\b: backspace

\f: form feed (go to next page)

\n: newline

\r: carriage return (return to beginning of current line). Does not work in python console

\t: tab

\v: vertical tab (not really useful unless printing to printer-handled files)

"""


"""
Operators (just the ones that need more reinforcement)

**: exponentiation

//: floor division

%: string interpolate or modulus. print("%s %s" % ("a", "b"))

[]: list brackets

{}: dict curly braces

@: decorator (learn more about this later)

,: unpacking, separating items in list of args

:: colon, slicing, starting block

.: dot, access class attributes and methods

;: semicolon, can be used to separate commands on one line like print("Hello"); print("World!")

//=: floor divide and assign

**=: power and assign

"""

