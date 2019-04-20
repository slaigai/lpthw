# Intro to functions!
"""
1. Functions start with def keyword
2. Only underscore and alphanumeric characters are allowed in function name (cannot start with number)
3. Open parentheses right after function name
4. Args come right after open parentheses, separated by commas
5. Each arg has unique name
6. Close parentheses, followed by colon
7. Indent lines within function with 4 spaces exactly
8. Dedent (end indentation) at end of function
"""


# this one is like your scripts with argv
def print_two(*args):
    # *args passes in all arguments as a list
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


#  this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
