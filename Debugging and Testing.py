### TASK ONE ###

"""
This is a possible interview coding question. Let's check the task,
implement our solution and then write tests for it:

Task
Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'

Constraint notes:
an input integer is always withing the range 1 to 100 inclusive
"""


# Return true when it is even , false otherwise
def is_even(num):
    return num % 2 == 0


# Return true if the given number is between min and max, otherwise return false
def within_range(num, min, max):
    if min <= num <= max:
        return True
    return False

def red_or_blue(num):
    if not within_range(num, 1, 100):
        raise ValueError('Number must be between 1 and 100')

    if not is_even(num) or within_range(num, 6, 20):
        return 'Red'

    if within_range(num, 2, 5) and num > 20:
        return 'Blue'