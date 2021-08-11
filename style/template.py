#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: I. M. Student
Directory ID: imstudent (= the first part of your email)
Date: YYYY-MM-DD
Assignment: Homework X
"""

# Module imports go here
import sys


# Constants and variables in global scope are normally defined here
YOUR_CONSTANT = "This is a constant you defined."
your_variable = [1, 2, 3]
your_dictionary = {
    'this': 'illustrates a strategy for',
    'managing': 'line breaks when needed"
}


# Functions you define
def your_function():
    """
    You can put functions and classes that 
    you create here, outside of the main function. You 
    should remove this block in any case.
    """
    print("Your custom function has been run.")


class YourClass():
    """Classes should have a documentation string"""

    def __init__(self, foo):
        """Methods can also have docstrings"""
        self.foo = foo


def main():
    """
    Put the main logic of your program in this function.
    You should replace the statements below, with your 
    program.
    """
    print("The main function has been run.")
    your_function()
    print(YOUR_CONSTANT)
    print(your_variable)


'''
The following block checks whether the code is being run directly 
(in which case the main function will be run), or imported 
into another program (in which case the main function will 
not run. You don't need to change the section below, but 
you probably want to delete this comment.
'''

if __name__ == '__main__':
    main()
