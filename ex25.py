# In python console, type help(ex25) and help(ex25.break_words) to see docstring behavior (documentation comments)
#
# Can import everything from ex25 by doing from ex25 import *

# If nothing is returned from a function, the return value will be "None"

# Variable scoping in regards to pop of the list inside of a function being able to modify the list. The list is
# mutable and you are modifying the list in the memory space where the variable name pointer is referencing.



def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
